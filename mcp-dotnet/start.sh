#!/usr/bin/env bash
# start.sh — bring up both mcp-dotnet containers.
# Self-heals: calls setup.sh first so a missing volume or image gets created.
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

"$SCRIPT_DIR/setup.sh"

echo "Starting dotnet-mcp-build..."
"$SCRIPT_DIR/service/start-container.sh"

echo "Starting dotnet-mcp-knowledge..."
"$SCRIPT_DIR/knowledge/start-container.sh"

echo "Done. Services on :5202 (build) and :5204 (knowledge)."
