#!/usr/bin/env bash
# start-container.sh — run the db-mcp-postgres container
#
# Persists PostgreSQL data across container lifetimes via the named volume
# 'db-mcp-postgres-data'. Removed only by ../clean.sh.
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

CONTAINER_NAME="db-mcp-postgres"
IMAGE_NAME="db-mcp-postgres"
VOLUME_NAME="db-mcp-postgres-data"
PORT=5188
PG_PORT=5432

# Revive a leftover container from a prior run if one exists; otherwise
# create a fresh one. Bridge networking — we publish the MCP port and the
# PostgreSQL port so host-side tools (psql, dbeaver, etc.) can connect
# directly bypassing the MCP transport.
if docker container inspect "$CONTAINER_NAME" >/dev/null 2>&1; then
    docker start "$CONTAINER_NAME" >/dev/null
else
    docker volume inspect "$VOLUME_NAME" >/dev/null 2>&1 || docker volume create "$VOLUME_NAME" >/dev/null
    docker run -d \
        --name "$CONTAINER_NAME" \
        -p "$PORT:$PORT" \
        -p "$PG_PORT:$PG_PORT" \
        -v "$VOLUME_NAME:/var/lib/postgresql/data" \
        "$IMAGE_NAME"
fi
