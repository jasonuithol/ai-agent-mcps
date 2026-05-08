#!/usr/bin/env bash
# start-container.sh — run the db-mcp-mssql container
#
# Persists SQL Server data via the named volume 'db-mcp-mssql-data'.
# Removed only by ../clean.sh.
#
# The SA password is a local-dev value. Both the MCP transport (5189) and
# SQL Server itself (1433) are published, so host-side tools can connect
# directly. Override the SA password via the MSSQL_SA_PASSWORD env var.
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

CONTAINER_NAME="db-mcp-mssql"
IMAGE_NAME="db-mcp-mssql"
VOLUME_NAME="db-mcp-mssql-data"
PORT=5189
MSSQL_PORT=1433

# Default dev password — must satisfy SQL Server's strong-password policy
# (>=8 chars, three of: upper, lower, digit, symbol). Override via env.
SA_PASSWORD="${MSSQL_SA_PASSWORD:-DevP@ssw0rd!42}"

if docker container inspect "$CONTAINER_NAME" >/dev/null 2>&1; then
    docker start "$CONTAINER_NAME" >/dev/null
else
    docker volume inspect "$VOLUME_NAME" >/dev/null 2>&1 || docker volume create "$VOLUME_NAME" >/dev/null
    docker run -d \
        --name "$CONTAINER_NAME" \
        -p "$PORT:$PORT" \
        -p "$MSSQL_PORT:$MSSQL_PORT" \
        -e "ACCEPT_EULA=Y" \
        -e "MSSQL_SA_PASSWORD=$SA_PASSWORD" \
        -e "MSSQL_PID=Developer" \
        -v "$VOLUME_NAME:/var/opt/mssql" \
        "$IMAGE_NAME"
fi
