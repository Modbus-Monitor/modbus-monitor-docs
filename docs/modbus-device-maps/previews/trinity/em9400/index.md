---
title: "Trinity EM9400 Modbus register preview"
description: "Sample register addresses and data types for Trinity EM9400. Public preview with JSON source and verification status."
---

# Trinity EM9400 Modbus register preview

Public preview for **Trinity EM9400** (Power Meter).
This sample is not a complete map or evidence of hardware testing.

## Preview details

- Catalog ID: `trinity/em9400`
- Map version: 1.0
- Verification: not-reviewed
- Protocols: RTU, TCP
- Public preview: 12 registers. Complete in-app availability is not established by this preview.

[JSON preview](https://modbus-monitor.github.io/modbus-device-maps/maps/trinity/em9400.json) · [Data terms](https://modbus-monitor.github.io/modbus-device-maps/data-license/)

## Register table (sample)

| Signal | Display address | Data type | Units | Category |
|---|---|---|---|---|
| Voltage R Y angle | 400269 | UINT32 | V | Voltage |
| Current R Y angle | 400273 | UINT32 | - | Current |
| Kw R | 400233 | UINT32 | - | Power |
| Kwh | 400259 | UINT32 | kWh | Energy |
| Pf R | 400225 | UINT32 | - | Power Factor |
| Vr thd | 400297 | UINT32 | - | Harmonics |
| Vrn | 400199 | UINT32 | - | General |
| Pf Y | 400227 | UINT32 | - | Power Factor |
| Pf B | 400229 | UINT32 | - | Power Factor |
| Sys pf | 400231 | UINT32 | - | Power Factor |
| Kw Y | 400235 | UINT32 | - | Power |
| Kw B | 400237 | UINT32 | - | Power |

## Addressing and setup

Addresses and values above are copied from the public JSON preview. Confirm the exact model, firmware, register function, address base, word order, scaling and units against the manufacturer manual before polling. No manufacturer manual revision or hardware validation is established by this page.

## Use with Modbus Monitor XPF

Check the device-map catalog in your installed XPF version for current map availability and licensing. The software download link does not open this map.

[Get Modbus Monitor XPF](https://docs.quantumbitsolutions.com/downloads-purchase/) · [Request a map or correction](https://github.com/Modbus-Monitor/modbus-device-maps/issues/new/choose) · [Browse all previews](https://docs.quantumbitsolutions.com/modbus-device-maps/)

<script type="application/ld+json">{"@context": "https://schema.org", "@type": "Dataset", "name": "Trinity EM9400 public register preview", "description": "Sample register addresses and data types; not a complete map or hardware verification.", "url": "https://docs.quantumbitsolutions.com/modbus-device-maps/previews/trinity/em9400/", "license": "https://modbus-monitor.github.io/modbus-device-maps/data-license/", "creator": {"@type": "Organization", "name": "Quantum Bit Solutions", "url": "https://quantumbitsolutions.com/"}, "distribution": {"@type": "DataDownload", "encodingFormat": "application/json", "contentUrl": "https://modbus-monitor.github.io/modbus-device-maps/maps/trinity/em9400.json"}}</script>
