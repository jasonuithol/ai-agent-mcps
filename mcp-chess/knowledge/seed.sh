#!/usr/bin/env bash
# seed.sh — seed the chess-knowledge database with curated docs.
# Run from the host. Requires chess-mcp-knowledge (port 5186) running.
#
# Sources (each only if present on the host):
#   docs/                       — any handwritten notes (topic=mcp-chess)
#   docs/chessprogramming/      — chessprogramming.org wiki cache
#                                 (populate via ingest-chessprogramming.sh)
#
# seed_docs upserts on content hash, so the LAST write to a given doc
# wins for both content and metadata. The catch-all pass tags everything
# 'mcp-chess'; the per-topic pass then overwrites chessprogramming/ docs
# with the specific topic so query-time topic filtering works.
set -euo pipefail

BASE="http://localhost:5186/mcp"
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO_DIR="$(cd "$SCRIPT_DIR/.." && pwd)"

# ---------------------------------------------------------------------------
# MCP session helpers
# ---------------------------------------------------------------------------

get_session() {
    local url="$1"
    curl -si -X POST "$url" \
        -H 'Content-Type: application/json' \
        -H 'Accept: application/json, text/event-stream' \
        -d '{"jsonrpc":"2.0","id":1,"method":"initialize","params":{"protocolVersion":"2024-11-05","capabilities":{},"clientInfo":{"name":"seed","version":"0"}}}' \
        2>/dev/null | grep -i 'mcp-session-id' | tr -d '\r' | awk '{print $2}'
}

call_tool() {
    local url="$1"
    local session="$2"
    local id="$3"
    local name="$4"
    local args="$5"
    # seed_docs over thousands of chunks on CPU embedding can take 10+ min.
    # 300s was the FastMCP default but isn't enough for large corpora.
    local max_time="${6:-3600}"
    RESPONSE=$(echo "{\"jsonrpc\":\"2.0\",\"id\":$id,\"method\":\"tools/call\",\"params\":{\"name\":\"$name\",\"arguments\":$args}}" \
        | curl -s -X POST "$url" \
            -H 'Content-Type: application/json' \
            -H 'Accept: application/json, text/event-stream' \
            -H "mcp-session-id: $session" \
            --data-binary @- \
            --max-time "$max_time")
    echo "$RESPONSE" | grep '^data:' | tail -1 | sed 's/^data: //' | python3 -c "
import sys, json
try:
    d = json.load(sys.stdin)
    for c in d.get('result',{}).get('content',[]):
        if c.get('type')=='text': print(c['text'])
except: print('(parse error)')
" 2>/dev/null || echo "(no response)"
}

# ---------------------------------------------------------------------------
# Get session
# ---------------------------------------------------------------------------

echo "Connecting to chess-mcp-knowledge..."
K_SESSION=$(get_session "$BASE")
if [ -z "$K_SESSION" ]; then
    echo "ERROR: Could not get MCP session from chess-mcp-knowledge ($BASE)"
    echo "Is the container running? (Check: docker ps | grep chess-mcp-knowledge)"
    exit 1
fi
echo "  Session: $K_SESSION"

# ---------------------------------------------------------------------------
# Seed local docs (if present)
# ---------------------------------------------------------------------------

if [ -d "$REPO_DIR/docs" ]; then
    echo ""
    echo "=== Seeding mcp-chess docs root (topic=mcp-chess, catch-all) ==="
    call_tool "$BASE" "$K_SESSION" 2 "seed_docs" \
        "{\"docs_path\":\"/opt/projects/mcp-chess/docs\",\"topic\":\"mcp-chess\"}"

    if [ -d "$REPO_DIR/docs/chessprogramming" ]; then
        echo ""
        echo "=== Seeding chessprogramming.org cache (topic=chessprogramming) ==="
        call_tool "$BASE" "$K_SESSION" 3 "seed_docs" \
            "{\"docs_path\":\"/opt/projects/mcp-chess/docs/chessprogramming\",\"topic\":\"chessprogramming\"}"
    fi
else
    echo ""
    echo "=== Skipping mcp-chess docs (no docs/ dir) ==="
    echo "    To populate: ./knowledge/ingest-chessprogramming.sh"
fi

# ---------------------------------------------------------------------------
# Stats
# ---------------------------------------------------------------------------

echo ""
echo "=== Stats ==="
call_tool "$BASE" "$K_SESSION" 9 "stats" '{}'

echo ""
echo "Done."
