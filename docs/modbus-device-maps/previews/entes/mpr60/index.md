---
title: "ENTES MPR60 Modbus register preview"
description: "Sample register addresses and data types for ENTES MPR60. Public preview with JSON source and verification status."
---

# ENTES MPR60 Modbus register preview

Public preview for **ENTES MPR60** (Power Meter).
This sample is not a complete map or evidence of hardware testing.

## Preview details

- Catalog ID: `entes/mpr60`
- Map version: 1.0
- Verification: not-reviewed
- Protocols: RTU, TCP
- Public preview: 12 registers. Complete in-app availability is not established by this preview.

[JSON preview](https://modbus-monitor.github.io/modbus-device-maps/maps/entes/mpr60.json) · [Data terms](https://modbus-monitor.github.io/modbus-device-maps/data-license/)

## Register table (sample)

| Signal | Display address | Data type | Units | Category |
|---|---|---|---|---|
| Voltage LN1 V | 416384 | UINT32 | V | Voltage |
| Current LN1 A | 416390 | UINT32 | A | Current |
| Active power L1 W | 416398 | INT32 | kW | Power |
| Import active energy kWh MWh | 416504 | UINT32 | kWh | Energy |
| Frequency Hz | 416438 | UINT32 | Hz | Frequency |
| Thd V1 | 416446 | UINT32 | - | Harmonics |
| Cos L1 | 416422 | INT32 | - | General |
| Voltage LN2 V | 416386 | UINT32 | V | Voltage |
| Voltage LN3 V | 416388 | UINT32 | V | Voltage |
| Current LN2 A | 416392 | UINT32 | A | Current |
| Current LN3 A | 416394 | UINT32 | A | Current |
| Total current A | 416396 | UINT32 | - | Current |

## Addressing and setup

Addresses and values above are copied from the public JSON preview. Confirm the exact model, firmware, register function, address base, word order, scaling and units against the manufacturer manual before polling. No manufacturer manual revision or hardware validation is established by this page.

## Use with Modbus Monitor XPF

Check the device-map catalog in your installed XPF version for current map availability and licensing. The software download link does not open this map.

[Get Modbus Monitor XPF](https://docs.quantumbitsolutions.com/downloads-purchase/) · [Request a map or correction](https://github.com/Modbus-Monitor/modbus-device-maps/issues/new/choose) · [Browse all previews](https://docs.quantumbitsolutions.com/modbus-device-maps/)

<script type="application/ld+json">{"@context": "https://schema.org", "@type": "Dataset", "name": "ENTES MPR60 public register preview", "description": "Sample register addresses and data types; not a complete map or hardware verification.", "url": "https://docs.quantumbitsolutions.com/modbus-device-maps/previews/entes/mpr60/", "license": "https://modbus-monitor.github.io/modbus-device-maps/data-license/", "creator": {"@type": "Organization", "name": "Quantum Bit Solutions", "url": "https://quantumbitsolutions.com/"}, "distribution": {"@type": "DataDownload", "encodingFormat": "application/json", "contentUrl": "https://modbus-monitor.github.io/modbus-device-maps/maps/entes/mpr60.json"}}</script>
