---
title: "PowerScout 3-8, ViewPoint Modbus register preview"
description: "Sample register addresses and data types for PowerScout 3-8, ViewPoint. Public preview with JSON source and verification status."
---

# PowerScout 3-8, ViewPoint Modbus register preview

Public preview for **PowerScout 3-8, ViewPoint** (Power Meter).
This sample is not a complete map or evidence of hardware testing.

## Preview details

- Catalog ID: `powerscout/3-8-viewpoint`
- Map version: 1.0
- Verification: not-reviewed
- Protocols: RTU, TCP
- Public preview: 12 registers. Complete in-app availability is not established by this preview.

[JSON preview](https://modbus-monitor.github.io/modbus-device-maps/maps/powerscout/3-8-viewpoint.json) · [Data terms](https://modbus-monitor.github.io/modbus-device-maps/data-license/)

## Register table (sample)

| Signal | Display address | Data type | Units | Category |
|---|---|---|---|---|
| Volts Line to Line Avg Volts | 404016 | UINT16 | - | Voltage |
| Amps System Avg Amps | 404015 | UINT16 | A | Current |
| kW System kW | 404002 | UINT16 | - | Power |
| kWh System LSW kWh | 404000 | UINT16 | kWh | Energy |
| Line Frequency Hz | 404021 | UINT16 | Hz | Frequency |
| Displacement PF System | 404013 | UINT16 | - | Power Factor |
| Demand Window Size | 404302 | UINT16 | kW | Demand |
| Volts L1 to L2 Volts | 404018 | UINT16 | - | General |
| kWh System MSW kWh | 404001 | UINT16 | kWh | Energy |
| kW Demand System Max kW | 404003 | UINT16 | kW | Power |
| kW Demand System Now kW | 404004 | UINT16 | kW | Power |
| kW System Max kW | 404005 | UINT16 | - | Power |

## Addressing and setup

Addresses and values above are copied from the public JSON preview. Confirm the exact model, firmware, register function, address base, word order, scaling and units against the manufacturer manual before polling. No manufacturer manual revision or hardware validation is established by this page.

## Use with Modbus Monitor XPF

Check the device-map catalog in your installed XPF version for current map availability and licensing. The software download link does not open this map.

[Get Modbus Monitor XPF](https://docs.quantumbitsolutions.com/downloads-purchase/) · [Request a map or correction](https://github.com/Modbus-Monitor/modbus-device-maps/issues/new/choose) · [Browse all previews](https://docs.quantumbitsolutions.com/modbus-device-maps/)

<script type="application/ld+json">{"@context": "https://schema.org", "@type": "Dataset", "name": "PowerScout 3-8, ViewPoint public register preview", "description": "Sample register addresses and data types; not a complete map or hardware verification.", "url": "https://docs.quantumbitsolutions.com/modbus-device-maps/previews/powerscout/3-8-viewpoint/", "license": "https://modbus-monitor.github.io/modbus-device-maps/data-license/", "creator": {"@type": "Organization", "name": "Quantum Bit Solutions", "url": "https://quantumbitsolutions.com/"}, "distribution": {"@type": "DataDownload", "encodingFormat": "application/json", "contentUrl": "https://modbus-monitor.github.io/modbus-device-maps/maps/powerscout/3-8-viewpoint.json"}}</script>
