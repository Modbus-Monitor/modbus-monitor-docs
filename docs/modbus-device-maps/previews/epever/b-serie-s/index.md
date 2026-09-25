---
title: "Epever B Serie s Modbus register preview"
description: "Sample register addresses and data types for Epever B Serie s. Public preview with JSON source and verification status."
---

# Epever B Serie s Modbus register preview

Public preview for **Epever B Serie s** (Power Meter).
This sample is not a complete map or evidence of hardware testing.

## Preview details

- Catalog ID: `epever/b-serie-s`
- Map version: 1.0
- Verification: not-reviewed
- Protocols: RTU, TCP
- Public preview: 12 registers. Complete in-app availability is not established by this preview.

[JSON preview](https://modbus-monitor.github.io/modbus-device-maps/maps/epever/b-serie-s.json) · [Data terms](https://modbus-monitor.github.io/modbus-device-maps/data-license/)

## Register table (sample)

| Signal | Display address | Data type | Units | Category |
|---|---|---|---|---|
| Array rated voltage V | 312288 | UINT16 | V | Voltage |
| Array rated current A | 312289 | UINT16 | - | Current |
| Array rated power W | 312290 | UINT32 | kW | Power |
| Consumed energy today | 313060 | UINT32 | kWh | Energy |
| Battery status | 312800 | UINT16 | - | Status |
| Battery temperature C | 312560 | UINT16 | degC | Temperature |
| Charging mode | 312296 | UINT16 | - | General |
| Battery rated voltage V | 312292 | UINT16 | V | Voltage |
| Battery rated current A | 312293 | UINT16 | - | Current |
| Battery rated power W | 312294 | UINT32 | kW | Power |
| Rated current of load W | 312302 | UINT16 | - | Current |
| Pv array input voltage V | 312544 | UINT16 | V | Voltage |

## Addressing and setup

Addresses and values above are copied from the public JSON preview. Confirm the exact model, firmware, register function, address base, word order, scaling and units against the manufacturer manual before polling. No manufacturer manual revision or hardware validation is established by this page.

## Use with Modbus Monitor XPF

Check the device-map catalog in your installed XPF version for current map availability and licensing. The software download link does not open this map.

[Get Modbus Monitor XPF](https://docs.quantumbitsolutions.com/downloads-purchase/) · [Request a map or correction](https://github.com/Modbus-Monitor/modbus-device-maps/issues/new/choose) · [Browse all previews](https://docs.quantumbitsolutions.com/modbus-device-maps/)

<script type="application/ld+json">{"@context": "https://schema.org", "@type": "Dataset", "name": "Epever B Serie s public register preview", "description": "Sample register addresses and data types; not a complete map or hardware verification.", "url": "https://docs.quantumbitsolutions.com/modbus-device-maps/previews/epever/b-serie-s/", "license": "https://modbus-monitor.github.io/modbus-device-maps/data-license/", "creator": {"@type": "Organization", "name": "Quantum Bit Solutions", "url": "https://quantumbitsolutions.com/"}, "distribution": {"@type": "DataDownload", "encodingFormat": "application/json", "contentUrl": "https://modbus-monitor.github.io/modbus-device-maps/maps/epever/b-serie-s.json"}}</script>
