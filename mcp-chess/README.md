# mcp-chess

MCP service pair for chess engine development. A workbench for building,
testing, and analysing UCI chess engines — Stockfish ships in the image
as the reference engine; arbitrary engine binaries can be registered at
runtime against it.

| Subdir | Container | Port | Purpose |
|--------|-----------|------|---------|
| `service/` | `chess-mcp-engine` | 5180 | engine registry, `bestmove`, `analyze`, `perft`, `match`, `sprt`, `epd_test`, position/PGN tooling |
| `knowledge/` | `chess-mcp-knowledge` | 5186 | RAG over chessprogramming.org wiki, Stockfish docs, python-chess docs |

The engine service uses [python-chess](https://python-chess.readthedocs.io/)
for UCI subprocess management, FEN/PGN/SAN parsing, perft, Polyglot books,
and Syzygy tablebases. Engine-vs-engine matches and SPRT testing are run
via [fastchess](https://github.com/Disservin/fastchess), the modern
cutechess-cli replacement used upstream by the Stockfish project.

## Tools (engine service)

**Engine management**
- `register_engine(name, path, options)` — add an engine to the registry.
  Stockfish is auto-registered as `stockfish` at startup.
- `list_engines()` — show registered engines.
- `unregister_engine(name)` — remove an engine (closes its UCI process).

**Position & analysis**
- `bestmove(engine, fen, depth?, movetime_ms?)` — single-engine search.
- `analyze(engine, fen, depth?, movetime_ms?, multipv?)` — eval + PV.
- `compare_eval(fen, engines, depth?)` — side-by-side analysis from N engines.
- `perft(fen, depth)` — node-count correctness check (move generation).

**Position handling (no engine needed)**
- `parse_fen(fen)` → board ASCII, side-to-move, legality, castling rights.
- `legal_moves(fen)` — UCI + SAN list.
- `apply_moves(fen, moves)` → resulting FEN.
- `pgn_to_fens(pgn)` — extract FEN history from a PGN string.

**Engine vs engine**
- `match(engine_a, engine_b, n_games, time_control, opening_book?)` —
  fastchess head-to-head, returns Elo + error bars.
- `sprt(engine_a, engine_b, elo0, elo1, alpha, beta, time_control, ...)` —
  Sequential Probability Ratio Test (the patch-acceptance methodology).
- `epd_test(engine, suite_path, time_per_pos_ms)` — score on a tactics
  suite (WAC, STS, ERET, Arasan, etc.).

## Consumers

Designed to be launched by [`claude-sandbox-core`](https://github.com/jasonuithol/claude-sandbox-core)
via a `chess` domain conf listing this repo in `MCP_REPOS`. Any MCP
client speaking streamable HTTP can mount these services.

## Usage

```bash
./setup.sh                # one-time, idempotent (builds both images)
./start.sh                # bring up both containers
./stop.sh                 # shut them down (containers preserved for revival)
./clean.sh                # remove containers + images (full teardown)

knowledge/ingest-chessprogramming.sh   # crawl chessprogramming.org wiki (~30-60 min)
knowledge/seed.sh                       # index cached docs into chroma
```

To validate setup works from bare state:

```bash
./clean.sh && ./setup.sh && ./start.sh
```

Both containers use host networking (ports above). The knowledge service
runs embeddings on GPU (all-MiniLM-L6-v2 via onnxruntime-gpu) — run
`knowledge/setup-gpu.sh` once on a fresh host to install the NVIDIA
Container Toolkit and patch the CDI spec for podman compatibility.

## Engine binaries

Engines under test live on the host under `~/Projects/<engine-repo>`
and are mounted read-only into the engine container at `/opt/projects`.
Register them by absolute container path:

```
register_engine(name="myengine", path="/opt/projects/myengine/build/myengine")
```

## Licence footprint

Bundled tools are copyleft / share-alike:
- Stockfish — GPLv3
- fastchess — GPLv3
- python-chess — GPLv3
- chessprogramming.org seed content — CC-BY-SA

The wrapper code in this repo is yours; image distribution would trigger
the upstream obligations. Per the project's local-rebuild install path,
nothing is redistributed — end users build the image themselves.
