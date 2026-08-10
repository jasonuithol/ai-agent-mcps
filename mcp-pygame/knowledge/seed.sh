#!/usr/bin/env bash
# seed.sh — seed the mcp-knowledge database with docs and project source
# Run from the host. Requires mcp-knowledge (port 5174) running.
set -euo pipefail

BASE="http://localhost:5174/mcp"

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

echo "Checking mcp-knowledge..."
if ! check_server "$BASE"; then
    echo "ERROR: No MCP response from mcp-knowledge ($BASE)"
    echo "Is the container running? (Check: docker ps | grep mcp-knowledge)"
    exit 1
fi
echo "  OK"

# ---------------------------------------------------------------------------
# Seed docs
# ---------------------------------------------------------------------------

echo ""
echo "=== Seeding mcp-pygame docs ==="
call_tool "$BASE" 2 "seed_docs" \
    '{"docs_path":"/opt/projects/mcp-pygame/docs"}'

# ---------------------------------------------------------------------------
# Seed UltimatePyve source
# ---------------------------------------------------------------------------

if [ -d "$HOME/Projects/UltimatePyve" ]; then
    echo ""
    echo "=== Seeding UltimatePyve source ==="
    call_tool "$BASE" 3 "seed_python_source" \
        '{"project":"UltimatePyve","source_dir":"/opt/projects/UltimatePyve","extra_tags":["successful-example"]}' \
        600
else
    echo ""
    echo "=== Skipping UltimatePyve (not found at ~/Projects/UltimatePyve) ==="
fi

# ---------------------------------------------------------------------------
# Optionally: pygame-ce source if the user has cloned it
# ---------------------------------------------------------------------------

if [ -d "$HOME/Projects/pygame-ce" ]; then
    echo ""
    echo "=== Seeding pygame-ce library source ==="
    call_tool "$BASE" 4 "seed_python_source" \
        '{"project":"pygame-ce","source_dir":"/opt/projects/pygame-ce","extra_tags":["library","pygame-ce"]}' \
        900
else
    echo ""
    echo "(skipping pygame-ce — clone to ~/Projects/pygame-ce to include)"
fi

# ---------------------------------------------------------------------------
# Stats
# ---------------------------------------------------------------------------

echo ""
echo "=== Stats ==="
call_tool "$BASE" 5 "stats" '{}'

echo ""
echo "Done."
