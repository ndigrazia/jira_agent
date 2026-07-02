import os
import logging
from google.adk.agents.llm_agent import LlmAgent
from google.adk.tools.mcp_tool import McpToolset, StreamableHTTPConnectionParams
from dotenv import load_dotenv

# System instructions for the Jira Assistant.
# Cleaned of leading/trailing indentation/whitespace for optimal prompt quality.
SYSTEM_INSTRUCTION = (
    "You are a Jira assistant. You will be given a user question and you should answer it to the best of "
    "your knowledge. If you don't know the answer, say 'I don't know'. You must only answer questions "
    "related to Jira. If a query is not related to Jira, refuse to answer it politely. You must always "
    "answer in Spanish."
).strip()

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


def create_mcp_toolset() -> McpToolset:
    """Configure and initialize the MCP Streamable HTTP Connection with fallback options and logging."""
    mcp_url = os.environ.get("JIRA_MCP_URL") or os.environ.get("MCP_URL") or "http://localhost:8000/mcp"
    logger.info(f"Initializing McpToolset with URL: {mcp_url}")

    # Retrieve and parse authorized tools from .env (comma-separated string, default to empty [])
    tools_filter_raw = os.environ.get("JIRA_TOOLS_FILTER") or os.environ.get("TOOLS_FILTER")
    if tools_filter_raw:
        tool_filter = [t.strip() for t in tools_filter_raw.split(",") if t.strip()]
        logger.info(f"Using configured tool filter from environment: {tool_filter}")
    else:
        tool_filter = []
        logger.info(f"No tool filter configured in environment. Using default: {tool_filter}")

    # Retrieve MCP token from environment (defaulting to empty string if not present)
    mcp_token = os.environ.get("JIRA_MCP_TOKEN") or os.environ.get("MCP_TOKEN") or ""
    headers = {"Authorization": f"Bearer {mcp_token}".strip()}

    streamable_http_params = StreamableHTTPConnectionParams(
        url=mcp_url,
        headers=headers
    )

    # McpToolset configuration using dynamic tool filter
    return McpToolset(
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


def create_agent() -> LlmAgent:
    """Create and return the main configured Jira LlmAgent."""
    mcp_toolset = create_mcp_toolset()
    model = create_model()

    # Root agent configuration
    return LlmAgent(
        model=model,
        instruction=SYSTEM_INSTRUCTION,
        name='jira_agent',
        description='An agent that answers questions about Jira',
        tools=[mcp_toolset],
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
