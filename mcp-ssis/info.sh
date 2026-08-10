#!/usr/bin/env bash
# info.sh — print connection details for the SSIS MCP service.
#
# Default host is `host.containers.internal` (the view from a sibling
# container, e.g. the claude-sandbox). Override with HOST=localhost when
# pointing at it from the host machine.
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

HOST="${HOST:-host.containers.internal}"
MCP_PORT=5190
PACKAGES_DIR="${PACKAGES_DIR:-$SCRIPT_DIR/packages}"
PEER_MSSQL_HOST="${MSSQL_HOST:-host.containers.internal}"
PEER_MSSQL_PORT="${MSSQL_PORT:-1433}"

cat <<EOF
ssis
  mcp url:        http://$HOST:$MCP_PORT/mcp
  packages dir:   $PACKAGES_DIR  (drop .dtsx files here)
  logs dir:       $PACKAGES_DIR/logs
  peer mssql:     $PEER_MSSQL_HOST:$PEER_MSSQL_PORT  (used for benchmark reset_sql)

Register with Claude Code:
  claude mcp add db-ssis --transport http http://localhost:$MCP_PORT/mcp

(Override host with HOST=localhost ./info.sh)
EOF
