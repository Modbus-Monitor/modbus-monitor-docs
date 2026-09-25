---
title: "SmartProcess SMARTRAIL X835 Modbus register preview"
description: "Sample register addresses and data types for SmartProcess SMARTRAIL X835. Public preview with JSON source and verification status."
---

# SmartProcess SMARTRAIL X835 Modbus register preview

Public preview for **SmartProcess SMARTRAIL X835** (Power Meter).
This sample is not a complete map or evidence of hardware testing.

## Preview details

- Catalog ID: `smartprocess/smartrail-x835`
- Map version: 1.0
- Verification: not-reviewed
- Protocols: RTU, TCP
- Public preview: 12 registers. Complete in-app availability is not established by this preview.

[JSON preview](https://modbus-monitor.github.io/modbus-device-maps/maps/smartprocess/smartrail-x835.json) · [Data terms](https://modbus-monitor.github.io/modbus-device-maps/data-license/)

## Register table (sample)

| Signal | Display address | Data type | Units | Category |
|---|---|---|---|---|
| System current 00 | 400008 | UINT32 | - | Current |
| System power 00 | 400036 | UINT32 | kW | Power |
| Energy units prefix 00 | 400030 | UINT32 | kWh | Energy |
| Demand time 00 | 400000 | UINT32 | kW | Demand |
| System volts 00 | 400006 | UINT32 | - | General |
| Network baud rate 00 | 400028 | UINT32 | - | Communication |
| Serial number hi 00 | 400042 | UINT32 | - | Identification |
| Demand period 00 | 400002 | UINT32 | kW | Demand |
| Relayl energy type 00 | 400086 | UINT32 | kWh | Energy |
| Relay2 energy type 00 | 400088 | UINT32 | kWh | Energy |
| System type 00 | 400010 | UINT32 | - | General |
| Relay pulse width 00 | 400012 | UINT32 | - | General |

## Addressing and setup

Addresses and values above are copied from the public JSON preview. Confirm the exact model, firmware, register function, address base, word order, scaling and units against the manufacturer manual before polling. No manufacturer manual revision or hardware validation is established by this page.

## Use with Modbus Monitor XPF

Check the device-map catalog in your installed XPF version for current map availability and licensing. The software download link does not open this map.

[Get Modbus Monitor XPF](https://docs.quantumbitsolutions.com/downloads-purchase/) · [Request a map or correction](https://github.com/Modbus-Monitor/modbus-device-maps/issues/new/choose) · [Browse all previews](https://docs.quantumbitsolutions.com/modbus-device-maps/)

<script type="application/ld+json">{"@context": "https://schema.org", "@type": "Dataset", "name": "SmartProcess SMARTRAIL X835 public register preview", "description": "Sample register addresses and data types; not a complete map or hardware verification.", "url": "https://docs.quantumbitsolutions.com/modbus-device-maps/previews/smartprocess/smartrail-x835/", "license": "https://modbus-monitor.github.io/modbus-device-maps/data-license/", "creator": {"@type": "Organization", "name": "Quantum Bit Solutions", "url": "https://quantumbitsolutions.com/"}, "distribution": {"@type": "DataDownload", "encodingFormat": "application/json", "contentUrl": "https://modbus-monitor.github.io/modbus-device-maps/maps/smartprocess/smartrail-x835.json"}}</script>
