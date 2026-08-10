#!/usr/bin/env bash
# start-container.sh — run the chess-mcp-engine container
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

# Load .env if present (reserved for future use)
if [ -f "$SCRIPT_DIR/.env" ]; then
    set -a
    source "$SCRIPT_DIR/.env"
    set +a
fi

CONTAINER_NAME="chess-mcp-engine"

# Revive a leftover container from a prior run if one exists; otherwise
# create a fresh one. Engine binaries under test are mounted read-only at
# /opt/projects so register_engine can address them by absolute path.
if docker container inspect "$CONTAINER_NAME" >/dev/null 2>&1; then
    docker start "$CONTAINER_NAME" >/dev/null
else
    docker run -d \
        --name "$CONTAINER_NAME" \
        --network host \
        -v "$HOME/Projects:/opt/projects:ro" \
        -e PROJECTS_DIR=/opt/projects \
        -e KNOWLEDGE_URL=http://localhost:5186/ingest \
        chess-mcp-engine
fi
