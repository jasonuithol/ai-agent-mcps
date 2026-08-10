#!/usr/bin/env bash
# start.sh — bring up both db-mcp containers.
# Idempotent: each inner script revives an existing container or creates a new one.
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

# Ensure images are built (idempotent — setup.sh skips already-built images).
"$SCRIPT_DIR/setup.sh"

echo "Starting db-mcp-postgres..."
"$SCRIPT_DIR/postgres/start-container.sh"

echo "Starting db-mcp-mssql..."
"$SCRIPT_DIR/mssql/start-container.sh"

echo "Done. MCP on :5188 (postgres) and :5189 (mssql); DBs on :5432 and :1433."
