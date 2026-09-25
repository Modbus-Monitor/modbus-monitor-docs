---
title: "Frako EMA1496 Modbus register preview"
description: "Sample register addresses and data types for Frako EMA1496. Public preview with JSON source and verification status."
---

# Frako EMA1496 Modbus register preview

Public preview for **Frako EMA1496** (Power Meter).
This sample is not a complete map or evidence of hardware testing.

## Preview details

- Catalog ID: `frako/ema1496`
- Map version: 1.0
- Verification: not-reviewed
- Protocols: RTU, TCP
- Public preview: 12 registers. Complete in-app availability is not established by this preview.

[JSON preview](https://modbus-monitor.github.io/modbus-device-maps/maps/frako/ema1496.json) · [Data terms](https://modbus-monitor.github.io/modbus-device-maps/data-license/)

## Register table (sample)

| Signal | Display address | Data type | Units | Category |
|---|---|---|---|---|
| Phase 1 line to neutral volts Volts | 300000 | FLOAT32 | - | Voltage |
| Phase 1 current Amps | 300006 | FLOAT32 | A | Current |
| Phase 1 power Watts | 300012 | FLOAT32 | kW | Power |
| Total system va demand VA | 300100 | FLOAT32 | kW | Demand |
| Phase 1 ln volts thd | 300234 | FLOAT32 | - | Harmonics |
| Phase 1 phase angle Degrees | 300036 | FLOAT32 | - | General |
| Phase 2 line to neutral volts Volts | 300002 | FLOAT32 | - | Voltage |
| Phase 3 line to neutral volts Volts | 300004 | FLOAT32 | - | Voltage |
| Phase 2 current Amps | 300008 | FLOAT32 | A | Current |
| Phase 3 current Amps | 300010 | FLOAT32 | A | Current |
| Phase 2 power Watts | 300014 | FLOAT32 | kW | Power |
| Phase 3 power Watts | 300016 | FLOAT32 | kW | Power |

## Addressing and setup

Addresses and values above are copied from the public JSON preview. Confirm the exact model, firmware, register function, address base, word order, scaling and units against the manufacturer manual before polling. No manufacturer manual revision or hardware validation is established by this page.

## Use with Modbus Monitor XPF

Check the device-map catalog in your installed XPF version for current map availability and licensing. The software download link does not open this map.

[Get Modbus Monitor XPF](https://docs.quantumbitsolutions.com/downloads-purchase/) · [Request a map or correction](https://github.com/Modbus-Monitor/modbus-device-maps/issues/new/choose) · [Browse all previews](https://docs.quantumbitsolutions.com/modbus-device-maps/)

<script type="application/ld+json">{"@context": "https://schema.org", "@type": "Dataset", "name": "Frako EMA1496 public register preview", "description": "Sample register addresses and data types; not a complete map or hardware verification.", "url": "https://docs.quantumbitsolutions.com/modbus-device-maps/previews/frako/ema1496/", "license": "https://modbus-monitor.github.io/modbus-device-maps/data-license/", "creator": {"@type": "Organization", "name": "Quantum Bit Solutions", "url": "https://quantumbitsolutions.com/"}, "distribution": {"@type": "DataDownload", "encodingFormat": "application/json", "contentUrl": "https://modbus-monitor.github.io/modbus-device-maps/maps/frako/ema1496.json"}}</script>
