FROM debian:bookworm-slim

LABEL maintainer="mcp-dotnet"
LABEL description="Generic .NET build + test + analyze tools MCP server"

# ── System dependencies ───────────────────────────────────────────────────────
#
# - python3 + pip            : MCP service runtime
# - curl + ca-certificates   : dotnet-install.sh, NuGet, Microsoft package keyring
# - libicu72                 : required by the .NET runtime
# - libssl3, zlib1g          : .NET native deps
# - git                      : occasionally needed by `dotnet restore` for SourceLink/git refs
# - gnupg                    : Microsoft package signing key
RUN apt-get update && apt-get install -y --no-install-recommends \
        python3 python3-pip \
        curl ca-certificates gnupg \
        libicu72 libssl3 zlib1g \
        git \
    && rm -rf /var/lib/apt/lists/*

# ── Python deps for the MCP service ───────────────────────────────────────────

RUN pip install --no-cache-dir --break-system-packages \
        fastmcp \
        "mcp-knowledge-base @ https://github.com/jasonuithol/mcp-knowledge-base/archive/refs/tags/v0.2.1.tar.gz"

# ── dotnet-install.sh (runtime SDK management) ────────────────────────────────
#
# Pulled into the image so install_sdk MCP tool can drop new SDKs into the
# persistent /opt/dotnet volume at runtime without needing network reach to
# Microsoft's package repo every time.
RUN curl -fsSL https://dot.net/v1/dotnet-install.sh -o /usr/local/bin/dotnet-install.sh \
    && chmod +x /usr/local/bin/dotnet-install.sh

# ── Pre-install default SDKs (.NET 8 LTS + .NET 9 current) ────────────────────
#
# Installed to /opt/dotnet. At runtime this path is overlaid by the
# mcp-dotnet-sdks named volume — but the volume is empty on first start,
# and docker will copy the image's /opt/dotnet contents into the volume
# on mount (anonymous + named volumes both inherit from the image's
# directory at the mount point if the volume is empty). So the SDKs we
# install here become the default volume contents on first run.
ENV DOTNET_ROOT=/opt/dotnet
ENV PATH="${DOTNET_ROOT}:${DOTNET_ROOT}/tools:${PATH}"
ENV DOTNET_CLI_TELEMETRY_OPTOUT=1
ENV DOTNET_NOLOGO=1

RUN dotnet-install.sh --channel 8.0 --install-dir /opt/dotnet --no-path \
 && dotnet-install.sh --channel 9.0 --install-dir /opt/dotnet --no-path

# ── ilspycmd (decompile_dll tool) ─────────────────────────────────────────────
#
# Installed as a global dotnet tool. Lands in /opt/dotnet/tools (per
# DOTNET_ROOT) so it's part of the persisted SDK volume.
RUN dotnet tool install ilspycmd --version 9.1.0.7988 --tool-path /opt/dotnet/tools

# ── NuGet config defaults ─────────────────────────────────────────────────────
#
# Container-global NuGet config + package cache live under /opt/nuget,
# overlaid at runtime by the mcp-dotnet-nuget volume so feed/cache state
# persists across restart and rebuild.
ENV NUGET_PACKAGES=/opt/nuget/packages
ENV DOTNET_NUGET_SIGNATURE_VERIFICATION=true
# Tell dotnet/nuget to read+write the global config from /opt/nuget so it
# lands in the persisted volume (instead of /root/.nuget which is not).
RUN mkdir -p /opt/nuget /opt/nuget/packages
COPY NuGet.Config /opt/nuget/NuGet.Config

# ── App ───────────────────────────────────────────────────────────────────────

WORKDIR /app
COPY mcp-service.py .

EXPOSE 5202

CMD ["python3", "mcp-service.py"]
