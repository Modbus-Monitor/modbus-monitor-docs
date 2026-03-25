#!/bin/bash

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$SCRIPT_DIR"

GENERATOR_SCRIPT="tools/device-maps/build_device_pages.py"
DEFAULT_SOURCE_DIR_WSL="/mnt/h/OneDrive - Quantum Bit Solutions/Docs/Modbus Map/ModbusMaps/Azure Blob/xpfmaps"
DEFAULT_SOURCE_DIR_WIN="H:/OneDrive - Quantum Bit Solutions/Docs/Modbus Map/ModbusMaps/Azure Blob/xpfmaps"

print_usage() {
    cat <<'EOF'
Usage: ./generate-device-pages.sh [generator args]

Runs the XPF device map generator from the docs repo root.

Defaults:
  --source-dir  Auto-detected from DEVICE_MAP_SOURCE_DIR, the WSL H: mount,
                or H:/... on Windows-style shells.
  --docs-output docs/products/xpf/device-maps
  --generated-output tools/device-maps/generated

Examples:
  ./generate-device-pages.sh
  ./generate-device-pages.sh --source-dir "/mnt/h/.../xpfmaps"
  DEVICE_MAP_SOURCE_DIR="/mnt/h/.../xpfmaps" ./generate-device-pages.sh

Pass-through generator args:
  --source-dir PATH
  --docs-output PATH
  --generated-output PATH
EOF
}

if [[ "${1:-}" == "-h" || "${1:-}" == "--help" ]]; then
    print_usage
    exit 0
fi

if [[ ! -f "mkdocs.yml" ]]; then
    echo "ERROR: mkdocs.yml not found."
    echo "Run this script from the modbus-monitor-docs repository root."
    exit 1
fi

if [[ ! -f "$GENERATOR_SCRIPT" ]]; then
    echo "ERROR: Generator script not found: $GENERATOR_SCRIPT"
    exit 1
fi

PYTHON_CMD="${PYTHON_CMD:-}"
if [[ -z "$PYTHON_CMD" ]]; then
    if command -v python3 >/dev/null 2>&1; then
        PYTHON_CMD="python3"
    elif command -v python >/dev/null 2>&1; then
        PYTHON_CMD="python"
    else
        echo "ERROR: Python is not installed or not on PATH."
        exit 1
    fi
fi

HAS_SOURCE_ARG=0
for arg in "$@"; do
    if [[ "$arg" == "--source-dir" || "$arg" == --source-dir=* ]]; then
        HAS_SOURCE_ARG=1
        break
    fi
done

GENERATOR_ARGS=("$@")

if [[ $HAS_SOURCE_ARG -eq 0 ]]; then
    SOURCE_DIR="${DEVICE_MAP_SOURCE_DIR:-}"

    if [[ -z "$SOURCE_DIR" ]]; then
        if [[ -d "$DEFAULT_SOURCE_DIR_WSL" ]]; then
            SOURCE_DIR="$DEFAULT_SOURCE_DIR_WSL"
        elif [[ -d "$DEFAULT_SOURCE_DIR_WIN" ]]; then
            SOURCE_DIR="$DEFAULT_SOURCE_DIR_WIN"
        else
            echo "ERROR: Could not find the default XPF maps source folder."
            echo "Set DEVICE_MAP_SOURCE_DIR or pass --source-dir explicitly."
            exit 1
        fi
    fi

    GENERATOR_ARGS=(--source-dir "$SOURCE_DIR" "${GENERATOR_ARGS[@]}")
fi

echo "Running device map generator..."
echo "Repo root: $SCRIPT_DIR"
echo "Python: $PYTHON_CMD"
echo "Generator: $GENERATOR_SCRIPT"

"$PYTHON_CMD" "$GENERATOR_SCRIPT" "${GENERATOR_ARGS[@]}"

echo
echo "Device page generation complete."
echo "Generated docs: docs/products/xpf/device-maps"
echo "Generated JSON: tools/device-maps/generated"