---
title: "Hobut M850 DC Modbus register preview"
description: "Sample register addresses and data types for Hobut M850 DC. Public preview with JSON source and verification status."
---

# Hobut M850 DC Modbus register preview

Public preview for **Hobut M850 DC** (Power Meter).
This sample is not a complete map or evidence of hardware testing.

## Preview details

- Catalog ID: `hobut/m850-dc`
- Map version: 1.0
- Verification: not-reviewed
- Protocols: RTU, TCP
- Public preview: 10 registers. Complete in-app availability is not established by this preview.

[JSON preview](https://modbus-monitor.github.io/modbus-device-maps/maps/hobut/m850-dc.json) · [Data terms](https://modbus-monitor.github.io/modbus-device-maps/data-license/)

## Register table (sample)

| Signal | Display address | Data type | Units | Category |
|---|---|---|---|---|
| Kw sum | 300018 | UINT16 | - | Power |
| Kwhr import | 300026 | UINT16 | kWh | Energy |
| Vi | 300006 | UINT16 | - | General |
| Kwd import | 300044 | UINT16 | - | Power |
| Kwhr export | 300064 | UINT16 | kWh | Energy |
| Max kwd import | 300074 | UINT16 | - | Power |
| 11 | 300012 | UINT16 | - | General |
| Ad | 300048 | UINT16 | - | General |
| Ahr | 300070 | UINT16 | - | General |
| Maxad | 300080 | UINT16 | - | General |

## Addressing and setup

Addresses and values above are copied from the public JSON preview. Confirm the exact model, firmware, register function, address base, word order, scaling and units against the manufacturer manual before polling. No manufacturer manual revision or hardware validation is established by this page.

## Use with Modbus Monitor XPF

Check the device-map catalog in your installed XPF version for current map availability and licensing. The software download link does not open this map.

[Get Modbus Monitor XPF](https://docs.quantumbitsolutions.com/downloads-purchase/) · [Request a map or correction](https://github.com/Modbus-Monitor/modbus-device-maps/issues/new/choose) · [Browse all previews](https://docs.quantumbitsolutions.com/modbus-device-maps/)

<script type="application/ld+json">{"@context": "https://schema.org", "@type": "Dataset", "name": "Hobut M850 DC public register preview", "description": "Sample register addresses and data types; not a complete map or hardware verification.", "url": "https://docs.quantumbitsolutions.com/modbus-device-maps/previews/hobut/m850-dc/", "license": "https://modbus-monitor.github.io/modbus-device-maps/data-license/", "creator": {"@type": "Organization", "name": "Quantum Bit Solutions", "url": "https://quantumbitsolutions.com/"}, "distribution": {"@type": "DataDownload", "encodingFormat": "application/json", "contentUrl": "https://modbus-monitor.github.io/modbus-device-maps/maps/hobut/m850-dc.json"}}</script>
