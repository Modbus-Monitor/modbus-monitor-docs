---
title: "Trinity Xpert Modbus register preview"
description: "Sample register addresses and data types for Trinity Xpert. Public preview with JSON source and verification status."
---

# Trinity Xpert Modbus register preview

Public preview for **Trinity Xpert** (Power Meter).
This sample is not a complete map or evidence of hardware testing.

## Preview details

- Catalog ID: `trinity/xpert`
- Map version: 1.0
- Verification: not-reviewed
- Protocols: RTU, TCP
- Public preview: 12 registers. Complete in-app availability is not established by this preview.

[JSON preview](https://modbus-monitor.github.io/modbus-device-maps/maps/trinity/xpert.json) · [Data terms](https://modbus-monitor.github.io/modbus-device-maps/data-license/)

## Register table (sample)

| Signal | Display address | Data type | Units | Category |
|---|---|---|---|---|
| System kw | 400239 | UINT32 | - | Power |
| Dg kwh | 400271 | UINT32 | kWh | Energy |
| Frequency | 400229 | UINT32 | Hz | Frequency |
| System pf | 400231 | UINT32 | - | Power Factor |
| Rising demand | 400267 | UINT32 | kW | Demand |
| Thd vr | 400299 | UINT32 | - | Harmonics |
| Vrn | 400199 | UINT32 | - | General |
| System kvar | 400241 | UINT32 | - | Power |
| System kva | 400243 | UINT32 | - | Power |
| Max demand | 400269 | UINT32 | kW | Demand |
| Dg kvarh | 400273 | UINT32 | kWh | Energy |
| Eb kwh | 400275 | UINT32 | kWh | Energy |

## Addressing and setup

Addresses and values above are copied from the public JSON preview. Confirm the exact model, firmware, register function, address base, word order, scaling and units against the manufacturer manual before polling. No manufacturer manual revision or hardware validation is established by this page.

## Use with Modbus Monitor XPF

Check the device-map catalog in your installed XPF version for current map availability and licensing. The software download link does not open this map.

[Get Modbus Monitor XPF](https://docs.quantumbitsolutions.com/downloads-purchase/) · [Request a map or correction](https://github.com/Modbus-Monitor/modbus-device-maps/issues/new/choose) · [Browse all previews](https://docs.quantumbitsolutions.com/modbus-device-maps/)

<script type="application/ld+json">{"@context": "https://schema.org", "@type": "Dataset", "name": "Trinity Xpert public register preview", "description": "Sample register addresses and data types; not a complete map or hardware verification.", "url": "https://docs.quantumbitsolutions.com/modbus-device-maps/previews/trinity/xpert/", "license": "https://modbus-monitor.github.io/modbus-device-maps/data-license/", "creator": {"@type": "Organization", "name": "Quantum Bit Solutions", "url": "https://quantumbitsolutions.com/"}, "distribution": {"@type": "DataDownload", "encodingFormat": "application/json", "contentUrl": "https://modbus-monitor.github.io/modbus-device-maps/maps/trinity/xpert.json"}}</script>
