---
title: "Veris H8035,H8036 Modbus register preview"
description: "Sample register addresses and data types for Veris H8035,H8036. Public preview with JSON source and verification status."
---

# Veris H8035,H8036 Modbus register preview

Public preview for **Veris H8035,H8036** (Power Meter).
This sample is not a complete map or evidence of hardware testing.

## Preview details

- Catalog ID: `veris/h8035-h8036`
- Map version: 1.0
- Verification: not-reviewed
- Protocols: RTU, TCP
- Public preview: 12 registers. Complete in-app availability is not established by this preview.

[JSON preview](https://modbus-monitor.github.io/modbus-device-maps/maps/veris/h8035-h8036.json) · [Data terms](https://modbus-monitor.github.io/modbus-device-maps/data-license/)

## Register table (sample)

| Signal | Display address | Data type | Units | Category |
|---|---|---|---|---|
| Voltage line to line VOLTS | 400268 | FLOAT32 | V | Voltage |
| Current AMPS | 400272 | FLOAT32 | A | Current |
| Real power KW | 400260 | FLOAT32 | kW | Power |
| Energy consumption KWH | 400256 | FLOAT32 | kWh | Energy |
| Yoltage phase A N VOLTS | 400292 | FLOAT32 | - | General |
| Energy onsumption same 40257 KWH | 400258 | FLOAT32 | kWh | Energy |
| Reactive power VAR | 400262 | FLOAT32 | kW | Power |
| Apparent power YA | 400264 | FLOAT32 | kW | Power |
| Power fator | 400266 | FLOAT32 | kW | Power |
| Voltage line to neutral VOLTS | 400270 | FLOAT32 | V | Voltage |
| Real power phase A KW | 400274 | FLOAT32 | kW | Power |
| Real power phase B KW | 400276 | FLOAT32 | kW | Power |

## Addressing and setup

Addresses and values above are copied from the public JSON preview. Confirm the exact model, firmware, register function, address base, word order, scaling and units against the manufacturer manual before polling. No manufacturer manual revision or hardware validation is established by this page.

## Use with Modbus Monitor XPF

Check the device-map catalog in your installed XPF version for current map availability and licensing. The software download link does not open this map.

[Get Modbus Monitor XPF](https://docs.quantumbitsolutions.com/downloads-purchase/) · [Request a map or correction](https://github.com/Modbus-Monitor/modbus-device-maps/issues/new/choose) · [Browse all previews](https://docs.quantumbitsolutions.com/modbus-device-maps/)

<script type="application/ld+json">{"@context": "https://schema.org", "@type": "Dataset", "name": "Veris H8035,H8036 public register preview", "description": "Sample register addresses and data types; not a complete map or hardware verification.", "url": "https://docs.quantumbitsolutions.com/modbus-device-maps/previews/veris/h8035-h8036/", "license": "https://modbus-monitor.github.io/modbus-device-maps/data-license/", "creator": {"@type": "Organization", "name": "Quantum Bit Solutions", "url": "https://quantumbitsolutions.com/"}, "distribution": {"@type": "DataDownload", "encodingFormat": "application/json", "contentUrl": "https://modbus-monitor.github.io/modbus-device-maps/maps/veris/h8035-h8036.json"}}</script>
