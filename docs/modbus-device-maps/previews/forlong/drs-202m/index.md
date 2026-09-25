---
title: "Forlong DRS 202M Modbus register preview"
description: "Sample register addresses and data types for Forlong DRS 202M. Public preview with JSON source and verification status."
---

# Forlong DRS 202M Modbus register preview

Public preview for **Forlong DRS 202M** (Power Meter).
This sample is not a complete map or evidence of hardware testing.

## Preview details

- Catalog ID: `forlong/drs-202m`
- Map version: 1.0
- Verification: not-reviewed
- Protocols: RTU, TCP
- Public preview: 12 registers. Complete in-app availability is not established by this preview.

[JSON preview](https://modbus-monitor.github.io/modbus-device-maps/maps/forlong/drs-202m.json) · [Data terms](https://modbus-monitor.github.io/modbus-device-maps/data-license/)

## Register table (sample)

| Signal | Display address | Data type | Units | Category |
|---|---|---|---|---|
| Voltage L1 V | 300016 | FLOAT32 | V | Voltage |
| Current L1 A | 300080 | FLOAT32 | A | Current |
| Import activeenergy KW | 300352 | FLOAT32 | kWh | Energy |
| Frequency Hz | 300078 | FLOAT32 | Hz | Frequency |
| Modbus slavea ddress number a | 301316 | UINT16 | - | Communication |
| Date and time | 364512 | INT16 | - | General |
| Current L2 A | 300082 | FLOAT32 | A | Current |
| Current total A | 300088 | FLOAT32 | - | Current |
| Channel1energy rate1 KW | 302026 | FLOAT32 | kWh | Energy |
| Channel2 energy rate2 KW | 302028 | FLOAT32 | kWh | Energy |
| Channel2energy rate1 KW | 302034 | FLOAT32 | kWh | Energy |
| Channel2energy rate2 KW | 302036 | FLOAT32 | kWh | Energy |

## Addressing and setup

Addresses and values above are copied from the public JSON preview. Confirm the exact model, firmware, register function, address base, word order, scaling and units against the manufacturer manual before polling. No manufacturer manual revision or hardware validation is established by this page.

## Use with Modbus Monitor XPF

Check the device-map catalog in your installed XPF version for current map availability and licensing. The software download link does not open this map.

[Get Modbus Monitor XPF](https://docs.quantumbitsolutions.com/downloads-purchase/) · [Request a map or correction](https://github.com/Modbus-Monitor/modbus-device-maps/issues/new/choose) · [Browse all previews](https://docs.quantumbitsolutions.com/modbus-device-maps/)

<script type="application/ld+json">{"@context": "https://schema.org", "@type": "Dataset", "name": "Forlong DRS 202M public register preview", "description": "Sample register addresses and data types; not a complete map or hardware verification.", "url": "https://docs.quantumbitsolutions.com/modbus-device-maps/previews/forlong/drs-202m/", "license": "https://modbus-monitor.github.io/modbus-device-maps/data-license/", "creator": {"@type": "Organization", "name": "Quantum Bit Solutions", "url": "https://quantumbitsolutions.com/"}, "distribution": {"@type": "DataDownload", "encodingFormat": "application/json", "contentUrl": "https://modbus-monitor.github.io/modbus-device-maps/maps/forlong/drs-202m.json"}}</script>
