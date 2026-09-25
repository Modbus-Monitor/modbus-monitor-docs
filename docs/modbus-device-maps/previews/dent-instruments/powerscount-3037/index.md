---
title: "Dent Instruments PowerScount 3037 Modbus register preview"
description: "Sample register addresses and data types for Dent Instruments PowerScount 3037. Public preview with JSON source and verification status."
---

# Dent Instruments PowerScount 3037 Modbus register preview

Public preview for **Dent Instruments PowerScount 3037** (Power Meter).
This sample is not a complete map or evidence of hardware testing.

## Preview details

- Catalog ID: `dent-instruments/powerscount-3037`
- Map version: 1.0
- Verification: not-reviewed
- Protocols: RTU, TCP
- Public preview: 12 registers. Complete in-app availability is not established by this preview.

[JSON preview](https://modbus-monitor.github.io/modbus-device-maps/maps/dent-instruments/powerscount-3037.json) · [Data terms](https://modbus-monitor.github.io/modbus-device-maps/data-license/)

## Register table (sample)

| Signal | Display address | Data type | Units | Category |
|---|---|---|---|---|
| Voltage line to line Volts | 404016 | UINT16 | V | Voltage |
| Phase currents L1 A | 404055 | UINT16 | - | Current |
| System total true power kW | 404002 | UINT16 | kW | Power |
| System total true energy kWh | 404000 | UINT32 | kWh | Energy |
| Line frequency Hz | 404021 | UINT16 | Hz | Frequency |
| System maximum demand | 404003 | UINT16 | kW | Demand |
| Average of all phases | 404015 | UINT16 | - | General |
| Average power kW | 404004 | UINT16 | kW | Power |
| System maximum instantaneous kW | 404005 | UINT16 | - | Power |
| System minimum instantaneous kW | 404006 | UINT16 | - | Power |
| System total reactive energy kVARh | 404007 | UINT32 | kWh | Energy |
| System total reactive power kVAR | 404009 | UINT16 | kW | Power |

## Addressing and setup

Addresses and values above are copied from the public JSON preview. Confirm the exact model, firmware, register function, address base, word order, scaling and units against the manufacturer manual before polling. No manufacturer manual revision or hardware validation is established by this page.

## Use with Modbus Monitor XPF

Check the device-map catalog in your installed XPF version for current map availability and licensing. The software download link does not open this map.

[Get Modbus Monitor XPF](https://docs.quantumbitsolutions.com/downloads-purchase/) · [Request a map or correction](https://github.com/Modbus-Monitor/modbus-device-maps/issues/new/choose) · [Browse all previews](https://docs.quantumbitsolutions.com/modbus-device-maps/)

<script type="application/ld+json">{"@context": "https://schema.org", "@type": "Dataset", "name": "Dent Instruments PowerScount 3037 public register preview", "description": "Sample register addresses and data types; not a complete map or hardware verification.", "url": "https://docs.quantumbitsolutions.com/modbus-device-maps/previews/dent-instruments/powerscount-3037/", "license": "https://modbus-monitor.github.io/modbus-device-maps/data-license/", "creator": {"@type": "Organization", "name": "Quantum Bit Solutions", "url": "https://quantumbitsolutions.com/"}, "distribution": {"@type": "DataDownload", "encodingFormat": "application/json", "contentUrl": "https://modbus-monitor.github.io/modbus-device-maps/maps/dent-instruments/powerscount-3037.json"}}</script>
