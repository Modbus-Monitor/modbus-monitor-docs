---
title: "Epsolar LS-B Se ries Modbus register preview"
description: "Sample register addresses and data types for Epsolar LS-B Se ries. Public preview with JSON source and verification status."
---

# Epsolar LS-B Se ries Modbus register preview

Public preview for **Epsolar LS-B Se ries** (Solar Inverter).
This sample is not a complete map or evidence of hardware testing.

## Preview details

- Catalog ID: `epsolar/ls-b-se-ries`
- Map version: 1.0
- Verification: not-reviewed
- Protocols: RTU, TCP
- Public preview: 12 registers. Complete in-app availability is not established by this preview.

[JSON preview](https://modbus-monitor.github.io/modbus-device-maps/maps/epsolar/ls-b-se-ries.json) · [Data terms](https://modbus-monitor.github.io/modbus-device-maps/data-license/)

## Register table (sample)

| Signal | Display address | Data type | Units | Category |
|---|---|---|---|---|
| Charging equipment rated input voltage | 312288 | UINT16 | V | Voltage |
| Charging equipment rated input current A | 312289 | UINT16 | - | Current |
| Charging equipment rated input power | 312290 | UINT32 | kW | Power |
| Consumed energy today KWH | 313060 | UINT32 | kWh | Energy |
| Battery temperature degree Celsius | 312560 | UINT16 | degC | Temperature |
| Charging mode | 312296 | UINT16 | - | General |
| Charging equipment rated output voltage V | 312292 | UINT16 | V | Voltage |
| Charging equipment rated output current A | 312293 | UINT16 | - | Current |
| Charging equipment rated output power | 312294 | UINT16 | kW | Power |
| Charging equipment rated output power | 312295 | UINT16 | kW | Power |
| Rated output current of load A | 312302 | UINT16 | - | Current |
| Charging equipment input voltage V | 312544 | UINT16 | V | Voltage |

## Addressing and setup

Addresses and values above are copied from the public JSON preview. Confirm the exact model, firmware, register function, address base, word order, scaling and units against the manufacturer manual before polling. No manufacturer manual revision or hardware validation is established by this page.

## Use with Modbus Monitor XPF

Check the device-map catalog in your installed XPF version for current map availability and licensing. The software download link does not open this map.

[Get Modbus Monitor XPF](https://docs.quantumbitsolutions.com/downloads-purchase/) · [Request a map or correction](https://github.com/Modbus-Monitor/modbus-device-maps/issues/new/choose) · [Browse all previews](https://docs.quantumbitsolutions.com/modbus-device-maps/)

<script type="application/ld+json">{"@context": "https://schema.org", "@type": "Dataset", "name": "Epsolar LS-B Se ries public register preview", "description": "Sample register addresses and data types; not a complete map or hardware verification.", "url": "https://docs.quantumbitsolutions.com/modbus-device-maps/previews/epsolar/ls-b-se-ries/", "license": "https://modbus-monitor.github.io/modbus-device-maps/data-license/", "creator": {"@type": "Organization", "name": "Quantum Bit Solutions", "url": "https://quantumbitsolutions.com/"}, "distribution": {"@type": "DataDownload", "encodingFormat": "application/json", "contentUrl": "https://modbus-monitor.github.io/modbus-device-maps/maps/epsolar/ls-b-se-ries.json"}}</script>
