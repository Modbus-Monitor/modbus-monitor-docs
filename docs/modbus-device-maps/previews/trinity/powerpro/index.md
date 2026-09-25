---
title: "Trinity PowerPro Modbus register preview"
description: "Sample register addresses and data types for Trinity PowerPro. Public preview with JSON source and verification status."
---

# Trinity PowerPro Modbus register preview

Public preview for **Trinity PowerPro** (Power Meter).
This sample is not a complete map or evidence of hardware testing.

## Preview details

- Catalog ID: `trinity/powerpro`
- Map version: 1.0
- Verification: not-reviewed
- Protocols: RTU, TCP
- Public preview: 12 registers. Complete in-app availability is not established by this preview.

[JSON preview](https://modbus-monitor.github.io/modbus-device-maps/maps/trinity/powerpro.json) · [Data terms](https://modbus-monitor.github.io/modbus-device-maps/data-license/)

## Register table (sample)

| Signal | Display address | Data type | Units | Category |
|---|---|---|---|---|
| Avgamps | 400211 | UINT32 | A | Current |
| Kva | 400199 | UINT32 | - | Power |
| Kwh | 400213 | UINT32 | kWh | Energy |
| Pf | 400205 | UINT32 | - | Power Factor |
| Demand | 400239 | UINT32 | kW | Demand |
| Vrthd | 400249 | UINT32 | - | Harmonics |
| Avgvll | 400207 | UINT32 | - | General |
| Kw | 400201 | UINT32 | - | Power |
| Kvar | 400203 | UINT32 | - | Power |
| Kvah | 400215 | UINT32 | - | Power |
| Kvarh | 400217 | UINT32 | kWh | Energy |
| Maxdemand | 400241 | UINT32 | kW | Demand |

## Addressing and setup

Addresses and values above are copied from the public JSON preview. Confirm the exact model, firmware, register function, address base, word order, scaling and units against the manufacturer manual before polling. No manufacturer manual revision or hardware validation is established by this page.

## Use with Modbus Monitor XPF

Check the device-map catalog in your installed XPF version for current map availability and licensing. The software download link does not open this map.

[Get Modbus Monitor XPF](https://docs.quantumbitsolutions.com/downloads-purchase/) · [Request a map or correction](https://github.com/Modbus-Monitor/modbus-device-maps/issues/new/choose) · [Browse all previews](https://docs.quantumbitsolutions.com/modbus-device-maps/)

<script type="application/ld+json">{"@context": "https://schema.org", "@type": "Dataset", "name": "Trinity PowerPro public register preview", "description": "Sample register addresses and data types; not a complete map or hardware verification.", "url": "https://docs.quantumbitsolutions.com/modbus-device-maps/previews/trinity/powerpro/", "license": "https://modbus-monitor.github.io/modbus-device-maps/data-license/", "creator": {"@type": "Organization", "name": "Quantum Bit Solutions", "url": "https://quantumbitsolutions.com/"}, "distribution": {"@type": "DataDownload", "encodingFormat": "application/json", "contentUrl": "https://modbus-monitor.github.io/modbus-device-maps/maps/trinity/powerpro.json"}}</script>
