#!/usr/bin/env bash
# start-container.sh — run the db-mcp-ssis container
#
# Connects to a peer db-mcp-mssql container (from the mcp-db repo) over
# host.containers.internal:1433. Override MSSQL_HOST / MSSQL_PORT /
# MSSQL_SA_PASSWORD to point at a different SQL Server instance.
#
# Host directory ../packages is bind-mounted at /packages so users can
# drop .dtsx files and dtsConfig files in from outside the container.
# Logs land under packages/logs/.
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO_ROOT="$(cd "$SCRIPT_DIR/.." && pwd)"

CONTAINER_NAME="db-mcp-ssis"
IMAGE_NAME="db-mcp-ssis"
PORT=5190

PACKAGES_HOST_DIR="${PACKAGES_DIR:-$REPO_ROOT/packages}"
MSSQL_HOST="${MSSQL_HOST:-host.containers.internal}"
MSSQL_PORT="${MSSQL_PORT:-1433}"
MSSQL_USER="${MSSQL_USER:-sa}"
SA_PASSWORD="${MSSQL_SA_PASSWORD:-DevP@ssw0rd!42}"

# Ensure the host packages dir exists before bind-mounting — docker would
# otherwise auto-create it as root, which then locks the user out.
mkdir -p "$PACKAGES_HOST_DIR/logs"

if docker container inspect "$CONTAINER_NAME" >/dev/null 2>&1; then
    docker start "$CONTAINER_NAME" >/dev/null
else
    docker run -d \
        --name "$CONTAINER_NAME" \
        --add-host="host.containers.internal:host-gateway" \
        -p "$PORT:$PORT" \
        -e "MSSQL_HOST=$MSSQL_HOST" \
        -e "MSSQL_PORT=$MSSQL_PORT" \
        -e "MSSQL_USER=$MSSQL_USER" \
        -e "MSSQL_SA_PASSWORD=$SA_PASSWORD" \
        -e "PACKAGES_DIR=/packages" \
        -v "$PACKAGES_HOST_DIR:/packages" \
        "$IMAGE_NAME"
fi
