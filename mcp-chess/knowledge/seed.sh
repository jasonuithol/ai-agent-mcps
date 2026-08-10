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
# MCP helpers — stateless per MCP 2026-07-28: one POST per call,
# no initialize handshake, no session id. Protocol version and client
# capabilities ride in _meta on every request, mirrored by the required
# MCP-Protocol-Version / Mcp-Method / Mcp-Name headers.
# ---------------------------------------------------------------------------

MCP_META='"_meta":{"io.modelcontextprotocol/protocolVersion":"2026-07-28","io.modelcontextprotocol/clientInfo":{"name":"seed","version":"0"},"io.modelcontextprotocol/clientCapabilities":{}}'

parse_result() {
    python3 -c "
import sys, json
raw = sys.stdin.read()
data = [l[5:].strip() for l in raw.splitlines() if l.startswith('data:')]
try:
    d = json.loads(data[-1] if data else raw)
    for c in d.get('result',{}).get('content',[]):
        if c.get('type')=='text': print(c['text'])
except Exception: print('(parse error)')
" 2>/dev/null || echo "(no response)"
}

check_server() {
    local url="$1"
    curl -s -X POST "$url" \
        -H 'Content-Type: application/json' \
        -H 'Accept: application/json, text/event-stream' \
        -H 'MCP-Protocol-Version: 2026-07-28' \
        -H 'Mcp-Method: tools/list' \
        -d "{\"jsonrpc\":\"2.0\",\"id\":1,\"method\":\"tools/list\",\"params\":{$MCP_META}}" \
        --max-time 10 2>/dev/null | grep -q '\"tools\"'
}

call_tool() {
    local url="$1"
    local id="$2"
    local name="$3"
    local args="$4"
    # seed_docs over thousands of chunks on CPU embedding can take 10+ min.
    # 300s (the old default) isn't enough for large corpora.
    local max_time="${5:-3600}"
    echo "{\"jsonrpc\":\"2.0\",\"id\":$id,\"method\":\"tools/call\",\"params\":{\"name\":\"$name\",\"arguments\":$args,$MCP_META}}" \
        | curl -s -X POST "$url" \
            -H 'Content-Type: application/json' \
            -H 'Accept: application/json, text/event-stream' \
            -H 'MCP-Protocol-Version: 2026-07-28' \
            -H 'Mcp-Method: tools/call' \
            -H "Mcp-Name: $name" \
            --data-binary @- \
            --max-time "$max_time" | parse_result
}


# ---------------------------------------------------------------------------
# Check server is up
# ---------------------------------------------------------------------------

echo "Checking chess-mcp-knowledge..."
if ! check_server "$BASE"; then
    echo "ERROR: No MCP response from chess-mcp-knowledge ($BASE)"
    echo "Is the container running? (Check: docker ps | grep chess-mcp-knowledge)"
    exit 1
fi
echo "  OK"

# ---------------------------------------------------------------------------
# Seed local docs (if present)
# ---------------------------------------------------------------------------

if [ -d "$REPO_DIR/docs" ]; then
    echo ""
    echo "=== Seeding mcp-chess docs root (topic=mcp-chess, catch-all) ==="
    call_tool "$BASE" 2 "seed_docs" \
        "{\"docs_path\":\"/opt/projects/mcp-chess/docs\",\"topic\":\"mcp-chess\"}"

    if [ -d "$REPO_DIR/docs/chessprogramming" ]; then
        echo ""
        echo "=== Seeding chessprogramming.org cache (topic=chessprogramming) ==="
        call_tool "$BASE" 3 "seed_docs" \
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
call_tool "$BASE" 9 "stats" '{}'

echo ""
echo "Done."
