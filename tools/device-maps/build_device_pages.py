#!/usr/bin/env python3
"""Generate MkDocs device map pages from Modbus CSV map exports.

This generator intentionally publishes preview subsets only (8-15 rows)
instead of full register tables.
"""

from __future__ import annotations

import argparse
import csv
import json
import re
import shutil
from collections import Counter, defaultdict
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable


SOURCE_DEFAULT = Path(r"H:\OneDrive - Quantum Bit Solutions\Docs\Modbus Map\ModbusMaps\Azure Blob\xpfmaps")
DOCS_OUTPUT_DEFAULT = Path("docs/products/xpf/device-maps")
GENERATED_OUTPUT_DEFAULT = Path("tools/device-maps/generated")


@dataclass(frozen=True)
class TargetSpec:
    manufacturer: str
    manufacturer_slug: str
    model: str
    slug: str
    device_type: str
    tier: int
    preferred_patterns: tuple[str, ...]
    combine_matches: bool = False


TARGET_SPECS = (
    # Tier 1 - highest conversion targets and grouped high-ROI families
    TargetSpec("Schneider Electric", "schneider-electric", "PM8000", "pm8000", "Power Meter", 1, ("PM8000",)),
    TargetSpec("Schneider Electric", "schneider-electric", "ION9000", "ion9000", "Power Meter", 1, ("ION9000",)),
    TargetSpec("Siemens", "siemens", "PAC3200", "sentron-pac-3200", "Power Meter", 1, ("PAC-3200", "PAC3200")),
    TargetSpec("Siemens", "siemens", "PAC4200", "sentron-pac-4200", "Power Meter", 1, ("PAC-4200", "PAC4200")),
    TargetSpec("ABB", "abb", "M4M", "m4m", "Power Meter", 1, ("M4M",)),
    TargetSpec("SolarEdge", "solaredge", "SE5000", "se5000", "Solar Inverter", 1, ("SE5000", "SE5K")),
    TargetSpec("Eaton", "eaton", "93PM", "93pm", "UPS", 1, ("93PM",)),
    TargetSpec("Schneider Electric", "schneider-electric", "PM5000 / PM5100 / PM5300", "pm5000-pm5100-pm5300", "Power Meter", 1, ("PM5100 PM5300", "PM5000"), True),
    TargetSpec("Schneider Electric", "schneider-electric", "PM5500 / PM5560 / PM5580", "pm5500-pm5560-pm5580", "Power Meter", 1, ("PM5500", "PM5560", "PM5580"), True),
    TargetSpec("Schneider Electric", "schneider-electric", "PM5650 / PM5760", "pm5650-pm5760", "Power Meter", 1, ("PM5650", "PM5760"), True),
    TargetSpec("Schneider Electric", "schneider-electric", "EM6400", "em6400", "Power Meter", 1, ("EM6400",)),
    TargetSpec("Schneider Electric", "schneider-electric", "ION7400", "ion7400", "Power Meter", 1, ("ION7400",)),
    TargetSpec("Schneider Electric", "schneider-electric", "ION8800", "ion8800", "Power Meter", 1, ("ION8800",)),
    TargetSpec("Schneider Electric", "schneider-electric", "ION7500 / ION7550", "ion7500-ion7550", "Power Meter", 1, ("ION7500", "ION7550"), True),
    TargetSpec("Schneider Electric", "schneider-electric", "EM4800", "em4800", "Power Meter", 1, ("EM4800",), True),
    TargetSpec("Schneider Electric", "schneider-electric", "EM7290", "em7290", "Power Meter", 1, ("EM7290",)),
    TargetSpec("Schneider Electric", "schneider-electric", "Symmetra PX", "symmetra-px", "UPS", 1, ("Symmetra-PX", "Symmetra PX")),
    TargetSpec("Siemens", "siemens", "PAC2200", "sentron-pac-2200", "Power Meter", 1, ("PAC-2200", "PAC2200")),
    TargetSpec("Siemens", "siemens", "SICAM P", "sicam-p", "Power Meter", 1, ("SICAM-P", "SICAM P")),
    TargetSpec("Siemens", "siemens", "SEM3 Series", "sem3-series", "Power Meter", 1, ("SEM3-", "SEM3"), True),
    TargetSpec("ABB", "abb", "B23 / B24", "b23-b24", "Power Meter", 1, ("B23 B24", "B23-B24")),
    TargetSpec("ABB", "abb", "A41 / A42", "a41-a42", "Power Meter", 1, ("A41-A42", "A41 A42")),
    TargetSpec("ABB", "abb", "Trio 50 / Trio 60", "trio-50-trio-60", "Solar Inverter", 1, ("Trio 50 Trio 60", "Trio")),
    TargetSpec("SolarEdge", "solaredge", "SE5K / SE7K / SE10K / SE12.5K", "se5k-se7k-se10k-se12-5k", "Solar Inverter", 1, ("SE5K", "SE7K", "SE10K", "SE12.5K"), True),
    TargetSpec("SolarEdge", "solaredge", "SE3000H", "se3000h", "Solar Inverter", 1, ("SE3000H",)),
    TargetSpec("Eaton", "eaton", "BladeUPS", "bladeups", "UPS", 1, ("BladeUPS",)),
    TargetSpec("Eaton", "eaton", "PXM2000", "pxm2000", "Power Meter", 1, ("PXM2000",)),
    TargetSpec("SEL", "sel", "SEL-735", "sel-735", "Power Quality and Revenue Meter", 1, ("SEL 735", "SEL-735")),
    # Tier 2 - useful long-tail pages
    TargetSpec("Carlo Gavazzi", "carlo-gavazzi", "EM24", "em24", "Power Meter", 2, ("EM24",)),
    TargetSpec("Accuenergy", "accuenergy", "Acuvim II", "acuvim-ii", "Power Meter", 2, ("Acuvim II", "Acuvim-II")),
)


def slugify(value: str) -> str:
    value = value.lower().strip()
    value = re.sub(r"[^a-z0-9]+", "-", value)
    return value.strip("-")


def infer_units(name: str) -> str:
    lowered = name.lower()
    if "version" in lowered:
        return "-"
    if "tariff" in lowered:
        return "-"
    rules = (
        (("power factor",), "PF"),
        (("kwh", "kvarh", "wh"), "kWh"),
        (("voltage",), "V"),
        (("current l", "current phase", "current average", "amps", "ampere"), "A"),
        (("frequency",), "Hz"),
        (("energy",), "kWh"),
        (("active power", "reactive power", "apparent power", "power"), "kW"),
        (("temperature",), "degC"),
        (("demand",), "kW"),
    )
    for keys, units in rules:
        if any(key in lowered for key in keys):
            return units
    return "-"


def classify_category(name: str) -> str:
    lowered = name.lower()
    if "tariff" in lowered:
        return "General"
    ordered = (
        ("Identification", ("serial", "model", "version", "name")),
        ("Voltage", ("voltage", "v l", "line to line", "line to neutral")),
        ("Current", ("current", "amps", "ampere")),
        ("Energy", ("energy", "kwh", "kvarh")),
        ("Power", ("power", "kw", "kvar", "kva")),
        ("Frequency", ("frequency", "hz")),
        ("Power Factor", ("power factor", "pf")),
        ("Demand", ("demand",)),
        ("Harmonics", ("thd", "harmonic")),
        ("Status", ("status", "alarm", "state", "validity")),
        ("Temperature", ("temperature", "temp")),
        ("Communication", ("modbus", "comm", "port", "address", "baud")),
    )
    for category, keys in ordered:
        if any(key in lowered for key in keys):
            return category
    return "General"


def looks_non_preview_row(name: str) -> bool:
    lowered = name.lower()
    blocked_tokens = (
        "password",
        "factory reset",
        "reset",
        "firmware",
        "write",
        "config",
        "setting",
        "command",
        "header",
        "snapshot",
        "next entry",
        "deviceaddress",
        "manufacturer:16",
    )
    return any(token in lowered for token in blocked_tokens)


def parse_csv_registers(csv_path: Path) -> list[dict[str, str]]:
    with csv_path.open("r", encoding="utf-8-sig", errors="ignore", newline="") as f:
        rows = list(csv.reader(f))

    header_idx = -1
    for idx, row in enumerate(rows):
        if row and row[0].strip() == "RegName":
            header_idx = idx
            break
    if header_idx < 0:
        return []

    registers: list[dict[str, str]] = []
    for row in rows[header_idx + 1 :]:
        if not row:
            continue
        name = (row[0] if len(row) > 0 else "").strip().strip('"')
        address = (row[1] if len(row) > 1 else "").strip().strip('"')
        reg_type = (row[5] if len(row) > 5 else "").strip().strip('"')

        if not name or name.startswith("//"):
            continue
        if not address or not re.search(r"\d", address):
            continue

        registers.append(
            {
                "signal": re.sub(r"\s+", " ", name),
                "address": address,
                "type": reg_type or "Unknown",
                "units": infer_units(name),
                "category": classify_category(name),
            }
        )

    return registers


def pick_preview_rows(registers: list[dict[str, str]], max_rows: int = 12) -> list[dict[str, str]]:
    if not registers:
        return []

    filtered = [row for row in registers if not looks_non_preview_row(row["signal"])]
    if not filtered:
        filtered = registers

    preferred_categories = [
        "Voltage",
        "Current",
        "Power",
        "Energy",
        "Frequency",
        "Power Factor",
        "Demand",
        "Status",
        "Temperature",
        "Harmonics",
    ]
    low_priority_categories = {"Identification", "Communication", "General"}

    # First pass: one representative row per preferred category.
    selected: list[dict[str, str]] = []
    for category in preferred_categories:
        for row in filtered:
            if row["category"] == category and row not in selected:
                selected.append(row)
                break
        if len(selected) >= max_rows:
            return selected

    # Second pass: one representative row per any remaining category.
    seen_categories = {row["category"] for row in selected}
    for row in filtered:
        category = row["category"]
        if category not in seen_categories:
            selected.append(row)
            seen_categories.add(category)
        if len(selected) >= max_rows:
            return selected

    # Third pass: fill to desired preview depth, preferring operational telemetry rows.
    for row in filtered:
        if row in selected:
            continue
        if row["category"] in low_priority_categories:
            continue
        selected.append(row)
        if len(selected) >= max_rows:
            break

    # Final pass: include low-priority rows only if needed to reach target count.
    if len(selected) < max_rows:
        for row in filtered:
            if row in selected:
                continue
            selected.append(row)
            if len(selected) >= max_rows:
                break

    return selected


def pick_categories(registers: list[dict[str, str]], max_items: int = 6) -> list[str]:
    counts = Counter(row["category"] for row in registers)
    ordered = [
        category
        for category, _ in counts.most_common()
        if category not in {"General", "Identification", "Communication"}
    ]
    if not ordered:
        ordered = ["General"]
    return ordered[:max_items]


def find_matching_csvs(source_files: Iterable[Path], spec: TargetSpec) -> list[Path]:
    matches: list[Path] = []
    manufacturer_token = spec.manufacturer.lower().split()[0]
    for f in source_files:
        if f.suffix.lower() != ".csv":
            continue
        name = f.name.lower()
        if manufacturer_token not in name and spec.manufacturer_slug.split("-")[0] not in name:
            continue
        if any(pattern.lower() in name for pattern in spec.preferred_patterns):
            matches.append(f)
    return sorted(matches, key=lambda path: path.name.lower())


def choose_best_csv(source_files: Iterable[Path], spec: TargetSpec) -> Path | None:
    candidates = []
    for f in source_files:
        if f.suffix.lower() != ".csv":
            continue
        name = f.name.lower()
        if spec.manufacturer_slug.split("-")[0] not in name and spec.manufacturer.lower().split()[0] not in name:
            continue
        score = 0
        for pattern in spec.preferred_patterns:
            if pattern.lower() in name:
                score += 10
        # Prefer clean spelling over obvious typo where possible.
        if "interverter" in name:
            score -= 2
        if score > 0:
            candidates.append((score, len(name), f))

    if not candidates:
        return None

    candidates.sort(key=lambda item: (-item[0], item[1]))
    return candidates[0][2]


def choose_source_csvs(source_files: Iterable[Path], spec: TargetSpec) -> list[Path]:
    if spec.combine_matches:
        return find_matching_csvs(source_files, spec)
    selected = choose_best_csv(source_files, spec)
    return [selected] if selected else []


def derive_typical_use(device_type: str) -> str:
    lowered = device_type.lower()
    if "inverter" in lowered:
        return "PV production monitoring, inverter diagnostics, and energy analytics"
    if "ups" in lowered:
        return "power continuity monitoring, alarm review, and resilience planning"
    if "quality" in lowered:
        return "power quality auditing, compliance reporting, and disturbance analysis"
    if "meter" in lowered:
        return "power monitoring, energy metering, and facility automation"
    return "commissioning, troubleshooting, and operational monitoring"


def build_intro(manufacturer: str, model: str, device_type: str) -> str:
    return (
        f"This {manufacturer} {model} Modbus map is supported in Modbus Monitor XPF, "
        "allowing engineers to quickly test, monitor, and visualize device data without "
        "manual register mapping."
    )


def build_preview_note() -> str:
    return "This page shows a preview subset of the full device map available in Modbus Monitor XPF."


def build_focus_phrase(categories: list[str]) -> str:
    normalized = [category.lower() for category in categories[:3]]
    if not normalized:
        return "device telemetry"
    if len(normalized) == 1:
        return f"{normalized[0]} data"
    if len(normalized) == 2:
        return f"{normalized[0]} and {normalized[1]} data"
    return f"{normalized[0]}, {normalized[1]}, and {normalized[2]} data"


def build_domain_phrase(manufacturer: str, device_type: str) -> str:
    lowered_type = device_type.lower()
    if manufacturer == "Schneider Electric":
        return "data centers, switchgear lineups, and advanced power monitoring projects"
    if manufacturer == "Siemens":
        return "industrial automation panels and building management systems"
    if manufacturer == "ABB":
        return "switchboards, facility power distribution, and commercial energy monitoring"
    if manufacturer == "SolarEdge" or "inverter" in lowered_type:
        return "solar inverter monitoring and renewable energy systems"
    if manufacturer == "Eaton" and "ups" in lowered_type:
        return "UPS infrastructure, backup power systems, and resilience programs"
    if manufacturer == "Eaton":
        return "critical power distribution and electrical monitoring systems"
    if manufacturer == "SEL":
        return "utility metering, substations, and power quality analysis"
    if manufacturer == "Carlo Gavazzi":
        return "panel metering, building automation, and energy submetering"
    if manufacturer == "Accuenergy":
        return "multi-circuit energy monitoring, tenant billing, and branch circuit analytics"
    if "ups" in lowered_type:
        return "backup power systems and critical infrastructure monitoring"
    if "quality" in lowered_type:
        return "power quality investigations and compliance reporting"
    if "meter" in lowered_type:
        return "facility metering, commissioning, and operational analytics"
    return "industrial monitoring and commissioning workflows"


def build_unique_context_sentence(
    manufacturer: str,
    model: str,
    device_type: str,
    categories: list[str],
) -> str:
    model_overrides = {
        "PM8000": "Commonly used in data centers and high-end power monitoring systems.",
        "PAC4200": "Common in industrial automation and building management systems.",
        "M4M": "Often deployed in switchboards and compact power monitoring panels.",
        "SE5000": "Widely used in solar inverter monitoring and renewable energy systems.",
        "93PM": "Common in critical backup power systems and UPS monitoring workflows.",
    }
    if model in model_overrides:
        return model_overrides[model]

    focus_phrase = build_focus_phrase(categories)
    domain_phrase = build_domain_phrase(manufacturer, device_type)
    return f"For {manufacturer} {model} deployments, teams often use this map to surface {focus_phrase} in {domain_phrase}."


def build_cta_block() -> list[str]:
    return [
        "## Use This Device Map in Modbus Monitor XPF",
        "",
        "Start using this device map in minutes - no manual register mapping required.",
        "",
        "- [Download Modbus Monitor XPF Free Trial](https://www.modbusmonitor.com/download)",
        "- [Compare Modbus Monitor XPF with Other Tools](https://www.modbusmonitor.com/compare)",
        "- [Modbus Tester for Windows](https://www.modbusmonitor.com/modbus-tester)",
    ]


def write_device_page(
    output_path: Path,
    manufacturer: str,
    model: str,
    device_type: str,
    categories: list[str],
    preview_rows: list[dict[str, str]],
    related_links: list[tuple[str, str]],
) -> None:
    title = f"{manufacturer} {model} Modbus Map"
    description = (
        f"Pre-built {manufacturer} {model} Modbus map for Modbus Monitor XPF with register preview, "
        "device overview, and setup guidance."
    )

    lines = [
        "---",
        f"title: {title}",
        f"description: {description}",
        "---",
        "",
        f"# {title}",
        "",
        build_intro(manufacturer, model, device_type),
        "",
        build_preview_note(),
        "",
        build_unique_context_sentence(manufacturer, model, device_type, categories),
        "",
        *build_cta_block(),
        "",
        "## Quick Facts",
        "",
        f"- **Manufacturer:** {manufacturer}",
        f"- **Model:** {model}",
        f"- **Device Type:** {device_type}",
        "- **Protocol:** Modbus",
        f"- **Typical Use:** {derive_typical_use(device_type)}",
        "- **Available in:** Modbus Monitor XPF",
        "",
        "## Why This Map Matters",
        "",
        "Instead of manually decoding registers and building your setup from scratch, Modbus Monitor XPF provides a pre-built device map to help engineers test, monitor, and visualize data faster.",
        "",
        f"Browse all [XPF device maps](../../index.md) for the full library, explore [{manufacturer} device maps](../index.md) to compare related models, and use [Compare Modbus Monitor XPF with Other Tools](https://www.modbusmonitor.com/compare) when evaluating fit across your stack.",
        "",
        "## Register Preview",
        "",
        "| Signal | Address | Type | Units | Category |",
        "|---|---:|---|---|---|",
    ]

    for row in preview_rows:
        safe_signal = row["signal"].replace("|", "-")
        lines.append(
            f"| {safe_signal} | {row['address']} | {row['type']} | {row['units']} | {row['category']} |"
        )

    lines.extend(
        [
            "",
            "## Common Data Categories",
            "",
        ]
    )

    for category in categories:
        lines.append(f"- {category}")

    lines.extend(
        [
            "",
            "## Typical Use Cases",
            "",
            "- Commissioning new devices with a known-good register baseline",
            "- Troubleshooting Modbus communication and addressing issues",
            "- Building HMI dashboards for operational visibility",
            "- Logging device telemetry for analysis and reporting",
            "",
            "## Related Device Maps",
            "",
        ]
    )

    if related_links:
        for label, rel_link in related_links:
            lines.append(f"- [{label}]({rel_link})")
    lines.append(f"- [All {manufacturer} Device Maps](../index.md)")
    lines.append("- [All XPF Device Maps](../../index.md)")

    lines.extend(
        [
            "",
            *build_cta_block(),
            "",
        ]
    )

    output_path.write_text("\n".join(lines), encoding="utf-8")


def write_manufacturer_index(output_path: Path, manufacturer: str, devices: list[dict[str, str]]) -> None:
    lines = [
        f"# {manufacturer} Modbus Maps",
        "",
        f"Modbus Monitor XPF includes pre-built {manufacturer} device maps to speed up commissioning, monitoring, and troubleshooting.",
        "",
        f"## Supported {manufacturer} Device Families",
        "",
    ]

    for item in sorted(devices, key=lambda d: d["order"]):
        lines.append(f"- {item['model']}")

    lines.extend(["", "## Available Device Pages", ""])

    for item in sorted(devices, key=lambda d: d["order"]):
        lines.append(f"- [{manufacturer} {item['model']} Modbus Map](./{item['slug']}.md)")

    lines.append("")
    output_path.write_text("\n".join(lines), encoding="utf-8")


def write_main_index(output_path: Path, grouped: dict[str, list[dict[str, str]]]) -> None:
    flat = [device for devices in grouped.values() for device in devices]
    tier1 = sorted([d for d in flat if d["tier"] == 1], key=lambda d: d["order"])
    tier2 = sorted([d for d in flat if d["tier"] == 2], key=lambda d: d["order"])

    by_manufacturer: dict[str, list[dict[str, str]]] = defaultdict(list)
    for d in tier1 + tier2:
        by_manufacturer[d["manufacturer"]].append(d)

    lines = [
        "---",
        "title: Modbus Device Maps for Modbus Monitor XPF",
        "description: Browse pre-built Modbus device map previews by manufacturer and model for faster commissioning with Modbus Monitor XPF.",
        "---",
        "",
        "# Modbus Device Maps for Modbus Monitor XPF",
        "",
        "Use these pre-built Modbus map previews to validate device compatibility before commissioning. Each page includes a practical register subset, common categories, and links back to Modbus Monitor XPF.",
        "",
        "Browse 120+ pre-built Modbus device map previews for power meters, inverters, UPS systems, and industrial equipment.",
        "",
        "## Why These Pages Help",
        "",
        "- Reduce startup time by reusing pre-built device maps",
        "- Confirm available telemetry before full integration",
        "- Compare supported manufacturers and model families quickly",
        "",
        "## Popular Device Maps",
        "",
        "- [Schneider Electric PM8000](./schneider-electric/pm8000.md)",
        "- [Siemens PAC4200](./siemens/sentron-pac-4200.md)",
        "- [ABB M4M](./abb/m4m.md)",
        "- [SolarEdge SE5000](./solaredge/se5000.md)",
        "- [Eaton 93PM](./eaton/93pm.md)",
        "",
        "## Tier 1 Priority Maps",
        "",
    ]

    for manufacturer, devices in by_manufacturer.items():
        if not any(d["tier"] == 1 for d in devices):
            continue
        man_slug = slugify(manufacturer)
        devices = sorted([d for d in devices if d["tier"] == 1], key=lambda d: d["order"])
        model_links = ", ".join(f"[{d['model']}](./{man_slug}/{d['slug']}.md)" for d in devices)
        lines.append(f"- [{manufacturer}](./{man_slug}/index.md): {model_links}")

    if tier2:
        lines.extend(["", "## Tier 2 Maps", ""])
        for manufacturer, devices in by_manufacturer.items():
            man_slug = slugify(manufacturer)
            devices = sorted([d for d in devices if d["tier"] == 2], key=lambda d: d["order"])
            if not devices:
                continue
            model_links = ", ".join(f"[{d['model']}](./{man_slug}/{d['slug']}.md)" for d in devices)
            lines.append(f"- [{manufacturer}](./{man_slug}/index.md): {model_links}")

    lines.extend(
        [
            "",
            "## Use Device Maps in Modbus Monitor XPF",
            "",
            "Start with the device maps hub, then open the free trial in Modbus Monitor XPF to test and import faster.",
            "",
            "- [Download Modbus Monitor XPF Free Trial](https://www.modbusmonitor.com/download)",
            "- [Compare Modbus Monitor XPF with Other Tools](https://www.modbusmonitor.com/compare)",
            "- [Modbus Tester for Windows](https://www.modbusmonitor.com/modbus-tester)",
            "",
        ]
    )

    output_path.write_text("\n".join(lines), encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser(description="Build device-map MkDocs pages from CSV files")
    parser.add_argument("--source-dir", type=Path, default=SOURCE_DEFAULT)
    parser.add_argument("--docs-output", type=Path, default=DOCS_OUTPUT_DEFAULT)
    parser.add_argument("--generated-output", type=Path, default=GENERATED_OUTPUT_DEFAULT)
    args = parser.parse_args()

    source_dir = args.source_dir
    docs_output = args.docs_output
    generated_output = args.generated_output

    if not source_dir.exists():
        raise SystemExit(f"Source directory not found: {source_dir}")

    docs_output.mkdir(parents=True, exist_ok=True)
    generated_output.mkdir(parents=True, exist_ok=True)

    # Remove stale generated JSON files from previous runs.
    for old_json in generated_output.glob("*.json"):
        old_json.unlink()

    # Keep only manufacturer folders that belong to current target specs.
    active_manufacturer_slugs = {spec.manufacturer_slug for spec in TARGET_SPECS}
    for child in docs_output.iterdir():
        if child.is_dir() and child.name not in active_manufacturer_slugs:
            shutil.rmtree(child)

    source_files = list(source_dir.glob("*.csv"))
    grouped: dict[str, list[dict[str, str]]] = defaultdict(list)
    missing: list[str] = []

    for order, spec in enumerate(TARGET_SPECS, start=1):
        csv_paths = choose_source_csvs(source_files, spec)
        if not csv_paths:
            missing.append(f"{spec.manufacturer} {spec.model}")
            continue

        merged_registers: list[dict[str, str]] = []
        for csv_path in csv_paths:
            merged_registers.extend(parse_csv_registers(csv_path))

        # Keep first occurrence of a register signature when combining files.
        deduped_registers: list[dict[str, str]] = []
        seen_signatures: set[tuple[str, str, str]] = set()
        for row in merged_registers:
            sig = (row["signal"], row["address"], row["type"])
            if sig in seen_signatures:
                continue
            seen_signatures.add(sig)
            deduped_registers.append(row)

        registers = deduped_registers
        if not registers:
            missing.append(f"{spec.manufacturer} {spec.model} (no registers parsed)")
            continue

        preview_rows = pick_preview_rows(registers, max_rows=12)
        categories = pick_categories(registers)

        device_record = {
            "slug": spec.slug,
            "manufacturer_slug": spec.manufacturer_slug,
            "manufacturer": spec.manufacturer,
            "model": spec.model,
            "title": f"{spec.manufacturer} {spec.model} Modbus Map",
            "description": f"Pre-built {spec.manufacturer} {spec.model} Modbus map for Modbus Monitor XPF.",
            "device_type": spec.device_type,
            "tier": spec.tier,
            "order": order,
            "protocol": "Modbus",
            "typical_use": derive_typical_use(spec.device_type),
            "categories": categories,
            "preview_registers": preview_rows,
            "source_csvs": [path.name for path in csv_paths],
            "related": [],
        }

        # Persist normalized JSON output for traceability.
        json_name = f"{spec.manufacturer_slug}-{spec.slug}.json"
        (generated_output / json_name).write_text(json.dumps(device_record, indent=2), encoding="utf-8")

        grouped[spec.manufacturer].append(device_record)

    # Build pages now that grouped data is available.
    for manufacturer, devices in grouped.items():
        man_slug = slugify(manufacturer)
        man_dir = docs_output / man_slug
        man_dir.mkdir(parents=True, exist_ok=True)

        for old_md in man_dir.glob("*.md"):
            old_md.unlink()

        for device in devices:
            related = []
            for peer in sorted(devices, key=lambda d: d["order"]):
                if peer["slug"] == device["slug"]:
                    continue
                related.append((f"{manufacturer} {peer['model']} Modbus Map", f"./{peer['slug']}.md"))
                if len(related) >= 3:
                    break

            write_device_page(
                output_path=man_dir / f"{device['slug']}.md",
                manufacturer=manufacturer,
                model=device["model"],
                device_type=device["device_type"],
                categories=device["categories"],
                preview_rows=device["preview_registers"],
                related_links=related,
            )

        write_manufacturer_index(man_dir / "index.md", manufacturer, devices)

    write_main_index(docs_output / "index.md", grouped)

    print("Generated device maps for:")
    for manufacturer in sorted(grouped.keys()):
        print(f"- {manufacturer}: {len(grouped[manufacturer])} page(s)")

    if missing:
        print("\nSkipped targets (missing source CSV or parse issue):")
        for item in missing:
            print(f"- {item}")


if __name__ == "__main__":
    main()
