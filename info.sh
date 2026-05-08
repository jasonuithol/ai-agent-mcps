#!/usr/bin/env bash
# info.sh — print connection details for both DB engines.
#
# Default host is `host.containers.internal` (the view from inside a
# sibling container, e.g. the claude-sandbox container). Override with
# HOST=localhost when connecting from the host machine directly.
# Override the SA password with MSSQL_SA_PASSWORD if you changed it.
set -euo pipefail

HOST="${HOST:-host.containers.internal}"
PG_PORT=5432
MSSQL_PORT=1433
SA_PASSWORD="${MSSQL_SA_PASSWORD:-DevP@ssw0rd!42}"

cat <<EOF
postgres
  host:      $HOST
  port:      $PG_PORT
  user:      postgres
  password:  (none — trust auth)
  database:  postgres
  DSN:       postgresql://postgres@$HOST:$PG_PORT/postgres

mssql
  host:      $HOST
  port:      $MSSQL_PORT
  user:      sa
  password:  $SA_PASSWORD
  database:  master
  DSN:       Server=$HOST,$MSSQL_PORT;User Id=sa;Password=$SA_PASSWORD;TrustServerCertificate=yes

(Override host with HOST=localhost ./info.sh; override password with MSSQL_SA_PASSWORD.)
EOF
