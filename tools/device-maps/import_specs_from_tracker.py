#!/usr/bin/env python3
"""
Import device map specs from modbus_map_tracker_family_dedup.csv and generate AI descriptions.

Usage:
    python import_specs_from_tracker.py --dry-run
    python import_specs_from_tracker.py --min-roi 9 --batch-size 20
    python import_specs_from_tracker.py --generate-specs --claude-api-key YOUR_KEY

Features:
    - Reads tracker CSV
    - Filters by ROI score (default: 10)
    - Excludes already-published specs
    - Generates AI descriptions via Claude API
    - Appends new TargetSpec entries to build_device_pages.py
    - Creates backup of Python file
"""

import argparse
import csv
import json
import re
import sys
from pathlib import Path
from dataclasses import dataclass
from typing import Optional

try:
    import anthropic
except ImportError:
    anthropic = None


@dataclass
class TrackerRecord:
    manufacturer: str
    model: str
    device_type: str
    roi_score: int
    priority_order: int
    status: str
    source_file: str
    notes: str


def load_tracker_csv(csv_path: Path) -> list[TrackerRecord]:
    """Load and parse the tracker CSV file."""
    records = []
    with open(csv_path, encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            try:
                roi = int(row.get("ROI_Score", "0").strip())
                priority = int(row.get("Priority_Order", "999").strip())
                records.append(
                    TrackerRecord(
                        manufacturer=row.get("Manufacturer", "").strip(),
                        model=row.get("Model", "").strip(),
                        device_type=row.get("Type", "").strip(),
                        roi_score=roi,
                        priority_order=priority,
                        status=row.get("Status", "").strip(),
                        source_file=row.get("SourceFile", "").strip(),
                        notes=row.get("Notes", "").strip(),
                    )
                )
            except (ValueError, KeyError):
                continue
    return records


def load_published_specs(published_state_path: Path) -> set[str]:
    """Load already-published spec keys."""
    if not published_state_path.exists():
        return set()
    try:
        data = json.loads(published_state_path.read_text(encoding="utf-8"))
        return set(data.get("published_spec_keys", []))
    except json.JSONDecodeError:
        return set()


def load_existing_specs(build_py_path: Path) -> set[str]:
    """Extract existing spec keys from build_device_pages.py."""
    content = build_py_path.read_text(encoding="utf-8")
    specs = set()
    pattern = r'TargetSpec\("([^"]+)",\s*"([^"]+)"'
    for match in re.finditer(pattern, content):
        man_slug = match.group(2)
        # Extract model slug from the next parts
        rest = content[match.end() : match.end() + 200]
        model_match = re.search(r'[\'"]([^\'"]+)[\'"],\s*[\'"]([^"\']+)[\'"]', rest)
        if model_match:
            model_slug = model_match.group(2)
            specs.add(f"{man_slug}/{model_slug}")
    return specs


def slugify(value: str) -> str:
    """Convert text to URL-safe slug."""
    value = value.lower().strip()
    value = re.sub(r"[^a-z0-9]+", "-", value)
    return value.strip("-")


def generate_ai_description(
    manufacturer: str,
    model: str,
    device_type: str,
    api_key: Optional[str] = None,
) -> str:
    """Generate a short technical description using Claude API."""
    if not anthropic or not api_key:
        return f"Modbus {device_type} device from {manufacturer}"

    try:
        client = anthropic.Anthropic(api_key=api_key)
        prompt = f"""Generate a brief 1-sentence technical description (max 140 chars) for this Modbus device:
Manufacturer: {manufacturer}
Model: {model}
Type: {device_type}

Description should mention key capabilities (e.g., energy measurement, power monitoring, solar inverter control).
Be concise and technical. Start with the manufacturer/model name."""

        message = client.messages.create(
            model="claude-3-5-sonnet-20241022",
            max_tokens=100,
            messages=[{"role": "user", "content": prompt}],
        )
        desc = message.content[0].text.strip()
        return desc[:140]  # Truncate to 140 chars
    except Exception as e:
        print(f"  ⚠ Claude API error: {e}", file=sys.stderr)
        return f"Modbus {device_type} device from {manufacturer}"


def generate_targetspec_line(
    manufacturer: str,
    model: str,
    device_type: str,
    api_key: Optional[str] = None,
) -> str:
    """Generate a TargetSpec Python line."""
    man_slug = slugify(manufacturer)
    model_slug = slugify(model)

    # Extract common patterns from model name
    patterns = tuple(model.split(", "))
    if len(patterns) == 1:
        patterns = (model,)

    # Determine device type category
    type_lower = device_type.lower()
    if "inverter" in type_lower:
        category = "Solar Inverter"
        tier = 1
    elif "meter" in type_lower or "power" in type_lower:
        category = "Power Meter"
        tier = 1
    elif "ups" in type_lower:
        category = "UPS"
        tier = 1
    elif "plc" in type_lower:
        category = "PLC"
        tier = 1
    else:
        category = device_type
        tier = 2

    # For multi-model specs, use combine_matches=True
    combine = len(patterns) > 1 and ", " in model

    patterns_str = ", ".join(f'"{p.strip()}"' for p in patterns)

    line = (
        f'    TargetSpec("{manufacturer}", "{man_slug}", "{model}", "{model_slug}", '
        f'"{category}", {tier}, ({patterns_str})'
    )
    if combine:
        line += ", True"
    line += "),"

    return line


def filter_candidates(
    records: list[TrackerRecord],
    min_roi: int = 10,
    max_batch: int = 20,
    published: set[str] = None,
    existing: set[str] = None,
) -> list[TrackerRecord]:
    """Filter and rank candidates for publication."""
    if published is None:
        published = set()
    if existing is None:
        existing = set()

    # Filter: ROI >= min_roi, Status=PENDING
    filtered = [
        r
        for r in records
        if r.roi_score >= min_roi
        and r.status == "PENDING"
        and f"{slugify(r.manufacturer)}/{slugify(r.model)}" not in published
        and f"{slugify(r.manufacturer)}/{slugify(r.model)}" not in existing
    ]

    # Sort: ROI descending, Priority ascending
    filtered.sort(key=lambda r: (-r.roi_score, r.priority_order))

    return filtered[:max_batch]


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--tracker-csv",
        type=Path,
        default=Path(
            r"C:\Users\prati\source\repos\Modbus-Monitor\ModbusMonitorXPF\ModbusMaps\ModbusMaps\modbus_map_tracker_family_dedup.csv"
        ),
        help="Path to tracker CSV file",
    )
    parser.add_argument(
        "--min-roi",
        type=int,
        default=10,
        help="Minimum ROI score to include (default: 10)",
    )
    parser.add_argument(
        "--batch-size",
        type=int,
        default=20,
        help="Maximum specs to generate (default: 20)",
    )
    parser.add_argument(
        "--generate-specs",
        action="store_true",
        help="Actually update build_device_pages.py (default: dry-run only)",
    )
    parser.add_argument(
        "--claude-api-key",
        type=str,
        help="Claude API key for AI descriptions (optional, uses fallback if not provided)",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Show what would be generated without modifying files",
    )
    args = parser.parse_args()

    print("[Device Map Spec Generator from Tracker]\n")

    # Load data
    if not args.tracker_csv.exists():
        print(f"[ERROR] Tracker CSV not found: {args.tracker_csv}")
        sys.exit(1)

    print(f"[INFO] Reading tracker CSV: {args.tracker_csv}")
    records = load_tracker_csv(args.tracker_csv)
    print(f"   OK: Loaded {len(records)} records\n")

    # Paths
    docs_root = Path(__file__).parent.parent.parent
    build_py = docs_root / "tools" / "device-maps" / "build_device_pages.py"
    published_json = docs_root / "tools" / "device-maps" / "published_maps.json"

    published = load_published_specs(published_json)
    existing = load_existing_specs(build_py)

    print(f"[STATE] Current state:")
    print(f"   - Published specs: {len(published)}")
    print(f"   - Existing in code: {len(existing)}\n")

    # Filter candidates
    candidates = filter_candidates(
        records,
        min_roi=args.min_roi,
        max_batch=args.batch_size,
        published=published,
        existing=existing,
    )

    print(f"[CANDIDATES] Filtered candidates (ROI>={args.min_roi}, not already published):\n")
    for i, cand in enumerate(candidates, 1):
        print(
            f"   {i:2d}. {cand.manufacturer} - {cand.model} "
            f"(ROI:{cand.roi_score}, Priority:{cand.priority_order})"
        )

    if not candidates:
        print("\n[OK] No new candidates to add (all high-ROI specs already published).")
        return

    print(f"\n[GENERATE] Generating {len(candidates)} new TargetSpec entries...\n")

    new_specs = []
    for cand in candidates:
        desc = generate_ai_description(
            cand.manufacturer, cand.model, cand.device_type, args.claude_api_key
        )
        line = generate_targetspec_line(
            cand.manufacturer, cand.model, cand.device_type, args.claude_api_key
        )
        new_specs.append(
            {
                "manufacturer": cand.manufacturer,
                "model": cand.model,
                "line": line,
                "description": desc,
            }
        )
        print(f"   [OK] {cand.manufacturer} {cand.model}")
        print(f"     -> {desc[:70]}...")

    if args.dry_run or not args.generate_specs:
        print(f"\n[DRY-RUN] DRY RUN MODE - no files modified.\n")
        print("Generated TargetSpec lines (ready to add to build_device_pages.py):\n")
        for spec in new_specs:
            print(spec["line"])
        print(f"\nTo apply changes, run with --generate-specs flag:")
        print(f"  python {Path(__file__).name} --generate-specs --min-roi {args.min_roi}\n")
        return

    # Actually update the file
    print(f"\n[UPDATE] Updating {build_py}...")

    # Create backup
    backup_path = build_py.with_suffix(".py.bak")
    build_py.write_text(build_py.read_text(encoding="utf-8"), encoding="utf-8")
    backup_path.write_text(build_py.read_text(encoding="utf-8"), encoding="utf-8")
    print(f"   [OK] Backup created: {backup_path}")

    # Find insertion point (end of TARGET_SPECS tuple)
    content = build_py.read_text(encoding="utf-8")
    match = re.search(r"^(\s*)\)\s*$", content, re.MULTILINE)
    if not match:
        print(f"[ERROR] Could not find end of TARGET_SPECS tuple")
        sys.exit(1)

    indent = match.group(1)
    insertion_point = match.start()

    # Build new lines
    new_lines = "\n".join(spec["line"] for spec in new_specs)
    new_section = f"{indent}# Auto-generated from tracker (2026-06-30)\n{new_lines}\n"

    # Insert
    updated_content = content[:insertion_point] + new_section + content[insertion_point:]
    build_py.write_text(updated_content, encoding="utf-8")

    print(f"   [OK] Added {len(new_specs)} new TargetSpec entries")
    print(f"   [OK] File updated: {build_py}\n")

    print(f"[SUCCESS] Next steps:\n")
    print(f"   1. Run the generator:")
    print(
        f"      cd {docs_root}"
    )
    print(
        f"      ./generate-device-pages.sh --publish-next-batch --max-pages-per-run {len(new_specs)} --release-date 2026-06-30"
    )
    print(f"\n   2. Review & commit:")
    print(f"      git diff {build_py}")
    print(f"      git add -A && git commit -m 'Add {len(new_specs)} new device map specs (ROI>={args.min_roi})'")
    print(f"      git push")


if __name__ == "__main__":
    main()
