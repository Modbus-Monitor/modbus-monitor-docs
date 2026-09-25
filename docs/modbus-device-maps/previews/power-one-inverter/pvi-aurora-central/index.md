---
title: "Power One Inverter PVI,Aurora Central Modbus register preview"
description: "Sample register addresses and data types for Power One Inverter PVI,Aurora Central. Public preview with JSON source and verification status."
---

# Power One Inverter PVI,Aurora Central Modbus register preview

Public preview for **Power One Inverter PVI,Aurora Central** (Solar Inverter).
This sample is not a complete map or evidence of hardware testing.

## Preview details

- Catalog ID: `power-one-inverter/pvi-aurora-central`
- Map version: 1.0
- Verification: not-reviewed
- Protocols: RTU, TCP
- Public preview: 12 registers. Complete in-app availability is not established by this preview.

[JSON preview](https://modbus-monitor.github.io/modbus-device-maps/maps/power-one-inverter/pvi-aurora-central.json) · [Data terms](https://modbus-monitor.github.io/modbus-device-maps/data-license/)

## Register table (sample)

| Signal | Display address | Data type | Units | Category |
|---|---|---|---|---|
| 3 phases grid voltage module 01 Slave Volt Rms | 400148 | FLOAT32 | V | Voltage |
| 3 phases grid current module 01 Slave Ampere Rms | 400150 | FLOAT32 | A | Current |
| 3 phases grid power module 01 Slave KWatt | 400152 | FLOAT32 | kW | Power |
| Collection daily energy of all modules KWattHour | 403700 | FLOAT32 | kWh | Energy |
| 3 phases frequence module 01 Slave Hz | 400154 | FLOAT32 | - | Frequency |
| Status0 module 01 Global state | 400131 | INT16 | - | Status |
| Supervisor temperature module 01 Celsius Degree | 400162 | FLOAT32 | degC | Temperature |
| Modbus interface type | 403650 | INT16 | - | Communication |
| PN5 module 01 | 400129 | INT16 | - | General |
| Collection total energy of all modules KWattHour | 403702 | FLOAT32 | kWh | Energy |
| Collection partial energy of all modules KWattHour | 403704 | FLOAT32 | kWh | Energy |
| Collection week energy of all modules KWattHour | 403706 | FLOAT32 | kWh | Energy |

## Addressing and setup

Addresses and values above are copied from the public JSON preview. Confirm the exact model, firmware, register function, address base, word order, scaling and units against the manufacturer manual before polling. No manufacturer manual revision or hardware validation is established by this page.

## Use with Modbus Monitor XPF

Check the device-map catalog in your installed XPF version for current map availability and licensing. The software download link does not open this map.

[Get Modbus Monitor XPF](https://docs.quantumbitsolutions.com/downloads-purchase/) · [Request a map or correction](https://github.com/Modbus-Monitor/modbus-device-maps/issues/new/choose) · [Browse all previews](https://docs.quantumbitsolutions.com/modbus-device-maps/)

<script type="application/ld+json">{"@context": "https://schema.org", "@type": "Dataset", "name": "Power One Inverter PVI,Aurora Central public register preview", "description": "Sample register addresses and data types; not a complete map or hardware verification.", "url": "https://docs.quantumbitsolutions.com/modbus-device-maps/previews/power-one-inverter/pvi-aurora-central/", "license": "https://modbus-monitor.github.io/modbus-device-maps/data-license/", "creator": {"@type": "Organization", "name": "Quantum Bit Solutions", "url": "https://quantumbitsolutions.com/"}, "distribution": {"@type": "DataDownload", "encodingFormat": "application/json", "contentUrl": "https://modbus-monitor.github.io/modbus-device-maps/maps/power-one-inverter/pvi-aurora-central.json"}}</script>
