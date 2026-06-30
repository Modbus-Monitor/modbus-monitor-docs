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
       ./generate-device-pages.sh --wizard
       ./generate-device-pages.sh --skip
       ./generate-device-pages.sh skip

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
    --publish-next-batch
    --max-pages-per-run N
    --release-date YYYY-MM-DD

Script-only options:
    --wizard  Run an interactive guided workflow.
    --skip    Skip all Q&A and run normally with current/default config.

Guided workflow can help you avoid missing steps:
    1) Confirm latest Azure maps were copied into xpfmaps.
    2) Choose regenerate-only vs publish-next-batch.
    3) Enter batch size and release date for new map publishing.
    4) Optionally run mkdocs strict build and local preview.
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

GUIDED_MODE=0
SKIP_QA=0
ORIGINAL_ARGS=("$@")

FILTERED_ARGS=()
for arg in "$@"; do
    case "$arg" in
        --wizard)
            GUIDED_MODE=1
            ;;
        --skip|skip)
            SKIP_QA=1
            ;;
        *)
            FILTERED_ARGS+=("$arg")
            ;;
    esac
done

set -- "${FILTERED_ARGS[@]}"

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

# Build a best-effort source-dir hint for guided prompts.
SOURCE_DIR_HINT=""
EXPECT_SOURCE_VALUE=0
for arg in "$@"; do
    if [[ $EXPECT_SOURCE_VALUE -eq 1 ]]; then
        SOURCE_DIR_HINT="$arg"
        EXPECT_SOURCE_VALUE=0
        continue
    fi

    case "$arg" in
        --source-dir)
            EXPECT_SOURCE_VALUE=1
            ;;
        --source-dir=*)
            SOURCE_DIR_HINT="${arg#--source-dir=}"
            ;;
    esac
done

if [[ -z "$SOURCE_DIR_HINT" ]]; then
    SOURCE_DIR_HINT="${DEVICE_MAP_SOURCE_DIR:-}"
fi

if [[ -z "$SOURCE_DIR_HINT" ]]; then
    if [[ -d "$DEFAULT_SOURCE_DIR_WSL" ]]; then
        SOURCE_DIR_HINT="$DEFAULT_SOURCE_DIR_WSL"
    elif [[ -d "$DEFAULT_SOURCE_DIR_WIN" ]]; then
        SOURCE_DIR_HINT="$DEFAULT_SOURCE_DIR_WIN"
    else
        SOURCE_DIR_HINT="$DEFAULT_SOURCE_DIR_WSL"
    fi
fi

GENERATOR_ARGS=("$@")

run_mkdocs_strict=0
run_mkdocs_serve=0

if [[ $SKIP_QA -eq 0 ]]; then
    if [[ $GUIDED_MODE -eq 1 || ${#ORIGINAL_ARGS[@]} -eq 0 ]]; then
        echo
        echo "Guided workflow mode"
        
        # Check for next_release_batch.csv
        BATCH_CSV="tools/device-maps/next_release_batch.csv"
        BATCH_COUNT=0
        if [[ -f "$BATCH_CSV" ]]; then
            BATCH_COUNT=$(tail -n +2 "$BATCH_CSV" | wc -l)
            echo "Found next_release_batch.csv with $BATCH_COUNT maps ready to publish"
        fi
        
        echo
        echo "Choose one option:"
        echo "  1) Regenerate current published pages only"
        if [[ $BATCH_COUNT -gt 0 ]]; then
            echo "  2) Publish next batch ($BATCH_COUNT maps from next_release_batch.csv)"
        fi
        echo "  3) Custom batch size (manual entry)"
        echo "  4) skip (no Q&A, run current/default config)"
        if [[ $BATCH_COUNT -gt 0 ]]; then
            read -r -p "Selection [1/2/3/4]: " workflow_choice
        else
            read -r -p "Selection [1/3/4]: " workflow_choice
        fi
        workflow_choice="${workflow_choice:-1}"

        if [[ "$workflow_choice" == "4" || "$workflow_choice" == "skip" || "$workflow_choice" == "SKIP" ]]; then
            SKIP_QA=1
        else
            echo
            echo "Step 1 target source folder: $SOURCE_DIR_HINT"
            read -r -p "Step 1: Did you update latest maps from Azure into this folder? [y/N]: " maps_synced
            maps_synced="${maps_synced:-n}"
            case "$maps_synced" in
                y|Y|yes|YES)
                    ;;
                *)
                    echo "Stopped. Please sync latest Azure maps into:"
                    echo "  $SOURCE_DIR_HINT"
                    echo "Then rerun this script."
                    exit 1
                    ;;
            esac

            if [[ "$workflow_choice" == "2" && $BATCH_COUNT -gt 0 ]]; then
                # Use batch from next_release_batch.csv
                batch_size=$BATCH_COUNT
                echo
                echo "Using batch from next_release_batch.csv: $batch_size maps"
                default_release_date="$(date +%F)"
                read -r -p "Release date [${default_release_date}]: " release_date
                release_date="${release_date:-$default_release_date}"
                GENERATOR_ARGS+=(--publish-next-batch --max-pages-per-run "$batch_size" --release-date "$release_date")
            elif [[ "$workflow_choice" == "3" ]] || [[ "$workflow_choice" == "2" && $BATCH_COUNT -eq 0 ]]; then
                # Custom batch size
                echo
                read -r -p "How many maps do you want to publish this batch? [20]: " batch_size
                batch_size="${batch_size:-20}"

                if [[ ! "$batch_size" =~ ^[0-9]+$ ]] || [[ "$batch_size" -lt 1 ]]; then
                    echo "ERROR: Batch size must be a positive integer."
                    exit 1
                fi

                default_release_date="$(date +%F)"
                read -r -p "Release date [${default_release_date}]: " release_date
                release_date="${release_date:-$default_release_date}"

                GENERATOR_ARGS+=(--publish-next-batch --max-pages-per-run "$batch_size" --release-date "$release_date")
            fi

            echo
            read -r -p "Run mkdocs strict build after generation? [Y/n]: " strict_choice
            strict_choice="${strict_choice:-y}"
            case "$strict_choice" in
                n|N|no|NO)
                    run_mkdocs_strict=0
                    ;;
                *)
                    run_mkdocs_strict=1
                    ;;
            esac

            if [[ $run_mkdocs_strict -eq 1 ]]; then
                read -r -p "Run local preview server (mkdocs serve) after strict build? [y/N]: " serve_choice
                serve_choice="${serve_choice:-n}"
                case "$serve_choice" in
                    y|Y|yes|YES)
                        run_mkdocs_serve=1
                        ;;
                    *)
                        run_mkdocs_serve=0
                        ;;
                esac
            fi
        fi
    fi
fi

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
if [[ ${#GENERATOR_ARGS[@]} -gt 0 ]]; then
    echo "Args: ${GENERATOR_ARGS[*]}"
fi

"$PYTHON_CMD" "$GENERATOR_SCRIPT" "${GENERATOR_ARGS[@]}"

echo
echo "Device page generation complete."
echo "Generated docs: docs/products/xpf/device-maps"
echo "Generated JSON: tools/device-maps/generated"

PUBLISHED_STATE_PATH="tools/device-maps/published_maps.json"
if [[ -f "$PUBLISHED_STATE_PATH" ]]; then
    NEXT_BATCH_COUNT="$($PYTHON_CMD - <<'PY'
import json
from pathlib import Path

state_path = Path("tools/device-maps/published_maps.json")
try:
    data = json.loads(state_path.read_text(encoding="utf-8"))
except Exception:
    print("-1")
else:
    next_batch = data.get("next_batch_spec_keys", [])
    print(len(next_batch) if isinstance(next_batch, list) else -1)
PY
)"

    if [[ "$NEXT_BATCH_COUNT" == "0" ]]; then
        echo
        echo "No next-batch candidates are currently queued (next batch = 0)."
        echo "To add the next maps, follow these steps:"
        echo "  1) Add new TargetSpec entries in tools/device-maps/build_device_pages.py"
        echo "  2) Copy matching CSVs into the source folder shown by this script"
        echo "  3) Run: ./generate-device-pages.sh --publish-next-batch --max-pages-per-run 20"

        if [[ $SKIP_QA -eq 0 ]]; then
            echo
            read -r -p "Do you want to add new target specs now? [y/N]: " add_specs_now
            add_specs_now="${add_specs_now:-n}"
            case "$add_specs_now" in
                y|Y|yes|YES)
                    echo
                    echo "Target spec checklist"
                    echo "- File: tools/device-maps/build_device_pages.py"
                    echo "- Section: TARGET_SPECS = ( ... )"
                    echo "- Add one TargetSpec(...) entry per new model"
                    echo "- Keep manufacturer_slug and slug stable/lowercase-kebab"
                    echo "- preferred_patterns must match real CSV filenames"
                    echo "- For model families sharing multiple CSVs, set combine_matches=True"
                    echo
                    echo "Template to copy:"
                    echo "  TargetSpec(\"Manufacturer\", \"manufacturer-slug\", \"Model\", \"model-slug\", \"Power Meter\", 2, (\"PATTERN1\", \"PATTERN2\"), False),"
                    echo
                    echo "CSV source folder to sync/update:"
                    echo "  $SOURCE_DIR_HINT"
                    echo
                    echo "After editing specs and syncing CSVs, run:"
                    echo "  ./generate-device-pages.sh --publish-next-batch --max-pages-per-run 20"
                    ;;
                *)
                    ;;
            esac
        fi
    fi
fi

if [[ $run_mkdocs_strict -eq 1 ]]; then
    echo
    echo "Running strict docs validation..."
    "$PYTHON_CMD" -m mkdocs build --strict
fi

if [[ $run_mkdocs_serve -eq 1 ]]; then
    echo
    echo "Starting local docs preview (Ctrl+C to stop)..."
    "$PYTHON_CMD" -m mkdocs serve
fi