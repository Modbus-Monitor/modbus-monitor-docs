---
title: "Chint Instrument DDSU666-H Modbus register preview"
description: "Sample register addresses and data types for Chint Instrument DDSU666-H. Public preview with JSON source and verification status."
---

# Chint Instrument DDSU666-H Modbus register preview

Public preview for **Chint Instrument DDSU666-H** (Power Meter).
This sample is not a complete map or evidence of hardware testing.

## Preview details

- Catalog ID: `chint-instrument/ddsu666-h`
- Map version: 1.0
- Verification: not-reviewed
- Protocols: RTU, TCP
- Public preview: 12 registers. Complete in-app availability is not established by this preview.

[JSON preview](https://modbus-monitor.github.io/modbus-device-maps/maps/chint-instrument/ddsu666-h.json) · [Data terms](https://modbus-monitor.github.io/modbus-device-maps/data-license/)

## Register table (sample)

| Signal | Display address | Data type | Units | Category |
|---|---|---|---|---|
| PVn voltage V | 302016 | INT16 | V | Voltage |
| Current time s | 310000 | UINT32 | - | Current |
| Rated power kW | 300073 | UINT32 | kW | Power |
| Accumulated energy yield kWh | 302106 | UINT32 | kWh | Energy |
| Grid frequency Hz | 302085 | UINT16 | Hz | Frequency |
| Active grid PF | 307117 | INT16 | - | Power Factor |
| Status 1 | 302000 | UINT16 | - | Status |
| Internal temperature DC | 302087 | INT16 | degC | Temperature |
| Serial number | 300015 | STRING | - | Identification |
| Number of strings | 300071 | UINT16 | - | General |
| Maximum active power kW | 300075 | UINT32 | kW | Power |
| Maximum apparent power kVA | 300077 | UINT32 | kW | Power |

## Addressing and setup

Addresses and values above are copied from the public JSON preview. Confirm the exact model, firmware, register function, address base, word order, scaling and units against the manufacturer manual before polling. No manufacturer manual revision or hardware validation is established by this page.

## Use with Modbus Monitor XPF

Check the device-map catalog in your installed XPF version for current map availability and licensing. The software download link does not open this map.

[Get Modbus Monitor XPF](https://docs.quantumbitsolutions.com/downloads-purchase/) · [Request a map or correction](https://github.com/Modbus-Monitor/modbus-device-maps/issues/new/choose) · [Browse all previews](https://docs.quantumbitsolutions.com/modbus-device-maps/)

<script type="application/ld+json">{"@context": "https://schema.org", "@type": "Dataset", "name": "Chint Instrument DDSU666-H public register preview", "description": "Sample register addresses and data types; not a complete map or hardware verification.", "url": "https://docs.quantumbitsolutions.com/modbus-device-maps/previews/chint-instrument/ddsu666-h/", "license": "https://modbus-monitor.github.io/modbus-device-maps/data-license/", "creator": {"@type": "Organization", "name": "Quantum Bit Solutions", "url": "https://quantumbitsolutions.com/"}, "distribution": {"@type": "DataDownload", "encodingFormat": "application/json", "contentUrl": "https://modbus-monitor.github.io/modbus-device-maps/maps/chint-instrument/ddsu666-h.json"}}</script>
