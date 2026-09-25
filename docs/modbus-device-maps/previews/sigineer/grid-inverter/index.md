---
title: "Sigineer [Grid Inverter Modbus register preview"
description: "Sample register addresses and data types for Sigineer [Grid Inverter. Public preview with JSON source and verification status."
---

# Sigineer [Grid Inverter Modbus register preview

Public preview for **Sigineer [Grid Inverter** (Solar Inverter).
This sample is not a complete map or evidence of hardware testing.

## Preview details

- Catalog ID: `sigineer/grid-inverter`
- Map version: 1.0
- Verification: not-reviewed
- Protocols: RTU, TCP
- Public preview: 12 registers. Complete in-app availability is not established by this preview.

[JSON preview](https://modbus-monitor.github.io/modbus-device-maps/maps/sigineer/grid-inverter.json) · [Data terms](https://modbus-monitor.github.io/modbus-device-maps/data-license/)

## Register table (sample)

| Signal | Display address | Data type | Units | Category |
|---|---|---|---|---|
| Battery voltage V | 300006 | UINT16 | V | Voltage |
| Battery current A | 300007 | UINT16 | - | Current |
| Pv power W | 300018 | UINT16 | kW | Power |
| System geneeraating capacity low KWH | 300020 | UINT16 | kWh | Energy |
| Input frequency Hz | 300008 | UINT16 | Hz | Frequency |
| Battery status | 300005 | UINT16 | - | Status |
| Ambient temperature C | 300000 | UINT16 | degC | Temperature |
| Master version | 300001 | UINT16 | - | Identification |
| Year month 39 | 300002 | UINT16 | - | General |
| Input voltage V | 300009 | UINT16 | V | Voltage |
| Inverter frequency Hz | 300012 | UINT16 | Hz | Frequency |
| Inverter voltage V | 300013 | UINT16 | V | Voltage |

## Addressing and setup

Addresses and values above are copied from the public JSON preview. Confirm the exact model, firmware, register function, address base, word order, scaling and units against the manufacturer manual before polling. No manufacturer manual revision or hardware validation is established by this page.

## Use with Modbus Monitor XPF

Check the device-map catalog in your installed XPF version for current map availability and licensing. The software download link does not open this map.

[Get Modbus Monitor XPF](https://docs.quantumbitsolutions.com/downloads-purchase/) · [Request a map or correction](https://github.com/Modbus-Monitor/modbus-device-maps/issues/new/choose) · [Browse all previews](https://docs.quantumbitsolutions.com/modbus-device-maps/)

<script type="application/ld+json">{"@context": "https://schema.org", "@type": "Dataset", "name": "Sigineer [Grid Inverter public register preview", "description": "Sample register addresses and data types; not a complete map or hardware verification.", "url": "https://docs.quantumbitsolutions.com/modbus-device-maps/previews/sigineer/grid-inverter/", "license": "https://modbus-monitor.github.io/modbus-device-maps/data-license/", "creator": {"@type": "Organization", "name": "Quantum Bit Solutions", "url": "https://quantumbitsolutions.com/"}, "distribution": {"@type": "DataDownload", "encodingFormat": "application/json", "contentUrl": "https://modbus-monitor.github.io/modbus-device-maps/maps/sigineer/grid-inverter.json"}}</script>
