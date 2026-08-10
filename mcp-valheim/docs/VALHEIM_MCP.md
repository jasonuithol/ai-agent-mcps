# Valheim Development Environment

This document describes how to control the Valheim server and client from inside
the Claude Code container using the MCP tool servers.

## Architecture

Three MCP services back the `valheim` domain of `claude-sandbox-core`.
`mod/` runs in a container (Thunderstore + BepInEx ops). `control/` runs
as a host process (needs access to host processes and container
management). `knowledge/` runs in a container (RAG knowledge base). Both
`mod/` and `control/` report every tool execution to `knowledge/` via
fire-and-forget HTTP POST.

Generic `dotnet build` and `ilspycmd` decompile are in the sibling
`mcp-dotnet` service (port 5202) — also listed in `domains/valheim.conf`'s
`MCP_REPOS`, so a full Valheim domain start brings up four services.

```
Podman (on host)
│
├── claude-sandbox-core     Claude Code (valheim domain)
│       │
│       ├──── HTTP (port 5182) ────────────────────────────────────┐
│       │                                                           ▼
│       │                                             valheim-mod      (port 5182, container)
│       │                                                  │
│       │                                                  ├── BepInEx deploy   (client + server)
│       │                                                  ├── Thunderstore     (package/publish/download)
│       │                                                  ├── rsvg-convert     (SVG→PNG)
│       │                                                  └── POST /ingest ──────────┐
│       │                                                                               │
│       ├──── HTTP (port 5173) ────────────────────────────────────┐                    │
│       │                                                           ▼                    │
│       │                                             valheim-control (port 5173, host)   │
│       │                                                  │                              │
│       │                                                  ├── docker (server container)  │
│       │                                                  ├── psutil (Steam/client)      │
│       │                                                  └── POST /ingest ──────────┐  │
│       │                                                                               │  │
│       └──── HTTP (port 5184) ────────────────────────────────────┐                    │  │
│                                                                   ▼                    │  │
│                                                     valheim-knowledge (port 5184, container)◄─┘
│                                                          │
│                                                          ├── ChromaDB    (vector store)
│                                                          ├── /ingest     (auto-learns from tool use)
│                                                          └── MCP tools   (ask, ask_class, stats, etc.)
│
├── valheim_server          Valheim dedicated server (managed by valheim-control)
│
└── [host]
        └── Valheim client  (Steam/native — started/stopped by valheim-control)
```

## Setup

### Prerequisites

Ensure the Podman socket is running:

```bash
systemctl --user enable --now podman.socket
```

### 1-3. Bring up the whole stack via claude-sandbox-core

```bash
~/Projects/claude-sandbox-core/bin/start.sh valheim <project>
```

`bin/start.sh` calls `mcp-valheim/setup.sh` (idempotent: builds the
`valheim-mod` and `valheim-knowledge` images) then
`mcp-valheim/start.sh` (which starts all three services: mod container,
control host process, knowledge container). `mcp-dotnet` is also brought
up by the domain start. The Claude container is launched last and
receives the registered MCP service URLs from the domain conf.

### 4. Service registration

Done automatically by `claude-sandbox-core`'s entrypoint, which reads
`domains/valheim.conf`'s `SERVICES` array and runs `claude mcp add` for
each. Verify with `/mcp` inside any Claude Code session.

### 5. Refresh the path map if the sandbox container is restarted

The path map (used by `convert_svg` to translate container paths to host
paths) is built when `valheim-mod` starts. If the Claude sandbox container
is restarted, call `refresh_path_map()` to rebuild it without restarting
`valheim-mod`.

---

## MCP Tools

### Deploy and Thunderstore (`valheim-mod`, port 5182)

These tools are **blocking** — they run to completion and return the full log.

| Tool | Argument | Description |
|------|----------|-------------|
| `deploy_server(project)` | Project folder name | Copy DLLs and configs to server BepInEx dirs |
| `deploy_client(project)` | Project folder name | Copy DLLs and configs to client BepInEx dirs |
| `package(project)` | Project folder name | Bundle mod into Thunderstore zip |
| `publish(project, community, categories)` | Project folder name, community slug (default: `"valheim"`), category slugs | Upload packaged zip to Thunderstore |
| `download(package, client, server)` | `namespace-name-version`, deploy flags | Fetch a Thunderstore package and deploy it |

For `build`, use the sibling `dotnet` MCP (port 5202) — run `dotnet build`
there first, then `deploy_*` / `package` here.

`project` is a folder name under `~/Projects` with no path separators,
e.g. `"ValheimRainDance"`. Always build (via `dotnet`) and verify success
before deploying or packaging. Always build and package before publishing.

### Thunderstore Publishing

`publish` requires a `THUNDERSTORE_TOKEN` environment variable. Place your
service account token (format `tss_XXXX`) in `mod/.env`:

```
THUNDERSTORE_TOKEN=tss_your_token_here
```

This file is gitignored. The token is loaded automatically by
`start-container.sh` and passed into the container.

### Decompiling Assemblies — moved

`decompile_dll` now lives in the sibling `mcp-dotnet` MCP (port 5202).
Pass the container-local path of the DLL as you would have here. No path
map translation is performed by mcp-dotnet — mount the DLL's directory
into both containers (claude-sandbox-core's valheim domain already mounts
`~/Projects` into both) and reference it under `/opt/projects/...`.

### Converting SVG to PNG (`valheim-mod`)

```
convert_svg(container_path)
```

Converts an SVG to a 256×256 PNG using `rsvg-convert`. Pass the path as
seen from inside the Claude sandbox container:

```
/workspace/ValheimRainDance/ThunderstoreAssets/icon.svg
```

Output PNG is written next to the source SVG with a `.png` extension, suitable
for Thunderstore mod icons.

### Utility (`valheim-mod`)

```
refresh_path_map()
```

Rebuilds the path map from environment variables. Only needed if mount paths
have changed since mcp-build started (rare — the map is static by default).

### Server Control (`valheim-control`, port 5173)

The dedicated server runs as a Docker container (`valheim_server`).

| Tool | Description |
|------|-------------|
| `start_server(vanilla)` | Start the server container. Builds the image if needed. `vanilla=False` (default) loads BepInEx; `vanilla=True` runs plain `start_server.sh` |
| `stop_server()` | Stop the server container gracefully (`docker stop`) |
| `kill_server()` | Kill the server container immediately (`docker kill`) |

#### Server config files (adminlist, bannedlist, etc.)

The server container uses a **named podman volume** (`valheim_server_data`)
mounted at `/root/.config/unity3d/IronGate/Valheim`. This is where the server
reads `adminlist.txt`, `bannedlist.txt`, and `permittedlist.txt` at runtime.

On the host, this volume lives at:
```
~/.local/share/containers/storage/volumes/valheim_server_data/_data/
```

Edit that copy directly — it is NOT the same as `~/.config/unity3d/IronGate/Valheim/`
(which is the client's copy and is not mapped into the container).

Use the `Steam_` prefix format for player IDs (e.g. `Steam_44445555666677788`).

### Client Control and Steam (`valheim-control`)

| Tool | Description |
|------|-------------|
| `steam_status()` | Check whether Steam is running on the host |
| `start_steam()` | Launch Steam on the host. Non-blocking |
| `start_client(extra_args)` | Start the client via `run_bepinex.sh`. Non-blocking. `extra_args` (list, default `[]`) are appended after all other flags — e.g. `["-skipIntro"]` |
| `stop_client()` | Stop the client process |

### Knowledge Base (`valheim-knowledge`, port 5184)

RAG-backed knowledge service. Grows automatically from tool use — every tool
execution in mcp-build and mcp-control reports to mcp-knowledge via
fire-and-forget POST. See `INGEST_MCP.md` for full
usage docs.

| Tool | Description |
|------|-------------|
| `ask(question)` | Semantic search across all knowledge (top 5 results) |
| `ask_class(class_name)` | Find all indexed knowledge about a specific Valheim class |
| `ask_tagged(question, tags)` | Semantic search filtered by tags (lowercase only) |
| `stats()` | Collection size, source breakdown, tag distribution |
| `list_sources()` | All indexed sources with chunk counts |
| `forget(source)` | Delete all chunks from a source |
| `seed_docs(docs_path)` | One-time: index the curated MODDING_*.md docs |
| `seed_decompile(class_name)` | One-time: decompile a class via mcp-build and index it |

#### First-time seeding

After starting mcp-knowledge for the first time, seed with the curated docs
and key Valheim classes:

```
seed_docs("/opt/projects/mcp-valheim/docs")
seed_decompile("Player")
seed_decompile("ZRoutedRpc")
seed_decompile("ZDOVars")
seed_decompile("EnvMan")
seed_decompile("ZNetPeer")
seed_decompile("Bed")
seed_decompile("RandEventSystem")
seed_decompile("VisEquipment")
seed_decompile("ZSyncAnimation")
```

Run `stats()` afterwards to confirm. After seeding, knowledge grows
automatically from normal tool usage.

---

## Logs

All `valheim-mod` tool logs are written to `~/Projects/claude-sandbox-core/workspaces/valheim/valheim/logs/`
on the host (mounted into the container at `/opt/workspace/valheim/logs/`),
and are also returned directly in the tool response.

| File | Written by |
|------|------------|
| `logs/deploy-server.log` | `deploy_server` |
| `logs/deploy-client.log` | `deploy_client` |
| `logs/package.log` | `package` |
| `logs/publish.log` | `publish` |
| `logs/download.log` | `download` |
| `logs/svg-to-png.log` | `convert_svg` |
| `logs/server.log` | `start_server` (server container stdout) |
| `logs/client.log` | `start_client` (client process stdout) |

Each log is overwritten on each run and includes timestamps at start and end.

---

## BepInEx

BepInEx is installed on both server and client. Plugin and config directories
are writable from inside the Claude sandbox container:

| Location | Path (in sandbox) |
|----------|--------------------------|
| Server plugins | `/workspace/valheim/server/BepInEx/plugins/` |
| Client plugins | `/workspace/valheim/client/BepInEx/plugins/` |
| Server config | `/workspace/valheim/server/BepInEx/config/` |
| Client config | `/workspace/valheim/client/BepInEx/config/` |

BepInEx logs are at:

- Server: `/workspace/valheim/server/BepInEx/LogOutput.log`
- Client: `/workspace/valheim/client/BepInEx/LogOutput.log`

> **Warning:** The server log only stays live if the BepInEx volume mount is in place.
> `start_server` in mcp-control mounts `{SERVER_DIR}/BepInEx` → `/opt/valheim-server/BepInEx`
> inside the container. Without this mount the container writes to its own internal path and
> the file at `/workspace/valheim/server/BepInEx/LogOutput.log` goes stale after the first run.

---

## Testing the MCP Servers

To test from the host without Claude Code (stateless MCP 2026-07-28 — one
POST per request, no handshake, no session id):

```bash
# List tools
curl -s -X POST http://localhost:5182/mcp \
  -H 'Content-Type: application/json' \
  -H 'Accept: application/json, text/event-stream' \
  -H 'MCP-Protocol-Version: 2026-07-28' \
  -H 'Mcp-Method: tools/list' \
  -d '{"jsonrpc":"2.0","id":1,"method":"tools/list","params":{"_meta":{"io.modelcontextprotocol/protocolVersion":"2026-07-28","io.modelcontextprotocol/clientInfo":{"name":"test","version":"0"},"io.modelcontextprotocol/clientCapabilities":{}}}}' \
  | python3 -c "import sys,json; [print(t['name']) for t in json.load(sys.stdin)['result']['tools']]"

# Call a tool (note the extra Mcp-Name header naming the tool)
curl -s -X POST http://localhost:5184/mcp \
  -H 'Content-Type: application/json' \
  -H 'Accept: application/json, text/event-stream' \
  -H 'MCP-Protocol-Version: 2026-07-28' \
  -H 'Mcp-Method: tools/call' \
  -H 'Mcp-Name: stats' \
  -d '{"jsonrpc":"2.0","id":2,"method":"tools/call","params":{"name":"stats","arguments":{},"_meta":{"io.modelcontextprotocol/protocolVersion":"2026-07-28","io.modelcontextprotocol/clientInfo":{"name":"test","version":"0"},"io.modelcontextprotocol/clientCapabilities":{}}}}'
```

---

## Files

| File | Purpose |
|------|---------|
| `mod/mcp-service.py` | valheim-mod MCP implementation (container, port 5182) |
| `mod/Dockerfile` | valheim-mod container image definition |
| `mod/build-container.sh` | Build the container image |
| `mod/start-container.sh` | Start the container |
| `control/mcp-service.py` | Control MCP implementation (host process, port 5173) |
| `control/start-mcp-service.sh` | Start the control MCP server on the host |
| `knowledge/` | Knowledge RAG service (container, port 5184) — see `knowledge/CLAUDE.md` |

---

## Notes

- Build and deploy tools block until complete — do not call multiple
  build/deploy tools simultaneously.
- Server and client start tools are non-blocking — check logs to confirm
  successful startup.
- The package zip is written to `release/<teamname>-<modname>-<version>.zip`
  inside the project directory. If `ThunderstoreAssets/CHANGELOG.md` exists
  it is included in the zip.
- Path environment variables can override default mount points:
  `VALHEIM_SERVER_DIR`, `VALHEIM_CLIENT_DIR`, `VALHEIM_PROJECT_DIR`, `VALHEIM_LOGS_DIR`.
- All tool executions in mcp-build and mcp-control are reported to
  mcp-knowledge (`localhost:5184/ingest`) via fire-and-forget HTTP POST.
  If mcp-knowledge is not running, the reports are silently dropped.
