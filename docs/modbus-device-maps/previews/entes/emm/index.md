---
title: "ENTES EMM Modbus register preview"
description: "Sample register addresses and data types for ENTES EMM. Public preview with JSON source and verification status."
---

# ENTES EMM Modbus register preview

Public preview for **ENTES EMM** (Power Meter).
This sample is not a complete map or evidence of hardware testing.

## Preview details

- Catalog ID: `entes/emm`
- Map version: 1.0
- Verification: not-reviewed
- Protocols: RTU, TCP
- Public preview: 12 registers. Complete in-app availability is not established by this preview.

[JSON preview](https://modbus-monitor.github.io/modbus-device-maps/maps/entes/emm.json) · [Data terms](https://modbus-monitor.github.io/modbus-device-maps/data-license/)

## Register table (sample)

| Signal | Display address | Data type | Units | Category |
|---|---|---|---|---|
| Voltage L1-N V | 400000 | FLOAT32 | V | Voltage |
| Current L1 mA | 400014 | FLOAT32 | A | Current |
| Active power L1-N W | 400026 | FLOAT32 | kW | Power |
| Measured frequency Hz | 400024 | FLOAT32 | Hz | Frequency |
| Internal temp DC | 400128 | FLOAT32 | - | Temperature |
| CosPhi L1 | 400086 | FLOAT32 | - | General |
| Voltage L2-N V | 400002 | FLOAT32 | V | Voltage |
| Voltage L3-N V | 400004 | FLOAT32 | V | Voltage |
| Voltage L1-L2 V | 400008 | FLOAT32 | V | Voltage |
| Voltage L2-L3 V | 400010 | FLOAT32 | V | Voltage |
| Voltage L3-L1 V | 400012 | FLOAT32 | V | Voltage |
| Current L2 mA | 400016 | FLOAT32 | A | Current |

## Addressing and setup

Addresses and values above are copied from the public JSON preview. Confirm the exact model, firmware, register function, address base, word order, scaling and units against the manufacturer manual before polling. No manufacturer manual revision or hardware validation is established by this page.

## Use with Modbus Monitor XPF

Check the device-map catalog in your installed XPF version for current map availability and licensing. The software download link does not open this map.

[Get Modbus Monitor XPF](https://docs.quantumbitsolutions.com/downloads-purchase/) · [Request a map or correction](https://github.com/Modbus-Monitor/modbus-device-maps/issues/new/choose) · [Browse all previews](https://docs.quantumbitsolutions.com/modbus-device-maps/)

<script type="application/ld+json">{"@context": "https://schema.org", "@type": "Dataset", "name": "ENTES EMM public register preview", "description": "Sample register addresses and data types; not a complete map or hardware verification.", "url": "https://docs.quantumbitsolutions.com/modbus-device-maps/previews/entes/emm/", "license": "https://modbus-monitor.github.io/modbus-device-maps/data-license/", "creator": {"@type": "Organization", "name": "Quantum Bit Solutions", "url": "https://quantumbitsolutions.com/"}, "distribution": {"@type": "DataDownload", "encodingFormat": "application/json", "contentUrl": "https://modbus-monitor.github.io/modbus-device-maps/maps/entes/emm.json"}}</script>
