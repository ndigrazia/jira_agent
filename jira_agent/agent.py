import os
import logging
from typing import Optional
from urllib.parse import urlparse

import asyncio
import httpx
from dotenv import load_dotenv

from jira_agent.prompts import build_instructions

from google.adk.agents.llm_agent import LlmAgent
from google.adk.agents.callback_context import CallbackContext
from google.adk.tools.mcp_tool.mcp_toolset import MCPToolset
from google.adk.tools.mcp_tool.mcp_session_manager import StreamableHTTPConnectionParams

from google.adk.tools.preload_memory_tool import PreloadMemoryTool
from google.genai import types

from mcp.client.streamable_http import create_mcp_http_client


logger = logging.getLogger(__name__)


def load_environment_configs() -> None:
    """Load environment variables at the very beginning with fallback paths."""
    load_dotenv()
    # Also load package-local .env in case working directory is different
    load_dotenv(dotenv_path=os.path.join(os.path.dirname(__file__), '.env'))


def setup_logging() -> None:
    """Configure the logging framework."""
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    )


_cached_id_credentials = {}


def get_mcp_token(mcp_url: str = "") -> str:
    """Dynamically retrieve or generate MCP Bearer authentication token for each request."""
    # 1. Check explicit environment variables first
    explicit_token = os.environ.get("JIRA_MCP_TOKEN") or os.environ.get("MCP_TOKEN")
    if explicit_token:
        return explicit_token.strip()

    # 2. Check service account key file
    sa_key_candidates = [
        os.environ.get("GCP_SA_KEY_PATH"),
        os.environ.get("GOOGLE_APPLICATION_CREDENTIALS"),
        os.path.join(os.path.dirname(__file__), "sa-key.json"),
        os.path.join(os.path.dirname(__file__), "..", "sa-key.json"),
        #os.path.join(os.path.dirname(__file__), "..", "..", "jira_mcp", "sa-key.json"),
        "sa-key.json",
    ]

    sa_key_path = None
    for candidate in sa_key_candidates:
        if candidate:
            for check_path in [candidate, os.path.join(os.path.dirname(__file__), candidate)]:
                if os.path.exists(check_path):
                    sa_key_path = os.path.abspath(check_path)
                    break
        if sa_key_path:
            break

    if sa_key_path and mcp_url:
        try:
            import google.auth.transport.requests
            from google.oauth2 import service_account

            parsed = urlparse(mcp_url)
            target_audience = f"{parsed.scheme}://{parsed.netloc}"

            creds = _cached_id_credentials.get(target_audience)
            if creds is None:
                creds = service_account.IDTokenCredentials.from_service_account_file(
                    sa_key_path,
                    target_audience=target_audience
                )
                _cached_id_credentials[target_audience] = creds

            auth_req = google.auth.transport.requests.Request()
            if not creds.valid or creds.expired or not creds.token:
                creds.refresh(auth_req)

            if creds.token:
                logger.info(f"Successfully fetched ID token from service account key ({sa_key_path}) for audience: {target_audience}")
                return creds.token.strip()
        except Exception as e:
            logger.debug(f"Failed to fetch ID token from service account key ({sa_key_path}): {e}")
    
    logger.warning("No valid MCP token found in environment or service account key. Returning empty token.")    
    return ""


class DynamicBearerAuth(httpx.Auth):
    """HTTPX authentication handler that dynamically injects Bearer token on each request."""

    def __init__(self, token_provider):
        self.token_provider = token_provider

    def sync_auth_flow(self, request: httpx.Request):
        token = self.token_provider()
        if token:
            request.headers["Authorization"] = f"Bearer {token}".strip()
        yield request

    async def async_auth_flow(self, request: httpx.Request):
        token = self.token_provider()
        if token:
            request.headers["Authorization"] = f"Bearer {token}".strip()
        yield request


def create_jira_mcp_toolset() -> MCPToolset:
    """Configure and initialize the MCP Streamable HTTP Connection with dynamic token resolution and fallback options."""
    mcp_url = os.environ.get("JIRA_MCP_URL") or os.environ.get("MCP_URL") or "http://localhost:8000/mcp"
    logger.info(f"Initializing MCPToolset with URL: {mcp_url}")

    # Retrieve and parse authorized tools from .env (comma-separated string, default to empty [])
    tools_filter_raw = os.environ.get("JIRA_TOOLS_FILTER") or os.environ.get("TOOLS_FILTER")
    if tools_filter_raw:
        tool_filter = [t.strip() for t in tools_filter_raw.split(",") if t.strip()]
        logger.info(f"Using configured tool filter from environment: {tool_filter}")
    else:
        tool_filter = []
        logger.info(f"No tool filter configured in environment. Using default: {tool_filter}")

    # Dynamic HTTP client factory to retrieve token for each query/request to MCP
    def dynamic_http_client_factory(
        headers: dict[str, str] | None = None,
        timeout: httpx.Timeout | None = None,
        auth: httpx.Auth | None = None,
    ) -> httpx.AsyncClient:
        dynamic_auth = auth or DynamicBearerAuth(lambda: get_mcp_token(mcp_url))
        return create_mcp_http_client(
            headers=headers,
            timeout=timeout,
            auth=dynamic_auth,
        )

    streamable_http_params = StreamableHTTPConnectionParams(
        url=mcp_url,
        httpx_client_factory=dynamic_http_client_factory
    )

    # MCPToolset configuration using dynamic tool filter
    return MCPToolset(
        connection_params=streamable_http_params,
        tool_filter=tool_filter
    )


def create_model() -> any:
    """Determine model provider and model details from environment, initialize and return it."""
    model_provider = (os.environ.get("MODEL_PROVIDER") or "gemini").lower()

    if model_provider == "litellm":
        required_vars = [
            "LITELLM_API_BASE",
            "LITELLM_API_KEY",
            "LITELLM_MODEL_NAME",
            "LITELLM_TOKEN",
        ]
        missing_vars = [var for var in required_vars if not os.environ.get(var)]
        if missing_vars:
            raise ValueError(f"Required environment variables are not set: {', '.join(missing_vars)}")

        api_base = os.environ["LITELLM_API_BASE"]
        api_key = os.environ["LITELLM_API_KEY"]
        model_name = os.environ["LITELLM_MODEL_NAME"]
        token = os.environ["LITELLM_TOKEN"]
        
        from google.adk.models.lite_llm import LiteLlm
        logger.info(f"Initializing LiteLlm model with name: {model_name}")
        return LiteLlm(
            model=model_name,
            api_base=api_base,
            api_key=api_key,
            extra_headers={
                "Authorization": f"Bearer {token}"
            }
        )
    else:
        agent_model = os.environ.get("GEMINI_MODEL_NAME", "gemini-2.5-flash")
        logger.info(f"Using Gemini model with name: {agent_model}")
        return agent_model


def load_memory() -> bool:
    USE_MEMORY_BANK = os.getenv("USE_MEMORY_BANK", "false").lower() == "true"
    return USE_MEMORY_BANK


async def add_session_to_memory(callback_context: CallbackContext) -> Optional[types.Content]:
    """Automatically save completed sessions to memory bank in the background"""
    if hasattr(callback_context, "_invocation_context"):
        invocation_context = callback_context._invocation_context
        if invocation_context.memory_service:
            # Use create_task to run this in the background without blocking the response
            asyncio.create_task(
                invocation_context.memory_service.add_session_to_memory(
                    invocation_context.session
                )
            )
            logger.info("Scheduled session save to memory bank in background")
            
            
def create_agent() -> LlmAgent:
    """Create and return the main configured Jira LlmAgent."""
    
    jira_mcp_toolset = create_jira_mcp_toolset()
    model = create_model()

    tools = [jira_mcp_toolset]
    if load_memory():
        tools.append(PreloadMemoryTool())

    # Root agent configuration with MCP tools and memory capabilities
    return LlmAgent(
        model=model,
        instruction=build_instructions(),
        name='jira_agent',
        description='An agent that answers questions about Jira',
        tools=tools,
        after_agent_callback=add_session_to_memory if load_memory() else None
    )


# Perform initialization when the module is imported
load_environment_configs()

setup_logging()

root_agent = create_agent()

# Export the agent using the A2A protocol as a Starlette application (app)
#try:
#    from google.adk.a2a.utils.agent_to_a2a import to_a2a
#    agent_card_path = os.path.join(os.path.dirname(__file__), 'agent.json')
#    app = to_a2a(root_agent, agent_card=agent_card_path)
#except ImportError:
#    app = None
