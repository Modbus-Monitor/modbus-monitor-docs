---
title: "Mikro DPM380 Modbus register preview"
description: "Sample register addresses and data types for Mikro DPM380. Public preview with JSON source and verification status."
---

# Mikro DPM380 Modbus register preview

Public preview for **Mikro DPM380** (Power Meter).
This sample is not a complete map or evidence of hardware testing.

## Preview details

- Catalog ID: `mikro/dpm380`
- Map version: 1.0
- Verification: not-reviewed
- Protocols: RTU, TCP
- Public preview: 12 registers. Complete in-app availability is not established by this preview.

[JSON preview](https://modbus-monitor.github.io/modbus-device-maps/maps/mikro/dpm380.json) · [Data terms](https://modbus-monitor.github.io/modbus-device-maps/data-license/)

## Register table (sample)

| Signal | Display address | Data type | Units | Category |
|---|---|---|---|---|
| Voltage phase L12 V | 404028 | UINT32 | V | Voltage |
| Instantaneous current L1 A | 404020 | UINT32 | A | Current |
| Total real power W | 404012 | INT32 | kW | Power |
| Negative real energy kWh | 404000 | UINT32 | kWh | Energy |
| Frequency Hz | 404019 | UINT32 | Hz | Frequency |
| Positive real energy kWh | 404002 | UINT32 | kWh | Energy |
| Apparent energy kVAh | 404006 | UINT32 | kWh | Energy |
| Negative reactive energy kVArh | 404008 | UINT32 | kWh | Energy |
| Positive reactive energy kVArh | 404010 | UINT32 | kWh | Energy |
| Total apparent power VA | 404014 | INT32 | kW | Power |
| Total reactive power VAR | 404016 | INT32 | kW | Power |
| Total power factor 1 | 404018 | UINT32 | PF | Power |

## Addressing and setup

Addresses and values above are copied from the public JSON preview. Confirm the exact model, firmware, register function, address base, word order, scaling and units against the manufacturer manual before polling. No manufacturer manual revision or hardware validation is established by this page.

## Use with Modbus Monitor XPF

Check the device-map catalog in your installed XPF version for current map availability and licensing. The software download link does not open this map.

[Get Modbus Monitor XPF](https://docs.quantumbitsolutions.com/downloads-purchase/) · [Request a map or correction](https://github.com/Modbus-Monitor/modbus-device-maps/issues/new/choose) · [Browse all previews](https://docs.quantumbitsolutions.com/modbus-device-maps/)

<script type="application/ld+json">{"@context": "https://schema.org", "@type": "Dataset", "name": "Mikro DPM380 public register preview", "description": "Sample register addresses and data types; not a complete map or hardware verification.", "url": "https://docs.quantumbitsolutions.com/modbus-device-maps/previews/mikro/dpm380/", "license": "https://modbus-monitor.github.io/modbus-device-maps/data-license/", "creator": {"@type": "Organization", "name": "Quantum Bit Solutions", "url": "https://quantumbitsolutions.com/"}, "distribution": {"@type": "DataDownload", "encodingFormat": "application/json", "contentUrl": "https://modbus-monitor.github.io/modbus-device-maps/maps/mikro/dpm380.json"}}</script>
