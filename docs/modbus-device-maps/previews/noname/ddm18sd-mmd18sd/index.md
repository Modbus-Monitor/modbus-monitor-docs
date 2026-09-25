---
title: "Noname DDM18SD,MMD18SD Modbus register preview"
description: "Sample register addresses and data types for Noname DDM18SD,MMD18SD. Public preview with JSON source and verification status."
---

# Noname DDM18SD,MMD18SD Modbus register preview

Public preview for **Noname DDM18SD,MMD18SD** (Power Meter).
This sample is not a complete map or evidence of hardware testing.

## Preview details

- Catalog ID: `noname/ddm18sd-mmd18sd`
- Map version: 1.0
- Verification: not-reviewed
- Protocols: RTU, TCP
- Public preview: 8 registers. Complete in-app availability is not established by this preview.

[JSON preview](https://modbus-monitor.github.io/modbus-device-maps/maps/noname/ddm18sd-mmd18sd.json) · [Data terms](https://modbus-monitor.github.io/modbus-device-maps/data-license/)

## Register table (sample)

| Signal | Display address | Data type | Units | Category |
|---|---|---|---|---|
| Voltage V | 400000 | FLOAT32 | V | Voltage |
| Current A | 400008 | FLOAT32 | - | Current |
| Active power KW | 400018 | FLOAT32 | kW | Power |
| Total active power kWh | 400256 | FLOAT32 | kWh | Energy |
| Frequency Hz | 400054 | FLOAT32 | Hz | Frequency |
| Reactive power VAr | 400026 | FLOAT32 | kW | Power |
| Power factor | 400042 | FLOAT32 | PF | Power |
| Total reactive power kVarh | 401024 | FLOAT32 | kWh | Energy |

## Addressing and setup

Addresses and values above are copied from the public JSON preview. Confirm the exact model, firmware, register function, address base, word order, scaling and units against the manufacturer manual before polling. No manufacturer manual revision or hardware validation is established by this page.

## Use with Modbus Monitor XPF

Check the device-map catalog in your installed XPF version for current map availability and licensing. The software download link does not open this map.

[Get Modbus Monitor XPF](https://docs.quantumbitsolutions.com/downloads-purchase/) · [Request a map or correction](https://github.com/Modbus-Monitor/modbus-device-maps/issues/new/choose) · [Browse all previews](https://docs.quantumbitsolutions.com/modbus-device-maps/)

<script type="application/ld+json">{"@context": "https://schema.org", "@type": "Dataset", "name": "Noname DDM18SD,MMD18SD public register preview", "description": "Sample register addresses and data types; not a complete map or hardware verification.", "url": "https://docs.quantumbitsolutions.com/modbus-device-maps/previews/noname/ddm18sd-mmd18sd/", "license": "https://modbus-monitor.github.io/modbus-device-maps/data-license/", "creator": {"@type": "Organization", "name": "Quantum Bit Solutions", "url": "https://quantumbitsolutions.com/"}, "distribution": {"@type": "DataDownload", "encodingFormat": "application/json", "contentUrl": "https://modbus-monitor.github.io/modbus-device-maps/maps/noname/ddm18sd-mmd18sd.json"}}</script>
