---
title: "Herholdt Controls M1PRO,M3PRO Modbus register preview"
description: "Sample register addresses and data types for Herholdt Controls M1PRO,M3PRO. Public preview with JSON source and verification status."
---

# Herholdt Controls M1PRO,M3PRO Modbus register preview

Public preview for **Herholdt Controls M1PRO,M3PRO** (Power Meter).
This sample is not a complete map or evidence of hardware testing.

## Preview details

- Catalog ID: `herholdt-controls/m1pro-m3pro`
- Map version: 1.0
- Verification: not-reviewed
- Protocols: RTU, TCP
- Public preview: 12 registers. Complete in-app availability is not established by this preview.

[JSON preview](https://modbus-monitor.github.io/modbus-device-maps/maps/herholdt-controls/m1pro-m3pro.json) · [Data terms](https://modbus-monitor.github.io/modbus-device-maps/data-license/)

## Register table (sample)

| Signal | Display address | Data type | Units | Category |
|---|---|---|---|---|
| Phase voltage L1-N V | 404267 | UINT32 | V | Voltage |
| Current L1 A | 404279 | UINT32 | A | Current |
| Active power L1 kW | 404151 | UINT32 | kW | Power |
| Active energy L1 T1 imported kWh | 404119 | INT64 | kWh | Energy |
| Frequency Hz | 404303 | UINT32 | Hz | Frequency |
| Range overflow alarm | 404101 | UINT16 | - | Status |
| Running tariff | 404102 | UINT16 | - | General |
| Active energy L2 T1 imported kWh | 404123 | INT64 | kWh | Energy |
| Active energy L3 T1 imported kWh | 404127 | INT64 | kWh | Energy |
| Active energy sum T1 imported kWh | 404131 | INT64 | kWh | Energy |
| Active energy L1 T2 imported kWh | 404135 | INT64 | kWh | Energy |
| Active energy L2 T2 imported kWh | 404139 | INT64 | kWh | Energy |

## Addressing and setup

Addresses and values above are copied from the public JSON preview. Confirm the exact model, firmware, register function, address base, word order, scaling and units against the manufacturer manual before polling. No manufacturer manual revision or hardware validation is established by this page.

## Use with Modbus Monitor XPF

Check the device-map catalog in your installed XPF version for current map availability and licensing. The software download link does not open this map.

[Get Modbus Monitor XPF](https://docs.quantumbitsolutions.com/downloads-purchase/) · [Request a map or correction](https://github.com/Modbus-Monitor/modbus-device-maps/issues/new/choose) · [Browse all previews](https://docs.quantumbitsolutions.com/modbus-device-maps/)

<script type="application/ld+json">{"@context": "https://schema.org", "@type": "Dataset", "name": "Herholdt Controls M1PRO,M3PRO public register preview", "description": "Sample register addresses and data types; not a complete map or hardware verification.", "url": "https://docs.quantumbitsolutions.com/modbus-device-maps/previews/herholdt-controls/m1pro-m3pro/", "license": "https://modbus-monitor.github.io/modbus-device-maps/data-license/", "creator": {"@type": "Organization", "name": "Quantum Bit Solutions", "url": "https://quantumbitsolutions.com/"}, "distribution": {"@type": "DataDownload", "encodingFormat": "application/json", "contentUrl": "https://modbus-monitor.github.io/modbus-device-maps/maps/herholdt-controls/m1pro-m3pro.json"}}</script>
