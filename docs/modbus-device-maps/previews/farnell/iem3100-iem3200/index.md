---
title: "Farnell iEM3100, iEM3200 Modbus register preview"
description: "Sample register addresses and data types for Farnell iEM3100, iEM3200. Public preview with JSON source and verification status."
---

# Farnell iEM3100, iEM3200 Modbus register preview

Public preview for **Farnell iEM3100, iEM3200** (Power Meter).
This sample is not a complete map or evidence of hardware testing.

## Preview details

- Catalog ID: `farnell/iem3100-iem3200`
- Map version: 1.0
- Verification: not-reviewed
- Protocols: RTU, TCP
- Public preview: 12 registers. Complete in-app availability is not established by this preview.

[JSON preview](https://modbus-monitor.github.io/modbus-device-maps/maps/farnell/iem3100-iem3200.json) · [Data terms](https://modbus-monitor.github.io/modbus-device-maps/data-license/)

## Register table (sample)

| Signal | Display address | Data type | Units | Category |
|---|---|---|---|---|
| Current Avg Voltage A | 403010 | FLOAT32 | V | Voltage |
| I1 phase 1 current A | 403000 | FLOAT32 | - | Current |
| Power System | 402016 | UINT16 | kW | Power |
| Energy Pulse Duration Millisecond | 402129 | UINT16 | kWh | Energy |
| Nominal Frequency Hz | 402017 | UINT16 | Hz | Frequency |
| Digital Output Control Mode Status | 409673 | UINT16 | - | Status |
| Serial Number | 400130 | UINT32 | - | Identification |
| Meter Operation Timer Secon | 402004 | UINT32 | - | General |
| Address | 406501 | UINT16 | - | Communication |
| Pulse Weight pulsekWh | 402132 | FLOAT32 | kWh | Energy |
| I2 phase 2 current A | 403002 | FLOAT32 | - | Current |
| I3 phase 3 current A | 403004 | FLOAT32 | - | Current |

## Addressing and setup

Addresses and values above are copied from the public JSON preview. Confirm the exact model, firmware, register function, address base, word order, scaling and units against the manufacturer manual before polling. No manufacturer manual revision or hardware validation is established by this page.

## Use with Modbus Monitor XPF

Check the device-map catalog in your installed XPF version for current map availability and licensing. The software download link does not open this map.

[Get Modbus Monitor XPF](https://docs.quantumbitsolutions.com/downloads-purchase/) · [Request a map or correction](https://github.com/Modbus-Monitor/modbus-device-maps/issues/new/choose) · [Browse all previews](https://docs.quantumbitsolutions.com/modbus-device-maps/)

<script type="application/ld+json">{"@context": "https://schema.org", "@type": "Dataset", "name": "Farnell iEM3100, iEM3200 public register preview", "description": "Sample register addresses and data types; not a complete map or hardware verification.", "url": "https://docs.quantumbitsolutions.com/modbus-device-maps/previews/farnell/iem3100-iem3200/", "license": "https://modbus-monitor.github.io/modbus-device-maps/data-license/", "creator": {"@type": "Organization", "name": "Quantum Bit Solutions", "url": "https://quantumbitsolutions.com/"}, "distribution": {"@type": "DataDownload", "encodingFormat": "application/json", "contentUrl": "https://modbus-monitor.github.io/modbus-device-maps/maps/farnell/iem3100-iem3200.json"}}</script>
