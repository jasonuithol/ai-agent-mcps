#!/usr/bin/env bash
# start-container.sh — run the valheim-mod MCP container
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

# Load .env if present (for THUNDERSTORE_TOKEN etc.)
if [ -f "$SCRIPT_DIR/.env" ]; then
    set -a
    source "$SCRIPT_DIR/.env"
    set +a
fi

CONTAINER_NAME="valheim-mcp-mod"

# Always recreate the container so mount/env changes take effect. Reviving a
# leftover container silently keeps stale config from a previous image build.
docker rm -f "$CONTAINER_NAME" >/dev/null 2>&1 || true
docker run -d \
    --name "$CONTAINER_NAME" \
    --network host \
    -v "$HOME/.steam/steam/steamapps/common/Valheim dedicated server:/opt/valheim-server" \
    -v "$HOME/.steam/steam/steamapps/common/Valheim:/opt/valheim-client" \
    -v "$HOME/Projects:/opt/projects" \
    -v "$HOME/Projects/claude-sandbox-core/workspaces/valheim:/opt/workspace" \
    -e VALHEIM_SERVER_DIR=/opt/valheim-server \
    -e VALHEIM_CLIENT_DIR=/opt/valheim-client \
    -e VALHEIM_PROJECT_DIR=/opt/projects \
    -e VALHEIM_LOGS_DIR=/opt/workspace/valheim/logs \
    -e KNOWLEDGE_URL=http://localhost:5184/ingest \
    ${THUNDERSTORE_TOKEN:+-e THUNDERSTORE_TOKEN="$THUNDERSTORE_TOKEN"} \
    valheim-mcp-mod
