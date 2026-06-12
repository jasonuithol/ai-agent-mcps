#!/usr/bin/env bash
# setup-gpu.sh — install NVIDIA Container Toolkit for GPU-accelerated embeddings
# Run once on a fresh machine. Requires sudo.
set -euo pipefail

echo "=== NVIDIA Container Toolkit Setup ==="
echo "This installs the toolkit so podman can pass your GPU into containers."
echo ""

# Check for NVIDIA GPU
if ! nvidia-smi &>/dev/null; then
    echo "ERROR: nvidia-smi not found. Install NVIDIA drivers first."
    exit 1
fi

GPU=$(nvidia-smi --query-gpu=name --format=csv,noheader)
echo "Detected GPU: $GPU"
echo ""

# Add NVIDIA container toolkit repo
sudo mkdir -p /usr/share/keyrings /etc/cdi

echo "Adding NVIDIA container toolkit repository..."
curl -fsSL https://nvidia.github.io/libnvidia-container/gpgkey \
    | sudo gpg --dearmor -o /usr/share/keyrings/nvidia-container-toolkit-keyring.gpg

curl -s -L https://nvidia.github.io/libnvidia-container/stable/deb/nvidia-container-toolkit.list \
    | sed 's#deb https://#deb [signed-by=/usr/share/keyrings/nvidia-container-toolkit-keyring.gpg] https://#g' \
    | sudo tee /etc/apt/sources.list.d/nvidia-container-toolkit.list > /dev/null

# Install
echo "Installing nvidia-container-toolkit..."
sudo apt-get update -qq
sudo apt-get install -y nvidia-container-toolkit

# Generate CDI spec for podman
echo "Generating CDI spec..."
sudo nvidia-ctk cdi generate --output=/etc/cdi/nvidia.yaml

# Workaround: nvidia-container-toolkit >= 1.19.0 emits a CDI spec at version
# 0.7.0 containing `additionalGids` fields (a v0.7-only feature for letting
# unprivileged containers reach /dev/dri without explicit group membership).
# Podman <= 4.9.3 (the version Ubuntu 24.04 ships) bundles an older CDI
# library that doesn't understand `additionalGids` and rejects the whole
# spec with `unresolvable CDI devices nvidia.com/gpu=all`. Downgrade the
# header to 0.5.0 (still supports the createContainer hook the toolkit
# uses) and strip the offending blocks. Mirror to /var/run/cdi/ — podman
# reads both locations and a stale copy there will mask the patched /etc.
# Re-run this script whenever the toolkit, driver, or kernel updates, as
# the CDI spec gets regenerated and the patch reverts.
echo "Patching CDI spec for podman 4.9.3 compatibility..."
sudo sed -i 's/^cdiVersion: 0\.7\.0/cdiVersion: 0.5.0/' /etc/cdi/nvidia.yaml
sudo sed -i '/^        additionalGids:$/{N;N;d;}' /etc/cdi/nvidia.yaml
sudo cp /etc/cdi/nvidia.yaml /var/run/cdi/nvidia.yaml

# Verify
echo ""
echo "=== Verification ==="
nvidia-ctk cdi list | grep -i nvidia && echo "CDI devices registered." || echo "WARNING: No CDI devices found."
echo ""
echo "Smoke-testing GPU passthrough into a container..."
if podman run --rm --security-opt=label=disable --device nvidia.com/gpu=all \
        docker.io/library/ubuntu:24.04 nvidia-smi -L &>/dev/null; then
    echo "GPU passthrough working."
else
    echo "WARNING: GPU passthrough smoke test failed. Run manually to debug:"
    echo "  podman run --rm --security-opt=label=disable --device nvidia.com/gpu=all \\"
    echo "      docker.io/library/ubuntu:24.04 nvidia-smi"
fi
echo ""
echo "Done. GPU is now available to podman containers via --device nvidia.com/gpu=all"
