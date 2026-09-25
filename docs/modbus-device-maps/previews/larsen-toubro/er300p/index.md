---
title: "Larsen Toubro ER300P Modbus register preview"
description: "Sample register addresses and data types for Larsen Toubro ER300P. Public preview with JSON source and verification status."
---

# Larsen Toubro ER300P Modbus register preview

Public preview for **Larsen Toubro ER300P** (Power Meter).
This sample is not a complete map or evidence of hardware testing.

## Preview details

- Catalog ID: `larsen-toubro/er300p`
- Map version: 1.0
- Verification: not-reviewed
- Protocols: RTU, TCP
- Public preview: 12 registers. Complete in-app availability is not established by this preview.

[JSON preview](https://modbus-monitor.github.io/modbus-device-maps/maps/larsen-toubro/er300p.json) · [Data terms](https://modbus-monitor.github.io/modbus-device-maps/data-license/)

## Register table (sample)

| Signal | Display address | Data type | Units | Category |
|---|---|---|---|---|
| R line voltage V | 300000 | UINT16 | V | Voltage |
| R phase current C | 300006 | UINT16 | - | Current |
| Total active power W | 300009 | INT16 | kW | Power |
| Cumulative energy forward Wh | 300022 | UINT32 | kWh | Energy |
| Average frequency | 300013 | UINT16 | Hz | Frequency |
| Tamper status | 300014 | UINT16 | - | Status |
| Anomaly string ASCII | 300030 | UINT32 | - | General |
| Y line voltage V | 300001 | UINT16 | V | Voltage |
| B line voltage V | 300002 | UINT16 | V | Voltage |
| R phase voltage V | 300003 | UINT16 | V | Voltage |
| Y phase voltage V | 300004 | UINT16 | V | Voltage |
| B phase voltage V | 300005 | UINT16 | V | Voltage |

## Addressing and setup

Addresses and values above are copied from the public JSON preview. Confirm the exact model, firmware, register function, address base, word order, scaling and units against the manufacturer manual before polling. No manufacturer manual revision or hardware validation is established by this page.

## Use with Modbus Monitor XPF

Check the device-map catalog in your installed XPF version for current map availability and licensing. The software download link does not open this map.

[Get Modbus Monitor XPF](https://docs.quantumbitsolutions.com/downloads-purchase/) · [Request a map or correction](https://github.com/Modbus-Monitor/modbus-device-maps/issues/new/choose) · [Browse all previews](https://docs.quantumbitsolutions.com/modbus-device-maps/)

<script type="application/ld+json">{"@context": "https://schema.org", "@type": "Dataset", "name": "Larsen Toubro ER300P public register preview", "description": "Sample register addresses and data types; not a complete map or hardware verification.", "url": "https://docs.quantumbitsolutions.com/modbus-device-maps/previews/larsen-toubro/er300p/", "license": "https://modbus-monitor.github.io/modbus-device-maps/data-license/", "creator": {"@type": "Organization", "name": "Quantum Bit Solutions", "url": "https://quantumbitsolutions.com/"}, "distribution": {"@type": "DataDownload", "encodingFormat": "application/json", "contentUrl": "https://modbus-monitor.github.io/modbus-device-maps/maps/larsen-toubro/er300p.json"}}</script>
