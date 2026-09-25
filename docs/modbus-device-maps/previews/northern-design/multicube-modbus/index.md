---
title: "Northern Design MultiCube Modbus Modbus register preview"
description: "Sample register addresses and data types for Northern Design MultiCube Modbus. Public preview with JSON source and verification status."
---

# Northern Design MultiCube Modbus Modbus register preview

Public preview for **Northern Design MultiCube Modbus** (Power Meter).
This sample is not a complete map or evidence of hardware testing.

## Preview details

- Catalog ID: `northern-design/multicube-modbus`
- Map version: 1.0
- Verification: not-reviewed
- Protocols: RTU, TCP
- Public preview: 12 registers. Complete in-app availability is not established by this preview.

[JSON preview](https://modbus-monitor.github.io/modbus-device-maps/maps/northern-design/multicube-modbus.json) · [Data terms](https://modbus-monitor.github.io/modbus-device-maps/data-license/)

## Register table (sample)

| Signal | Display address | Data type | Units | Category |
|---|---|---|---|---|
| Phase 1 amps Amps | 402822 | UINT16 | A | Current |
| kVAh kVAh | 400516 | UINT32 | - | Power |
| kWh kWh | 400514 | UINT32 | kWh | Energy |
| Frequency | 402820 | UINT16 | Hz | Frequency |
| System PF | 402819 | UINT16 | - | Power Factor |
| Peak ph1 volts demand Volts | 403843 | UINT16 | kW | Demand |
| V1 THD | 404352 | UINT16 | - | Harmonics |
| eScale | 400512 | UINT32 | - | General |
| Baud | 403588 | UINT16 | - | Communication |
| Meter model | 403590 | UINT16 | - | Identification |
| Kvarh inductive kvarh | 400518 | UINT32 | kWh | Energy |
| Kvarh capacitive kvarh | 400520 | UINT32 | kWh | Energy |

## Addressing and setup

Addresses and values above are copied from the public JSON preview. Confirm the exact model, firmware, register function, address base, word order, scaling and units against the manufacturer manual before polling. No manufacturer manual revision or hardware validation is established by this page.

## Use with Modbus Monitor XPF

Check the device-map catalog in your installed XPF version for current map availability and licensing. The software download link does not open this map.

[Get Modbus Monitor XPF](https://docs.quantumbitsolutions.com/downloads-purchase/) · [Request a map or correction](https://github.com/Modbus-Monitor/modbus-device-maps/issues/new/choose) · [Browse all previews](https://docs.quantumbitsolutions.com/modbus-device-maps/)

<script type="application/ld+json">{"@context": "https://schema.org", "@type": "Dataset", "name": "Northern Design MultiCube Modbus public register preview", "description": "Sample register addresses and data types; not a complete map or hardware verification.", "url": "https://docs.quantumbitsolutions.com/modbus-device-maps/previews/northern-design/multicube-modbus/", "license": "https://modbus-monitor.github.io/modbus-device-maps/data-license/", "creator": {"@type": "Organization", "name": "Quantum Bit Solutions", "url": "https://quantumbitsolutions.com/"}, "distribution": {"@type": "DataDownload", "encodingFormat": "application/json", "contentUrl": "https://modbus-monitor.github.io/modbus-device-maps/maps/northern-design/multicube-modbus.json"}}</script>
