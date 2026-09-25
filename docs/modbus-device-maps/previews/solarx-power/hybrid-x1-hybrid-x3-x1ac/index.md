---
title: "SolarX Power Hybrid X1,Hybrid X3,X1AC Modbus register preview"
description: "Sample register addresses and data types for SolarX Power Hybrid X1,Hybrid X3,X1AC. Public preview with JSON source and verification status."
---

# SolarX Power Hybrid X1,Hybrid X3,X1AC Modbus register preview

Public preview for **SolarX Power Hybrid X1,Hybrid X3,X1AC** (Solar Inverter).
This sample is not a complete map or evidence of hardware testing.

## Preview details

- Catalog ID: `solarx-power/hybrid-x1-hybrid-x3-x1ac`
- Map version: 1.0
- Verification: not-reviewed
- Protocols: RTU, TCP
- Public preview: 12 registers. Complete in-app availability is not established by this preview.

[JSON preview](https://modbus-monitor.github.io/modbus-device-maps/maps/solarx-power/hybrid-x1-hybrid-x3-x1ac.json) · [Data terms](https://modbus-monitor.github.io/modbus-device-maps/data-license/)

## Register table (sample)

| Signal | Display address | Data type | Units | Category |
|---|---|---|---|---|
| Pv voltage1 Hybrid V | 300003 | UINT16 | V | Voltage |
| Grid current X1 V | 300001 | INT16 | - | Current |
| Grid power X1 W | 300002 | INT16 | kW | Power |
| Output energy ChargeLSB KWh | 300029 | UINT16 | kWh | Energy |
| Grid frequency X1 Hz | 300007 | UINT16 | Hz | Frequency |
| BMS connect state | 300023 | UINT16 | - | Status |
| Temperature | 300008 | INT16 | degC | Temperature |
| Run mode | 300009 | UINT16 | - | General |
| Pv voltage2 Hybrid V | 300004 | UINT16 | V | Voltage |
| Pv current1 Hybrid A | 300005 | UINT16 | - | Current |
| Pv current2 Hybrid A | 300006 | UINT16 | - | Current |
| Powerdc1 Hybrid W | 300010 | UINT16 | kW | Power |

## Addressing and setup

Addresses and values above are copied from the public JSON preview. Confirm the exact model, firmware, register function, address base, word order, scaling and units against the manufacturer manual before polling. No manufacturer manual revision or hardware validation is established by this page.

## Use with Modbus Monitor XPF

Check the device-map catalog in your installed XPF version for current map availability and licensing. The software download link does not open this map.

[Get Modbus Monitor XPF](https://docs.quantumbitsolutions.com/downloads-purchase/) · [Request a map or correction](https://github.com/Modbus-Monitor/modbus-device-maps/issues/new/choose) · [Browse all previews](https://docs.quantumbitsolutions.com/modbus-device-maps/)

<script type="application/ld+json">{"@context": "https://schema.org", "@type": "Dataset", "name": "SolarX Power Hybrid X1,Hybrid X3,X1AC public register preview", "description": "Sample register addresses and data types; not a complete map or hardware verification.", "url": "https://docs.quantumbitsolutions.com/modbus-device-maps/previews/solarx-power/hybrid-x1-hybrid-x3-x1ac/", "license": "https://modbus-monitor.github.io/modbus-device-maps/data-license/", "creator": {"@type": "Organization", "name": "Quantum Bit Solutions", "url": "https://quantumbitsolutions.com/"}, "distribution": {"@type": "DataDownload", "encodingFormat": "application/json", "contentUrl": "https://modbus-monitor.github.io/modbus-device-maps/maps/solarx-power/hybrid-x1-hybrid-x3-x1ac.json"}}</script>
