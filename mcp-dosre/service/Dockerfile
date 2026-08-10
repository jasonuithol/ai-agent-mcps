FROM python:3.12-slim-bookworm

LABEL maintainer="mcp-dosre"
LABEL description="DOS-era binary reverse-engineering tools MCP server"

# Binary-analysis tool chest. strings + od come from coreutils/binutils in the
# base image; the rest we install explicitly.
#   xxd            -> hex dump (split out of vim-common on Debian bookworm)
#   bsdmainutils   -> hexdump
#   file           -> magic-byte sniffer
#   hexyl          -> colorised hex viewer
#   nasm           -> ndisasm (x86 disassembler, 16/32/64-bit)
#   binutils       -> strings (in case base image lacks it)
#   coreutils      -> md5sum, dd, stat
RUN apt-get update && apt-get install -y --no-install-recommends \
    xxd \
    bsdmainutils \
    file \
    hexyl \
    nasm \
    binutils \
    coreutils \
    ca-certificates \
    && rm -rf /var/lib/apt/lists/*

# rizin + rz-ghidra: headless Ghidra decompiler engine (provides `pdg`) for the
# `decompile` tool. Decompiles individual functions of stripped/optimized 64-bit
# PE binaries where disasm/offset reading is too noisy. No JVM, no GUI.
RUN apt-get update && apt-get install -y --no-install-recommends \
      build-essential cmake ninja-build pkg-config git \
      libuv1-dev libpcre2-dev zlib1g-dev \
    && pip install --no-cache-dir meson ninja \
    && git clone --depth 1 --branch v0.8.2 https://github.com/rizinorg/rizin /tmp/rizin \
    && cd /tmp/rizin && meson setup build --buildtype=release \
    && meson compile -C build && meson install -C build && ldconfig \
    && git clone --depth 1 --branch v0.8.0 --recurse-submodules \
         https://github.com/rizinorg/rz-ghidra /tmp/rzg \
    && cd /tmp/rzg && cmake -B build -G Ninja -DCMAKE_BUILD_TYPE=Release \
         -DCMAKE_PREFIX_PATH=/usr/local -DBUILD_CUTTER_PLUGIN=OFF \
    && cmake --build build && cmake --install build && ldconfig \
    && rizin -v \
    && rm -rf /tmp/rizin /tmp/rzg \
    && rm -rf /var/lib/apt/lists/*

RUN pip install --no-cache-dir \
    "mcp>=2,<3" \
    "mcp-knowledge-base @ https://github.com/jasonuithol/ai-agent-mcps/archive/refs/tags/kb-v0.3.0.tar.gz#subdirectory=mcp-knowledge-base"

WORKDIR /app
COPY mcp-service.py .

EXPOSE 5175

CMD ["python", "mcp-service.py"]
