# Jira Assistant Agent

An intelligent assistant designed to answer questions about Jira. This agent is built using the **Google GenAI SDK (ADK) framework**, managed with **uv**, and integrated with the Model Context Protocol (MCP) to access Jira tools dynamically.

---

## Features

- **Advanced LLM Orchestration:** Powered by Google's `LlmAgent` supporting multiple model providers.
- **Dual Model Provider Support:** 
  - **Gemini:** Directly utilize Google's models like `gemini-3.5-flash` (default).
  - **LiteLLM:** Plug in any LLM provider (e.g., OpenAI, Anthropic, etc.) supported by the `LiteLlm` model wrapper from `google.adk.models.lite_llm`.
- **Dynamic MCP Integration:** Utilizes `McpToolset` with `SseConnectionParams` to connect directly to a Model Context Protocol (MCP) server over SSE (Server-Sent Events) for real-time tool discovery and execution.
- **Configurable Tool Authorization:** Allows fine-grained control over which tools the agent is permitted to use via the `JIRA_TOOLS_FILTER` or `TOOLS_FILTER` environment variable (comma-separated list of tool names).
- **Localized Response Support:** Tailored with robust system instructions ensuring the agent always formulates its responses in **Spanish**.
- **Structured Runtime Logging:** Out-of-the-box standard Python `logging` configuration for clear visibility and debugging of model and MCP connectivity actions.
- **Modern Package Management:** Seamlessly managed using [uv](https://github.com/astral-sh/uv) with defined pyproject dependencies.

---

## Repository Structure

```text
├── .env                  # Development environment variables
├── pyproject.toml        # UV project configuration and dependencies
├── uv.lock               # Deterministic dependency lock file
├── Dockerfile            # Production Docker configuration
├── Dockerfile_a2a        # Alternative A2A Docker configuration
├── docker-compose.yml    # Docker Compose multi-container orchestration
└── jira_agent/
    ├── __init__.py       # Package entrypoint
    ├── .gitignore        # Local ignore rules
    └── agent.py          # Main implementation of the Jira LlmAgent
```

---

## Configuration Options

The application is highly configurable through environment variables. You can specify these variables in a `.env` file at the root or within the `jira_agent/` directory:

| Variable | Description | Default |
|----------|-------------|---------|
| `GOOGLE_API_KEY` | Your Google Gemini API credentials. | *Required* (if using Gemini) |
| `MODEL_PROVIDER` | The LLM provider framework to use (`gemini` or `litellm`). | `gemini` |
| `MODEL_NAME` | The exact identifier for the model (e.g., `gemini-3.5-flash` or `openai/gpt-4o`). | `gemini-3.5-flash` (for Gemini) or `openai/gpt-4o` (for LiteLLM) |
| `JIRA_MCP_URL` or `MCP_URL` | The endpoint of your Jira MCP Server supporting SSE. | `http://localhost:8000/sse` |
| `JIRA_TOOLS_FILTER` or `TOOLS_FILTER` | Comma-separated list of allowed Jira tools (e.g., `getIssue,getBoard`). | `[]` (Allows all tools if empty) |

---

## Getting Started

### Prerequisites

- **Python 3.12+**
- **uv** (Fast Python Package Installer and Resolver)

### Setup

1. **Clone the repository and install dependencies:**
   ```bash
   uv sync
   ```

2. **Configure your environment variables:**
   Create a `.env` file in the project root:

   **For Gemini (Default):**
   ```env
   GOOGLE_API_KEY=your-gemini-api-key
   MODEL_PROVIDER=gemini
   MODEL_NAME=gemini-3.5-flash
   JIRA_MCP_URL=http://localhost:8000/sse
   ```

   **For LiteLLM (e.g., OpenAI):**
   ```env
   OPENAI_API_KEY=your-openai-api-key
   MODEL_PROVIDER=litellm
   MODEL_NAME=openai/gpt-4o
   JIRA_MCP_URL=http://localhost:8000/sse
   ```

---

## Code Architecture

The agent code in `jira_agent/agent.py` is semantically structured into separate functions to improve modularity, readability, and ease of testing:

- **`load_environment_configs()`**: Loads environment variables from `.env` files with proper fallback paths.
- **`setup_logging()`**: Configures the standard Python `logging` framework.
- **`create_mcp_toolset()`**: Initializes and configures the `McpToolset` with connection parameters and dynamic tool filtering.
- **`create_model()`**: Validates and dynamically configures the LLM provider (either standard Gemini models or LiteLLM wrapper).
- **`create_agent()`**: Combines the prompt instructions, LLM model, and MCP toolset to build and return the configured `LlmAgent`.

---

## Usage

You can import and interact with the configured `root_agent` inside your Python workflow:

```python
from jira_agent.agent import root_agent

# Examine the configured agent properties
print(f"Agent Name: {root_agent.name}")
print(f"Model: {root_agent.model}")
print(f"System Instruction: {root_agent.instruction}")

# Use root_agent inside your application flow to handle queries
# (Make sure your environment variables and MCP Server are active)
```

### Logging & Diagnostics

The agent outputs clear operational logs showing configuration details upon initialization:
- McpToolset connection endpoints
- Current active tool filters
- Model provider and model name selection
- Initialization statuses

---

## Running with Docker

You can build and execute the Jira Assistant Agent containerized using Docker or Docker Compose.

### Dockerfile Patch Details
A known issue in the `google-adk` package causes an `UnboundLocalError` (`cannot access local variable 'json' where it is not associated with a value`) during the initialization of the A2A agent. To resolve this, both `Dockerfile` and `Dockerfile_a2a` include a patch step to automatically fix the file structure after dependency synchronization.

### Using Docker Compose (Recommended)
We provide a `docker-compose.yml` file to build and run the agent easily with your environment configurations loaded from the `.env` file.

To start the agent:
```bash
docker-compose up -d --build
```

To stop the agent:
```bash
docker-compose down
```

---

### Using Docker CLI

#### Build the Image
To build the Docker image with the ADK runtime manually:
```bash
docker build -f Dockerfile -t jira-agent-a2a .
```

#### Run the Container
Run the container mapping the required port (default `8081`):
```bash
docker run --name jira-agent-a2a-container -d -p 8081:8081 jira-agent-a2a
```

### Verify Status
Check the logs of the running container to ensure the A2A agent configured successfully without errors:
```bash
docker logs jira-agent-a2a-container
```

You should see log lines indicating:
```text
INFO - Successfully configured A2A agent: jira_agent
INFO:     Started server process
INFO:     Uvicorn running on http://0.0.0.0:8081
```

You can also retrieve the well-known agent-card using `curl`:
```bash
curl http://localhost:8081/a2a/jira_agent/.well-known/agent-card.json
```

---

## Testing the Agent with the Python Test Client

We have created a dedicated test client (`test_client.py`) that queries the agent API server using a standardized JSON-RPC `message/send` payload.

To run the test client and get a live response:
```bash
uv run python test_client.py
```

It sends a query in Spanish and displays the JSON-RPC response returned by the container.
