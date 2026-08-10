#!/usr/bin/env bash
# seed.sh — seed the mcp-knowledge database with docs and decompiled assembly
# Run from the host. Requires valheim-mcp-knowledge (port 5184) and mcp-build (port 5182).
set -euo pipefail

BASE="http://localhost:5184/mcp"
BUILD_BASE="http://localhost:5182/mcp"
DLL_PATH="/workspace/valheim/server/valheim_server_Data/Managed/assembly_valheim.dll"

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
    local max_time="${5:-120}"
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
# Check servers are up
# ---------------------------------------------------------------------------

echo "Checking mcp-knowledge..."
if ! check_server "$BASE"; then
    echo "ERROR: No MCP response from mcp-knowledge ($BASE)"
    exit 1
fi
echo "  OK"

echo "Checking mcp-build..."
if ! check_server "$BUILD_BASE"; then
    echo "ERROR: No MCP response from mcp-build ($BUILD_BASE)"
    exit 1
fi
echo "  OK"

# ---------------------------------------------------------------------------
# Seed docs
# ---------------------------------------------------------------------------

echo ""
echo "=== Seeding docs ==="
call_tool "$BASE" 2 "seed_docs" '{"docs_path":"/opt/projects/ai-agent-mcps/mcp-valheim/docs"}'

# ---------------------------------------------------------------------------
# Decompile full DLL and seed
# ---------------------------------------------------------------------------

TMPDIR=$(mktemp -d)
trap 'rm -rf "$TMPDIR"' EXIT

echo ""
echo "=== Decompiling assembly_valheim.dll (this may take a while) ==="
call_tool "$BUILD_BASE" 3 "decompile_dll" "{\"container_path\":\"$DLL_PATH\"}" 600 \
    > "$TMPDIR/decompiled.txt"

# Strip the header line
sed -i '1{/^DECOMPILE/d;}' "$TMPDIR/decompiled.txt"

LINES=$(wc -l < "$TMPDIR/decompiled.txt")
if [ "$LINES" -lt 10 ]; then
    echo "ERROR: Decompile returned only $LINES lines"
    cat "$TMPDIR/decompiled.txt"
    exit 1
fi
echo "  Got $LINES lines of decompiled source"

echo ""
echo "=== Seeding decompiled source ==="
# Payload is too large for command-line args — build JSON in Python and pipe to curl
python3 -c "
import json, sys
with open(sys.argv[1]) as f:
    source = f.read()
meta = json.loads('{' + sys.argv[2] + '}')['_meta']
payload = {
    'jsonrpc': '2.0', 'id': 4,
    'method': 'tools/call',
    'params': {'name': 'seed_decompile',
               'arguments': {'decompiled_source': source},
               '_meta': meta}
}
sys.stdout.buffer.write(json.dumps(payload).encode())
" "$TMPDIR/decompiled.txt" "$MCP_META" \
    | curl -s -X POST "$BASE" \
        -H 'Content-Type: application/json' \
        -H 'Accept: application/json, text/event-stream' \
        -H 'MCP-Protocol-Version: 2026-07-28' \
        -H 'Mcp-Method: tools/call' \
        -H 'Mcp-Name: seed_decompile' \
        --data-binary @- \
        --max-time 300 \
    | parse_result

# ---------------------------------------------------------------------------
# Stats
# ---------------------------------------------------------------------------

echo ""
echo "=== Stats ==="
call_tool "$BASE" 5 "stats" '{}'

echo ""
echo "Done."
