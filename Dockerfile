# Use a lightweight Python base image
FROM python:3.12-slim

# Copy the uv executable from the official image
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

# Set working directory
WORKDIR /app

# Copy dependency files first to leverage Docker layer caching
COPY pyproject.toml uv.lock ./

# Install dependencies using uv sync
RUN uv sync --frozen --no-cache

# Patch google-adk fast_api.py file to fix UnboundLocalError regarding 'json'
RUN uv run python -c "import pathlib; p = pathlib.Path('.venv/lib/python3.12/site-packages/google/adk/cli/fast_api.py'); content = p.read_text(); p.write_text(content.replace('    import json\n', ''))"

# Copy the rest of the application files
COPY . .

# Expose port 8081 (as configured in agent.json)
ENV PORT=8081

EXPOSE 8081

# Run the app using uvicorn via uv run
CMD ["uv", "run", "adk", "api_server", "--a2a", "--host", "0.0.0.0", "--port", "8081", "."]
#CMD sh -c "uv run adk api_server --a2a --host 0.0.0.0 --port ${PORT:-8081}"