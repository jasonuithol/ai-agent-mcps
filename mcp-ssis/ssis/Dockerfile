FROM ubuntu:22.04

LABEL maintainer="mcp-ssis"
LABEL description="SSIS-on-Linux dev/benchmark rig: validate, run, and benchmark .dtsx packages via MCP"

# We start from a clean Ubuntu rather than the mssql/server image because
# this container does NOT run sqlservr — SQL Server lives in the peer
# db-mcp-mssql container (reached over host.containers.internal:1433).
# Bundling sqlservr here would just contaminate benchmark CPU/RAM.
#
# Microsoft's "SSIS on Linux is not supported in containers" caveat
# applies. This image is for a dev/benchmark rig only — do not point it
# at a load you care about.

ENV DEBIAN_FRONTEND=noninteractive

# Base deps + Microsoft apt repo. curl/gnupg2/lsb-release are used only
# during install and could be pruned, but keeping them helps when someone
# `docker exec`s in to debug a misbehaving package.
RUN apt-get update && apt-get install -y --no-install-recommends \
        ca-certificates \
        curl \
        gnupg2 \
        lsb-release \
        apt-transport-https \
        software-properties-common \
        time \
        python3 \
        python3-pip \
        python3-venv \
        unixodbc \
    && rm -rf /var/lib/apt/lists/*

# Drop the key in /etc/apt/trusted.gpg.d/ so it's consulted globally —
# the Microsoft-published .list files don't carry a signed-by= clause
# pointing at a custom keyring, so a path under /usr/share/keyrings/
# would be silently ignored and apt-get update would fail with
# NO_PUBKEY EB3E94ADBE1229CF.
RUN curl -fsSL https://packages.microsoft.com/keys/microsoft.asc \
        | gpg --dearmor -o /etc/apt/trusted.gpg.d/microsoft.gpg \
    && curl -fsSL https://packages.microsoft.com/config/ubuntu/22.04/mssql-server-2022.list \
        -o /etc/apt/sources.list.d/mssql-server-2022.list \
    && curl -fsSL https://packages.microsoft.com/config/ubuntu/22.04/prod.list \
        -o /etc/apt/sources.list.d/microsoft-prod.list

# Install SSIS runtime + sqlcmd. ACCEPT_EULA is for ssis-conf below; the
# mssql-tools18 package needs an interactive EULA otherwise, which we
# bypass via the env var.
RUN apt-get update \
    && ACCEPT_EULA=Y apt-get install -y --no-install-recommends \
        mssql-server-is \
        mssql-tools18 \
    && rm -rf /var/lib/apt/lists/*

# Non-interactive SSIS setup: accepts EULA, picks edition. Developer is
# free and full-featured — matches the peer db-mcp-mssql container's PID.
#
# Two non-fatal failures are tolerated:
#   * Pre-set telemetry off so the customer-feedback prompt is skipped.
#     This sub-command also returns non-zero in containers (no systemd),
#     hence the '|| true' on the same line.
#   * The main 'setup' call accepts EULA and writes the config file
#     before trying to start the telemetry systemd service. In a
#     container there's no systemd, so service-start fails — but the
#     config is on disk already, which is all we need at runtime.
RUN ACCEPT_EULA=Y MSSQL_PID=Developer /opt/ssis/bin/ssis-conf -n setup || true \
    && test -f /var/opt/ssis/ssis.conf \
        || (echo "ssis-conf did not write /var/opt/ssis/ssis.conf — install is broken" >&2 && exit 1)

# Python venv for the MCP service. Same pattern as mcp-db/mssql to keep
# the two services symmetric.
ENV VIRTUAL_ENV=/opt/venv
RUN python3 -m venv "$VIRTUAL_ENV"
ENV PATH="$VIRTUAL_ENV/bin:/opt/mssql-tools18/bin:/opt/ssis/bin:$PATH"

RUN pip install --no-cache-dir \
        fastmcp \
        pymssql

WORKDIR /app
COPY mcp-service.py entrypoint.sh ./
RUN chmod +x entrypoint.sh \
    && mkdir -p /packages/logs \
    && chown -R ssis:ssis /app /packages

# MCP transport port. No native port — dtexec is a CLI, not a service.
EXPOSE 5190

# The mssql-server-is package creates a 'ssis' user that owns /var/opt/ssis.
# /opt/ssis itself is root-owned but world-readable, so the ssis user
# can invoke dtexec.
USER ssis
CMD ["./entrypoint.sh"]
