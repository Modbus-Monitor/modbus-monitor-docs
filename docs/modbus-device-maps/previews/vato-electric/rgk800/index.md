---
title: "vato Electric RGK800 Modbus register preview"
description: "Sample register addresses and data types for vato Electric RGK800. Public preview with JSON source and verification status."
---

# vato Electric RGK800 Modbus register preview

Public preview for **vato Electric RGK800** (Power Meter).
This sample is not a complete map or evidence of hardware testing.

## Preview details

- Catalog ID: `vato-electric/rgk800`
- Map version: 1.0
- Verification: not-reviewed
- Protocols: RTU, TCP
- Public preview: 12 registers. Complete in-app availability is not established by this preview.

[JSON preview](https://modbus-monitor.github.io/modbus-device-maps/maps/vato-electric/rgk800.json) · [Data terms](https://modbus-monitor.github.io/modbus-device-maps/data-license/)

## Register table (sample)

| Signal | Display address | Data type | Units | Category |
|---|---|---|---|---|
| L1 phase voltage - mains V | 400002 | UINT32 | V | Voltage |
| L1 current A | 400014 | UINT32 | - | Current |
| L1 active power - mains W | 400034 | INT32 | kW | Power |
| Total imp active energy - mains kWh | 406688 | UINT32 | kWh | Energy |
| Frequency - mains Hz | 400086 | UINT32 | Hz | Frequency |
| Temperature DC | 404000 | UINT32 | degC | Temperature |
| Engine speed Rpm | 400142 | UINT32 | - | General |
| Modbus function 17 clone | 403992 | UINT32 | - | Communication |
| L2 phase voltage - mains V | 400004 | UINT32 | V | Voltage |
| L3 phase voltage - mains V | 400006 | UINT32 | V | Voltage |
| L1 phase voltage - generator V | 400008 | UINT32 | V | Voltage |
| L2 phase voltage - generator V | 400010 | UINT32 | V | Voltage |

## Addressing and setup

Addresses and values above are copied from the public JSON preview. Confirm the exact model, firmware, register function, address base, word order, scaling and units against the manufacturer manual before polling. No manufacturer manual revision or hardware validation is established by this page.

## Use with Modbus Monitor XPF

Check the device-map catalog in your installed XPF version for current map availability and licensing. The software download link does not open this map.

[Get Modbus Monitor XPF](https://docs.quantumbitsolutions.com/downloads-purchase/) · [Request a map or correction](https://github.com/Modbus-Monitor/modbus-device-maps/issues/new/choose) · [Browse all previews](https://docs.quantumbitsolutions.com/modbus-device-maps/)

<script type="application/ld+json">{"@context": "https://schema.org", "@type": "Dataset", "name": "vato Electric RGK800 public register preview", "description": "Sample register addresses and data types; not a complete map or hardware verification.", "url": "https://docs.quantumbitsolutions.com/modbus-device-maps/previews/vato-electric/rgk800/", "license": "https://modbus-monitor.github.io/modbus-device-maps/data-license/", "creator": {"@type": "Organization", "name": "Quantum Bit Solutions", "url": "https://quantumbitsolutions.com/"}, "distribution": {"@type": "DataDownload", "encodingFormat": "application/json", "contentUrl": "https://modbus-monitor.github.io/modbus-device-maps/maps/vato-electric/rgk800.json"}}</script>
