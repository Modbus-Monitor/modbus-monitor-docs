---
title: "Northern Design Cube 350, Cube 400, Rail 350, Modbus Modbus register preview"
description: "Sample register addresses and data types for Northern Design Cube 350, Cube 400, Rail 350, Modbus. Public preview with JSON source and verification status."
---

# Northern Design Cube 350, Cube 400, Rail 350, Modbus Modbus register preview

Public preview for **Northern Design Cube 350, Cube 400, Rail 350, Modbus** (Power Meter).
This sample is not a complete map or evidence of hardware testing.

## Preview details

- Catalog ID: `northern-design/cube-350-cube-400-rail-350-modbus`
- Map version: 1.0
- Verification: not-reviewed
- Protocols: RTU, TCP
- Public preview: 12 registers. Complete in-app availability is not established by this preview.

[JSON preview](https://modbus-monitor.github.io/modbus-device-maps/maps/northern-design/cube-350-cube-400-rail-350-modbus.json) · [Data terms](https://modbus-monitor.github.io/modbus-device-maps/data-license/)

## Register table (sample)

| Signal | Display address | Data type | Units | Category |
|---|---|---|---|---|
| Phase 1 amps cube 350 only Amps | 402822 | UINT16 | A | Current |
| kVAh cube 350 only kVAh | 400516 | UINT32 | - | Power |
| Energy scaling cube 350 only eScale | 400512 | UINT32 | kWh | Energy |
| Frequency cube 350 only | 402820 | UINT16 | Hz | Frequency |
| System PF cube 350 only | 402819 | UINT16 | - | Power Factor |
| Peak ph1 volts demand cube 350 only Volts | 403843 | UINT16 | kW | Demand |
| Combined contact status | 406912 | UINT16 | - | Status |
| V1 THD cube 350 only | 404352 | UINT16 | - | Harmonics |
| Hours run cube 350 only | 400528 | UINT32 | - | General |
| Baud cube 350 only | 403588 | UINT16 | - | Communication |
| Meter model cube cube 350 only | 403590 | UINT16 | - | Identification |
| kWh cube 350 only kWh | 400514 | UINT32 | kWh | Energy |

## Addressing and setup

Addresses and values above are copied from the public JSON preview. Confirm the exact model, firmware, register function, address base, word order, scaling and units against the manufacturer manual before polling. No manufacturer manual revision or hardware validation is established by this page.

## Use with Modbus Monitor XPF

Check the device-map catalog in your installed XPF version for current map availability and licensing. The software download link does not open this map.

[Get Modbus Monitor XPF](https://docs.quantumbitsolutions.com/downloads-purchase/) · [Request a map or correction](https://github.com/Modbus-Monitor/modbus-device-maps/issues/new/choose) · [Browse all previews](https://docs.quantumbitsolutions.com/modbus-device-maps/)

<script type="application/ld+json">{"@context": "https://schema.org", "@type": "Dataset", "name": "Northern Design Cube 350, Cube 400, Rail 350, Modbus public register preview", "description": "Sample register addresses and data types; not a complete map or hardware verification.", "url": "https://docs.quantumbitsolutions.com/modbus-device-maps/previews/northern-design/cube-350-cube-400-rail-350-modbus/", "license": "https://modbus-monitor.github.io/modbus-device-maps/data-license/", "creator": {"@type": "Organization", "name": "Quantum Bit Solutions", "url": "https://quantumbitsolutions.com/"}, "distribution": {"@type": "DataDownload", "encodingFormat": "application/json", "contentUrl": "https://modbus-monitor.github.io/modbus-device-maps/maps/northern-design/cube-350-cube-400-rail-350-modbus.json"}}</script>
