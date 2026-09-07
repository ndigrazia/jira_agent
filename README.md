# Jira Assistant Agent

An intelligent assistant designed to answer questions and interact with Jira. This agent is built using the **Google GenAI SDK (ADK) framework**, managed with **uv**, and integrated with the **Model Context Protocol (MCP)** to discover and execute Jira tools dynamically.

---

## Features

- **Advanced LLM Orchestration:** Powered by Google's `LlmAgent` supporting multiple model providers and dynamic toolsets.
- **Dual Model Provider Support:** 
  - **Gemini:** Directly utilize Google Gemini models such as `gemini-2.5-flash` (default) or `gemini-1.5-pro`.
  - **LiteLLM:** Connect to any LLM provider (OpenAI, Anthropic, self-hosted LLMs, etc.) supported by `google.adk.models.lite_llm.LiteLlm`.
- **Dynamic MCP Integration:** Utilizes `McpToolset` with `StreamableHTTPConnectionParams` to connect directly to an MCP server over Streamable HTTP for real-time tool discovery and execution with Bearer token authentication.
- **Conversational Memory Integration:** Incorporates ADK conversational memory features:
  - `load_memory` tool for explicit on-demand memory retrieval by the model.
  - `after_agent_callback` (`save_session_to_memory`) to automatically persist session events and conversation history across turns.
- **Specialized Behavior Rules & Prompts:**
  - **Localized Language:** Formulates all responses in **Spanish**.
  - **Greeting & Capabilities:** Greets users on the first interaction and outlines core capabilities (issue details, summary search, assignee lookup, description search, manager search).
  - **Strict Issue Search Rule:** Enforces the use of `searchAndReconsileIssuesUsingJql` for issue lookups by summary or description.
  - **Manager Search Rule:** Enforces custom field lookups (`customfield_10390`) in JQL for manager queries.
  - **User Lookup Rule:** Enforces a two-step user discovery workflow (`findUsers` to resolve `accountId`, followed by `getUser`).
- **Configurable Tool Authorization:** Fine-grained control over allowed Jira tools via `JIRA_TOOLS_FILTER` or `TOOLS_FILTER` (comma-separated list).
- **A2A Protocol & Agent Card Generation:** Fully compatible with the Agent-to-Agent (A2A) protocol with built-in agent card export (`jira_agent/agent.json`).
- **Containerized & Cloud-Ready:** Supports Docker, Docker Compose, and Google Cloud Run deployment via `adk deploy`.

---

## Repository Structure

```text
├── .env                  # Environment variables for local development
├── pyproject.toml        # UV project configuration and dependencies
├── uv.lock               # Deterministic dependency lock file
├── Dockerfile            # Production Docker configuration
├── Dockerfile_dev        # Development Docker configuration
├── docker-compose.yml    # Docker Compose multi-container orchestration
├── generate_card.py      # Script to build and export agent card (jira_agent/agent.json)
├── test_client.py        # Python test client querying the agent over JSON-RPC
├── cloud_run/
│   ├── setup_gcp.sh      # Environment configuration script for GCP deployment
│   ├── cleanup.sh        # GCP resource teardown and cleanup script
│   └── lab.sh            # Script to deploy the agent to Google Cloud Run
└── jira_agent/
    ├── __init__.py       # Package entrypoint
    ├── agent.json        # Pre-built / exported Agent Card (A2A metadata)
    └── agent.py          # Main implementation of the Jira LlmAgent
```

---

## Configuration Options

The application is configured using environment variables defined in a `.env` file at the root or within `jira_agent/`:

| Variable | Description | Default |
|----------|-------------|---------|
| `MODEL_PROVIDER` | LLM provider framework (`gemini` or `litellm`). | `gemini` |
| `GOOGLE_API_KEY` | Google Gemini API key (required if `MODEL_PROVIDER=gemini`). | — |
| `GEMINI_MODEL_NAME` | Gemini model name identifier. | `gemini-2.5-flash` |
| `GOOGLE_GENAI_USE_ENTERPRISE` | Set to `1` or `0` for Enterprise Gemini endpoint access. | `0` |
| `LITELLM_API_BASE` | Base endpoint URL for LiteLLM proxy (required if `MODEL_PROVIDER=litellm`). | — |
| `LITELLM_API_KEY` | API key for LiteLLM provider (required if `MODEL_PROVIDER=litellm`). | — |
| `LITELLM_MODEL_NAME` | Model identifier for LiteLLM (e.g. `openai/gpt-4o`). | — |
| `LITELLM_TOKEN` | Bearer token for LiteLLM authentication headers. | — |
| `JIRA_MCP_URL` or `MCP_URL` | Endpoint of the Jira MCP Server (Streamable HTTP). | `http://localhost:8000/mcp` |
| `JIRA_MCP_TOKEN` or `MCP_TOKEN` | Bearer token used for MCP Server authentication. | `""` |
| `JIRA_TOOLS_FILTER` or `TOOLS_FILTER` | Comma-separated list of allowed Jira tool names (e.g. `getIssue,findUsers`). | `[]` (All tools allowed) |

---

## Getting Started

### Prerequisites

- **Python 3.12+**
- **uv** (Fast Python package manager)
- **Docker & Docker Compose** (Optional, for containerized execution)

### Setup

1. **Clone the repository and install dependencies:**
   ```bash
   uv sync
   ```

2. **Configure your environment variables:**
   Create a `.env` file in the project root:

   **For Gemini (Default):**
   ```env
   MODEL_PROVIDER=gemini
   GOOGLE_API_KEY=your-google-gemini-api-key
   GEMINI_MODEL_NAME=gemini-2.5-flash
   GOOGLE_GENAI_USE_ENTERPRISE=0
   JIRA_MCP_URL=http://localhost:8000/mcp
   JIRA_MCP_TOKEN=your-mcp-bearer-token
   ```

   **For LiteLLM:**
   ```env
   MODEL_PROVIDER=litellm
   LITELLM_API_BASE=https://api.openai.com/v1
   LITELLM_API_KEY=your-litellm-api-key
   LITELLM_MODEL_NAME=openai/gpt-4o
   LITELLM_TOKEN=your-litellm-bearer-token
   JIRA_MCP_URL=http://localhost:8000/mcp
   JIRA_MCP_TOKEN=your-mcp-bearer-token
   ```

---

## Code Architecture

The agent implementation in `jira_agent/agent.py` is modularized into dedicated functions:

- **`load_environment_configs()`**: Loads environment variables from `.env` files with proper fallback paths across the workspace.
- **`setup_logging()`**: Configures Python's standard `logging` with structured operational diagnostics.
- **`create_mcp_toolset()`**: Configures `McpToolset` with `StreamableHTTPConnectionParams`, Bearer token authentication headers, and dynamic tool filtering.
- **`create_model()`**: Instantiates the selected model provider (either standard Gemini models or LiteLLM wrapper with custom headers).
- **`save_session_to_memory()`**: An asynchronous `after_agent_callback` that commits session events to the active ADK memory service via `add_session_to_memory()`.
- **`create_agent()`**: Constructs the `LlmAgent` combining system prompt instructions, LLM model, MCP toolset, `load_memory` tool, and the memory persistence callback.

---

## Usage

### 1. Generating the Agent Card (`agent.json`)

To generate or update the A2A Agent Card (`jira_agent/agent.json`), execute:

```bash
uv run python generate_card.py
```

### 2. Programmatic Usage in Python

You can import and interact with the configured `root_agent` inside your Python workflow:

```python
from jira_agent.agent import root_agent

# Examine configured agent properties
print(f"Agent Name: {root_agent.name}")
print(f"Model: {root_agent.model}")
print(f"Description: {root_agent.description}")
print(f"Instruction: {root_agent.instruction}")
```

### 3. Logging & Diagnostics

Upon startup, the agent outputs diagnostic logs detailing:
- MCP Server connection URL
- Configured active tool filters
- Model provider and model name selection
- Agent initialization statuses

---

## Running with Docker

You can build and run the containerized Jira Assistant Agent using Docker or Docker Compose.

### Dockerfile Patch Details
A known issue in the `google-adk` package causes an `UnboundLocalError` (`cannot access local variable 'json' where it is not associated with a value`) during the initialization of the A2A agent. Both `Dockerfile` and `Dockerfile_dev` include an automated patch step during build time to ensure seamless container execution.

### Using Docker Compose (Recommended)

Start the agent container with environment variables loaded from `.env`:

```bash
docker-compose up -d --build
```

To stop the agent container:

```bash
docker-compose down
```

### Using Docker CLI

1. **Build the image:**
   ```bash
   docker build -f Dockerfile -t jira-agent-a2a .
   ```

2. **Run the container:**
   ```bash
   docker run --name jira-agent-a2a-container -d -p 8080:8080 --env-file .env jira-agent-a2a
   ```

3. **Check container logs:**
   ```bash
   docker logs jira-agent-a2a-container
   ```

   Expected output:
   ```text
   INFO - Successfully configured A2A agent: jira_agent
   INFO:     Started server process
   INFO:     Uvicorn running on http://0.0.0.0:8080
   ```

4. **Verify the Agent Card endpoint:**
   ```bash
   curl http://localhost:8080/a2a/jira_agent/.well-known/agent-card.json
   ```

---

## Testing with the Python Test Client

A dedicated test client is provided in `test_client.py` to query the agent API server using a standardized JSON-RPC `message/send` payload.

Run the test client:

```bash
uv run python test_client.py
```

The test client sends a query to the agent endpoint and outputs the structured response payload returned by the container.

---

## Deployment to Google Cloud Run

Deployment scripts and configuration files for Google Cloud Run are located in `cloud_run/`:

1. **Set up GCP configuration (`cloud_run/setup_gcp.sh`):**
   ```bash
   export GOOGLE_CLOUD_PROJECT="your-gcp-project-id"
   export GOOGLE_CLOUD_LOCATION="us-central1"
   export GOOGLE_API_KEY="your-gemini-api-key"
   ```

2. **Deploy using ADK CLI:**
   ```bash
   cd cloud_run
   bash lab.sh
   ```

3. **Teardown / Cleanup resources:**
   ```bash
   cd cloud_run
   bash cleanup.sh
   ```
