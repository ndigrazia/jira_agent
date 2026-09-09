# Jira Assistant Agent

An intelligent assistant designed to answer questions and interact with Jira. This agent is built using the **Google GenAI SDK (ADK) framework**, managed with **uv**, and integrated with the **Model Context Protocol (MCP)** to discover and execute Jira tools dynamically over Streamable HTTP. It features long-term conversational memory powered by **Vertex AI Memory Bank** and flexible LLM orchestration supporting both Google Gemini and LiteLLM.

---

## Features

- **Advanced LLM Orchestration:** Powered by Google's `LlmAgent` supporting multiple model providers, structured system instructions, and dynamic toolsets.
- **Dual Model Provider Support:** 
  - **Gemini:** Directly utilize Google Gemini models such as `gemini-2.5-flash` (default) or `gemini-1.5-pro`.
  - **LiteLLM:** Connect to any LLM provider (OpenAI, Anthropic, self-hosted LLMs, etc.) supported by `google.adk.models.lite_llm.LiteLlm`.
- **Dynamic MCP Integration:** Utilizes `McpToolset` with `StreamableHTTPConnectionParams` to connect directly to an MCP server over Streamable HTTP for real-time tool discovery and execution with Bearer token authentication.
- **Conversational Memory Integration:** Incorporates ADK conversational memory features with **Vertex AI Memory Bank**:
  - `PreloadMemoryTool` (`load_memory`) enables explicit on-demand retrieval of user details, conversation history, and past queries.
  - Asynchronous `after_agent_callback` (`add_session_to_memory`) automatically persists session events and conversation history to the memory bank in the background.
  - Enabled conditionally via the `USE_MEMORY_BANK` environment variable.
- **Specialized Behavior Rules & Prompts (`jira_agent/prompts.py`):**
  - **Localized Language:** Formulates all responses in **Spanish** (or responds with `"No lo sé"` when unknown).
  - **User Context & Identity Recall:** Remembers user identity, name, role, preferences, and past queries across interactions by calling the memory tool.
  - **Greeting & Capabilities:** Greets users on the first interaction and outlines the 6 core capabilities:
    1. Retrieve details of a specific issue.
    2. Search issues based on a summary.
    3. Retrieve issues assigned to a user.
    4. Search issues based on a description.
    5. Search issues based on manager information.
    6. Retrieve all issues assigned to a parent issue (including child issues).
  - **Topic Scope Rule:** Restricts conversation to Jira topics, user identity, and conversation context, politely refusing unrelated topics.
  - **Strict Issue Search Rule:** Enforces the use of `searchAndReconsileIssuesUsingJql` for issue lookups by summary or description.
  - **Issue Status Search Rule:** Restricts status filtering strictly to `statusCategory` values (`"To Do"`, `"In Progress"`, and `"Done"`).
  - **Manager Search Rule:** Enforces custom field lookups (`customfield_10390`) in JQL for manager queries (accepting name, surname, or full name).
  - **User Lookup Rule:** Enforces a two-step user discovery workflow (`findUsers` to resolve `accountId`, followed by `getUser`).
  - **Parent / Child Issues Search Rule:** Queries child issues using `parent = <issue_key>` via `searchAndReconsileIssuesUsingJql`.
  - **Multiple Issue Details Rule:** Enforces individual `getIssue` tool calls for each issue ID when multiple issue details are requested.
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
├── memory_bank/
│   ├── create_memory_bank.py # Utility script to create a Vertex AI Memory Bank / Agent Engine
│   └── query_memory_bank.py  # Utility script to list existing Vertex AI Agent Engines
└── jira_agent/
    ├── __init__.py       # Package entrypoint
    ├── agent.json        # Pre-built / exported Agent Card (A2A metadata)
    ├── agent.py          # Main implementation of the Jira LlmAgent
    └── prompts.py        # System instructions, behavior rules, and prompt definitions
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
| `USE_MEMORY_BANK` | Enable/disable ADK conversational memory tools and persistence (`true` or `false`). | `false` |
| `VERTEX_AI_AGENT_ENGINE_ID` or `AGENT_ENGINE_ID` | Reasoning Engine / Agent Engine ID for Vertex AI Memory Bank. | — |
| `GOOGLE_CLOUD_PROJECT` | Google Cloud Project ID for Vertex AI Memory Bank and GCP deployment. | — |
| `GOOGLE_CLOUD_LOCATION` | Google Cloud region for Vertex AI Memory Bank. | `us-central1` |
| `EXPRESS_MODE_API_KEY` | Optional Express Mode API key for Vertex AI Memory Bank. | — |
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
- **Google Cloud SDK (`gcloud`)** (Optional, for Vertex AI Memory Bank and Cloud Run deployment)

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
   USE_MEMORY_BANK=true
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
   USE_MEMORY_BANK=true
   JIRA_MCP_URL=http://localhost:8000/mcp
   JIRA_MCP_TOKEN=your-mcp-bearer-token
   ```

---

## Conversational Memory Bank Setup

The agent integrates with Vertex AI Memory Bank to retain user context and previous questions across conversational turns.

### 1. Create a Memory Bank
Run the creation script to provision a new Vertex AI Agent Engine with memory bank context:

```bash
uv run python memory_bank/create_memory_bank.py
```

*Note: Edit `PROJECT_ID` and `LOCATION` in `memory_bank/create_memory_bank.py` to match your GCP project configuration.*

### 2. Query Existing Memory Banks
To list active memory banks / agent engines in your project:

```bash
uv run python memory_bank/query_memory_bank.py
```

### 3. Run with ADK Web UI and Memory Bank
You can launch the interactive ADK Web interface with your memory bank connected:

```bash
uv run adk web --memory_service_uri agentengine://<YOUR_ENGINE_ID> .
```

---

## Code Architecture

The agent implementation is organized into modular components across `jira_agent/agent.py` and `jira_agent/prompts.py`:

### `jira_agent/agent.py`
- **`load_environment_configs()`**: Loads environment variables from `.env` files with fallback paths across the workspace.
- **`setup_logging()`**: Configures Python's standard `logging` with structured operational diagnostics.
- **`create_mcp_toolset()`**: Configures `McpToolset` with `StreamableHTTPConnectionParams`, Bearer token authentication headers, and dynamic tool filtering.
- **`create_model()`**: Instantiates the selected model provider (either standard Gemini models or LiteLLM wrapper with custom headers).
- **`load_memory()`**: Evaluates the `USE_MEMORY_BANK` environment variable to determine if conversational memory is enabled.
- **`add_session_to_memory(callback_context)`**: Asynchronous `after_agent_callback` that schedules background session persistence to the active `memory_service`.
- **`create_agent()`**: Constructs the `LlmAgent` combining system prompt instructions (`build_instructions()`), LLM model, MCP toolset, `PreloadMemoryTool()`, and memory persistence callbacks.

### `jira_agent/prompts.py`
- **`BASE_INSTRUCTIONS`**: Centralized, comprehensive system instruction definitions governing Spanish response formatting, user context recall, capabilities greeting, and deterministic rules for Jira tool execution.
- **`build_instructions()`**: Returns the formatted instruction string used by `create_agent()`.

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
