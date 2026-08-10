FROM python:3.12-slim-bookworm

LABEL maintainer="mcp-valheim"
LABEL description="Valheim mod ops (Thunderstore package/publish/download + BepInEx deploy) MCP server"

# ── System dependencies ───────────────────────────────────────────────────────
#
# librsvg2-bin: convert_svg (Thunderstore icon SVG → PNG)
# curl/ca-certificates: httpx HTTPS connections to Thunderstore
RUN apt-get update && apt-get install -y --no-install-recommends \
    curl \
    ca-certificates \
    librsvg2-bin \
    && rm -rf /var/lib/apt/lists/*

# ── Python dependencies ───────────────────────────────────────────────────────
#
# Generic `dotnet build` + `ilspycmd` decompile moved to the sibling
# mcp-dotnet service (port 5202). Building Valheim mods is now a two-step
# workflow: `dotnet build` via mcp-dotnet, then `deploy_*` / `package` /
# `publish` here.

RUN pip install --no-cache-dir \
    fastmcp \
    httpx \
    "mcp-knowledge-base @ https://github.com/jasonuithol/mcp-knowledge-base/archive/refs/tags/v0.2.1.tar.gz"

# ── App ───────────────────────────────────────────────────────────────────────

WORKDIR /app
COPY mcp-service.py .

EXPOSE 5182

CMD ["python", "mcp-service.py"]
