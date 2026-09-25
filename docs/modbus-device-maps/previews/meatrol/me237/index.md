---
title: "Meatrol ME237 Modbus register preview"
description: "Sample register addresses and data types for Meatrol ME237. Public preview with JSON source and verification status."
---

# Meatrol ME237 Modbus register preview

Public preview for **Meatrol ME237** (Power Meter).
This sample is not a complete map or evidence of hardware testing.

## Preview details

- Catalog ID: `meatrol/me237`
- Map version: 1.0
- Verification: not-reviewed
- Protocols: RTU, TCP
- Public preview: 12 registers. Complete in-app availability is not established by this preview.

[JSON preview](https://modbus-monitor.github.io/modbus-device-maps/maps/meatrol/me237.json) · [Data terms](https://modbus-monitor.github.io/modbus-device-maps/data-license/)

## Register table (sample)

| Signal | Display address | Data type | Units | Category |
|---|---|---|---|---|
| Voltage value of phase A V | 401000 | FLOAT32 | V | Voltage |
| Current value of phase A A | 401016 | FLOAT32 | - | Current |
| Active power of phase A W | 401026 | FLOAT32 | kW | Power |
| Positive active energy of phase A 01kWh | 404000 | UINT32 | kWh | Energy |
| Grid frequency Hz | 401066 | FLOAT32 | Hz | Frequency |
| Calculation method of demand 0 sliding 1 fixed | 405000 | UINT16 | kW | Demand |
| Maximum value of phase B reactive powe Var | 406082 | FLOAT32 | - | General |
| Voltage value of phase B V | 401002 | FLOAT32 | V | Voltage |
| Voltage value of phase C V | 401004 | FLOAT32 | V | Voltage |
| Average phase voltage value V | 401006 | FLOAT32 | V | Voltage |
| Voltage value of line A-B V | 401008 | FLOAT32 | V | Voltage |
| Voltage value of line B-C V | 401010 | FLOAT32 | V | Voltage |

## Addressing and setup

Addresses and values above are copied from the public JSON preview. Confirm the exact model, firmware, register function, address base, word order, scaling and units against the manufacturer manual before polling. No manufacturer manual revision or hardware validation is established by this page.

## Use with Modbus Monitor XPF

Check the device-map catalog in your installed XPF version for current map availability and licensing. The software download link does not open this map.

[Get Modbus Monitor XPF](https://docs.quantumbitsolutions.com/downloads-purchase/) · [Request a map or correction](https://github.com/Modbus-Monitor/modbus-device-maps/issues/new/choose) · [Browse all previews](https://docs.quantumbitsolutions.com/modbus-device-maps/)

<script type="application/ld+json">{"@context": "https://schema.org", "@type": "Dataset", "name": "Meatrol ME237 public register preview", "description": "Sample register addresses and data types; not a complete map or hardware verification.", "url": "https://docs.quantumbitsolutions.com/modbus-device-maps/previews/meatrol/me237/", "license": "https://modbus-monitor.github.io/modbus-device-maps/data-license/", "creator": {"@type": "Organization", "name": "Quantum Bit Solutions", "url": "https://quantumbitsolutions.com/"}, "distribution": {"@type": "DataDownload", "encodingFormat": "application/json", "contentUrl": "https://modbus-monitor.github.io/modbus-device-maps/maps/meatrol/me237.json"}}</script>
