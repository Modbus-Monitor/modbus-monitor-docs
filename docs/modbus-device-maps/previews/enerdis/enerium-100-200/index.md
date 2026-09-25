---
title: "Enerdis Enerium 100-200 Modbus register preview"
description: "Sample register addresses and data types for Enerdis Enerium 100-200. Public preview with JSON source and verification status."
---

# Enerdis Enerium 100-200 Modbus register preview

Public preview for **Enerdis Enerium 100-200** (Power Meter).
This sample is not a complete map or evidence of hardware testing.

## Preview details

- Catalog ID: `enerdis/enerium-100-200`
- Map version: 1.0
- Verification: not-reviewed
- Protocols: RTU, TCP
- Public preview: 12 registers. Complete in-app availability is not established by this preview.

[JSON preview](https://modbus-monitor.github.io/modbus-device-maps/maps/enerdis/enerium-100-200.json) · [Data terms](https://modbus-monitor.github.io/modbus-device-maps/data-license/)

## Register table (sample)

| Signal | Display address | Data type | Units | Category |
|---|---|---|---|---|
| Unbalance of the voltages | 401348 | INT16 | V | Voltage |
| Hour meter presence of current | 402564 | UINT32 | - | Current |
| Active energy receiver mode Wh | 402566 | UINT32 | kWh | Energy |
| Frequency Hz | 401349 | UINT16 | Hz | Frequency |
| PF1 | 401326 | INT16 | - | Power Factor |
| Harmonics order by order V1 0 to 50 | 401536 | UINT16 | - | Harmonics |
| V1 V | 401280 | UINT32 | - | General |
| Quadrant PF1 | 401327 | UINT16 | - | Power Factor |
| PF2 | 401328 | INT16 | - | Power Factor |
| Quadrant PF2 | 401329 | UINT16 | - | Power Factor |
| PF3 | 401330 | INT16 | - | Power Factor |
| Quadrant PF3 | 401331 | UINT16 | - | Power Factor |

## Addressing and setup

Addresses and values above are copied from the public JSON preview. Confirm the exact model, firmware, register function, address base, word order, scaling and units against the manufacturer manual before polling. No manufacturer manual revision or hardware validation is established by this page.

## Use with Modbus Monitor XPF

Check the device-map catalog in your installed XPF version for current map availability and licensing. The software download link does not open this map.

[Get Modbus Monitor XPF](https://docs.quantumbitsolutions.com/downloads-purchase/) · [Request a map or correction](https://github.com/Modbus-Monitor/modbus-device-maps/issues/new/choose) · [Browse all previews](https://docs.quantumbitsolutions.com/modbus-device-maps/)

<script type="application/ld+json">{"@context": "https://schema.org", "@type": "Dataset", "name": "Enerdis Enerium 100-200 public register preview", "description": "Sample register addresses and data types; not a complete map or hardware verification.", "url": "https://docs.quantumbitsolutions.com/modbus-device-maps/previews/enerdis/enerium-100-200/", "license": "https://modbus-monitor.github.io/modbus-device-maps/data-license/", "creator": {"@type": "Organization", "name": "Quantum Bit Solutions", "url": "https://quantumbitsolutions.com/"}, "distribution": {"@type": "DataDownload", "encodingFormat": "application/json", "contentUrl": "https://modbus-monitor.github.io/modbus-device-maps/maps/enerdis/enerium-100-200.json"}}</script>
