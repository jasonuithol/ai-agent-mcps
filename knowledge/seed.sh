#!/usr/bin/env bash
# seed.sh — seed the ue4ss-knowledge database with curated docs.
# Run from the host. Requires ue4ss-mcp-knowledge (port 5196) running.
#
# Sources (in priority order, each only if present on the host):
#   1. mcp-ue4ss/docs/                             — handwritten notes
#   2. Advanced-SCUM-Modding/third_party/UE4SS/docs — canonical UE4SS docs
#      split into sub-topics (cpp-api, lua-api, guides, feature-overview,
#      devlogs) so query-time filtering by `topic` is useful.
#
# Add other sources here as you grow the corpus (Doxygen-parsed headers,
# scraped wiki, etc).
set -euo pipefail

BASE="http://localhost:5196/mcp"

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

echo "Connecting to ue4ss-mcp-knowledge..."
K_SESSION=$(get_session "$BASE")
if [ -z "$K_SESSION" ]; then
    echo "ERROR: Could not get MCP session from ue4ss-mcp-knowledge ($BASE)"
    echo "Is the container running? (Check: docker ps | grep ue4ss-mcp-knowledge)"
    exit 1
fi
echo "  Session: $K_SESSION"

# ---------------------------------------------------------------------------
# Seed local mcp-ue4ss docs (if present)
# ---------------------------------------------------------------------------

if [ -d "$HOME/Projects/mcp-ue4ss/docs" ] && [ -n "$(find "$HOME/Projects/mcp-ue4ss/docs" -name '*.md' -print -quit 2>/dev/null)" ]; then
    echo ""
    echo "=== Seeding mcp-ue4ss/docs ==="
    call_tool "$BASE" "$K_SESSION" 2 "seed_docs" \
        "{\"docs_path\":\"/opt/projects/mcp-ue4ss/docs\",\"topic\":\"ue4ss-notes\"}"
else
    echo ""
    echo "=== Skipping mcp-ue4ss/docs (none present) ==="
fi

# ---------------------------------------------------------------------------
# Seed UE4SS canonical docs from Advanced-SCUM-Modding/third_party/UE4SS
# ---------------------------------------------------------------------------

UE4SS_DOCS="$HOME/Projects/Advanced-SCUM-Modding/third_party/UE4SS/docs"
if [ -d "$UE4SS_DOCS" ]; then
    # seed_docs upserts on content hash, so the LAST write to a given doc
    # wins for both content and metadata. Order matters:
    #   1. Catch-all recursive pass tags everything as 'ue4ss-misc'.
    #   2. Per-topic passes then overwrite the docs inside each sub-dir
    #      with their specific topic. Top-level .md files that aren't
    #      covered by any per-topic pass retain 'ue4ss-misc'.
    echo ""
    echo "=== Seeding UE4SS docs root (topic=ue4ss-misc, catch-all) ==="
    call_tool "$BASE" "$K_SESSION" 10 "seed_docs" \
        "{\"docs_path\":\"/opt/projects/Advanced-SCUM-Modding/third_party/UE4SS/docs\",\"topic\":\"ue4ss-misc\"}"

    declare -a TOPICS=(
        "cpp-api"
        "lua-api"
        "guides"
        "feature-overview"
        "devlogs"
    )
    id=11
    for t in "${TOPICS[@]}"; do
        if [ -d "$UE4SS_DOCS/$t" ]; then
            echo ""
            echo "=== Seeding UE4SS docs/$t (topic=$t) ==="
            call_tool "$BASE" "$K_SESSION" "$id" "seed_docs" \
                "{\"docs_path\":\"/opt/projects/Advanced-SCUM-Modding/third_party/UE4SS/docs/$t\",\"topic\":\"$t\"}"
            id=$((id + 1))
        fi
    done
else
    echo ""
    echo "=== Skipping UE4SS canonical docs (third_party/UE4SS not cloned) ==="
fi

# ---------------------------------------------------------------------------
# Seed SCUM-specific RE notes from Advanced-SCUM-Modding/docs/
# Per the project's CLAUDE.md this is the canonical home for AOB signatures,
# struct layouts, and RPC IDs keyed by SCUM build. Unique knowledge — no
# upstream source for any of it.
# ---------------------------------------------------------------------------

SCUM_DOCS="$HOME/Projects/Advanced-SCUM-Modding/docs"
if [ -d "$SCUM_DOCS" ] && [ -n "$(find "$SCUM_DOCS" -name '*.md' -print -quit 2>/dev/null)" ]; then
    echo ""
    echo "=== Seeding Advanced-SCUM-Modding/docs (topic=scum-re-notes) ==="
    call_tool "$BASE" "$K_SESSION" 20 "seed_docs" \
        "{\"docs_path\":\"/opt/projects/Advanced-SCUM-Modding/docs\",\"topic\":\"scum-re-notes\"}"
else
    echo ""
    echo "=== Skipping Advanced-SCUM-Modding/docs (none present) ==="
fi

# ---------------------------------------------------------------------------
# Seed reference native mod (Mods/DeveloperMode) as the canonical pattern:
# build.sh template, AOB-scan + sanity-check approach, log conventions.
# ---------------------------------------------------------------------------

DEV_MOD="$HOME/Projects/Advanced-SCUM-Modding/Mods/DeveloperMode"
if [ -d "$DEV_MOD" ]; then
    echo ""
    echo "=== Seeding Mods/DeveloperMode (topic=scum-mod-examples) ==="
    call_tool "$BASE" "$K_SESSION" 21 "seed_docs" \
        "{\"docs_path\":\"/opt/projects/Advanced-SCUM-Modding/Mods/DeveloperMode\",\"topic\":\"scum-mod-examples\"}"
else
    echo ""
    echo "=== Skipping Mods/DeveloperMode (not present) ==="
fi

# ---------------------------------------------------------------------------
# Seed UE4SS upstream reference cppmods (EventViewerMod, KismetDebuggerMod).
# These are the canonical UE4SS-blessed examples of how a C++ mod is
# structured (CMakeLists + include/ + src/ + README.md).
# ---------------------------------------------------------------------------

CPPMODS="$HOME/Projects/Advanced-SCUM-Modding/third_party/UE4SS/cppmods"
if [ -d "$CPPMODS" ]; then
    echo ""
    echo "=== Seeding UE4SS cppmods (topic=ue4ss-cppmod-examples) ==="
    call_tool "$BASE" "$K_SESSION" 22 "seed_docs" \
        "{\"docs_path\":\"/opt/projects/Advanced-SCUM-Modding/third_party/UE4SS/cppmods\",\"topic\":\"ue4ss-cppmod-examples\"}"
else
    echo ""
    echo "=== Skipping UE4SS cppmods (not present) ==="
fi

# ---------------------------------------------------------------------------
# Seed Doxygen-generated UE4SS C++ API reference (one .md per class/struct/
# namespace/file). Populate via knowledge/ingest-cpp-api.sh — that script
# runs doxygen against UE4SS/include/ and converts the XML to markdown.
# ---------------------------------------------------------------------------

CPP_API_DOCS="$HOME/Projects/mcp-ue4ss/docs/ue4ss-cpp-api"
if [ -d "$CPP_API_DOCS" ] && [ -n "$(find "$CPP_API_DOCS" -name '*.md' -print -quit 2>/dev/null)" ]; then
    echo ""
    echo "=== Seeding UE4SS C++ API reference (topic=ue4ss-cpp-api-generated) ==="
    call_tool "$BASE" "$K_SESSION" 23 "seed_docs" \
        "{\"docs_path\":\"/opt/projects/mcp-ue4ss/docs/ue4ss-cpp-api\",\"topic\":\"ue4ss-cpp-api-generated\"}"
else
    echo ""
    echo "=== Skipping UE4SS C++ API reference (run ./knowledge/ingest-cpp-api.sh to generate it) ==="
fi

# ---------------------------------------------------------------------------
# Stats
# ---------------------------------------------------------------------------

echo ""
echo "=== Stats ==="
call_tool "$BASE" "$K_SESSION" 99 "stats" '{}'

echo ""
echo "Done."
