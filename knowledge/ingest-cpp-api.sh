#!/usr/bin/env bash
# ingest-cpp-api.sh — regenerate the UE4SS C++ API reference AND re-seed the
# vector store. End-to-end: one command, fresh API knowledge in the KB.
#
# Pipeline:
#   1. doxygen on UE4SS/UE4SS/include/ -> XML at knowledge/.doxygen-out/xml/
#   2. ingest/doxygen-xml-to-md.py converts XML -> one markdown file per
#      class/struct/namespace/file, written to docs/ue4ss-cpp-api/.
#   3. knowledge/seed.sh indexes every docs/ source into the chroma store
#      (including the freshly-regenerated ue4ss-cpp-api-generated topic).
#
# Pass --no-seed to skip step 3 if you only want to inspect the markdown
# output without touching the vector store.
#
# Idempotent: clears .doxygen-out/ and docs/ue4ss-cpp-api/ on each run.
# seed_docs upserts on content hash so unchanged docs aren't re-embedded.
#
# Requires doxygen on the host PATH. Install with:
#   sudo apt install -y doxygen
set -euo pipefail

SEED_AFTER=1
for arg in "$@"; do
    case "$arg" in
        --no-seed) SEED_AFTER=0 ;;
        -h|--help) sed -n '2,/^$/p' "$0" | sed 's/^# \{0,1\}//'; exit 0 ;;
        *) echo "Unknown flag: $arg" >&2; exit 2 ;;
    esac
done

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO_DIR="$(cd "$SCRIPT_DIR/.." && pwd)"
INGEST_DIR="$REPO_DIR/ingest"
DOXY_OUT="$SCRIPT_DIR/.doxygen-out"
OUT_DIR="$REPO_DIR/docs/ue4ss-cpp-api"

if ! command -v doxygen >/dev/null 2>&1; then
    echo "ERROR: doxygen not installed."
    echo "  sudo apt install -y doxygen"
    exit 1
fi

UE4SS_INC="$HOME/Projects/Advanced-SCUM-Modding/third_party/UE4SS/UE4SS/include"
if [ ! -d "$UE4SS_INC" ]; then
    echo "ERROR: UE4SS include dir not found at $UE4SS_INC"
    echo "  Clone UE4SS into Advanced-SCUM-Modding/third_party/ first."
    exit 1
fi

echo "=== Running doxygen against $UE4SS_INC ==="
rm -rf "$DOXY_OUT"
mkdir -p "$DOXY_OUT"
# Doxyfile uses paths relative to the ingest/ dir so we cd there.
(cd "$INGEST_DIR" && doxygen Doxyfile) 2>&1 | tail -20
echo ""

XML_DIR="$DOXY_OUT/xml"
if [ ! -d "$XML_DIR" ]; then
    echo "ERROR: doxygen ran but no XML output at $XML_DIR"
    exit 1
fi
N_XML=$(find "$XML_DIR" -name '*.xml' | wc -l)
echo "doxygen produced $N_XML XML files."

echo ""
echo "=== Converting XML -> markdown ==="
python3 "$INGEST_DIR/doxygen-xml-to-md.py" \
    --xml-dir "$XML_DIR" \
    --out-dir "$OUT_DIR"

echo ""
if [ "$SEED_AFTER" -eq 1 ]; then
    echo "=== Seeding into chroma (calling seed.sh) ==="
    exec "$SCRIPT_DIR/seed.sh"
else
    echo "Done (--no-seed). To index into chroma, run: ./knowledge/seed.sh"
fi
