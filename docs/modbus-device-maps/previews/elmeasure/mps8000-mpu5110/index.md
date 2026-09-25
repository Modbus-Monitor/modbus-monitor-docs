---
title: "Elmeasure MPS8000,MPU5110 Modbus register preview"
description: "Sample register addresses and data types for Elmeasure MPS8000,MPU5110. Public preview with JSON source and verification status."
---

# Elmeasure MPS8000,MPU5110 Modbus register preview

Public preview for **Elmeasure MPS8000,MPU5110** (Power Meter).
This sample is not a complete map or evidence of hardware testing.

## Preview details

- Catalog ID: `elmeasure/mps8000-mpu5110`
- Map version: 1.0
- Verification: not-reviewed
- Protocols: RTU, TCP
- Public preview: 12 registers. Complete in-app availability is not established by this preview.

[JSON preview](https://modbus-monitor.github.io/modbus-device-maps/maps/elmeasure/mps8000-mpu5110.json) · [Data terms](https://modbus-monitor.github.io/modbus-device-maps/data-license/)

## Register table (sample)

| Signal | Display address | Data type | Units | Category |
|---|---|---|---|---|
| Voltage R harmonics | 400184 | FLOAT32 | V | Voltage |
| Current average | 400148 | FLOAT32 | A | Current |
| Frequency | 400156 | FLOAT32 | Hz | Frequency |
| Pf avg inst | 400116 | FLOAT32 | - | Power Factor |
| Watts total | 400100 | FLOAT32 | - | General |
| Pf R phase | 400118 | FLOAT32 | - | Power Factor |
| Pf Y phase | 400120 | FLOAT32 | - | Power Factor |
| Pf B phase | 400122 | FLOAT32 | - | Power Factor |
| Current R phase | 400150 | FLOAT32 | - | Current |
| Current Y phase | 400152 | FLOAT32 | - | Current |
| Current B phase | 400154 | FLOAT32 | - | Current |
| Pf average received | 400174 | FLOAT32 | - | Power Factor |

## Addressing and setup

Addresses and values above are copied from the public JSON preview. Confirm the exact model, firmware, register function, address base, word order, scaling and units against the manufacturer manual before polling. No manufacturer manual revision or hardware validation is established by this page.

## Use with Modbus Monitor XPF

Check the device-map catalog in your installed XPF version for current map availability and licensing. The software download link does not open this map.

[Get Modbus Monitor XPF](https://docs.quantumbitsolutions.com/downloads-purchase/) · [Request a map or correction](https://github.com/Modbus-Monitor/modbus-device-maps/issues/new/choose) · [Browse all previews](https://docs.quantumbitsolutions.com/modbus-device-maps/)

<script type="application/ld+json">{"@context": "https://schema.org", "@type": "Dataset", "name": "Elmeasure MPS8000,MPU5110 public register preview", "description": "Sample register addresses and data types; not a complete map or hardware verification.", "url": "https://docs.quantumbitsolutions.com/modbus-device-maps/previews/elmeasure/mps8000-mpu5110/", "license": "https://modbus-monitor.github.io/modbus-device-maps/data-license/", "creator": {"@type": "Organization", "name": "Quantum Bit Solutions", "url": "https://quantumbitsolutions.com/"}, "distribution": {"@type": "DataDownload", "encodingFormat": "application/json", "contentUrl": "https://modbus-monitor.github.io/modbus-device-maps/maps/elmeasure/mps8000-mpu5110.json"}}</script>
