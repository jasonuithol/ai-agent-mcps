#!/usr/bin/env bash
# start-container.sh — run the dotnet-mcp-build container.
#
# Revives a leftover container from a prior run if one exists; otherwise
# creates a fresh one. SDKs and NuGet state live in named volumes so
# install_sdk / add_feed survive restart.
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

if [ -f "$SCRIPT_DIR/.env" ]; then
    set -a
    source "$SCRIPT_DIR/.env"
    set +a
fi

CONTAINER_NAME="dotnet-mcp-build"

if docker container inspect "$CONTAINER_NAME" >/dev/null 2>&1; then
    docker start "$CONTAINER_NAME" >/dev/null
else
    docker run -d \
        --name "$CONTAINER_NAME" \
        --network host \
        -v "$HOME/Projects:/opt/projects" \
        -v mcp-dotnet-sdks:/opt/dotnet \
        -v mcp-dotnet-nuget:/opt/nuget \
        -e PROJECTS_DIR=/opt/projects \
        -e DOTNET_ROOT=/opt/dotnet \
        -e PATH=/opt/dotnet:/opt/dotnet/tools:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin \
        -e DOTNET_CLI_TELEMETRY_OPTOUT=1 \
        -e DOTNET_NOLOGO=1 \
        -e NUGET_PACKAGES=/opt/nuget/packages \
        -e KNOWLEDGE_URL=http://localhost:5204/ingest \
        dotnet-mcp-build
fi
