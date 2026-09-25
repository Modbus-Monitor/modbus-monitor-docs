"""Render browsing pages from the public catalog; never read private map sources.

Generated Markdown is committed so MkDocs builds need no network or sibling repo.
Refresh explicitly against a reviewed checkout of modbus-device-maps.
"""
from __future__ import annotations

import argparse
from collections import defaultdict
import hashlib
import html
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
BASE = "https://docs.quantumbitsolutions.com/"
DATA = "https://modbus-monitor.github.io/modbus-device-maps/"
HUB = BASE + "modbus-device-maps/"
TERMS = DATA + "data-license/"
REQUEST = "https://github.com/Modbus-Monitor/modbus-device-maps/issues/new/choose"


def write(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content.rstrip() + "\n", encoding="utf-8", newline="\n")


def cell(value: object) -> str:
    return html.escape(str(value)).replace("|", "&#124;").replace("\n", " ")


def build(catalog_root: Path, docs_root: Path = ROOT / "docs") -> dict:
    catalog = json.loads((catalog_root / "catalog.json").read_text(encoding="utf-8"))
    entries = catalog["maps"]
    hashes = {}
    for path in [catalog_root / "catalog.json", *sorted((catalog_root / "maps").rglob("*.json"))]:
        hashes[path.relative_to(catalog_root).as_posix()] = hashlib.sha256(path.read_bytes()).hexdigest()
    guides = sorted(p for p in (docs_root / "products/xpf/device-maps").glob("*/*.md") if p.name != "index.md")
    routes, manufacturers, categories = {}, defaultdict(list), defaultdict(list)
    for entry in entries:
        identifier = entry["id"]
        if not re.fullmatch(r"[a-z0-9-]+/[a-z0-9-]+", identifier):
            raise ValueError(f"Unsafe catalog ID: {identifier}")
        guide = docs_root / f"products/xpf/device-maps/{identifier}.md"
        routes[identifier] = (f"products/xpf/device-maps/{identifier}/" if guide.exists()
                              else f"modbus-device-maps/previews/{identifier}/")
        manufacturers[entry["manufacturer"]].append(entry)
        categories[entry["device_type"]].append(entry)
        payload = json.loads((catalog_root / entry["json_url"]).read_text(encoding="utf-8"))
        if payload["id"] != identifier:
            raise ValueError(f"Mismatched map ID: {identifier}")
        json_url = DATA + entry["json_url"]
        dataset = {'@context': 'https://schema.org', '@type': 'Dataset',
                   'name': f"{entry['manufacturer']} {entry['model']} public register preview",
                   'description': 'Sample register addresses and data types; not a complete map or hardware verification.',
                   'url': BASE + routes[identifier],
                   'license': TERMS,
                   'creator': {'@type': 'Organization', 'name': 'Quantum Bit Solutions', 'url': 'https://quantumbitsolutions.com/'},
                   'distribution': {'@type': 'DataDownload', 'encodingFormat': 'application/json', 'contentUrl': json_url}}
        structured = '<script type="application/ld+json">' + json.dumps(dataset).replace('<', '\\u003c') + '</script>'
        if guide.exists():
            # Add the data provenance without changing the existing register table or headings.
            source = guide.read_text(encoding="utf-8")
            source = re.sub(r'\n<!-- public-preview-metadata -->.*?<!-- /public-preview-metadata -->\n?', '', source, flags=re.S)
            if json_url not in source:
                source = source.replace("## Register Table (Sample)",
                    f"[Public JSON preview]({json_url}) · [Preview data terms]({TERMS})\n\n## Register Table (Sample)")
            normalized = re.sub(r'[^a-z0-9]', '', source.lower())
            differs = any(re.sub(r'[^a-z0-9]', '', str(row['name']).lower()) not in normalized
                          or str(row['display_address']) not in source for row in payload['registers'])
            supplemental = ''
            if differs:
                supplemental = '<details><summary>Public catalog sample</summary><p>The public JSON sample differs from the guide table above. Both are previews; confirm the exact model and firmware before use.</p><table><thead><tr><th>Signal</th><th>Display address</th><th>Data type</th><th>Units</th><th>Category</th></tr></thead><tbody>'
                supplemental += ''.join('<tr>' + ''.join('<td>' + html.escape(str(row[k])) + '</td>' for k in ('name', 'display_address', 'data_type', 'unit', 'category')) + '</tr>' for row in payload['registers'])
                supplemental += '</tbody></table></details>\n'
            source += '\n<!-- public-preview-metadata -->\n' + supplemental + structured + '\n<!-- /public-preview-metadata -->\n'
            write(guide, source)
            continue
        title = f"{entry['manufacturer']} {entry['model']} Modbus register preview"
        description = f"Sample register addresses and data types for {entry['manufacturer']} {entry['model']}. Public preview with JSON source and verification status."
        protocols = ", ".join(entry.get("supported_protocols", [])) or "Not specified in the public catalog; check the device manual."
        lines = ["---", f"title: {json.dumps(title)}", f"description: {json.dumps(description)}", "---", "",
                 f"# {cell(title)}", "", f"Public preview for **{cell(entry['manufacturer'])} {cell(entry['model'])}** ({cell(entry['device_type'])}).",
                 "This sample is not a complete map or evidence of hardware testing.", "", "## Preview details", "",
                 f"- Catalog ID: `{identifier}`", f"- Map version: {cell(entry.get('map_version', 'Not specified'))}",
                 f"- Verification: {cell(entry['verification_level'])}", f"- Protocols: {cell(protocols)}",
                 f"- Public preview: {len(payload['registers'])} registers. Complete in-app availability is not established by this preview.", "",
                 f"[JSON preview]({json_url}) · [Data terms]({TERMS})", "", "## Register table (sample)", "",
                 "| Signal | Display address | Data type | Units | Category |", "|---|---|---|---|---|"]
        lines += ["| " + " | ".join(cell(row[k]) for k in ("name", "display_address", "data_type", "unit", "category")) + " |" for row in payload["registers"]]
        lines += ["", "## Addressing and setup", "",
                  "Addresses and values above are copied from the public JSON preview. Confirm the exact model, firmware, register function, address base, word order, scaling and units against the manufacturer manual before polling. No manufacturer manual revision or hardware validation is established by this page.", "",
                  "## Use with Modbus Monitor XPF", "",
                  "Check the device-map catalog in your installed XPF version for current map availability and licensing. The software download link does not open this map.", "",
                  f"[Get Modbus Monitor XPF]({BASE}downloads-purchase/) · [Request a map or correction]({REQUEST}) · [Browse all previews]({HUB})"]
        lines += ['', structured]
        write(docs_root / routes[identifier] / "index.md", "\n".join(lines))
    def link(entry):
        return f"[{cell(entry['manufacturer'] + ' ' + entry['model'])}]({BASE + routes[entry['id']]})"
    lines = ["---", "title: Modbus Register Maps & Device Previews | Modbus Monitor",
             "description: Find Modbus register-map previews by manufacturer and model. View sample addresses and data types, JSON sources, and device guides for Modbus Monitor XPF.", "---", "",
             "# Modbus Device Maps", "", "Browse sample register addresses and data types by manufacturer and model.", "",
             f"**{len(entries)} public previews** and **{len(guides)} published device guides** are listed separately. These collections overlap; their counts must not be added. A preview does not confirm complete map availability, supported firmware, or hardware testing. Check the catalog in your installed XPF version for map availability and licensing.", "",
             "## Start Here {#start-here}", "",
             "[Browse previews](#all-device-maps){ .md-button .md-button--primary }",
             "[Get Modbus Monitor XPF](../downloads-purchase.md){ .md-button }",
             f"[Request a map]({REQUEST}){{ .md-button }}", "",
             "- [XPF user guide](../products/xpf/user-guide.md)",
             "- [Device maps guide](../blog/modbus-device-maps.md)",
             "- [Product information](https://www.modbusmonitor.com/) · [Documentation](../index.md) · [Quantum Bit Solutions](https://quantumbitsolutions.com/) · [GitHub projects](https://github.com/Modbus-Monitor)",
             f"- [Public JSON catalog]({DATA}catalog.json) · [Preview data terms]({TERMS})", "",
             "## Popular Device Maps {#popular-device-maps}", ""]
    lines += ["- " + link(e) for e in entries if e.get("featured")][:12]
    lines += ["", "## All Device Maps", "", '<div class="map-filters" hidden>',
              '<label for="mapSearch">Filter by manufacturer, model or device type</label>',
              '<input id="mapSearch" type="search" placeholder="e.g. Huawei Sun2000" />',
              '<label for="manufacturerFilter">Manufacturer</label>', '<select id="manufacturerFilter"><option value="">All manufacturers</option>']
    lines += [f'<option value="{html.escape(name, quote=True)}">{html.escape(name)}</option>' for name in sorted(manufacturers)]
    lines += ['</select>', '<p id="mapCount" role="status" aria-live="polite"></p>', '</div>', '<ul id="deviceMapList">']
    for e in sorted(entries, key=lambda e: (e['manufacturer'], e['model'])):
        name = html.escape(e['manufacturer'] + ' ' + e['model'])
        search = html.escape(e['manufacturer'] + ' ' + e['model'] + ' ' + e['device_type'], quote=True)
        lines.append(f'<li data-manufacturer="{html.escape(e["manufacturer"], quote=True)}" data-search="{search}"><a href="{BASE + routes[e["id"]]}">{name}</a> — {html.escape(e["device_type"])} · {e["preview_register_count"]} sample registers · <a href="{DATA + e["json_url"]}">JSON preview</a></li>')
    lines += ['</ul>', '', '## Categories {#categories}', '']
    for name, group in sorted(categories.items()):
        lines += [f"### {cell(name)}", "", ", ".join(link(e) for e in group), ""]
    lines += ['## Browse by Manufacturer {#browse-by-manufacturer}', '']
    for name, group in sorted(manufacturers.items()):
        lines += [f"- **{cell(name)}** ({len(group)} previews): " + ", ".join(link(e) for e in group)]
    lines += ['', '## Published Device Guides {#full-list}', '']
    for guide in guides:
        title = re.search(r'^# (.+)$', guide.read_text(encoding='utf-8'), re.M).group(1)
        lines.append(f"- [{title}]({BASE + guide.relative_to(docs_root).with_suffix('').as_posix()}/)")
    # Preserve old hub fragments without retaining duplicate browsing pages.
    lines += ['', '<span id="recently-added"></span><span id="why-these-pages-help"></span><span id="energy-meters"></span><span id="solar-inverters"></span><span id="other-devices"></span>',
              '', '## Use Device Maps in Modbus Monitor XPF', '',
              'Choose a preview above, check its model and addressing notes, then consult the [XPF user guide](../products/xpf/user-guide.md). Preview data is licensed separately from application features and complete maps.']
    write(docs_root / 'modbus-device-maps/index.md', '\n'.join(lines))
    manifest = {'schema_version': 1, 'hub': HUB, 'source_sha256': hashes,
                'public_preview_count': len(entries), 'published_guide_count': len(guides),
                'redirects': [{'source': DATA, 'target': HUB}] + [
                    {'source': DATA + e['preview_url'], 'target': BASE + routes[e['id']], 'id': e['id']}
                    for e in entries]}
    write(ROOT / 'tools/device-maps/consolidation-manifest.json', json.dumps(manifest, indent=2))
    return manifest


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--catalog-root', type=Path, required=True)
    args = parser.parse_args()
    result = build(args.catalog_root)
    print(f"Rendered {result['public_preview_count']} previews; {result['published_guide_count']} existing guides.")
