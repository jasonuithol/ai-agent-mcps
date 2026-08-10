#!/usr/bin/env bash
# seed.sh — seed the dotnet-knowledge database with project source.
# Run from the host. Requires dotnet-mcp-knowledge (port 5204) running.
#
# Out of the box this seeds nothing automatically — edit the bottom of
# the file to add your project(s). External doc seeding (MS Learn, xUnit,
# MSBuild reference) is left as a manual step because the relevant pages
# don't ship as a tarball — fetch with `wget --mirror` or similar then
# call seed_docs with the local path.
set -euo pipefail

BASE="http://localhost:5204/mcp"

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

echo "Checking dotnet-mcp-knowledge..."
if ! check_server "$BASE"; then
    echo "ERROR: No MCP response from dotnet-mcp-knowledge ($BASE)"
    echo "Is the container running? (Check: docker ps | grep dotnet-mcp-knowledge)"
    exit 1
fi
echo "  OK"

# ---------------------------------------------------------------------------
# Seed any .NET project source the user has cloned.
# Add more blocks below — pattern matches mcp-c/knowledge/seed.sh.
# ---------------------------------------------------------------------------

if [ -d "$HOME/Projects/betl" ]; then
    echo ""
    echo "=== Seeding betl source ==="
    call_tool "$BASE" 3 "seed_dotnet_source" \
        '{"project":"betl","source_dir":"/opt/projects/betl"}' \
        600
else
    echo ""
    echo "=== Skipping betl (not found at ~/Projects/betl) ==="
fi

# ---------------------------------------------------------------------------
# Stats
# ---------------------------------------------------------------------------

echo ""
echo "=== Stats ==="
call_tool "$BASE" 9 "stats" '{}'

echo ""
echo "Done."
