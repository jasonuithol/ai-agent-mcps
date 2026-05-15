# mcp-dotnet

MCP service pair for .NET development. Two containers:

| Subdir | Container | Port | Purpose |
|--------|-----------|------|---------|
| `service/` | `dotnet-mcp-build` | 5202 | `build`, `restore`, `run_tests`, `format`, `analyze`, `pack`, `publish`, NuGet + SDK management, `decompile_dll` |
| `knowledge/` | `dotnet-mcp-knowledge` | 5204 | RAG over .NET docs (MS Learn, xUnit, MSBuild) + project source |

The two halves are paired: `service/` fires fire-and-forget POSTs at
`knowledge/`'s `/ingest` endpoint, so build errors, test failures, and
analyzer warnings accumulate as retrievable context.

The build tool dispatches `dotnet build` against any solution / project
under `~/Projects/<project>` — `global.json` SDK pinning is honoured
automatically. SDKs and NuGet feeds are persistent across container
restarts (named volumes `mcp-dotnet-sdks`, `mcp-dotnet-nuget`).

## SDKs

Image ships with .NET 8 (LTS) + .NET 9 (current) pre-installed at
`/opt/dotnet`. Add more at runtime with the `install_sdk` tool — the
new SDK lands in the `mcp-dotnet-sdks` volume and survives restart.

`ensure_sdk(project)` reads the project's `global.json` and installs the
pinned SDK if missing.

## NuGet

Container starts with `nuget.org` as the only feed. Manage with
`add_feed` / `remove_feed` / `list_feeds`. Per-project `nuget.config`
files in source trees are respected automatically by `dotnet restore`.

## Consumers

Launched by [`claude-sandbox-core`](https://github.com/jasonuithol/claude-sandbox-core)
via `bin/start.sh <domain> <project>` when the domain conf lists this
repo in `MCP_REPOS`. Any MCP client speaking streamable HTTP can mount
these services — the protocol is provider-agnostic.

## Usage

```bash
./setup.sh                # one-time, idempotent (builds both images, creates volumes)
./start.sh                # bring up both containers (calls setup.sh first — self-heals)
./stop.sh                 # shut them down (containers preserved for revival)
./clean.sh                # remove containers + images + named volumes (full teardown)

knowledge/seed.sh         # first-time KB seed
```

To validate setup works from bare state:

```bash
./clean.sh && ./setup.sh && ./start.sh
```

Both containers use host networking (ports above). The knowledge
container needs an NVIDIA GPU + container toolkit for accelerated
embeddings.
