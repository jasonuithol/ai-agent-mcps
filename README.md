# mcp-steam

MCP service exposing Steam client process control (status, start, stop,
restart). Cross-domain — applies to any Steam game.

Runs directly on the host (NOT in a container) — needs `psutil` access to
host processes and the ability to launch the Steam GUI.

| Endpoint | Port |
|----------|------|
| `http://localhost:5174/mcp` | 5174 |

No knowledge base — runtime status is ephemeral. Game-specific lifecycle
(e.g. Valheim server/client) lives in per-domain control MCPs like
`mcp-valheim/control`.

## Setup

```bash
./setup.sh                # one-time, idempotent (creates .venv/, installs deps)
./start-mcp-service.sh    # run
```

To validate setup works from bare state:

```bash
./clean.sh && ./setup.sh && ./start-mcp-service.sh
```

## Register

```bash
claude mcp add steam --transport http http://localhost:5174/mcp
```

## Consumers

Any MCP client speaking streamable HTTP. Currently launched by
`claude-sandbox/start.sh` for Valheim sessions.
