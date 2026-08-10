#!/usr/bin/env bash
# start.sh — bring up both mcp-chess containers.
# Idempotent: each inner script revives an existing container or creates a new one.
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

# Ensure images are built (idempotent — setup.sh skips already-built images).
# Orchestrators should self-heal, not fail with "go run X first".
"$SCRIPT_DIR/setup.sh"

echo "Starting chess-mcp-engine..."
"$SCRIPT_DIR/service/start-container.sh"

echo "Starting chess-mcp-knowledge..."
"$SCRIPT_DIR/knowledge/start-container.sh"

echo "Done. Services on :5180 (engine) and :5186 (knowledge)."
