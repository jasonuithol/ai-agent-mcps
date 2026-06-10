#!/usr/bin/env bash
# start.sh — bring up the mcp-ue4ss knowledge container.
# Idempotent: revives an existing container or creates a new one.
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

# Ensure image is built (idempotent — setup.sh skips already-built images).
# Orchestrators should self-heal, not fail with "go run X first".
"$SCRIPT_DIR/setup.sh"

echo "Starting ue4ss-mcp-knowledge..."
"$SCRIPT_DIR/knowledge/start-container.sh"

echo "Done. Service on :5196 (knowledge)."
