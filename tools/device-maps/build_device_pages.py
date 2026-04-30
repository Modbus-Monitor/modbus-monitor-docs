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
PUBLISHED_STATE_DEFAULT = Path("tools/device-maps/published_maps.json")


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
    # Next publish batch candidates (requested)
    TargetSpec("Eaton", "eaton", "EM19 M", "em19-m", "Power Meter", 2, ("EM19 M", "EM19-M", "EM19M")),
    TargetSpec("Eaton", "eaton", "EM20", "em20", "Power Meter", 2, ("EM20",)),
    TargetSpec("Eaton", "eaton", "EM22-DIN", "em22-din", "Power Meter", 2, ("EM22-DIN", "EM22 DIN", "EM22")),
    TargetSpec("Eaton", "eaton", "PXM1000 Series", "pxm1000-series", "Power Meter", 2, ("PXM1000", "PXM 1000"), True),
    TargetSpec("Eaton", "eaton", "PXM3000", "pxm3000", "Power Meter", 2, ("PXM3000", "PXM 3000")),
    TargetSpec("Eaton", "eaton", "PXM4000", "pxm4000", "Power Meter", 2, ("PXM4000", "PXM 4000")),
    TargetSpec("Schneider Electric", "schneider-electric", "PM200", "pm200", "Power Meter", 2, ("PM200",)),
    TargetSpec("Schneider Electric", "schneider-electric", "PM200P", "pm200p", "Power Meter", 2, ("PM200P", "PM 200P")),
    TargetSpec("Schneider Electric", "schneider-electric", "PM210", "pm210", "Power Meter", 2, ("PM210",)),
    TargetSpec("Schneider Electric", "schneider-electric", "iEM3000", "iem3000", "Power Meter", 2, ("IEM3000", "iEM3000", "iEM 3000")),
    TargetSpec("Schneider Electric", "schneider-electric", "CM2000", "cm2000", "Power Meter", 2, ("CM2000", "CM 2000")),
    TargetSpec("SolarEdge", "solaredge", "SE6000", "se6000", "Solar Inverter", 2, ("SE6000", "SE6K")),
    TargetSpec("SolarEdge", "solaredge", "SE10K", "se10k", "Solar Inverter", 2, ("SE10K",)),
    TargetSpec("SolarEdge", "solaredge", "SE12.5K", "se12-5k", "Solar Inverter", 2, ("SE12.5K", "SE12.5", "SE12K5")),
    TargetSpec("SolarEdge", "solaredge", "SE3800H", "se3800h", "Solar Inverter", 2, ("SE3800H",)),
    TargetSpec("SEL", "sel", "SEL-351A", "sel-351a", "Relay", 2, ("SEL-351A", "SEL 351A", "SEL351A")),
    TargetSpec("SEL", "sel", "SEL-751A", "sel-751a", "Relay", 2, ("SEL-751A", "SEL 751A", "SEL751A")),
    TargetSpec("SEL", "sel", "SEL-710", "sel-710", "Relay", 2, ("SEL-710", "SEL 710", "SEL710")),
)


def slugify(value: str) -> str:
    value = value.lower().strip()
    value = re.sub(r"[^a-z0-9]+", "-", value)
    return value.strip("-")


def spec_key(spec: TargetSpec) -> str:
    return f"{spec.manufacturer_slug}/{spec.slug}"


def infer_category_bucket(device_type: str) -> str:
    lowered = device_type.lower()
    if "meter" in lowered:
        return "Energy Meters"
    if "inverter" in lowered:
        return "Solar Inverters"
    if "plc" in lowered:
        return "PLCs"
    return "Other Devices"


def load_published_state(published_state_path: Path, generated_output: Path) -> dict[str, object]:
    state: dict[str, object] = {
        "max_pages_per_run": 15,
        "published_spec_keys": [],
        "release_history": [],
        "last_newly_added": [],
        "next_batch_spec_keys": [],
    }

    if published_state_path.exists():
        try:
            payload = json.loads(published_state_path.read_text(encoding="utf-8"))
            if isinstance(payload, dict):
                max_pages = payload.get("max_pages_per_run", 15)
                if isinstance(max_pages, int) and max_pages > 0:
                    state["max_pages_per_run"] = max_pages

                keys = payload.get("published_spec_keys", payload.get("released_spec_keys", []))
                if isinstance(keys, list):
                    state["published_spec_keys"] = [k for k in keys if isinstance(k, str)]

                release_history = payload.get("release_history", [])
                if isinstance(release_history, list):
                    state["release_history"] = release_history

                last_new = payload.get("last_newly_added", [])
                if isinstance(last_new, list):
                    state["last_newly_added"] = [k for k in last_new if isinstance(k, str)]

                next_batch = payload.get("next_batch_spec_keys", [])
                if isinstance(next_batch, list):
                    state["next_batch_spec_keys"] = [k for k in next_batch if isinstance(k, str)]

            return state
        except json.JSONDecodeError:
            return state

    # Bootstrap from existing generated files so current published maps remain stable.
    bootstrap: set[str] = set()
    for json_file in generated_output.glob("*.json"):
        try:
            payload = json.loads(json_file.read_text(encoding="utf-8"))
        except json.JSONDecodeError:
            continue
        man_slug = str(payload.get("manufacturer_slug", "")).strip()
        slug = str(payload.get("slug", "")).strip()
        if man_slug and slug:
            bootstrap.add(f"{man_slug}/{slug}")
    state["published_spec_keys"] = sorted(bootstrap)
    return state


def save_published_state(
    published_state_path: Path,
    published_keys: set[str],
    newly_added_keys: list[str],
    max_pages_per_run: int,
    release_history: list[dict[str, object]],
    next_batch_spec_keys: list[str],
) -> None:
    published_state_path.parent.mkdir(parents=True, exist_ok=True)
    payload = {
        "max_pages_per_run": max_pages_per_run,
        "published_spec_keys": sorted(published_keys),
        "last_newly_added": newly_added_keys,
        "release_history": release_history,
        "next_batch_spec_keys": next_batch_spec_keys,
    }
    published_state_path.write_text(json.dumps(payload, indent=2), encoding="utf-8")


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


def normalize_device_type(device_type: str) -> str:
    return device_type.strip().lower()


def build_device_meta_description(manufacturer: str, model: str, device_type: str) -> str:
    device_type_lower = normalize_device_type(device_type)
    return (
        f"{manufacturer} {model} Modbus map and register map with sample Modbus registers, "
        f"register addresses, and {device_type_lower} overview for engineers. "
        "Works with Modbus Monitor XPF (import directly) and includes downloadable CSV access in-app."
    )


def build_manufacturer_meta_description(manufacturer: str, devices: list[dict[str, str]]) -> str:
    device_types = sorted({normalize_device_type(d.get("device_type", "")) for d in devices if d.get("device_type")})
    if not device_types:
        summary = "industrial devices"
    elif len(device_types) == 1:
        summary = device_types[0]
    elif len(device_types) == 2:
        summary = f"{device_types[0]} and {device_types[1]}"
    else:
        summary = f"{device_types[0]}, {device_types[1]}, and other industrial devices"

    return (
        f"Browse {manufacturer} Modbus maps for {summary}. "
        "Preview supported models and open pre-built device pages for faster setup "
        "in Modbus Monitor XPF."
    )


def build_main_index_meta_description(device_count: int) -> str:
    return (
        f"Browse {device_count} Modbus device map previews for power meters, solar inverters, UPS systems, "
        "and industrial equipment. Use pre-built maps to reduce setup time in Modbus Monitor XPF."
    )


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
        "## Works with modern Modbus tools",
        "",
        "Use this map with Modbus tools:",
        "",
        "- [Download Modbus Monitor XPF](/download)",
        "- [Build dashboards using Modbus HMI](/modbus-hmi)",
        "- [Compare Modbus tools](/compare)",
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
    title = f"{manufacturer} {model} Modbus Register Map"
    description = build_device_meta_description(manufacturer, model, device_type)
    typical_use = derive_typical_use(device_type)
    unique_context = build_unique_context_sentence(manufacturer, model, device_type, categories)

    # Intro: what the device is and why the map matters.
    intro = (
        f"The {manufacturer} {model} is a {device_type.lower()} used for {typical_use}. "
        f"This page provides a sample Modbus register map with addresses, data types, and "
        f"signal categories to help engineers commission, troubleshoot, and monitor the device. "
        f"{unique_context}"
    )

    lines = [
        "---",
        f"title: {title}",
        f"description: {description}",
        "---",
        "",
        f"# {title}",
        "",
        intro,
        "",
        build_preview_note(),
        "",
        (
            f"Engineers searching for {manufacturer} {model} Modbus map, "
            f"{manufacturer} {model} register map, or {manufacturer} {model} Modbus registers "
            "can use this page as a compatibility snapshot before importing the full map into Modbus Monitor XPF."
        ),
        "",
        "## Overview",
        "",
        f"- **Device:** {manufacturer} {model}",
        f"- **Type:** {device_type}",
        "- **Protocol:** Modbus RTU / Modbus TCP",
        f"- **Use case:** {typical_use}",
        "- **Works with:** Modbus Monitor XPF (import directly)",
        "",
        "## Download Modbus Map",
        "",
        f"The full {manufacturer} {model} Modbus register map is available inside Modbus Monitor XPF "
        "as a pre-built device map. Download the free feature-locked version to access and export the complete map.",
        "",
        "- [Download Modbus Monitor XPF Free](/download)",
        "",
        "## Register Table (Sample)",
        "",
        f"Sample registers from the {manufacturer} {model} Modbus map. "
        "Import the full map in Modbus Monitor XPF to access all registers.",
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
            "## How to Use This Map",
            "",
            f"1. **Download Modbus Monitor XPF** — [Get the free version](/download).",
            f"2. **Select the {manufacturer} {model} device map** — pre-built maps are bundled and ready to load.",
            "3. **Connect to your device** — enter the device IP or COM port and start polling registers immediately.",
            "4. **Visualise and log** — build dashboards, trend data, and export readings without manual register entry.",
            "",
            "## Why Use Pre-Built Maps",
            "",
            "- **Saves time** — no need to manually look up or enter register addresses",
            "- **Reduces errors** — pre-validated maps eliminate mis-typed addresses and wrong data types",
            "- **Speeds commissioning** — connect and poll within minutes instead of hours",
            "- **Reusable across projects** — use the same map across multiple sites and installations",
            "",
            "## Data Categories Available",
            "",
        ]
    )

    for category in categories:
        lines.append(f"- {category}")

    lines.extend(
        [
            "",
            "## Related Tools",
            "",
            "- [Modbus Monitor XPF — Windows Modbus Tool](https://www.modbusmonitor.com/download)",
            "- [Modbus HMI Builder](https://www.modbusmonitor.com/modbus-hmi)",
            "- [Compare Modbus Monitor XPF with Other Tools](https://www.modbusmonitor.com/compare)",
            "",
            "## Related Device Maps",
            "",
        ]
    )

    if related_links:
        for label, rel_link in related_links:
            lines.append(f"- [{label}]({rel_link})")
    lines.append(f"- [All {manufacturer} Modbus Register Maps](../index.md)")
    lines.append("- [All XPF Device Maps](../../index.md)")

    lines.append("")
    output_path.write_text("\n".join(lines), encoding="utf-8")


def write_manufacturer_index(output_path: Path, manufacturer: str, devices: list[dict[str, str]]) -> None:
    title = f"{manufacturer} Modbus Maps"
    description = build_manufacturer_meta_description(manufacturer, devices)

    lines = [
        "---",
        f"title: {title}",
        f"description: {description}",
        "---",
        "",
        f"# {title}",
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
        lines.append(f"- [{manufacturer} {item['model']} Modbus Register Map](./{item['slug']}.md)")

    lines.append("")
    output_path.write_text("\n".join(lines), encoding="utf-8")


def write_main_index(
    output_path: Path,
    grouped: dict[str, list[dict[str, str]]],
    newly_added: list[dict[str, str]],
) -> None:
    flat = [device for devices in grouped.values() for device in devices]
    all_ordered = sorted(flat, key=lambda d: d["order"])
    device_count = len(flat)

    by_manufacturer: dict[str, list[dict[str, str]]] = defaultdict(list)
    for d in all_ordered:
        by_manufacturer[d["manufacturer"]].append(d)

    category_buckets: dict[str, list[dict[str, str]]] = defaultdict(list)
    for d in all_ordered:
        bucket = infer_category_bucket(d.get("device_type", ""))
        category_buckets[bucket].append(d)

    alphabetic = sorted(flat, key=lambda d: (d["manufacturer"].lower(), d["model"].lower()))

    lines = [
        "---",
        "title: Modbus Device Maps for Modbus Monitor XPF",
        f"description: {build_main_index_meta_description(device_count)}",
        "---",
        "",
        "# Modbus Device Maps for Modbus Monitor XPF",
        "",
        "Use these pre-built Modbus map previews to validate device compatibility before commissioning. Each page includes a practical register subset, common categories, and links back to Modbus Monitor XPF.",
        "",
        f"Browse {device_count} pre-built Modbus device map previews for power meters, inverters, UPS systems, and industrial equipment.",
        "",
        "## Start Here {#start-here}",
        "",
        "- [Search and Filter All Device Maps](../../../modbus-device-maps/index.md)",
        "- [Popular Device Maps](#popular-device-maps)",
        "- [Recently Added](#recently-added)",
        "- [Categories](#categories)",
        "- [Browse by Manufacturer](#browse-by-manufacturer)",
        "- [Full List](#full-list)",
        "",
        "## Why These Pages Help",
        "",
        "- Reduce startup time by reusing pre-built device maps",
        "- Confirm available telemetry before full integration",
        "- Compare supported manufacturers and model families quickly",
        "",
        "## Popular Device Maps {#popular-device-maps}",
        "",
        "- [Schneider Electric PM8000 Modbus Register Map](./schneider-electric/pm8000.md)",
        "- [Siemens PAC4200 Modbus Register Map](./siemens/sentron-pac-4200.md)",
        "- [ABB M4M Modbus Register Map](./abb/m4m.md)",
        "- [SolarEdge SE5000 Modbus Register Map](./solaredge/se5000.md)",
        "- [Eaton 93PM Modbus Register Map](./eaton/93pm.md)",
        "",
        "## Recently Added {#recently-added}",
        "",
    ]

    if newly_added:
        for d in newly_added:
            man_slug = slugify(d["manufacturer"])
            lines.append(f"- [{d['manufacturer']} {d['model']} Modbus Register Map](./{man_slug}/{d['slug']}.md)")
    else:
        lines.append("- No new maps were added in this release run.")

    lines.extend(
        [
            "",
            "## Categories {#categories}",
            "",
        ]
    )

    for bucket in ("Energy Meters", "Solar Inverters", "PLCs", "Other Devices"):
        bucket_devices = category_buckets.get(bucket, [])
        if not bucket_devices:
            continue
        lines.append(f"### {bucket}")
        for d in bucket_devices:
            man_slug = slugify(d["manufacturer"])
            lines.append(f"- [{d['manufacturer']} {d['model']}](./{man_slug}/{d['slug']}.md)")
        lines.append("")

    lines.extend(
        [
        "## Browse by Manufacturer {#browse-by-manufacturer}",
        "",
        ]
    )

    for manufacturer, devices in by_manufacturer.items():
        man_slug = slugify(manufacturer)
        devices = sorted(devices, key=lambda d: d["order"])
        model_links = ", ".join(f"[{d['model']}](./{man_slug}/{d['slug']}.md)" for d in devices)
        lines.append(f"- [{manufacturer}](./{man_slug}/index.md): {model_links}")

    lines.extend(["", "## Full List {#full-list}", ""])
    for d in alphabetic:
        man_slug = slugify(d["manufacturer"])
        lines.append(f"- [{d['manufacturer']} {d['model']} Modbus Register Map](./{man_slug}/{d['slug']}.md)")

    lines.extend(
        [
            "",
            "## Use Device Maps in Modbus Monitor XPF",
            "",
            "Start with the device maps hub, then open the free feature-locked version of Modbus Monitor XPF to test and import faster.",
            "",
            "- [Download Modbus Monitor XPF Free](https://www.modbusmonitor.com/download)",
            "- [Compare Modbus Monitor XPF with Other Tools](https://www.modbusmonitor.com/compare)",
            "- [Modbus Tester for Windows](https://www.modbusmonitor.com/modbus-tester)",
            "",
        ]
    )

    output_path.write_text("\n".join(lines), encoding="utf-8")


def write_public_maps_alias_index(output_path: Path, grouped: dict[str, list[dict[str, str]]]) -> None:
    flat = sorted((device for devices in grouped.values() for device in devices), key=lambda d: d["order"])
    manufacturers = sorted({device["manufacturer"] for device in flat})

    lines = [
        "---",
        "title: Modbus Device Maps",
        (
            "description: Search and filter Modbus device maps by manufacturer and model. "
            "Open all map previews and import directly into Modbus Monitor XPF."
        ),
        "---",
        "",
        "# Modbus Device Maps",
        "",
        "Search and filter all generated device maps in one place.",
        "",
        "## Start Here {#start-here}",
        "",
        "- [Map Hub (Popular, Categories, Full List)](../products/xpf/device-maps/index.md)",
        "- [Device Maps Guide Blog Post](../blog/modbus-device-maps.md)",
        "- [XPF User Guide](../products/xpf/user-guide.md)",
        "",
        "See all maps here: [Modbus Device Maps for Modbus Monitor XPF](../products/xpf/device-maps/index.md)",
        "",
        "<div class=\"mdx-device-map-filter\">",
        "  <p><label for=\"mapSearch\"><strong>Search devices</strong></label></p>",
        "  <input id=\"mapSearch\" type=\"search\" placeholder=\"Type model, manufacturer, or keyword...\" style=\"width:100%;max-width:720px;padding:0.6rem;\" />",
        "  <p style=\"margin-top:0.8rem;\"><label for=\"manufacturerFilter\"><strong>Filter by manufacturer</strong></label></p>",
        "  <select id=\"manufacturerFilter\" style=\"width:100%;max-width:420px;padding:0.5rem;\">",
        "    <option value=\"\">All manufacturers</option>",
    ]

    for manufacturer in manufacturers:
        lines.append(f"    <option value=\"{manufacturer}\">{manufacturer}</option>")

    lines.extend(
        [
            "  </select>",
            "  <p style=\"margin-top:0.8rem;\"><strong><span id=\"mapCount\"></span></strong></p>",
            "</div>",
            "",
            "## All Device Maps",
            "",
            "<ul id=\"deviceMapList\">",
        ]
    )

    for device in flat:
        manufacturer = device["manufacturer"]
        model = device["model"]
        device_type = device["device_type"]
        man_slug = slugify(manufacturer)
        link = f"../products/xpf/device-maps/{man_slug}/{device['slug']}/"
        search_blob = f"{manufacturer} {model} {device_type} modbus map register map modbus registers"
        lines.append(
            "  <li "
            f"data-manufacturer=\"{manufacturer}\" "
            f"data-search=\"{search_blob.lower()}\""
            ">"
            f"<a href=\"{link}\">{manufacturer} {model} Modbus Register Map</a>"
            f" - {device_type}"
            "</li>"
        )

    lines.extend(
        [
            "</ul>",
            "",
            "<script>",
            "(function () {",
            "  const searchInput = document.getElementById('mapSearch');",
            "  const manufacturerFilter = document.getElementById('manufacturerFilter');",
            "  const list = document.getElementById('deviceMapList');",
            "  const count = document.getElementById('mapCount');",
            "  if (!searchInput || !manufacturerFilter || !list || !count) return;",
            "",
            "  const items = Array.from(list.querySelectorAll('li'));",
            "",
            "  function applyFilter() {",
            "    const q = searchInput.value.trim().toLowerCase();",
            "    const manufacturer = manufacturerFilter.value;",
            "    let visible = 0;",
            "",
            "    for (const item of items) {",
            "      const matchesManufacturer = !manufacturer || item.dataset.manufacturer === manufacturer;",
            "      const haystack = item.dataset.search || '';",
            "      const matchesSearch = !q || haystack.includes(q);",
            "      const show = matchesManufacturer && matchesSearch;",
            "      item.style.display = show ? '' : 'none';",
            "      if (show) visible += 1;",
            "    }",
            "",
            "    count.textContent = visible + ' map(s) shown';",
            "  }",
            "",
            "  searchInput.addEventListener('input', applyFilter);",
            "  manufacturerFilter.addEventListener('change', applyFilter);",
            "  applyFilter();",
            "})();",
            "</script>",
            "",
        ]
    )

    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text("\n".join(lines), encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser(description="Build device-map MkDocs pages from CSV files")
    parser.add_argument("--source-dir", type=Path, default=SOURCE_DEFAULT)
    parser.add_argument("--docs-output", type=Path, default=DOCS_OUTPUT_DEFAULT)
    parser.add_argument("--generated-output", type=Path, default=GENERATED_OUTPUT_DEFAULT)
    parser.add_argument("--published-state", type=Path, default=PUBLISHED_STATE_DEFAULT)
    parser.add_argument("--max-pages-per-run", type=int, default=15)
    parser.add_argument("--publish-next-batch", action="store_true")
    parser.add_argument("--release-date", type=str, default="")
    args = parser.parse_args()

    source_dir = args.source_dir
    docs_output = args.docs_output
    generated_output = args.generated_output
    published_state_path = args.published_state
    max_pages_per_run = max(args.max_pages_per_run, 1)
    publish_next_batch = args.publish_next_batch
    release_date = args.release_date.strip() if args.release_date else ""

    if not source_dir.exists():
        raise SystemExit(f"Source directory not found: {source_dir}")

    docs_output.mkdir(parents=True, exist_ok=True)
    generated_output.mkdir(parents=True, exist_ok=True)

    # Load release state before JSON cleanup so first-run bootstrap can read existing outputs.
    loaded_state = load_published_state(published_state_path, generated_output)
    known_specs = {spec_key(spec) for spec in TARGET_SPECS}
    loaded_max_pages = loaded_state.get("max_pages_per_run", 15)
    if isinstance(loaded_max_pages, int) and loaded_max_pages > 0:
        max_pages_per_run = max_pages_per_run or loaded_max_pages

    published_keys = set(loaded_state.get("published_spec_keys", []))
    published_keys = {key for key in published_keys if key in known_specs}
    release_history = loaded_state.get("release_history", [])
    if not isinstance(release_history, list):
        release_history = []

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
    already_published_keys = set(published_keys)
    pending_specs = [spec for spec in TARGET_SPECS if spec_key(spec) not in already_published_keys]

    newly_added_keys: list[str] = []
    if publish_next_batch:
        newly_added_specs = pending_specs[:max_pages_per_run]
        newly_added_keys = [spec_key(spec) for spec in newly_added_specs]

    candidate_keys = already_published_keys | set(newly_added_keys)
    successful_new_keys: set[str] = set()

    selected_specs = [spec for spec in TARGET_SPECS if spec_key(spec) in candidate_keys]

    if not selected_specs:
        raise SystemExit(
            "No target specs selected for publishing. Use --publish-next-batch to release first batch."
        )

    for order, spec in enumerate(selected_specs, start=1):
        current_spec_key = spec_key(spec)
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
            "title": f"{spec.manufacturer} {spec.model} Modbus Register Map",
            "description": build_device_meta_description(spec.manufacturer, spec.model, spec.device_type),
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
        if current_spec_key in set(newly_added_keys):
            successful_new_keys.add(current_spec_key)

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
                related.append((f"{manufacturer} {peer['model']} Modbus Register Map", f"./{peer['slug']}.md"))
                if len(related) >= 4:
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

    final_published_keys = already_published_keys | successful_new_keys
    newly_added_key_set = successful_new_keys
    newly_added_records = [
        d
        for devices in grouped.values()
        for d in devices
        if f"{d['manufacturer_slug']}/{d['slug']}" in newly_added_key_set
    ]

    write_main_index(docs_output / "index.md", grouped, newly_added_records)

    release_date_value = release_date if release_date else ""
    if publish_next_batch and successful_new_keys:
        if not release_date_value:
            from datetime import date

            release_date_value = date.today().isoformat()
        release_history.append(
            {
                "released_on": release_date_value,
                "batch_size": len(successful_new_keys),
                "spec_keys": sorted(successful_new_keys),
            }
        )

    next_batch_spec_keys = [spec_key(spec) for spec in TARGET_SPECS if spec_key(spec) not in final_published_keys][
        :max_pages_per_run
    ]

    print("Generated device maps for:")
    for manufacturer in sorted(grouped.keys()):
        print(f"- {manufacturer}: {len(grouped[manufacturer])} page(s)")

    print(f"\nRelease throttle: {max_pages_per_run} map(s) per batch")
    print(f"Publish action used: {'yes' if publish_next_batch else 'no'}")
    print(f"Newly added this run: {len(newly_added_records)}")
    for d in newly_added_records:
        print(f"- {d['manufacturer']} {d['model']}")

    print(f"Next batch candidate size: {len(next_batch_spec_keys)}")
    for key in next_batch_spec_keys:
        print(f"- {key}")

    docs_root = docs_output.parents[2]
    write_public_maps_alias_index(docs_root / "modbus-device-maps" / "index.md", grouped)
    save_published_state(
        published_state_path,
        final_published_keys,
        sorted(successful_new_keys),
        max_pages_per_run,
        release_history,
        next_batch_spec_keys,
    )

    if missing:
        print("\nSkipped targets (missing source CSV or parse issue):")
        for item in missing:
            print(f"- {item}")


if __name__ == "__main__":
    main()
