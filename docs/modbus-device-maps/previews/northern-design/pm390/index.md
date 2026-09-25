---
title: "Northern Design PM390 Modbus register preview"
description: "Sample register addresses and data types for Northern Design PM390. Public preview with JSON source and verification status."
---

# Northern Design PM390 Modbus register preview

Public preview for **Northern Design PM390** (Power Meter).
This sample is not a complete map or evidence of hardware testing.

## Preview details

- Catalog ID: `northern-design/pm390`
- Map version: 1.0
- Verification: not-reviewed
- Protocols: RTU, TCP
- Public preview: 12 registers. Complete in-app availability is not established by this preview.

[JSON preview](https://modbus-monitor.github.io/modbus-device-maps/maps/northern-design/pm390.json) · [Data terms](https://modbus-monitor.github.io/modbus-device-maps/data-license/)

## Register table (sample)

| Signal | Display address | Data type | Units | Category |
|---|---|---|---|---|
| Phase 1 amps Amps | 405388 | FLOAT32 | A | Current |
| kW 3-Ph kW | 405376 | FLOAT32 | - | Power |
| Frequency | 405384 | FLOAT32 | Hz | Frequency |
| PF 3-Ph | 405382 | FLOAT32 | - | Power Factor |
| Phase 1 volts Volts | 405386 | FLOAT32 | - | General |
| Export wh Wh | 405642 | UINT32 | kWh | Communication |
| kVA 3-Ph kVA | 405378 | FLOAT32 | - | Power |
| Kvar 3-Ph kvar | 405380 | FLOAT32 | - | Power |
| Phase 1 kW kW | 405390 | FLOAT32 | - | Power |
| Phase 2 amps Amps | 405394 | FLOAT32 | A | Current |
| Phase 2 kW kW | 405396 | FLOAT32 | - | Power |
| Phase 3 amps Amps | 405400 | FLOAT32 | A | Current |

## Addressing and setup

Addresses and values above are copied from the public JSON preview. Confirm the exact model, firmware, register function, address base, word order, scaling and units against the manufacturer manual before polling. No manufacturer manual revision or hardware validation is established by this page.

## Use with Modbus Monitor XPF

Check the device-map catalog in your installed XPF version for current map availability and licensing. The software download link does not open this map.

[Get Modbus Monitor XPF](https://docs.quantumbitsolutions.com/downloads-purchase/) · [Request a map or correction](https://github.com/Modbus-Monitor/modbus-device-maps/issues/new/choose) · [Browse all previews](https://docs.quantumbitsolutions.com/modbus-device-maps/)

<script type="application/ld+json">{"@context": "https://schema.org", "@type": "Dataset", "name": "Northern Design PM390 public register preview", "description": "Sample register addresses and data types; not a complete map or hardware verification.", "url": "https://docs.quantumbitsolutions.com/modbus-device-maps/previews/northern-design/pm390/", "license": "https://modbus-monitor.github.io/modbus-device-maps/data-license/", "creator": {"@type": "Organization", "name": "Quantum Bit Solutions", "url": "https://quantumbitsolutions.com/"}, "distribution": {"@type": "DataDownload", "encodingFormat": "application/json", "contentUrl": "https://modbus-monitor.github.io/modbus-device-maps/maps/northern-design/pm390.json"}}</script>
