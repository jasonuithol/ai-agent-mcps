#!/usr/bin/env bash
# start.sh — bring up the mcp-ssis container.
# Idempotent: revives an existing container or creates a new one.
#
# This service expects the mcp-db mssql container to be running for
# benchmark reset_sql to work. It does NOT depend on it for validate /
# run — packages with self-contained connection managers will work fine
# either way.
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

"$SCRIPT_DIR/setup.sh"

echo "Starting db-mcp-ssis..."
"$SCRIPT_DIR/ssis/start-container.sh"

echo "Done. MCP on :5190. Packages dir: $SCRIPT_DIR/packages"
