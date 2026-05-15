# mcp-valheim

MCP service trio for Valheim mod development (BepInEx + Thunderstore + server/client lifecycle).

| Subdir | Container | Port | Purpose |
|--------|-----------|------|---------|
| `mod/` | `valheim-mcp-mod` | 5182 | BepInEx deploy (client + server), Thunderstore package/publish/download, SVG → PNG icon conversion |
| `control/` | host process | 5173 | Valheim server/client lifecycle (host-runner — needs psutil + GUI) |
| `knowledge/` | `valheim-mcp-knowledge` | 5184 | RAG over Valheim/BepInEx/Unity APIs, project source, curated docs |

`mod/` and `control/` both fire fire-and-forget POSTs at `knowledge/`'s
`/ingest` endpoint, so deploy errors AND runtime/server logs accumulate as
retrievable context — closing the loop between deploy and feedback.

## .NET build is in mcp-dotnet

Generic `dotnet build` and `ilspycmd` decompile are **not** in this repo
— they moved to the sibling [`mcp-dotnet`](https://github.com/jasonuithol/mcp-dotnet)
service (port 5202). The full mod workflow is now two-step:

1. `mcp-dotnet`: `build`, `restore`, `run_tests`, `add_package`, etc.
2. `mcp-valheim/mod`: `deploy_server` / `deploy_client` / `package` / `publish` / `download`

Both services must be running for an end-to-end build → deploy → publish
pass. `claude-sandbox-core`'s `valheim` domain conf wires both up
automatically.

## Consumers

Launched by [`claude-sandbox-core`](https://github.com/jasonuithol/claude-sandbox-core)
via `bin/start.sh valheim <project>` (the `valheim` domain conf lists
this repo in `MCP_REPOS`). Any MCP client speaking streamable HTTP can
mount these services — the protocol is provider-agnostic.

## Usage

```bash
./setup.sh                       # one-time: host venv (control/) + build images
./start.sh                       # bring up mod + control + knowledge
./stop.sh                        # shut everything down
./clean.sh                       # remove venv + containers + images

knowledge/seed.sh                # first-time KB seed
```

To validate setup works from bare state:

```bash
./clean.sh && ./setup.sh && ./start.sh
```

Both containers use host networking (ports above). The knowledge
container needs an NVIDIA GPU + container toolkit for accelerated
embeddings.
