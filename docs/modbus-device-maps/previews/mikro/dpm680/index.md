---
title: "Mikro DPM680 Modbus register preview"
description: "Sample register addresses and data types for Mikro DPM680. Public preview with JSON source and verification status."
---

# Mikro DPM680 Modbus register preview

Public preview for **Mikro DPM680** (Power Meter).
This sample is not a complete map or evidence of hardware testing.

## Preview details

- Catalog ID: `mikro/dpm680`
- Map version: 1.0
- Verification: not-reviewed
- Protocols: RTU, TCP
- Public preview: 12 registers. Complete in-app availability is not established by this preview.

[JSON preview](https://modbus-monitor.github.io/modbus-device-maps/maps/mikro/dpm680.json) · [Data terms](https://modbus-monitor.github.io/modbus-device-maps/data-license/)

## Register table (sample)

| Signal | Display address | Data type | Units | Category |
|---|---|---|---|---|
| Voltage line ab V | 404028 | UINT32 | V | Voltage |
| Instantaneous current A A | 404020 | UINT32 | - | Current |
| Total real power W | 404012 | INT32 | kW | Power |
| Real energy Wh | 404000 | INT64 | kWh | Energy |
| Frequency Hz | 404019 | UINT16 | Hz | Frequency |
| Device type sub x0000 | 400003 | UINT16 | - | General |
| Version number main x0000 0x0002 | 400004 | UINT16 | - | Identification |
| Baudrate selection 300 2600 31200 42400 54800 69600 719200 838400 | 401002 | UINT16 | - | Communication |
| Apparent energy VAh | 404004 | INT64 | kWh | Energy |
| Reactive energy VArh | 404008 | INT64 | kWh | Energy |
| Total apparent power VA | 404014 | INT32 | kW | Power |
| Total reactive power VAr | 404016 | INT32 | kW | Power |

## Addressing and setup

Addresses and values above are copied from the public JSON preview. Confirm the exact model, firmware, register function, address base, word order, scaling and units against the manufacturer manual before polling. No manufacturer manual revision or hardware validation is established by this page.

## Use with Modbus Monitor XPF

Check the device-map catalog in your installed XPF version for current map availability and licensing. The software download link does not open this map.

[Get Modbus Monitor XPF](https://docs.quantumbitsolutions.com/downloads-purchase/) · [Request a map or correction](https://github.com/Modbus-Monitor/modbus-device-maps/issues/new/choose) · [Browse all previews](https://docs.quantumbitsolutions.com/modbus-device-maps/)

<script type="application/ld+json">{"@context": "https://schema.org", "@type": "Dataset", "name": "Mikro DPM680 public register preview", "description": "Sample register addresses and data types; not a complete map or hardware verification.", "url": "https://docs.quantumbitsolutions.com/modbus-device-maps/previews/mikro/dpm680/", "license": "https://modbus-monitor.github.io/modbus-device-maps/data-license/", "creator": {"@type": "Organization", "name": "Quantum Bit Solutions", "url": "https://quantumbitsolutions.com/"}, "distribution": {"@type": "DataDownload", "encodingFormat": "application/json", "contentUrl": "https://modbus-monitor.github.io/modbus-device-maps/maps/mikro/dpm680.json"}}</script>
