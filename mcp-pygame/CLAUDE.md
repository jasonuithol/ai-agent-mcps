# mcp-pygame

Host-side notes for working on this repo. **Sandbox-side operating guide
is at [`docs/SANDBOX.md`](docs/SANDBOX.md)** — that file is mounted into
the sandbox and surfaces to in-sandbox Claude via auto-load.

## What this repo is

The Python/pygame development half of the `claude-sandbox-core` `pygame`
domain. Two sibling containers:

| Subdir | Container | Port | Purpose |
|--------|-----------|------|---------|
| `service/` | `pygame-mcp-build` | 5172 | `run_tests`, `lint`, `install_deps` |
| `knowledge/` | `pygame-mcp-knowledge` | 5174 | RAG over pygame source, project source, curated docs, accumulated failure/fix history |

The two halves are paired: `service/` fires fire-and-forget POSTs at
`knowledge/`'s `/ingest` endpoint, so signals from test/lint runs
accumulate as retrievable context.

## Where to look

- **`README.md`** — user-facing setup / start / stop instructions.
- **`docs/SANDBOX.md`** — sandbox-side operating guide (auto-loaded inside
  the sandbox).
- **`docs/`** — curated reference docs mounted read-only into the sandbox
  at `/workspace/docs/` (`PYGAME_BASICS.md`, `PYGAME_GOTCHAS.md`,
  `PYGAME_MCP.md`, `PYTHON_GENERAL.md`, `INGEST_MCP.md`,
  `projects/<PROJECT>.md`).
- **`knowledge/CLAUDE.md`** — design doc for the knowledge service
  (chunking strategy, ingest routing, metadata schema, known concerns).
- **`service/mcp-service.py`** — the run_tests/lint/install_deps tools.
- **`knowledge/mcp-service.py`** — the MCP query server + `/ingest`
  HTTP endpoint.

## Conventions worth preserving

- Domain-scoped collection: every pygame project shares one ChromaDB
  collection with `project` metadata. Cross-project retrieval is the
  point — don't refactor toward per-project collections.
- Headless test execution: `run_tests` sets `SDL_VIDEODRIVER=dummy` and
  `SDL_AUDIODRIVER=dummy`. Don't reintroduce a hard dependency on a real
  display.
- Test failures and lint errors are indexed via the same `/ingest` flow
  described in `docs/INGEST_MCP.md`. Any new tool that emits actionable
  failure output should hook into that.
- The two `.venv*` dirs are deliberately split: `.venv-mcp/` is the
  container's, `.venv/` is the host's. `install_deps` only touches the
  former.
