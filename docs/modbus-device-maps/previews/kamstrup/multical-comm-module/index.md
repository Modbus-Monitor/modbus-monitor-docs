---
title: "Kamstrup Multical Comm Module Modbus register preview"
description: "Sample register addresses and data types for Kamstrup Multical Comm Module. Public preview with JSON source and verification status."
---

# Kamstrup Multical Comm Module Modbus register preview

Public preview for **Kamstrup Multical Comm Module** (Power Meter).
This sample is not a complete map or evidence of hardware testing.

## Preview details

- Catalog ID: `kamstrup/multical-comm-module`
- Map version: 1.0
- Verification: not-reviewed
- Protocols: RTU, TCP
- Public preview: 12 registers. Complete in-app availability is not established by this preview.

[JSON preview](https://modbus-monitor.github.io/modbus-device-maps/maps/kamstrup/multical-comm-module.json) · [Data terms](https://modbus-monitor.github.io/modbus-device-maps/data-license/)

## Register table (sample)

| Signal | Display address | Data type | Units | Category |
|---|---|---|---|---|
| Actual power | 400012 | FLOAT32 | kW | Power |
| Heat energy E1 | 400000 | FLOAT32 | kWh | Energy |
| Inlet temperature T1 | 400016 | FLOAT32 | degC | Temperature |
| Actual flow | 400004 | FLOAT32 | - | General |
| Version | 400084 | UINT16 | - | Identification |
| Outlet temperature T2 | 400020 | FLOAT32 | degC | Temperature |
| Heat energy E1 | 400032 | UINT32 | kWh | Energy |
| Cooling energy E3 | 400092 | FLOAT32 | kWh | Energy |
| Temperature T3 | 400100 | FLOAT32 | degC | Temperature |
| Max power | 400124 | FLOAT32 | kW | Power |
| Volume V1 | 400008 | FLOAT32 | - | General |
| Pulse input A | 400024 | FLOAT32 | - | General |

## Addressing and setup

Addresses and values above are copied from the public JSON preview. Confirm the exact model, firmware, register function, address base, word order, scaling and units against the manufacturer manual before polling. No manufacturer manual revision or hardware validation is established by this page.

## Use with Modbus Monitor XPF

Check the device-map catalog in your installed XPF version for current map availability and licensing. The software download link does not open this map.

[Get Modbus Monitor XPF](https://docs.quantumbitsolutions.com/downloads-purchase/) · [Request a map or correction](https://github.com/Modbus-Monitor/modbus-device-maps/issues/new/choose) · [Browse all previews](https://docs.quantumbitsolutions.com/modbus-device-maps/)

<script type="application/ld+json">{"@context": "https://schema.org", "@type": "Dataset", "name": "Kamstrup Multical Comm Module public register preview", "description": "Sample register addresses and data types; not a complete map or hardware verification.", "url": "https://docs.quantumbitsolutions.com/modbus-device-maps/previews/kamstrup/multical-comm-module/", "license": "https://modbus-monitor.github.io/modbus-device-maps/data-license/", "creator": {"@type": "Organization", "name": "Quantum Bit Solutions", "url": "https://quantumbitsolutions.com/"}, "distribution": {"@type": "DataDownload", "encodingFormat": "application/json", "contentUrl": "https://modbus-monitor.github.io/modbus-device-maps/maps/kamstrup/multical-comm-module.json"}}</script>
