---
title: "Larsen Toubro Vega Modbus register preview"
description: "Sample register addresses and data types for Larsen Toubro Vega. Public preview with JSON source and verification status."
---

# Larsen Toubro Vega Modbus register preview

Public preview for **Larsen Toubro Vega** (Power Meter).
This sample is not a complete map or evidence of hardware testing.

## Preview details

- Catalog ID: `larsen-toubro/vega`
- Map version: 1.0
- Verification: not-reviewed
- Protocols: RTU, TCP
- Public preview: 12 registers. Complete in-app availability is not established by this preview.

[JSON preview](https://modbus-monitor.github.io/modbus-device-maps/maps/larsen-toubro/vega.json) · [Data terms](https://modbus-monitor.github.io/modbus-device-maps/data-license/)

## Register table (sample)

| Signal | Display address | Data type | Units | Category |
|---|---|---|---|---|
| R phase voltage | 300000 | UINT32 | V | Voltage |
| R phase current | 300006 | UINT32 | - | Current |
| Active power R phase | 300012 | UINT32 | kW | Power |
| Import apparent energy | 300231 | FLOAT64 | kWh | Energy |
| Line frequency | 300056 | UINT32 | Hz | Frequency |
| Import apparent rising demand | 300144 | UINT32 | kW | Demand |
| Percentage load R phase | 300098 | UINT32 | - | General |
| Md import apparent | 300132 | UINT32 | - | Communication |
| Y phase voltage | 300002 | UINT32 | V | Voltage |
| B phase voltage | 300004 | UINT32 | V | Voltage |
| Y phase current | 300008 | UINT32 | - | Current |
| B phase current | 300010 | UINT32 | - | Current |

## Addressing and setup

Addresses and values above are copied from the public JSON preview. Confirm the exact model, firmware, register function, address base, word order, scaling and units against the manufacturer manual before polling. No manufacturer manual revision or hardware validation is established by this page.

## Use with Modbus Monitor XPF

Check the device-map catalog in your installed XPF version for current map availability and licensing. The software download link does not open this map.

[Get Modbus Monitor XPF](https://docs.quantumbitsolutions.com/downloads-purchase/) · [Request a map or correction](https://github.com/Modbus-Monitor/modbus-device-maps/issues/new/choose) · [Browse all previews](https://docs.quantumbitsolutions.com/modbus-device-maps/)

<script type="application/ld+json">{"@context": "https://schema.org", "@type": "Dataset", "name": "Larsen Toubro Vega public register preview", "description": "Sample register addresses and data types; not a complete map or hardware verification.", "url": "https://docs.quantumbitsolutions.com/modbus-device-maps/previews/larsen-toubro/vega/", "license": "https://modbus-monitor.github.io/modbus-device-maps/data-license/", "creator": {"@type": "Organization", "name": "Quantum Bit Solutions", "url": "https://quantumbitsolutions.com/"}, "distribution": {"@type": "DataDownload", "encodingFormat": "application/json", "contentUrl": "https://modbus-monitor.github.io/modbus-device-maps/maps/larsen-toubro/vega.json"}}</script>
