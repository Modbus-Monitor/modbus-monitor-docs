---
title: "SATEC Powermeters Modbus register preview"
description: "Sample register addresses and data types for SATEC Powermeters. Public preview with JSON source and verification status."
---

# SATEC Powermeters Modbus register preview

Public preview for **SATEC Powermeters** (Power Meter).
This sample is not a complete map or evidence of hardware testing.

## Preview details

- Catalog ID: `satec/powermeters`
- Map version: 1.0
- Verification: not-reviewed
- Protocols: RTU, TCP
- Public preview: 12 registers. Complete in-app availability is not established by this preview.

[JSON preview](https://modbus-monitor.github.io/modbus-device-maps/maps/satec/powermeters.json) · [Data terms](https://modbus-monitor.github.io/modbus-device-maps/data-license/)

## Register table (sample)

| Signal | Display address | Data type | Units | Category |
|---|---|---|---|---|
| Voltage l1l12 V | 400256 | UINT16 | V | Voltage |
| Current l1 A | 400259 | UINT16 | A | Current |
| Kw l1 kW | 400262 | UINT16 | - | Power |
| Kwh import low kWh | 400287 | UINT16 | kWh | Energy |
| Frequency Hz | 400279 | UINT16 | Hz | Frequency |
| Voltage l2l23 V | 400257 | UINT16 | V | Voltage |
| Voltage l3l31 V | 400258 | UINT16 | V | Voltage |
| Current l2 A | 400260 | UINT16 | A | Current |
| Current l3 A | 400261 | UINT16 | A | Current |
| Kw l2 kW | 400263 | UINT16 | - | Power |
| Kw l3 kW | 400264 | UINT16 | - | Power |
| Kvar l1 kvar | 400265 | UINT16 | - | Power |

## Addressing and setup

Addresses and values above are copied from the public JSON preview. Confirm the exact model, firmware, register function, address base, word order, scaling and units against the manufacturer manual before polling. No manufacturer manual revision or hardware validation is established by this page.

## Use with Modbus Monitor XPF

Check the device-map catalog in your installed XPF version for current map availability and licensing. The software download link does not open this map.

[Get Modbus Monitor XPF](https://docs.quantumbitsolutions.com/downloads-purchase/) · [Request a map or correction](https://github.com/Modbus-Monitor/modbus-device-maps/issues/new/choose) · [Browse all previews](https://docs.quantumbitsolutions.com/modbus-device-maps/)

<script type="application/ld+json">{"@context": "https://schema.org", "@type": "Dataset", "name": "SATEC Powermeters public register preview", "description": "Sample register addresses and data types; not a complete map or hardware verification.", "url": "https://docs.quantumbitsolutions.com/modbus-device-maps/previews/satec/powermeters/", "license": "https://modbus-monitor.github.io/modbus-device-maps/data-license/", "creator": {"@type": "Organization", "name": "Quantum Bit Solutions", "url": "https://quantumbitsolutions.com/"}, "distribution": {"@type": "DataDownload", "encodingFormat": "application/json", "contentUrl": "https://modbus-monitor.github.io/modbus-device-maps/maps/satec/powermeters.json"}}</script>
