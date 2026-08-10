# mcp-db

MCP services for relational databases: list/create/drop databases, run
DDL, run SQL. One container per engine — currently PostgreSQL and
Microsoft SQL Server. SQLite is intentionally omitted (in-process; no
client/server semantics to drive over MCP).

| Subdir | Container | MCP port | DB port | Engine |
|--------|-----------|----------|---------|--------|
| `postgres/` | `db-mcp-postgres` | 5188 | 5432 | PostgreSQL 16 |
| `mssql/` | `db-mcp-mssql` | 5189 | 1433 | SQL Server 2022 (Developer) |

Both the MCP transport port and the engine's native port are published,
so host-side tools (`psql`, `sqlcmd`, DBeaver, etc.) can connect
directly when the MCP surface isn't enough. Postgres uses `trust` auth
for both socket and host connections (matches the unauthenticated MCP
transport — local dev only). MSSQL requires the SA password
(`MSSQL_SA_PASSWORD`, defaults to `DevP@ssw0rd!42`). Each engine has
its own named volume for persistence.

## Tools (per engine, identical surface)

**Database management**
- `list_databases()` — name, owner, size, plus engine-specific metadata
  (`recovery model` for mssql, `template` flag for postgres).
- `create_database(name, ...)` — `CREATE DATABASE`. Postgres accepts
  `owner` and `encoding`; MSSQL takes only `name`.
- `drop_database(name, force?)` — `DROP DATABASE`. With `force=True`,
  postgres uses `WITH (FORCE)`; mssql does
  `ALTER DATABASE ... SET SINGLE_USER WITH ROLLBACK IMMEDIATE` first.
  System databases are protected on each engine
  (`postgres`/`template0`/`template1` for pg;
  `master`/`tempdb`/`model`/`msdb` for mssql).

**DDL & SQL**
- `execute_ddl(database, ddl)` — autocommit; multi-statement OK. (mssql
  does NOT auto-split `GO` batches — split client-side if you need that.)
- `execute_sql(database, query, params?, max_rows?)` — transactional.
  SELECTs render as ASCII tables; DML returns rowcount. `%s` placeholder
  binding in both engines.

**Introspection**
- `list_tables(database, schema?)` — default schema is `public` for pg,
  `dbo` for mssql.
- `describe_table(database, table, schema?)` — columns, types,
  nullability, defaults via `information_schema.columns` (works the
  same on both engines).
- `connection_info()` — returns a libpq DSN (postgres) or SQL Server
  connection string (mssql) for direct DB access from a sibling
  container, when you need a tool that doesn't speak MCP.

## Usage

```bash
./setup.sh                # one-time, idempotent (builds both images)
./start.sh                # bring up both containers
./stop.sh                 # shut them down (databases preserved)
./clean.sh                # full teardown (DESTROYS both data volumes)
./info.sh                 # print connection details / DSNs for both engines
```

`./info.sh` defaults to `host.containers.internal` (the view from a
sibling container — e.g. the claude-sandbox); use `HOST=localhost
./info.sh` for connections from the host itself.

To validate setup works from bare state:

```bash
./clean.sh && ./setup.sh && ./start.sh
```

First `./setup.sh` pulls ~1.5 GB for the SQL Server base image. First
`./start.sh` waits ~10 s for SQL Server to extract template DBs.

## Consumers

Designed to be launched by [`claude-sandbox-core`](https://github.com/jasonuithol/claude-sandbox-core)
via a domain conf listing this repo in `MCP_REPOS`. Both services
register independently:

```bash
claude mcp add db-postgres --transport http http://localhost:5188/mcp
claude mcp add db-mssql    --transport http http://localhost:5189/mcp
```

## See also

[`mcp-ssis`](https://github.com/jasonuithol/mcp-ssis) — peer container
that wraps SSIS-on-Linux (`dtexec`) for validating, running, and
benchmarking `.dtsx` packages. Issues its benchmark state-reset SQL
against this repo's mssql container over `host.containers.internal:1433`,
so the two are designed to run side by side. Dev/benchmark rig for
building an SSIS replacement.

## Configuration

**Postgres container** (`postgres/start-container.sh`):
- `MAX_ROWS` — row cap for `execute_sql` (default 1000).
- `STATEMENT_TIMEOUT_MS` — server-side per-statement timeout (default 30000).

**MSSQL container** (`mssql/start-container.sh`):
- `MSSQL_SA_PASSWORD` — SA password. Defaults to a local-dev value
  (`DevP@ssw0rd!42`). SQL Server enforces a strong-password policy.
- `MSSQL_PID` — edition, set to `Developer` (free, full-featured).
- `MAX_ROWS`, `QUERY_TIMEOUT_S` — same idea as postgres.

## Safety notes

- The MCP services connect as the engine's superuser (`postgres` /
  `sa`). Anything the client can call, it can do — including dropping
  user databases. Only system databases are protected.
- Identifiers passed to `create_database` / `drop_database` /
  `list_tables` / `describe_table` are validated against
  `[A-Za-z_][A-Za-z0-9_]{0,62}` before being interpolated. SQL bodies
  passed to `execute_ddl` and `execute_sql` are *not* sanitised — they
  go straight to the engine.
- Both the MCP transport port (`localhost:518x`) and the engine's native
  port (postgres 5432, mssql 1433) are published on the host. Postgres
  trusts all host connections; MSSQL requires the SA password. Local
  dev only — do not point this at a network you don't trust.
