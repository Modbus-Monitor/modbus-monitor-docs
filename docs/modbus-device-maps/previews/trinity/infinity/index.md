---
title: "Trinity Infinity Modbus register preview"
description: "Sample register addresses and data types for Trinity Infinity. Public preview with JSON source and verification status."
---

# Trinity Infinity Modbus register preview

Public preview for **Trinity Infinity** (Power Meter).
This sample is not a complete map or evidence of hardware testing.

## Preview details

- Catalog ID: `trinity/infinity`
- Map version: 1.0
- Verification: not-reviewed
- Protocols: RTU, TCP
- Public preview: 12 registers. Complete in-app availability is not established by this preview.

[JSON preview](https://modbus-monitor.github.io/modbus-device-maps/maps/trinity/infinity.json) · [Data terms](https://modbus-monitor.github.io/modbus-device-maps/data-license/)

## Register table (sample)

| Signal | Display address | Data type | Units | Category |
|---|---|---|---|---|
| Eb kvah | 403059 | UINT32 | - | Power |
| Eb kwh | 403029 | UINT32 | kWh | Energy |
| Eb time hours | 403033 | UINT32 | - | General |
| Dg kwh | 403031 | UINT32 | kWh | Energy |
| Dg kvah | 403061 | UINT32 | - | Power |
| Kwh | 403029 | UINT32 | kWh | Energy |
| Kvah | 403059 | UINT32 | - | Power |
| Eb time minutes | 403035 | UINT32 | - | General |
| Dg time hours | 403037 | UINT32 | - | General |
| Dg time minutes | 403039 | UINT32 | - | General |
| Eb time hour | 403063 | UINT32 | - | General |
| Eb time minute | 403065 | UINT32 | - | General |

## Addressing and setup

Addresses and values above are copied from the public JSON preview. Confirm the exact model, firmware, register function, address base, word order, scaling and units against the manufacturer manual before polling. No manufacturer manual revision or hardware validation is established by this page.

## Use with Modbus Monitor XPF

Check the device-map catalog in your installed XPF version for current map availability and licensing. The software download link does not open this map.

[Get Modbus Monitor XPF](https://docs.quantumbitsolutions.com/downloads-purchase/) · [Request a map or correction](https://github.com/Modbus-Monitor/modbus-device-maps/issues/new/choose) · [Browse all previews](https://docs.quantumbitsolutions.com/modbus-device-maps/)

<script type="application/ld+json">{"@context": "https://schema.org", "@type": "Dataset", "name": "Trinity Infinity public register preview", "description": "Sample register addresses and data types; not a complete map or hardware verification.", "url": "https://docs.quantumbitsolutions.com/modbus-device-maps/previews/trinity/infinity/", "license": "https://modbus-monitor.github.io/modbus-device-maps/data-license/", "creator": {"@type": "Organization", "name": "Quantum Bit Solutions", "url": "https://quantumbitsolutions.com/"}, "distribution": {"@type": "DataDownload", "encodingFormat": "application/json", "contentUrl": "https://modbus-monitor.github.io/modbus-device-maps/maps/trinity/infinity.json"}}</script>
