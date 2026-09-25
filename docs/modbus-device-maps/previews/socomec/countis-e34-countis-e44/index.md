---
title: "Socomec Countis E34, Countis E44 Modbus register preview"
description: "Sample register addresses and data types for Socomec Countis E34, Countis E44. Public preview with JSON source and verification status."
---

# Socomec Countis E34, Countis E44 Modbus register preview

Public preview for **Socomec Countis E34, Countis E44** (Power Meter).
This sample is not a complete map or evidence of hardware testing.

## Preview details

- Catalog ID: `socomec/countis-e34-countis-e44`
- Map version: 1.0
- Verification: not-reviewed
- Protocols: RTU, TCP
- Public preview: 12 registers. Complete in-app availability is not established by this preview.

[JSON preview](https://modbus-monitor.github.io/modbus-device-maps/maps/socomec/countis-e34-countis-e44.json) · [Data terms](https://modbus-monitor.github.io/modbus-device-maps/data-license/)

## Register table (sample)

| Signal | Display address | Data type | Units | Category |
|---|---|---|---|---|
| Phase to phase voltage U12 | 450514 | UINT32 | V | Voltage |
| Current transformer primary | 457346 | UINT16 | - | Current |
| Active power - P | 450536 | INT32 | kW | Power |
| Partial positive active energy ea | 450780 | UINT32 | kWh | Energy |
| Frequency F | 450526 | UINT32 | Hz | Frequency |
| Product name | 450000 | STRING | - | Identification |
| Product order ID Countis100 protection200 atys300 diris400 | 450004 | UINT16 | - | General |
| Communication board VLO | 438919 | STRING | - | Communication |
| Phase to phase voltage U23 | 450516 | UINT32 | V | Voltage |
| Phase to phase voltage U31 | 450518 | UINT32 | V | Voltage |
| Simple voltage V1 | 450520 | UINT32 | V | Voltage |
| Simple voltage V2 | 450522 | UINT32 | V | Voltage |

## Addressing and setup

Addresses and values above are copied from the public JSON preview. Confirm the exact model, firmware, register function, address base, word order, scaling and units against the manufacturer manual before polling. No manufacturer manual revision or hardware validation is established by this page.

## Use with Modbus Monitor XPF

Check the device-map catalog in your installed XPF version for current map availability and licensing. The software download link does not open this map.

[Get Modbus Monitor XPF](https://docs.quantumbitsolutions.com/downloads-purchase/) · [Request a map or correction](https://github.com/Modbus-Monitor/modbus-device-maps/issues/new/choose) · [Browse all previews](https://docs.quantumbitsolutions.com/modbus-device-maps/)

<script type="application/ld+json">{"@context": "https://schema.org", "@type": "Dataset", "name": "Socomec Countis E34, Countis E44 public register preview", "description": "Sample register addresses and data types; not a complete map or hardware verification.", "url": "https://docs.quantumbitsolutions.com/modbus-device-maps/previews/socomec/countis-e34-countis-e44/", "license": "https://modbus-monitor.github.io/modbus-device-maps/data-license/", "creator": {"@type": "Organization", "name": "Quantum Bit Solutions", "url": "https://quantumbitsolutions.com/"}, "distribution": {"@type": "DataDownload", "encodingFormat": "application/json", "contentUrl": "https://modbus-monitor.github.io/modbus-device-maps/maps/socomec/countis-e34-countis-e44.json"}}</script>
