---
title: "Bytronic By6150 Modbus register preview"
description: "Sample register addresses and data types for Bytronic By6150. Public preview with JSON source and verification status."
---

# Bytronic By6150 Modbus register preview

Public preview for **Bytronic By6150** (Power Meter).
This sample is not a complete map or evidence of hardware testing.

## Preview details

- Catalog ID: `bytronic/by6150`
- Map version: 1.0
- Verification: not-reviewed
- Protocols: RTU, TCP
- Public preview: 12 registers. Complete in-app availability is not established by this preview.

[JSON preview](https://modbus-monitor.github.io/modbus-device-maps/maps/bytronic/by6150.json) · [Data terms](https://modbus-monitor.github.io/modbus-device-maps/data-license/)

## Register table (sample)

| Signal | Display address | Data type | Units | Category |
|---|---|---|---|---|
| Voltage V1 Volt | 400526 | UINT32 | V | Voltage |
| Current I1 Amp | 400534 | UINT32 | - | Current |
| Power factor phase 1 Cos | 400541 | UINT32 | PF | Power |
| Consumed active energy kWh | 400570 | UINT32 | kWh | Energy |
| Frequencymeter calibration value | 400521 | UINT32 | Hz | Frequency |
| Family instrument type instrument | 400512 | UINT32 | - | General |
| Version | 400513 | UINT32 | - | Identification |
| Medium measurement frequencymeter | 400523 | UINT32 | Hz | Frequency |
| Voltage V2 Volt | 400527 | UINT32 | V | Voltage |
| Voltage V3 Volt | 400528 | UINT32 | V | Voltage |
| Voltage V12 Volt | 400529 | UINT32 | V | Voltage |
| Voltage V23 Volt | 400530 | UINT32 | V | Voltage |

## Addressing and setup

Addresses and values above are copied from the public JSON preview. Confirm the exact model, firmware, register function, address base, word order, scaling and units against the manufacturer manual before polling. No manufacturer manual revision or hardware validation is established by this page.

## Use with Modbus Monitor XPF

Check the device-map catalog in your installed XPF version for current map availability and licensing. The software download link does not open this map.

[Get Modbus Monitor XPF](https://docs.quantumbitsolutions.com/downloads-purchase/) · [Request a map or correction](https://github.com/Modbus-Monitor/modbus-device-maps/issues/new/choose) · [Browse all previews](https://docs.quantumbitsolutions.com/modbus-device-maps/)

<script type="application/ld+json">{"@context": "https://schema.org", "@type": "Dataset", "name": "Bytronic By6150 public register preview", "description": "Sample register addresses and data types; not a complete map or hardware verification.", "url": "https://docs.quantumbitsolutions.com/modbus-device-maps/previews/bytronic/by6150/", "license": "https://modbus-monitor.github.io/modbus-device-maps/data-license/", "creator": {"@type": "Organization", "name": "Quantum Bit Solutions", "url": "https://quantumbitsolutions.com/"}, "distribution": {"@type": "DataDownload", "encodingFormat": "application/json", "contentUrl": "https://modbus-monitor.github.io/modbus-device-maps/maps/bytronic/by6150.json"}}</script>
