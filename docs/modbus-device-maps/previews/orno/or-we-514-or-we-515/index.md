---
title: "Orno OR-WE-514,OR-WE-515 Modbus register preview"
description: "Sample register addresses and data types for Orno OR-WE-514,OR-WE-515. Public preview with JSON source and verification status."
---

# Orno OR-WE-514,OR-WE-515 Modbus register preview

Public preview for **Orno OR-WE-514,OR-WE-515** (Power Meter).
This sample is not a complete map or evidence of hardware testing.

## Preview details

- Catalog ID: `orno/or-we-514-or-we-515`
- Map version: 1.0
- Verification: not-reviewed
- Protocols: RTU, TCP
- Public preview: 12 registers. Complete in-app availability is not established by this preview.

[JSON preview](https://modbus-monitor.github.io/modbus-device-maps/maps/orno/or-we-514-or-we-515.json) · [Data terms](https://modbus-monitor.github.io/modbus-device-maps/data-license/)

## Register table (sample)

| Signal | Display address | Data type | Units | Category |
|---|---|---|---|---|
| Phase voltage V1 V | 400305 | UINT16 | V | Voltage |
| Phase current I1 A | 400314 | UINT16 | - | Current |
| Split phase active powerp1 kW | 400321 | INT32 | kW | Power |
| Last month demand | 441008 | UINT32 | kW | Demand |
| Phase voltage V2 V | 400306 | UINT16 | V | Voltage |
| Phase voltage V3 V | 400307 | UINT16 | V | Voltage |
| Phase current I2 A | 400316 | UINT16 | - | Current |
| Phase current I3 A | 400318 | UINT16 | - | Current |
| Split phase active powerp2 kW | 400323 | INT32 | kW | Power |
| Split phase active powerp3 kW | 400325 | INT32 | kW | Power |
| System active power psum kW | 400327 | INT32 | kW | Power |
| Split phase reactive power Q1 kvar | 400329 | INT32 | kW | Power |

## Addressing and setup

Addresses and values above are copied from the public JSON preview. Confirm the exact model, firmware, register function, address base, word order, scaling and units against the manufacturer manual before polling. No manufacturer manual revision or hardware validation is established by this page.

## Use with Modbus Monitor XPF

Check the device-map catalog in your installed XPF version for current map availability and licensing. The software download link does not open this map.

[Get Modbus Monitor XPF](https://docs.quantumbitsolutions.com/downloads-purchase/) · [Request a map or correction](https://github.com/Modbus-Monitor/modbus-device-maps/issues/new/choose) · [Browse all previews](https://docs.quantumbitsolutions.com/modbus-device-maps/)

<script type="application/ld+json">{"@context": "https://schema.org", "@type": "Dataset", "name": "Orno OR-WE-514,OR-WE-515 public register preview", "description": "Sample register addresses and data types; not a complete map or hardware verification.", "url": "https://docs.quantumbitsolutions.com/modbus-device-maps/previews/orno/or-we-514-or-we-515/", "license": "https://modbus-monitor.github.io/modbus-device-maps/data-license/", "creator": {"@type": "Organization", "name": "Quantum Bit Solutions", "url": "https://quantumbitsolutions.com/"}, "distribution": {"@type": "DataDownload", "encodingFormat": "application/json", "contentUrl": "https://modbus-monitor.github.io/modbus-device-maps/maps/orno/or-we-514-or-we-515.json"}}</script>
