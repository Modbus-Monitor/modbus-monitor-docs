---
title: "Elmeasure Prepaid 1P,Prepaid 3P Modbus register preview"
description: "Sample register addresses and data types for Elmeasure Prepaid 1P,Prepaid 3P. Public preview with JSON source and verification status."
---

# Elmeasure Prepaid 1P,Prepaid 3P Modbus register preview

Public preview for **Elmeasure Prepaid 1P,Prepaid 3P** (Power Meter).
This sample is not a complete map or evidence of hardware testing.

## Preview details

- Catalog ID: `elmeasure/prepaid-1p-prepaid-3p`
- Map version: 1.0
- Verification: not-reviewed
- Protocols: RTU, TCP
- Public preview: 12 registers. Complete in-app availability is not established by this preview.

[JSON preview](https://modbus-monitor.github.io/modbus-device-maps/maps/elmeasure/prepaid-1p-prepaid-3p.json) · [Data terms](https://modbus-monitor.github.io/modbus-device-maps/data-license/)

## Register table (sample)

| Signal | Display address | Data type | Units | Category |
|---|---|---|---|---|
| Current total | 400148 | FLOAT32 | - | Current |
| Frequency | 400156 | FLOAT32 | Hz | Frequency |
| PF ave Instantaneous | 400116 | FLOAT32 | - | Power Factor |
| Watts total | 400100 | FLOAT32 | - | General |
| PF R phase | 400118 | FLOAT32 | - | Power Factor |
| PF Y phase | 400120 | FLOAT32 | - | Power Factor |
| PF B phase | 400122 | FLOAT32 | - | Power Factor |
| Current R phase | 400150 | FLOAT32 | - | Current |
| Current Y phase | 400152 | FLOAT32 | - | Current |
| Current B phase | 400154 | FLOAT32 | - | Current |
| Watts R phase | 400102 | FLOAT32 | - | General |
| Watts Y phase | 400104 | FLOAT32 | - | General |

## Addressing and setup

Addresses and values above are copied from the public JSON preview. Confirm the exact model, firmware, register function, address base, word order, scaling and units against the manufacturer manual before polling. No manufacturer manual revision or hardware validation is established by this page.

## Use with Modbus Monitor XPF

Check the device-map catalog in your installed XPF version for current map availability and licensing. The software download link does not open this map.

[Get Modbus Monitor XPF](https://docs.quantumbitsolutions.com/downloads-purchase/) · [Request a map or correction](https://github.com/Modbus-Monitor/modbus-device-maps/issues/new/choose) · [Browse all previews](https://docs.quantumbitsolutions.com/modbus-device-maps/)

<script type="application/ld+json">{"@context": "https://schema.org", "@type": "Dataset", "name": "Elmeasure Prepaid 1P,Prepaid 3P public register preview", "description": "Sample register addresses and data types; not a complete map or hardware verification.", "url": "https://docs.quantumbitsolutions.com/modbus-device-maps/previews/elmeasure/prepaid-1p-prepaid-3p/", "license": "https://modbus-monitor.github.io/modbus-device-maps/data-license/", "creator": {"@type": "Organization", "name": "Quantum Bit Solutions", "url": "https://quantumbitsolutions.com/"}, "distribution": {"@type": "DataDownload", "encodingFormat": "application/json", "contentUrl": "https://modbus-monitor.github.io/modbus-device-maps/maps/elmeasure/prepaid-1p-prepaid-3p.json"}}</script>
