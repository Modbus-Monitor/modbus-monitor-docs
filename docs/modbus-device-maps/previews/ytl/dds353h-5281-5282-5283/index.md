---
title: "YTL DDS353H,5281,5282,5283 Modbus register preview"
description: "Sample register addresses and data types for YTL DDS353H,5281,5282,5283. Public preview with JSON source and verification status."
---

# YTL DDS353H,5281,5282,5283 Modbus register preview

Public preview for **YTL DDS353H,5281,5282,5283** (Power Meter).
This sample is not a complete map or evidence of hardware testing.

## Preview details

- Catalog ID: `ytl/dds353h-5281-5282-5283`
- Map version: 1.0
- Verification: not-reviewed
- Protocols: RTU, TCP
- Public preview: 12 registers. Complete in-app availability is not established by this preview.

[JSON preview](https://modbus-monitor.github.io/modbus-device-maps/maps/ytl/dds353h-5281-5282-5283.json) · [Data terms](https://modbus-monitor.github.io/modbus-device-maps/data-license/)

## Register table (sample)

| Signal | Display address | Data type | Units | Category |
|---|---|---|---|---|
| Phase voltage V1 V | 400305 | UINT16 | V | Voltage |
| Phase wire current I1 A | 400313 | UINT16 | - | Current |
| Active power P1 Phase a kW | 400320 | INT32 | kW | Power |
| Present total active energy kwh | 440960 | UINT32 | kWh | Energy |
| Frequency F Hz | 400304 | UINT16 | Hz | Frequency |
| Last 1 month demand | 441008 | UINT32 | kW | Demand |
| Temperature | 465280 | INT16 | degC | Temperature |
| Time offset | 465281 | INT16 | - | General |
| Phase voltage V2 V | 400306 | UINT16 | V | Voltage |
| Phase voltage V3 V | 400307 | UINT16 | V | Voltage |
| Phase wire current I2 A | 400315 | UINT16 | - | Current |
| Phase wire current I3 A | 400317 | UINT16 | - | Current |

## Addressing and setup

Addresses and values above are copied from the public JSON preview. Confirm the exact model, firmware, register function, address base, word order, scaling and units against the manufacturer manual before polling. No manufacturer manual revision or hardware validation is established by this page.

## Use with Modbus Monitor XPF

Check the device-map catalog in your installed XPF version for current map availability and licensing. The software download link does not open this map.

[Get Modbus Monitor XPF](https://docs.quantumbitsolutions.com/downloads-purchase/) · [Request a map or correction](https://github.com/Modbus-Monitor/modbus-device-maps/issues/new/choose) · [Browse all previews](https://docs.quantumbitsolutions.com/modbus-device-maps/)

<script type="application/ld+json">{"@context": "https://schema.org", "@type": "Dataset", "name": "YTL DDS353H,5281,5282,5283 public register preview", "description": "Sample register addresses and data types; not a complete map or hardware verification.", "url": "https://docs.quantumbitsolutions.com/modbus-device-maps/previews/ytl/dds353h-5281-5282-5283/", "license": "https://modbus-monitor.github.io/modbus-device-maps/data-license/", "creator": {"@type": "Organization", "name": "Quantum Bit Solutions", "url": "https://quantumbitsolutions.com/"}, "distribution": {"@type": "DataDownload", "encodingFormat": "application/json", "contentUrl": "https://modbus-monitor.github.io/modbus-device-maps/maps/ytl/dds353h-5281-5282-5283.json"}}</script>
