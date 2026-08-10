#!/usr/bin/env python3
"""
mcp-service.py — db-postgres

Runs inside a Docker container alongside PostgreSQL. Exposes database
management (list/create/drop) and arbitrary DDL/SQL execution to Claude
Code over MCP streamable HTTP.

PostgreSQL is reached via Unix socket (no TCP), connecting as the
'postgres' superuser created at initdb time.

Register with Claude Code:
    claude mcp add db-postgres --transport http http://localhost:5188/mcp
"""

from __future__ import annotations

import asyncio
import atexit
import os
import re
from typing import Any

import psycopg
from psycopg import sql
from mcp.server.mcpserver import MCPServer

# ── Config ────────────────────────────────────────────────────────────────────

PG_SOCKET_DIR = os.environ.get("PG_SOCKET_DIR", "/var/run/postgresql")
PG_USER = os.environ.get("PG_USER", "postgres")
MAX_ROWS = int(os.environ.get("MAX_ROWS", "1000"))
STATEMENT_TIMEOUT_MS = int(os.environ.get("STATEMENT_TIMEOUT_MS", "30000"))

# Database names PostgreSQL ships with that should not be droppable through
# this service. 'postgres' is the maintenance DB we connect to for CREATE/DROP.
PROTECTED_DBS = {"postgres", "template0", "template1"}

# Conservative identifier check: PostgreSQL allows more, but anything beyond
# this is a strong smell of injection or accidental quoting.
_IDENT_RE = re.compile(r"^[A-Za-z_][A-Za-z0-9_]{0,62}$")


def _check_ident(name: str, kind: str = "identifier") -> None:
    if not _IDENT_RE.match(name):
        raise ValueError(
            f"Invalid {kind} {name!r}: must match [A-Za-z_][A-Za-z0-9_]{{0,62}}"
        )


# ── Connection helpers ───────────────────────────────────────────────────────

def _conn(dbname: str, autocommit: bool = False) -> psycopg.Connection:
    """Open a fresh connection to the given database via Unix socket."""
    conn = psycopg.connect(
        host=PG_SOCKET_DIR,
        user=PG_USER,
        dbname=dbname,
        autocommit=autocommit,
    )
    with conn.cursor() as cur:
        cur.execute(f"SET statement_timeout = {STATEMENT_TIMEOUT_MS}")
    if not autocommit:
        conn.commit()
    return conn


async def _to_thread(fn, *args, **kwargs):
    return await asyncio.to_thread(fn, *args, **kwargs)


# ── MCP server ────────────────────────────────────────────────────────────────

mcp = MCPServer(
    name="db-postgres",
    instructions=(
        "PostgreSQL workbench. Use list_databases / create_database / drop_database "
        "to manage databases. Use execute_ddl(database, sql) for schema changes "
        "(autocommit) and execute_sql(database, sql, params) for queries and DML "
        "(transactional, results returned as rows). list_tables and describe_table "
        "are convenience helpers. connection_info() returns a libpq DSN if you "
        "need to drive the database with a tool that doesn't speak MCP. The "
        "'postgres', 'template0', and 'template1' databases are protected from "
        "dropping."
    ),
)


# ── Database management ──────────────────────────────────────────────────────

@mcp.tool()
async def list_databases() -> str:
    """List all databases on the server, with size and owner."""
    def _do() -> list[tuple]:
        with _conn("postgres") as c, c.cursor() as cur:
            cur.execute(
                """
                SELECT d.datname,
                       pg_get_userbyid(d.datdba) AS owner,
                       pg_size_pretty(pg_database_size(d.datname)) AS size,
                       d.datistemplate
                FROM pg_database d
                ORDER BY d.datname
                """
            )
            return cur.fetchall()
    rows = await _to_thread(_do)
    if not rows:
        return "(no databases — that should be impossible)"
    width = max(len(r[0]) for r in rows)
    lines = [f"{len(rows)} database(s):", ""]
    for name, owner, size, is_template in rows:
        tag = "  [template]" if is_template else ""
        lines.append(f"  {name.ljust(width)}  owner={owner}  size={size}{tag}")
    return "\n".join(lines)


@mcp.tool()
async def create_database(name: str, owner: str = None, encoding: str = "UTF8") -> str:
    """
    Create a new database.

    Args:
        name: Database name. Must match [A-Za-z_][A-Za-z0-9_]{0,62}.
        owner: Optional role to own the new database (default: current user).
        encoding: Character encoding (default UTF8).
    """
    try:
        _check_ident(name, "database name")
        if owner is not None:
            _check_ident(owner, "owner")
        _check_ident(encoding, "encoding")
    except ValueError as e:
        return f"CREATE FAILED ✗\n{e}"

    def _do() -> None:
        # CREATE DATABASE cannot run inside a transaction block.
        with _conn("postgres", autocommit=True) as c, c.cursor() as cur:
            stmt = sql.SQL("CREATE DATABASE {name} ENCODING {enc}").format(
                name=sql.Identifier(name),
                enc=sql.Literal(encoding),
            )
            if owner:
                stmt = sql.SQL("CREATE DATABASE {name} OWNER {owner} ENCODING {enc}").format(
                    name=sql.Identifier(name),
                    owner=sql.Identifier(owner),
                    enc=sql.Literal(encoding),
                )
            cur.execute(stmt)

    try:
        await _to_thread(_do)
    except psycopg.Error as e:
        return f"CREATE FAILED ✗\n{e}"
    return f"Created database {name!r} (encoding={encoding}, owner={owner or PG_USER})"


@mcp.tool()
async def drop_database(name: str, force: bool = False) -> str:
    """
    Drop a database. Will fail if there are open connections to it
    unless force=True (DROP DATABASE ... WITH (FORCE)).

    The 'postgres', 'template0', and 'template1' databases are protected
    and cannot be dropped through this tool.
    """
    try:
        _check_ident(name, "database name")
    except ValueError as e:
        return f"DROP FAILED ✗\n{e}"
    if name in PROTECTED_DBS:
        return f"DROP FAILED ✗\n{name!r} is a protected system database."

    def _do() -> None:
        with _conn("postgres", autocommit=True) as c, c.cursor() as cur:
            if force:
                stmt = sql.SQL("DROP DATABASE IF EXISTS {name} WITH (FORCE)").format(
                    name=sql.Identifier(name),
                )
            else:
                stmt = sql.SQL("DROP DATABASE IF EXISTS {name}").format(
                    name=sql.Identifier(name),
                )
            cur.execute(stmt)

    try:
        await _to_thread(_do)
    except psycopg.Error as e:
        return f"DROP FAILED ✗\n{e}"
    return f"Dropped database {name!r}{' (forced)' if force else ''}"


# ── DDL & SQL execution ──────────────────────────────────────────────────────

@mcp.tool()
async def execute_ddl(database: str, ddl: str) -> str:
    """
    Execute one or more DDL statements (CREATE/ALTER/DROP TABLE, INDEX,
    SCHEMA, etc.) against a database. Runs in autocommit mode — each
    statement commits independently.

    Args:
        database: Target database name.
        ddl: SQL text. May contain multiple statements separated by ';'.
    """
    try:
        _check_ident(database, "database name")
    except ValueError as e:
        return f"DDL FAILED ✗\n{e}"
    if database in {"template0", "template1"}:
        return f"DDL FAILED ✗\nrefusing to modify template database {database!r}"

    def _do() -> str:
        with _conn(database, autocommit=True) as c, c.cursor() as cur:
            cur.execute(ddl)
            # statusmessage reflects only the last statement when multiple
            # are submitted; that's the best psycopg gives us here.
            return cur.statusmessage or "(no status)"

    try:
        status = await _to_thread(_do)
    except psycopg.Error as e:
        return f"DDL FAILED ✗\ndatabase={database}\n{e}"
    return f"DDL OK ✓  database={database}\nlast status: {status}"


@mcp.tool()
async def execute_sql(
    database: str,
    query: str,
    params: list[Any] = None,
    max_rows: int = None,
) -> str:
    """
    Execute a SQL query or DML against a database, transactionally.
    SELECT results are returned as rows; INSERT/UPDATE/DELETE return the
    affected row count. Statement timeout is enforced server-side.

    Args:
        database: Target database name.
        query: SQL text. A single statement is recommended; multiple
               statements run in one transaction (commits at end).
        params: Optional positional parameters for %s placeholders.
        max_rows: Cap on returned rows (default from MAX_ROWS env var).
    """
    try:
        _check_ident(database, "database name")
    except ValueError as e:
        return f"SQL FAILED ✗\n{e}"
    cap = max_rows if max_rows is not None else MAX_ROWS

    def _do() -> tuple[str, list[str], list[tuple], int, bool]:
        with _conn(database, autocommit=False) as c, c.cursor() as cur:
            cur.execute(query, params or None)
            status = cur.statusmessage or "(no status)"
            rowcount = cur.rowcount
            if cur.description is None:
                # Non-result-producing statement (INSERT/UPDATE/DELETE/DDL).
                c.commit()
                return status, [], [], rowcount, False
            cols = [d.name for d in cur.description]
            rows = cur.fetchmany(cap + 1)
            truncated = len(rows) > cap
            rows = rows[:cap]
            c.commit()
            return status, cols, rows, rowcount, truncated

    try:
        status, cols, rows, rowcount, truncated = await _to_thread(_do)
    except psycopg.Error as e:
        return f"SQL FAILED ✗\ndatabase={database}\n{e}"

    if not cols:
        return f"SQL OK ✓  database={database}\nstatus: {status}  rowcount={rowcount}"

    # Rendering: ASCII table with column-width sizing. Cap cell width so
    # large bytea/text values don't blow up the response.
    CELL_CAP = 80
    def render(v: Any) -> str:
        if v is None:
            return "NULL"
        s = str(v)
        return s if len(s) <= CELL_CAP else s[:CELL_CAP - 1] + "…"

    rendered = [[render(v) for v in row] for row in rows]
    widths = [len(c) for c in cols]
    for row in rendered:
        for i, cell in enumerate(row):
            if len(cell) > widths[i]:
                widths[i] = len(cell)

    sep = "  ".join("-" * w for w in widths)
    header = "  ".join(c.ljust(widths[i]) for i, c in enumerate(cols))
    body_lines = ["  ".join(cell.ljust(widths[i]) for i, cell in enumerate(row)) for row in rendered]

    note = f"  ({len(rows)} row{'s' if len(rows) != 1 else ''}{' — truncated' if truncated else ''})"
    return (
        f"SQL OK ✓  database={database}  status={status}{note}\n\n"
        f"{header}\n{sep}\n" + "\n".join(body_lines)
    )


# ── Convenience introspection ────────────────────────────────────────────────

@mcp.tool()
async def list_tables(database: str, schema: str = "public") -> str:
    """List tables in a schema (default 'public') with row-count estimates."""
    try:
        _check_ident(database, "database name")
        _check_ident(schema, "schema name")
    except ValueError as e:
        return f"LIST FAILED ✗\n{e}"

    def _do() -> list[tuple]:
        with _conn(database) as c, c.cursor() as cur:
            cur.execute(
                """
                SELECT c.relname,
                       c.reltuples::bigint AS approx_rows,
                       pg_size_pretty(pg_total_relation_size(c.oid)) AS size
                FROM pg_class c
                JOIN pg_namespace n ON n.oid = c.relnamespace
                WHERE c.relkind = 'r' AND n.nspname = %s
                ORDER BY c.relname
                """,
                (schema,),
            )
            return cur.fetchall()

    try:
        rows = await _to_thread(_do)
    except psycopg.Error as e:
        return f"LIST FAILED ✗\n{e}"
    if not rows:
        return f"No tables in {database}.{schema}"
    width = max(len(r[0]) for r in rows)
    lines = [f"{len(rows)} table(s) in {database}.{schema}:", ""]
    for name, approx, size in rows:
        lines.append(f"  {name.ljust(width)}  ~{approx} rows  size={size}")
    return "\n".join(lines)


@mcp.tool()
async def describe_table(database: str, table: str, schema: str = "public") -> str:
    """Show column names, types, nullability, and defaults for a table."""
    try:
        _check_ident(database, "database name")
        _check_ident(schema, "schema name")
        _check_ident(table, "table name")
    except ValueError as e:
        return f"DESCRIBE FAILED ✗\n{e}"

    def _do() -> list[tuple]:
        with _conn(database) as c, c.cursor() as cur:
            cur.execute(
                """
                SELECT column_name, data_type, is_nullable, column_default
                FROM information_schema.columns
                WHERE table_schema = %s AND table_name = %s
                ORDER BY ordinal_position
                """,
                (schema, table),
            )
            return cur.fetchall()

    try:
        rows = await _to_thread(_do)
    except psycopg.Error as e:
        return f"DESCRIBE FAILED ✗\n{e}"
    if not rows:
        return f"Table {schema}.{table} not found in {database}"
    name_w = max(len(r[0]) for r in rows)
    type_w = max(len(r[1]) for r in rows)
    lines = [f"{schema}.{table} in {database}:", ""]
    for col, dtype, nullable, default in rows:
        nul = "NULL" if nullable == "YES" else "NOT NULL"
        dflt = f"  default={default}" if default else ""
        lines.append(f"  {col.ljust(name_w)}  {dtype.ljust(type_w)}  {nul}{dflt}")
    return "\n".join(lines)


# ── Connection metadata ──────────────────────────────────────────────────────

@mcp.tool()
async def connection_info() -> str:
    """Return connection details for connecting directly to PostgreSQL,
    bypassing this MCP service. Useful when you need a tool that speaks
    libpq (psql, pgcli, sqlalchemy, psycopg, etc.) rather than MCP.

    Default host is 'host.containers.internal' (the view from a sibling
    container, e.g. the claude-sandbox). From the host machine itself,
    use 'localhost' instead.
    """
    host = "host.containers.internal"
    port = 5432
    user = PG_USER
    return (
        "PostgreSQL direct connection (bypasses MCP):\n"
        f"  host:      {host}\n"
        f"  port:      {port}\n"
        f"  user:      {user}\n"
        f"  password:  (none — trust auth on host connections)\n"
        f"  database:  postgres (default; user-created DBs also reachable)\n"
        f"  DSN:       postgresql://{user}@{host}:{port}/postgres\n"
        "\n"
        f"From the host machine, replace '{host}' with 'localhost'."
    )


# ── Entrypoint ────────────────────────────────────────────────────────────────

if __name__ == "__main__":
    print(f"PG_SOCKET_DIR={PG_SOCKET_DIR}")
    print(f"PG_USER={PG_USER}")
    print(f"MAX_ROWS={MAX_ROWS}  STATEMENT_TIMEOUT_MS={STATEMENT_TIMEOUT_MS}")
    print("Starting db-postgres MCP on http://0.0.0.0:5188")
    print()
    print("Register with Claude Code:")
    print("  claude mcp add db-postgres --transport http http://localhost:5188/mcp")
    print()
    mcp.run(
        transport="streamable-http",
        host="0.0.0.0",
        port=5188,
        stateless_http=True,
        json_response=True,
    )
