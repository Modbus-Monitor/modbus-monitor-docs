---
title: "Odenberg HALO Sorter Modbus register preview"
description: "Sample register addresses and data types for Odenberg HALO Sorter. Public preview with JSON source and verification status."
---

# Odenberg HALO Sorter Modbus register preview

Public preview for **Odenberg HALO Sorter** (Power Meter).
This sample is not a complete map or evidence of hardware testing.

## Preview details

- Catalog ID: `odenberg/halo-sorter`
- Map version: 1.0
- Verification: not-reviewed
- Protocols: RTU, TCP
- Public preview: 12 registers. Complete in-app availability is not established by this preview.

[JSON preview](https://modbus-monitor.github.io/modbus-device-maps/maps/odenberg/halo-sorter.json) · [Data terms](https://modbus-monitor.github.io/modbus-device-maps/data-license/)

## Register table (sample)

| Signal | Display address | Data type | Units | Category |
|---|---|---|---|---|
| Current Program ID | 400002 | UINT16 | - | Current |
| System Alarms Enabled | 400000 | UINT16 | - | Status |
| Selected Program ID | 400003 | UINT16 | - | General |
| System Alarms Flags | 400001 | UINT16 | - | Status |
| Current Application Number | 400020 | UINT16 | - | Current |
| Current User ID | 400025 | UINT16 | - | Current |
| Accept Count | 400004 | UINT32 | - | General |
| Reject A Count | 400006 | UINT32 | - | General |
| Reject B Count | 400008 | UINT32 | - | General |
| FM Count | 400010 | UINT32 | - | General |
| Undersized Count | 400014 | UINT32 | - | General |
| Oversized Count | 400018 | UINT32 | - | General |

## Addressing and setup

Addresses and values above are copied from the public JSON preview. Confirm the exact model, firmware, register function, address base, word order, scaling and units against the manufacturer manual before polling. No manufacturer manual revision or hardware validation is established by this page.

## Use with Modbus Monitor XPF

Check the device-map catalog in your installed XPF version for current map availability and licensing. The software download link does not open this map.

[Get Modbus Monitor XPF](https://docs.quantumbitsolutions.com/downloads-purchase/) · [Request a map or correction](https://github.com/Modbus-Monitor/modbus-device-maps/issues/new/choose) · [Browse all previews](https://docs.quantumbitsolutions.com/modbus-device-maps/)

<script type="application/ld+json">{"@context": "https://schema.org", "@type": "Dataset", "name": "Odenberg HALO Sorter public register preview", "description": "Sample register addresses and data types; not a complete map or hardware verification.", "url": "https://docs.quantumbitsolutions.com/modbus-device-maps/previews/odenberg/halo-sorter/", "license": "https://modbus-monitor.github.io/modbus-device-maps/data-license/", "creator": {"@type": "Organization", "name": "Quantum Bit Solutions", "url": "https://quantumbitsolutions.com/"}, "distribution": {"@type": "DataDownload", "encodingFormat": "application/json", "contentUrl": "https://modbus-monitor.github.io/modbus-device-maps/maps/odenberg/halo-sorter.json"}}</script>
