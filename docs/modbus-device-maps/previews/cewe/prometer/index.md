---
title: "Cewe Prometer Modbus register preview"
description: "Sample register addresses and data types for Cewe Prometer. Public preview with JSON source and verification status."
---

# Cewe Prometer Modbus register preview

Public preview for **Cewe Prometer** (Power Meter).
This sample is not a complete map or evidence of hardware testing.

## Preview details

- Catalog ID: `cewe/prometer`
- Map version: 1.0
- Verification: not-reviewed
- Protocols: RTU, TCP
- Public preview: 12 registers. Complete in-app availability is not established by this preview.

[JSON preview](https://modbus-monitor.github.io/modbus-device-maps/maps/cewe/prometer.json) · [Data terms](https://modbus-monitor.github.io/modbus-device-maps/data-license/)

## Register table (sample)

| Signal | Display address | Data type | Units | Category |
|---|---|---|---|---|
| Phase voltage L1 1 volts | 400000 | FLOAT32 | V | Voltage |
| Current L1 ampere | 400012 | FLOAT32 | A | Current |
| Power factor L1 | 400036 | FLOAT32 | PF | Power |
| Active energy imp Wh | 400464 | FLOAT64 | kWh | Energy |
| Frequency Hz | 400082 | FLOAT32 | Hz | Frequency |
| Phase angle L1 rad -PiPi | 400030 | FLOAT32 | - | General |
| Phase voltage L2 | 400002 | FLOAT32 | V | Voltage |
| Phase voltage L3 | 400004 | FLOAT32 | V | Voltage |
| Main voltage L1-L2 volts | 400006 | FLOAT32 | V | Voltage |
| Main voltage L2-L3 | 400008 | FLOAT32 | V | Voltage |
| Main voltage L3-L1 | 400010 | FLOAT32 | V | Voltage |
| Current L2 | 400014 | FLOAT32 | A | Current |

## Addressing and setup

Addresses and values above are copied from the public JSON preview. Confirm the exact model, firmware, register function, address base, word order, scaling and units against the manufacturer manual before polling. No manufacturer manual revision or hardware validation is established by this page.

## Use with Modbus Monitor XPF

Check the device-map catalog in your installed XPF version for current map availability and licensing. The software download link does not open this map.

[Get Modbus Monitor XPF](https://docs.quantumbitsolutions.com/downloads-purchase/) · [Request a map or correction](https://github.com/Modbus-Monitor/modbus-device-maps/issues/new/choose) · [Browse all previews](https://docs.quantumbitsolutions.com/modbus-device-maps/)

<script type="application/ld+json">{"@context": "https://schema.org", "@type": "Dataset", "name": "Cewe Prometer public register preview", "description": "Sample register addresses and data types; not a complete map or hardware verification.", "url": "https://docs.quantumbitsolutions.com/modbus-device-maps/previews/cewe/prometer/", "license": "https://modbus-monitor.github.io/modbus-device-maps/data-license/", "creator": {"@type": "Organization", "name": "Quantum Bit Solutions", "url": "https://quantumbitsolutions.com/"}, "distribution": {"@type": "DataDownload", "encodingFormat": "application/json", "contentUrl": "https://modbus-monitor.github.io/modbus-device-maps/maps/cewe/prometer.json"}}</script>
