#!/usr/bin/env bash
# seed.sh — seed the c-knowledge database with docs and project source
# Run from the host. Requires c-mcp-knowledge (port 5194) running.
set -euo pipefail

BASE="http://localhost:5194/mcp"

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
    local max_time="${5:-300}"
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

echo "Checking c-mcp-knowledge..."
if ! check_server "$BASE"; then
    echo "ERROR: No MCP response from c-mcp-knowledge ($BASE)"
    echo "Is the container running? (Check: docker ps | grep c-mcp-knowledge)"
    exit 1
fi
echo "  OK"

# ---------------------------------------------------------------------------
# Seed docs
# ---------------------------------------------------------------------------

echo ""
echo "=== Seeding mcp-c docs ==="
call_tool "$BASE" 2 "seed_docs" \
    '{"docs_path":"/opt/projects/mcp-c/docs"}'

# ---------------------------------------------------------------------------
# Optional: seed any C project the user has cloned. Drop in your
# project name(s) here once you have one to seed.
# ---------------------------------------------------------------------------

if [ -d "$HOME/Projects/bchess" ]; then
    echo ""
    echo "=== Seeding bchess source ==="
    call_tool "$BASE" 3 "seed_c_source" \
        '{"project":"bchess","source_dir":"/opt/projects/bchess","extra_tags":["successful-example"]}' \
        600
else
    echo ""
    echo "=== Skipping bchess (not found at ~/Projects/bchess) ==="
fi

# ---------------------------------------------------------------------------
# Stats
# ---------------------------------------------------------------------------

echo ""
echo "=== Stats ==="
call_tool "$BASE" 9 "stats" '{}'

echo ""
echo "Done."
