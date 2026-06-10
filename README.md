# mcp-ue4ss

UE4SS domain knowledge base — RAG over the [RE-UE4SS](https://github.com/UE4SS-RE/RE-UE4SS)
documentation tree, exposed as an MCP service.

## Why this exists

UE4SS is a runtime modding framework for Unreal Engine 4. Mods for it
come in two flavours — **C++ DLLs** and **Lua scripts** — both backed by
the same underlying API surface, the same Unreal type system, and the
same Patternsleuth signatures. A language-bound KB would force the same
content to be indexed twice; a **domain-bound** KB indexes it once and
lets any consumer query it.

Consumers (current and anticipated):

- **mcp-c** — DLL authors compiling native UE4SS C++ mods (e.g.
  Advanced-SCUM-Modding).
- **Hypothetical mcp-lua** — when/if a Lua build/runtime MCP service
  appears.
- **Non-containerised Lua scripting workflows** — straight HTTP queries
  to `localhost:5196/mcp` from any editor or tool, no MCP host required.

## Layout

```
mcp-ue4ss/
├── setup.sh / start.sh / stop.sh / clean.sh   — top-level orchestrator
└── knowledge/
    ├── Dockerfile, build-container.sh, start-container.sh
    ├── mcp-service.py            (port 5196, collection `ue4ss_knowledge`)
    ├── requirements.txt
    ├── seed.sh                   (host-side, seeds from mounted UE4SS docs)
    └── knowledge/                (ChromaDB index, created at runtime)
```

There is no `service/` half — UE4SS itself isn't a runtime this project
controls, only documentation about it.

## Endpoints

| URL                              | Purpose                                                    |
|----------------------------------|------------------------------------------------------------|
| `http://localhost:5196/mcp`      | MCP (JSON-RPC) — Claude queries and maintenance            |
| `http://localhost:5196/ingest`   | Plain HTTP POST — service-to-service tool reporting        |

Register with Claude:

```bash
claude mcp add ue4ss-knowledge --transport http http://localhost:5196/mcp
```

## Usage

```bash
./setup.sh        # one-time: builds container image
./start.sh        # bring up the container
./knowledge/seed.sh   # seed from third_party/UE4SS/docs (host-side)
./stop.sh         # stop (container preserved)
./clean.sh        # remove container + image
```

## Seeding sources

`seed.sh` looks for, and indexes if present:

1. `~/Projects/mcp-ue4ss/docs/` — handwritten notes / RE annotations
   (topic: `ue4ss-notes`).
2. `~/Projects/Advanced-SCUM-Modding/third_party/UE4SS/docs/`, split by
   sub-tree so query-time filtering by `topic` works:
   - `cpp-api/` → topic `cpp-api`
   - `lua-api/` → topic `lua-api`
   - `guides/` → topic `guides`
   - `feature-overview/` → topic `feature-overview`
   - `devlogs/` → topic `devlogs`
   - top-level `*.md` (installation-guide.md, etc.) → topic `ue4ss-misc`

Each seed call is idempotent (upsert by stable id), so re-running after a
UE4SS pull just refreshes changed chunks.

The container mounts `$HOME/Projects:/opt/projects:ro`, so paths above
appear inside the container as `/opt/projects/...`. If you keep UE4SS
cloned in a non-standard location, edit `seed.sh` to point at it.

## Querying

The collection is `ue4ss_knowledge`. Useful metadata fields:

- `topic` — `cpp-api`, `lua-api`, `guides`, `feature-overview`,
  `devlogs`, `ue4ss-notes`, `ue4ss-misc`
- `source` — original file name
- `section` — `## ` header within the source

Filter by topic at query time when you want only Lua-side or only
C++-side answers; leave it open when you want cross-cutting context
(e.g. "how is `UObject::ProcessEvent` exposed").

## Domain-bound, not language-bound

This is the load-bearing design choice. If you find yourself writing a
seeding path that only makes sense for one language ABI, that content
probably belongs in a *language* KB (mcp-c, mcp-lua), not here. UE4SS
documentation that happens to use a code-block in one language is still
UE4SS documentation.
