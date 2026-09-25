---
title: "Hobut M553 Modbus register preview"
description: "Sample register addresses and data types for Hobut M553. Public preview with JSON source and verification status."
---

# Hobut M553 Modbus register preview

Public preview for **Hobut M553** (Power Meter).
This sample is not a complete map or evidence of hardware testing.

## Preview details

- Catalog ID: `hobut/m553`
- Map version: 1.0
- Verification: not-reviewed
- Protocols: RTU, TCP
- Public preview: 12 registers. Complete in-app availability is not established by this preview.

[JSON preview](https://modbus-monitor.github.io/modbus-device-maps/maps/hobut/m553.json) · [Data terms](https://modbus-monitor.github.io/modbus-device-maps/data-license/)

## Register table (sample)

| Signal | Display address | Data type | Units | Category |
|---|---|---|---|---|
| Neutralcurrent | 300050 | UINT16 | - | Current |
| Kw sum | 300018 | UINT16 | - | Power |
| Kwhr import | 300026 | UINT16 | kWh | Energy |
| Hz | 300030 | UINT16 | - | Frequency |
| Pf avg | 300024 | UINT16 | - | Power Factor |
| Vu 2 | 300000 | UINT16 | - | General |
| Kva sum | 300020 | UINT16 | - | Power |
| Kvar sum | 300022 | UINT16 | - | Power |
| Kvarhr import | 300028 | UINT16 | kWh | Energy |
| Kwd import | 300044 | UINT16 | - | Power |
| Kvad | 300046 | UINT16 | - | Power |
| Max kwd import | 300074 | UINT16 | - | Power |

## Addressing and setup

Addresses and values above are copied from the public JSON preview. Confirm the exact model, firmware, register function, address base, word order, scaling and units against the manufacturer manual before polling. No manufacturer manual revision or hardware validation is established by this page.

## Use with Modbus Monitor XPF

Check the device-map catalog in your installed XPF version for current map availability and licensing. The software download link does not open this map.

[Get Modbus Monitor XPF](https://docs.quantumbitsolutions.com/downloads-purchase/) · [Request a map or correction](https://github.com/Modbus-Monitor/modbus-device-maps/issues/new/choose) · [Browse all previews](https://docs.quantumbitsolutions.com/modbus-device-maps/)

<script type="application/ld+json">{"@context": "https://schema.org", "@type": "Dataset", "name": "Hobut M553 public register preview", "description": "Sample register addresses and data types; not a complete map or hardware verification.", "url": "https://docs.quantumbitsolutions.com/modbus-device-maps/previews/hobut/m553/", "license": "https://modbus-monitor.github.io/modbus-device-maps/data-license/", "creator": {"@type": "Organization", "name": "Quantum Bit Solutions", "url": "https://quantumbitsolutions.com/"}, "distribution": {"@type": "DataDownload", "encodingFormat": "application/json", "contentUrl": "https://modbus-monitor.github.io/modbus-device-maps/maps/hobut/m553.json"}}</script>
