---
title: "ENTES EPM-07 Modbus register preview"
description: "Sample register addresses and data types for ENTES EPM-07. Public preview with JSON source and verification status."
---

# ENTES EPM-07 Modbus register preview

Public preview for **ENTES EPM-07** (Power Meter).
This sample is not a complete map or evidence of hardware testing.

## Preview details

- Catalog ID: `entes/epm-07`
- Map version: 1.0
- Verification: not-reviewed
- Protocols: RTU, TCP
- Public preview: 12 registers. Complete in-app availability is not established by this preview.

[JSON preview](https://modbus-monitor.github.io/modbus-device-maps/maps/entes/epm-07.json) · [Data terms](https://modbus-monitor.github.io/modbus-device-maps/data-license/)

## Register table (sample)

| Signal | Display address | Data type | Units | Category |
|---|---|---|---|---|
| L1 phase max Voltage Volt | 400164 | UINT16 | V | Voltage |
| L1 phase max Current Amper | 400176 | UINT16 | - | Current |
| L3 phase min Apparent power VA | 400152 | UINT16 | kW | Power |
| Energy counter 1 selection | 432775 | INT16 | kWh | Energy |
| Demand time minute | 432771 | INT16 | kW | Demand |
| Calculation method | 432770 | INT16 | - | General |
| Communication address | 432777 | INT16 | - | Communication |
| Total min Import active power Watt | 400154 | INT32 | kW | Power |
| Total min Export active power Watt | 400156 | INT32 | kW | Power |
| Total min Import reactive power Var | 400158 | INT32 | kW | Power |
| Total min Export reactive power Var | 400160 | INT32 | kW | Power |
| Total min Apparent power VA | 400162 | UINT16 | kW | Power |

## Addressing and setup

Addresses and values above are copied from the public JSON preview. Confirm the exact model, firmware, register function, address base, word order, scaling and units against the manufacturer manual before polling. No manufacturer manual revision or hardware validation is established by this page.

## Use with Modbus Monitor XPF

Check the device-map catalog in your installed XPF version for current map availability and licensing. The software download link does not open this map.

[Get Modbus Monitor XPF](https://docs.quantumbitsolutions.com/downloads-purchase/) · [Request a map or correction](https://github.com/Modbus-Monitor/modbus-device-maps/issues/new/choose) · [Browse all previews](https://docs.quantumbitsolutions.com/modbus-device-maps/)

<script type="application/ld+json">{"@context": "https://schema.org", "@type": "Dataset", "name": "ENTES EPM-07 public register preview", "description": "Sample register addresses and data types; not a complete map or hardware verification.", "url": "https://docs.quantumbitsolutions.com/modbus-device-maps/previews/entes/epm-07/", "license": "https://modbus-monitor.github.io/modbus-device-maps/data-license/", "creator": {"@type": "Organization", "name": "Quantum Bit Solutions", "url": "https://quantumbitsolutions.com/"}, "distribution": {"@type": "DataDownload", "encodingFormat": "application/json", "contentUrl": "https://modbus-monitor.github.io/modbus-device-maps/maps/entes/epm-07.json"}}</script>
