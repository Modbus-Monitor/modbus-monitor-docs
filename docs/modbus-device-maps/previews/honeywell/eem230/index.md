---
title: "Honeywell EEM230 Modbus register preview"
description: "Sample register addresses and data types for Honeywell EEM230. Public preview with JSON source and verification status."
---

# Honeywell EEM230 Modbus register preview

Public preview for **Honeywell EEM230** (Power Meter).
This sample is not a complete map or evidence of hardware testing.

## Preview details

- Catalog ID: `honeywell/eem230`
- Map version: 1.0
- Verification: not-reviewed
- Protocols: RTU, TCP
- Public preview: 12 registers. Complete in-app availability is not established by this preview.

[JSON preview](https://modbus-monitor.github.io/modbus-device-maps/maps/honeywell/eem230.json) · [Data terms](https://modbus-monitor.github.io/modbus-device-maps/data-license/)

## Register table (sample)

| Signal | Display address | Data type | Units | Category |
|---|---|---|---|---|
| Urms effective voltage | 400035 | UINT16 | V | Voltage |
| Irms effective current | 400036 | UINT16 | - | Current |
| Prms effective active power | 400037 | UINT16 | kW | Power |
| WT1 total counter energy total tariff 1 | 400027 | UINT32 | kWh | Energy |
| Status protect | 400021 | UINT16 | - | Status |
| Number of supported registers | 400001 | UINT16 | - | Communication |
| Hw vers Modif | 400014 | UINT16 | - | General |
| Serial number low | 400015 | UINT32 | - | Identification |
| WT1 partial counter energy partial tariff 1 | 400029 | UINT32 | kWh | Energy |
| Qrms effective reactive power | 400038 | UINT16 | kW | Power |
| Number of supported flags | 400002 | UINT16 | - | Communication |
| Baud rate | 400003 | UINT32 | - | Communication |

## Addressing and setup

Addresses and values above are copied from the public JSON preview. Confirm the exact model, firmware, register function, address base, word order, scaling and units against the manufacturer manual before polling. No manufacturer manual revision or hardware validation is established by this page.

## Use with Modbus Monitor XPF

Check the device-map catalog in your installed XPF version for current map availability and licensing. The software download link does not open this map.

[Get Modbus Monitor XPF](https://docs.quantumbitsolutions.com/downloads-purchase/) · [Request a map or correction](https://github.com/Modbus-Monitor/modbus-device-maps/issues/new/choose) · [Browse all previews](https://docs.quantumbitsolutions.com/modbus-device-maps/)

<script type="application/ld+json">{"@context": "https://schema.org", "@type": "Dataset", "name": "Honeywell EEM230 public register preview", "description": "Sample register addresses and data types; not a complete map or hardware verification.", "url": "https://docs.quantumbitsolutions.com/modbus-device-maps/previews/honeywell/eem230/", "license": "https://modbus-monitor.github.io/modbus-device-maps/data-license/", "creator": {"@type": "Organization", "name": "Quantum Bit Solutions", "url": "https://quantumbitsolutions.com/"}, "distribution": {"@type": "DataDownload", "encodingFormat": "application/json", "contentUrl": "https://modbus-monitor.github.io/modbus-device-maps/maps/honeywell/eem230.json"}}</script>
