FROM python:3.12-slim-bookworm

LABEL maintainer="mcp-pygame"
LABEL description="Python / pygame build + test tools MCP server"

# System deps: build essentials so pygame-ce wheels with fallbacks compile if needed,
# SDL libs so the dummy video driver actually has SDL present, curl for debugging.
RUN apt-get update && apt-get install -y --no-install-recommends \
    curl \
    ca-certificates \
    build-essential \
    libsdl2-dev \
    libsdl2-image-dev \
    libsdl2-mixer-dev \
    libsdl2-ttf-dev \
    && rm -rf /var/lib/apt/lists/*

# Python deps for the MCP service itself. pytest/ruff are not installed here —
# they go into each project's .venv-mcp so per-project versions can differ.
RUN pip install --no-cache-dir \
    "mcp>=2,<3" \
    "mcp-knowledge-base @ https://github.com/jasonuithol/ai-agent-mcps/archive/refs/tags/kb-v0.3.0.tar.gz#subdirectory=mcp-knowledge-base"

WORKDIR /app
COPY mcp-service.py .

EXPOSE 5172

CMD ["python", "mcp-service.py"]
