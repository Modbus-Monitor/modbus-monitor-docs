---
title: "ENTES MPR2 Series Modbus register preview"
description: "Sample register addresses and data types for ENTES MPR2 Series. Public preview with JSON source and verification status."
---

# ENTES MPR2 Series Modbus register preview

Public preview for **ENTES MPR2 Series** (Power Meter).
This sample is not a complete map or evidence of hardware testing.

## Preview details

- Catalog ID: `entes/mpr2-series`
- Map version: 1.0
- Verification: not-reviewed
- Protocols: RTU, TCP
- Public preview: 12 registers. Complete in-app availability is not established by this preview.

[JSON preview](https://modbus-monitor.github.io/modbus-device-maps/maps/entes/mpr2-series.json) · [Data terms](https://modbus-monitor.github.io/modbus-device-maps/data-license/)

## Register table (sample)

| Signal | Display address | Data type | Units | Category |
|---|---|---|---|---|
| Voltage L1 N V10 | 400000 | UINT32 | V | Voltage |
| Current L1 mA | 400014 | UINT32 | A | Current |
| Active power L1 N W | 400026 | FLOAT32 | kW | Power |
| Consumed active energy L1 Wh | 400200 | INT64 | kWh | Energy |
| Measured frequency Hz 100 | 400024 | UINT32 | Hz | Frequency |
| Quadrant 1 total reactive powe demand Var10 | 401208 | FLOAT32 | kW | Demand |
| Input status | 400158 | UINT32 | - | Status |
| Temperature input 1 C | 400138 | FLOAT32 | degC | Temperature |
| Total harmonic distorsion VL1 | 402006 | UINT32 | - | Harmonics |
| Cosphi L1 | 400082 | INT32 | - | General |
| Voltage L2 N V10 | 400002 | UINT32 | V | Voltage |
| Voltage L3 N V10 | 400004 | UINT32 | V | Voltage |

## Addressing and setup

Addresses and values above are copied from the public JSON preview. Confirm the exact model, firmware, register function, address base, word order, scaling and units against the manufacturer manual before polling. No manufacturer manual revision or hardware validation is established by this page.

## Use with Modbus Monitor XPF

Check the device-map catalog in your installed XPF version for current map availability and licensing. The software download link does not open this map.

[Get Modbus Monitor XPF](https://docs.quantumbitsolutions.com/downloads-purchase/) · [Request a map or correction](https://github.com/Modbus-Monitor/modbus-device-maps/issues/new/choose) · [Browse all previews](https://docs.quantumbitsolutions.com/modbus-device-maps/)

<script type="application/ld+json">{"@context": "https://schema.org", "@type": "Dataset", "name": "ENTES MPR2 Series public register preview", "description": "Sample register addresses and data types; not a complete map or hardware verification.", "url": "https://docs.quantumbitsolutions.com/modbus-device-maps/previews/entes/mpr2-series/", "license": "https://modbus-monitor.github.io/modbus-device-maps/data-license/", "creator": {"@type": "Organization", "name": "Quantum Bit Solutions", "url": "https://quantumbitsolutions.com/"}, "distribution": {"@type": "DataDownload", "encodingFormat": "application/json", "contentUrl": "https://modbus-monitor.github.io/modbus-device-maps/maps/entes/mpr2-series.json"}}</script>
