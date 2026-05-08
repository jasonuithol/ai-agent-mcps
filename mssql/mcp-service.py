#!/usr/bin/env python3
"""
mcp-service.py — db-mssql

Runs inside a Docker container alongside SQL Server 2022. Exposes
database management (list/create/drop) and arbitrary DDL/SQL execution
to Claude Code over MCP streamable HTTP.

SQL Server is reached via TCP on localhost:1433 (in-container only),
authenticating as the 'sa' superuser. The SA password is provided by
the container env (MSSQL_SA_PASSWORD).

Register with Claude Code:
    claude mcp add db-mssql --transport http http://localhost:5189/mcp
"""

from __future__ import annotations

import asyncio
import os
import re
from typing import Any

import pymssql
from fastmcp import FastMCP

# ── Config ────────────────────────────────────────────────────────────────────

MSSQL_HOST = os.environ.get("MSSQL_HOST", "127.0.0.1")
MSSQL_PORT = int(os.environ.get("MSSQL_PORT", "1433"))
MSSQL_USER = os.environ.get("MSSQL_USER", "sa")
MSSQL_PASSWORD = os.environ["MSSQL_SA_PASSWORD"]
MAX_ROWS = int(os.environ.get("MAX_ROWS", "1000"))
QUERY_TIMEOUT_S = int(os.environ.get("QUERY_TIMEOUT_S", "30"))

# System databases that ship with SQL Server. We refuse to drop these.
PROTECTED_DBS = {"master", "tempdb", "model", "msdb"}

# Identifier check: SQL Server allows more (delimited identifiers), but we
# restrict to plain ASCII to keep injection surface small.
_IDENT_RE = re.compile(r"^[A-Za-z_][A-Za-z0-9_]{0,62}$")


def _check_ident(name: str, kind: str = "identifier") -> None:
    if not _IDENT_RE.match(name):
        raise ValueError(
            f"Invalid {kind} {name!r}: must match [A-Za-z_][A-Za-z0-9_]{{0,62}}"
        )


def _quote(ident: str) -> str:
    """Quote a pre-validated identifier for inline SQL composition.

    pymssql has no equivalent of psycopg.sql.Identifier, so we hand-quote.
    The identifier must already have passed _check_ident — this only adds
    the [brackets], it does NOT sanitise."""
    return f"[{ident}]"


# ── Connection helpers ───────────────────────────────────────────────────────

def _conn(dbname: str, autocommit: bool = False) -> pymssql.Connection:
    """Open a fresh connection to the given database."""
    return pymssql.connect(
        server=MSSQL_HOST,
        port=MSSQL_PORT,
        user=MSSQL_USER,
        password=MSSQL_PASSWORD,
        database=dbname,
        autocommit=autocommit,
        timeout=QUERY_TIMEOUT_S,
        login_timeout=10,
    )


async def _to_thread(fn, *args, **kwargs):
    return await asyncio.to_thread(fn, *args, **kwargs)


# ── MCP server ────────────────────────────────────────────────────────────────

mcp = FastMCP(
    name="db-mssql",
    instructions=(
        "SQL Server (mssql) workbench. Use list_databases / create_database / "
        "drop_database to manage user databases. Use execute_ddl(database, sql) "
        "for schema changes and execute_sql(database, sql, params) for queries "
        "and DML. list_tables and describe_table are convenience helpers. "
        "connection_info() returns a SQL Server connection string if you need "
        "to drive the database with a tool that doesn't speak MCP. Parameter "
        "placeholders for execute_sql use %s (pymssql convention). The system "
        "databases 'master', 'tempdb', 'model', and 'msdb' are protected from "
        "dropping."
    ),
)


# ── Database management ──────────────────────────────────────────────────────

@mcp.tool()
async def list_databases() -> str:
    """List all databases on the server, with size (MB) and recovery model."""
    def _do() -> list[tuple]:
        with _conn("master") as c, c.cursor() as cur:
            # sys.databases for owner/state, then size from sys.master_files.
            cur.execute(
                """
                SELECT d.name,
                       SUSER_SNAME(d.owner_sid) AS owner,
                       d.state_desc,
                       d.recovery_model_desc,
                       CAST(SUM(mf.size) * 8.0 / 1024 AS DECIMAL(10,1)) AS size_mb
                FROM sys.databases d
                LEFT JOIN sys.master_files mf ON mf.database_id = d.database_id
                GROUP BY d.name, d.owner_sid, d.state_desc, d.recovery_model_desc
                ORDER BY d.name
                """
            )
            return cur.fetchall()
    rows = await _to_thread(_do)
    if not rows:
        return "(no databases — that should be impossible)"
    width = max(len(r[0]) for r in rows)
    lines = [f"{len(rows)} database(s):", ""]
    for name, owner, state, recovery, size_mb in rows:
        sys_tag = "  [system]" if name in PROTECTED_DBS else ""
        lines.append(
            f"  {name.ljust(width)}  owner={owner}  state={state}  "
            f"recovery={recovery}  size={size_mb} MB{sys_tag}"
        )
    return "\n".join(lines)


@mcp.tool()
async def create_database(name: str) -> str:
    """
    Create a new database. The owner is the connecting login (sa) and the
    collation is the server default (SQL_Latin1_General_CP1_CI_AS).

    Args:
        name: Database name. Must match [A-Za-z_][A-Za-z0-9_]{0,62}.
    """
    try:
        _check_ident(name, "database name")
    except ValueError as e:
        return f"CREATE FAILED ✗\n{e}"

    def _do() -> None:
        # CREATE DATABASE cannot run inside a user transaction, so we use
        # autocommit=True on a connection to master.
        with _conn("master", autocommit=True) as c, c.cursor() as cur:
            cur.execute(f"CREATE DATABASE {_quote(name)}")

    try:
        await _to_thread(_do)
    except pymssql.Error as e:
        return f"CREATE FAILED ✗\n{e}"
    return f"Created database {name!r}"


@mcp.tool()
async def drop_database(name: str, force: bool = False) -> str:
    """
    Drop a database. With force=True, first sets the database to
    SINGLE_USER WITH ROLLBACK IMMEDIATE so any open connections are
    severed before the drop.

    The 'master', 'tempdb', 'model', and 'msdb' system databases are
    protected and cannot be dropped through this tool.
    """
    try:
        _check_ident(name, "database name")
    except ValueError as e:
        return f"DROP FAILED ✗\n{e}"
    if name in PROTECTED_DBS:
        return f"DROP FAILED ✗\n{name!r} is a protected system database."

    def _do() -> None:
        with _conn("master", autocommit=True) as c, c.cursor() as cur:
            if force:
                cur.execute(
                    f"ALTER DATABASE {_quote(name)} "
                    f"SET SINGLE_USER WITH ROLLBACK IMMEDIATE"
                )
            cur.execute(f"DROP DATABASE IF EXISTS {_quote(name)}")

    try:
        await _to_thread(_do)
    except pymssql.Error as e:
        return f"DROP FAILED ✗\n{e}"
    return f"Dropped database {name!r}{' (forced)' if force else ''}"


# ── DDL & SQL execution ──────────────────────────────────────────────────────

@mcp.tool()
async def execute_ddl(database: str, ddl: str) -> str:
    """
    Execute one or more DDL statements (CREATE/ALTER/DROP TABLE, INDEX,
    SCHEMA, etc.) against a database. Runs in autocommit mode — each batch
    commits as it executes.

    Args:
        database: Target database name.
        ddl: T-SQL text. May contain multiple statements separated by ';'
             (or 'GO' batch separators if you submit them; pymssql does NOT
             parse GO — split on it client-side if you need batches).
    """
    try:
        _check_ident(database, "database name")
    except ValueError as e:
        return f"DDL FAILED ✗\n{e}"
    if database in {"tempdb", "model"}:
        return f"DDL FAILED ✗\nrefusing to modify system database {database!r}"

    def _do() -> str:
        with _conn(database, autocommit=True) as c, c.cursor() as cur:
            cur.execute(ddl)
            # Drain any result sets DDL might emit.
            try:
                while cur.nextset():
                    pass
            except pymssql.Error:
                pass
            return "OK"

    try:
        status = await _to_thread(_do)
    except pymssql.Error as e:
        return f"DDL FAILED ✗\ndatabase={database}\n{e}"
    return f"DDL OK ✓  database={database}\nstatus: {status}"


@mcp.tool()
async def execute_sql(
    database: str,
    query: str,
    params: list[Any] = None,
    max_rows: int = None,
) -> str:
    """
    Execute a T-SQL query or DML against a database, transactionally.
    SELECT results are returned as rows; INSERT/UPDATE/DELETE return the
    affected row count.

    Args:
        database: Target database name.
        query: T-SQL text.
        params: Optional positional parameters for %s placeholders
                (pymssql 'pyformat' style without dict).
        max_rows: Cap on returned rows (default from MAX_ROWS env var).
    """
    try:
        _check_ident(database, "database name")
    except ValueError as e:
        return f"SQL FAILED ✗\n{e}"
    cap = max_rows if max_rows is not None else MAX_ROWS

    def _do() -> tuple[list[str], list[tuple], int, bool]:
        with _conn(database, autocommit=False) as c, c.cursor() as cur:
            cur.execute(query, tuple(params) if params else None)
            rowcount = cur.rowcount
            if cur.description is None:
                c.commit()
                return [], [], rowcount, False
            cols = [d[0] for d in cur.description]
            rows = cur.fetchmany(cap + 1)
            truncated = len(rows) > cap
            rows = rows[:cap]
            c.commit()
            return cols, rows, rowcount, truncated

    try:
        cols, rows, rowcount, truncated = await _to_thread(_do)
    except pymssql.Error as e:
        return f"SQL FAILED ✗\ndatabase={database}\n{e}"

    if not cols:
        return f"SQL OK ✓  database={database}  rowcount={rowcount}"

    # Rendering: same ASCII-table format as the postgres service so output
    # is consistent between engines.
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
        f"SQL OK ✓  database={database}{note}\n\n"
        f"{header}\n{sep}\n" + "\n".join(body_lines)
    )


# ── Convenience introspection ────────────────────────────────────────────────

@mcp.tool()
async def list_tables(database: str, schema: str = "dbo") -> str:
    """List user tables in a schema (default 'dbo') with row counts and size."""
    try:
        _check_ident(database, "database name")
        _check_ident(schema, "schema name")
    except ValueError as e:
        return f"LIST FAILED ✗\n{e}"

    def _do() -> list[tuple]:
        with _conn(database) as c, c.cursor() as cur:
            # sys.dm_db_partition_stats gives row counts and pages; sum across
            # heap+clustered partitions only (index_id 0 or 1) to avoid double-
            # counting nonclustered indexes.
            cur.execute(
                """
                SELECT t.name,
                       SUM(CASE WHEN ps.index_id IN (0, 1) THEN ps.row_count ELSE 0 END) AS rows_,
                       CAST(SUM(ps.used_page_count) * 8.0 / 1024 AS DECIMAL(10,2)) AS size_mb
                FROM sys.tables t
                JOIN sys.schemas s ON s.schema_id = t.schema_id
                LEFT JOIN sys.dm_db_partition_stats ps ON ps.object_id = t.object_id
                WHERE s.name = %s
                GROUP BY t.name
                ORDER BY t.name
                """,
                (schema,),
            )
            return cur.fetchall()

    try:
        rows = await _to_thread(_do)
    except pymssql.Error as e:
        return f"LIST FAILED ✗\n{e}"
    if not rows:
        return f"No tables in {database}.{schema}"
    width = max(len(r[0]) for r in rows)
    lines = [f"{len(rows)} table(s) in {database}.{schema}:", ""]
    for name, rc, size_mb in rows:
        lines.append(f"  {name.ljust(width)}  ~{rc} rows  size={size_mb} MB")
    return "\n".join(lines)


@mcp.tool()
async def describe_table(database: str, table: str, schema: str = "dbo") -> str:
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
    except pymssql.Error as e:
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
    """Return connection details for connecting directly to SQL Server,
    bypassing this MCP service. Useful when you need a tool that speaks
    TDS (sqlcmd, pyodbc, pymssql, sqlalchemy, etc.) rather than MCP.

    Default host is 'host.containers.internal' (the view from a sibling
    container, e.g. the claude-sandbox). From the host machine itself,
    use 'localhost' instead.
    """
    host = "host.containers.internal"
    port = 1433
    user = MSSQL_USER
    password = MSSQL_PASSWORD
    return (
        "SQL Server direct connection (bypasses MCP):\n"
        f"  host:      {host}\n"
        f"  port:      {port}\n"
        f"  user:      {user}\n"
        f"  password:  {password}\n"
        f"  database:  master (default; user-created DBs also reachable)\n"
        f"  conn str:  Server={host},{port};User Id={user};Password={password};TrustServerCertificate=yes\n"
        "\n"
        f"From the host machine, replace '{host}' with 'localhost'."
    )


# ── Entrypoint ────────────────────────────────────────────────────────────────

if __name__ == "__main__":
    print(f"MSSQL_HOST={MSSQL_HOST}:{MSSQL_PORT}")
    print(f"MSSQL_USER={MSSQL_USER}")
    print(f"MAX_ROWS={MAX_ROWS}  QUERY_TIMEOUT_S={QUERY_TIMEOUT_S}")
    print("Starting db-mssql MCP on http://0.0.0.0:5189")
    print()
    print("Register with Claude Code:")
    print("  claude mcp add db-mssql --transport http http://localhost:5189/mcp")
    print()
    mcp.run(transport="streamable-http", host="0.0.0.0", port=5189)
