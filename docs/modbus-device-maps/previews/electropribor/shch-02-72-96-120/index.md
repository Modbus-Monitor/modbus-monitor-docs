---
title: "Electropribor SHCH 02,72,96,120 Modbus register preview"
description: "Sample register addresses and data types for Electropribor SHCH 02,72,96,120. Public preview with JSON source and verification status."
---

# Electropribor SHCH 02,72,96,120 Modbus register preview

Public preview for **Electropribor SHCH 02,72,96,120** (Power Meter).
This sample is not a complete map or evidence of hardware testing.

## Preview details

- Catalog ID: `electropribor/shch-02-72-96-120`
- Map version: 1.0
- Verification: not-reviewed
- Protocols: RTU, TCP
- Public preview: 9 registers. Complete in-app availability is not established by this preview.

[JSON preview](https://modbus-monitor.github.io/modbus-device-maps/maps/electropribor/shch-02-72-96-120.json) · [Data terms](https://modbus-monitor.github.io/modbus-device-maps/data-license/)

## Register table (sample)

| Signal | Display address | Data type | Units | Category |
|---|---|---|---|---|
| Frequency 1 | 300009 | FLOAT32 | Hz | Frequency |
| Device state | 300005 | UINT16 | - | Status |
| Result 1 | 300000 | FLOAT32 | - | General |
| Frequency 2 | 300011 | FLOAT32 | Hz | Frequency |
| Result 2 | 300002 | FLOAT32 | - | General |
| EEPROM errors | 300006 | UINT16 | - | General |
| ADC | 300012 | UINT32 | - | General |
| PWM1 | 300014 | UINT16 | - | General |
| PWM2 | 300015 | UINT16 | - | General |

## Addressing and setup

Addresses and values above are copied from the public JSON preview. Confirm the exact model, firmware, register function, address base, word order, scaling and units against the manufacturer manual before polling. No manufacturer manual revision or hardware validation is established by this page.

## Use with Modbus Monitor XPF

Check the device-map catalog in your installed XPF version for current map availability and licensing. The software download link does not open this map.

[Get Modbus Monitor XPF](https://docs.quantumbitsolutions.com/downloads-purchase/) · [Request a map or correction](https://github.com/Modbus-Monitor/modbus-device-maps/issues/new/choose) · [Browse all previews](https://docs.quantumbitsolutions.com/modbus-device-maps/)

<script type="application/ld+json">{"@context": "https://schema.org", "@type": "Dataset", "name": "Electropribor SHCH 02,72,96,120 public register preview", "description": "Sample register addresses and data types; not a complete map or hardware verification.", "url": "https://docs.quantumbitsolutions.com/modbus-device-maps/previews/electropribor/shch-02-72-96-120/", "license": "https://modbus-monitor.github.io/modbus-device-maps/data-license/", "creator": {"@type": "Organization", "name": "Quantum Bit Solutions", "url": "https://quantumbitsolutions.com/"}, "distribution": {"@type": "DataDownload", "encodingFormat": "application/json", "contentUrl": "https://modbus-monitor.github.io/modbus-device-maps/maps/electropribor/shch-02-72-96-120.json"}}</script>
