---
title: "Forlong DRT 301M Modbus register preview"
description: "Sample register addresses and data types for Forlong DRT 301M. Public preview with JSON source and verification status."
---

# Forlong DRT 301M Modbus register preview

Public preview for **Forlong DRT 301M** (Power Meter).
This sample is not a complete map or evidence of hardware testing.

## Preview details

- Catalog ID: `forlong/drt-301m`
- Map version: 1.0
- Verification: not-reviewed
- Protocols: RTU, TCP
- Public preview: 12 registers. Complete in-app availability is not established by this preview.

[JSON preview](https://modbus-monitor.github.io/modbus-device-maps/maps/forlong/drt-301m.json) · [Data terms](https://modbus-monitor.github.io/modbus-device-maps/data-license/)

## Register table (sample)

| Signal | Display address | Data type | Units | Category |
|---|---|---|---|---|
| Voltage L1 V | 400016 | UINT32 | V | Voltage |
| Current L1 A | 400080 | UINT32 | A | Current |
| Power L1 kW | 400144 | UINT32 | kW | Power |
| Import energy KW | 400352 | UINT32 | kWh | Energy |
| Frequency Hz | 400078 | UINT32 | Hz | Frequency |
| Time | 461440 | INT16 | - | General |
| Voltage L2 V | 400018 | UINT32 | V | Voltage |
| Voltage L3 V | 400020 | UINT32 | V | Voltage |
| Current L2 A | 400082 | UINT32 | A | Current |
| Current L3 A | 400084 | UINT32 | A | Current |
| Current neutral A | 400086 | UINT32 | - | Current |
| Power L2 kW | 400146 | UINT32 | kW | Power |

## Addressing and setup

Addresses and values above are copied from the public JSON preview. Confirm the exact model, firmware, register function, address base, word order, scaling and units against the manufacturer manual before polling. No manufacturer manual revision or hardware validation is established by this page.

## Use with Modbus Monitor XPF

Check the device-map catalog in your installed XPF version for current map availability and licensing. The software download link does not open this map.

[Get Modbus Monitor XPF](https://docs.quantumbitsolutions.com/downloads-purchase/) · [Request a map or correction](https://github.com/Modbus-Monitor/modbus-device-maps/issues/new/choose) · [Browse all previews](https://docs.quantumbitsolutions.com/modbus-device-maps/)

<script type="application/ld+json">{"@context": "https://schema.org", "@type": "Dataset", "name": "Forlong DRT 301M public register preview", "description": "Sample register addresses and data types; not a complete map or hardware verification.", "url": "https://docs.quantumbitsolutions.com/modbus-device-maps/previews/forlong/drt-301m/", "license": "https://modbus-monitor.github.io/modbus-device-maps/data-license/", "creator": {"@type": "Organization", "name": "Quantum Bit Solutions", "url": "https://quantumbitsolutions.com/"}, "distribution": {"@type": "DataDownload", "encodingFormat": "application/json", "contentUrl": "https://modbus-monitor.github.io/modbus-device-maps/maps/forlong/drt-301m.json"}}</script>
