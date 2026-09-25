---
title: "Sungrow Inverter SG Modbus register preview"
description: "Sample register addresses and data types for Sungrow Inverter SG. Public preview with JSON source and verification status."
---

# Sungrow Inverter SG Modbus register preview

Public preview for **Sungrow Inverter SG** (Solar Inverter).
This sample is not a complete map or evidence of hardware testing.

## Preview details

- Catalog ID: `sungrow-inverter/sg`
- Map version: 1.0
- Verification: not-reviewed
- Protocols: RTU, TCP
- Public preview: 12 registers. Complete in-app availability is not established by this preview.

[JSON preview](https://modbus-monitor.github.io/modbus-device-maps/maps/sungrow-inverter/sg.json) · [Data terms](https://modbus-monitor.github.io/modbus-device-maps/data-license/)

## Register table (sample)

| Signal | Display address | Data type | Units | Category |
|---|---|---|---|---|
| DC voltage1 V | 305011 | UINT16 | V | Voltage |
| DC current1 A | 305012 | UINT16 | - | Current |
| Total power yields kW | 305004 | UINT32 | kW | Power |
| Grid frequency Hz | 305036 | UINT16 | Hz | Frequency |
| Work state | 305038 | UINT16 | - | Status |
| Internal temperature | 305008 | INT16 | degC | Temperature |
| Total running time | 305006 | UINT32 | - | General |
| DC voltage 2 V | 305013 | UINT16 | V | Voltage |
| DC current 2 A | 305014 | UINT16 | - | Current |
| DC voltage 3 V | 305015 | UINT16 | V | Voltage |
| DC current 3 A | 305016 | UINT16 | - | Current |
| Total DC power W | 305017 | UINT32 | kW | Power |

## Addressing and setup

Addresses and values above are copied from the public JSON preview. Confirm the exact model, firmware, register function, address base, word order, scaling and units against the manufacturer manual before polling. No manufacturer manual revision or hardware validation is established by this page.

## Use with Modbus Monitor XPF

Check the device-map catalog in your installed XPF version for current map availability and licensing. The software download link does not open this map.

[Get Modbus Monitor XPF](https://docs.quantumbitsolutions.com/downloads-purchase/) · [Request a map or correction](https://github.com/Modbus-Monitor/modbus-device-maps/issues/new/choose) · [Browse all previews](https://docs.quantumbitsolutions.com/modbus-device-maps/)

<script type="application/ld+json">{"@context": "https://schema.org", "@type": "Dataset", "name": "Sungrow Inverter SG public register preview", "description": "Sample register addresses and data types; not a complete map or hardware verification.", "url": "https://docs.quantumbitsolutions.com/modbus-device-maps/previews/sungrow-inverter/sg/", "license": "https://modbus-monitor.github.io/modbus-device-maps/data-license/", "creator": {"@type": "Organization", "name": "Quantum Bit Solutions", "url": "https://quantumbitsolutions.com/"}, "distribution": {"@type": "DataDownload", "encodingFormat": "application/json", "contentUrl": "https://modbus-monitor.github.io/modbus-device-maps/maps/sungrow-inverter/sg.json"}}</script>
