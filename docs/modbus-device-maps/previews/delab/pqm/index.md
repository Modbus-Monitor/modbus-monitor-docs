---
title: "Delab PQM Modbus register preview"
description: "Sample register addresses and data types for Delab PQM. Public preview with JSON source and verification status."
---

# Delab PQM Modbus register preview

Public preview for **Delab PQM** (Power Meter).
This sample is not a complete map or evidence of hardware testing.

## Preview details

- Catalog ID: `delab/pqm`
- Map version: 1.0
- Verification: not-reviewed
- Protocols: RTU, TCP
- Public preview: 12 registers. Complete in-app availability is not established by this preview.

[JSON preview](https://modbus-monitor.github.io/modbus-device-maps/maps/delab/pqm.json) · [Data terms](https://modbus-monitor.github.io/modbus-device-maps/data-license/)

## Register table (sample)

| Signal | Display address | Data type | Units | Category |
|---|---|---|---|---|
| Voltage L1 V | 400008 | UINT32 | V | Voltage |
| Ampere L1 A | 400000 | UINT32 | A | Current |
| Kw L1 W | 400022 | INT32 | - | Power |
| Energy import kwh kWh | 400048 | UINT32 | kWh | Energy |
| Frequency Hz | 400021 | UINT16 | Hz | Frequency |
| Pf L1 | 400040 | INT16 | - | Power Factor |
| Demand elapsed time sec | 400116 | UINT16 | kW | Demand |
| Thd V1 | 400117 | UINT16 | - | Harmonics |
| Cos L1 | 400044 | INT16 | - | General |
| Ampere L2 A | 400002 | UINT32 | A | Current |
| Ampere L3 A | 400004 | UINT32 | A | Current |
| Ampere neutral current A | 400006 | UINT32 | A | Current |

## Addressing and setup

Addresses and values above are copied from the public JSON preview. Confirm the exact model, firmware, register function, address base, word order, scaling and units against the manufacturer manual before polling. No manufacturer manual revision or hardware validation is established by this page.

## Use with Modbus Monitor XPF

Check the device-map catalog in your installed XPF version for current map availability and licensing. The software download link does not open this map.

[Get Modbus Monitor XPF](https://docs.quantumbitsolutions.com/downloads-purchase/) · [Request a map or correction](https://github.com/Modbus-Monitor/modbus-device-maps/issues/new/choose) · [Browse all previews](https://docs.quantumbitsolutions.com/modbus-device-maps/)

<script type="application/ld+json">{"@context": "https://schema.org", "@type": "Dataset", "name": "Delab PQM public register preview", "description": "Sample register addresses and data types; not a complete map or hardware verification.", "url": "https://docs.quantumbitsolutions.com/modbus-device-maps/previews/delab/pqm/", "license": "https://modbus-monitor.github.io/modbus-device-maps/data-license/", "creator": {"@type": "Organization", "name": "Quantum Bit Solutions", "url": "https://quantumbitsolutions.com/"}, "distribution": {"@type": "DataDownload", "encodingFormat": "application/json", "contentUrl": "https://modbus-monitor.github.io/modbus-device-maps/maps/delab/pqm.json"}}</script>
