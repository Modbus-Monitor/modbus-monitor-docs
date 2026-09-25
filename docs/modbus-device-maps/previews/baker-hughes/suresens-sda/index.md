---
title: "Baker Hughes SureSens SDA Modbus register preview"
description: "Sample register addresses and data types for Baker Hughes SureSens SDA. Public preview with JSON source and verification status."
---

# Baker Hughes SureSens SDA Modbus register preview

Public preview for **Baker Hughes SureSens SDA** (Power Meter).
This sample is not a complete map or evidence of hardware testing.

## Preview details

- Catalog ID: `baker-hughes/suresens-sda`
- Map version: 1.0
- Verification: not-reviewed
- Protocols: RTU, TCP
- Public preview: 12 registers. Complete in-app availability is not established by this preview.

[JSON preview](https://modbus-monitor.github.io/modbus-device-maps/maps/baker-hughes/suresens-sda.json) · [Data terms](https://modbus-monitor.github.io/modbus-device-maps/data-license/)

## Register table (sample)

| Signal | Display address | Data type | Units | Category |
|---|---|---|---|---|
| Gauge 1 status Gauge Status 0 good | 300021 | FLOAT32 | - | Status |
| Gauge 1 temperature Degrees F | 300019 | FLOAT32 | degC | Temperature |
| Gauge 1 pressure Psia | 300017 | FLOAT32 | - | General |
| Gauge 2 temperature Degrees F | 300025 | FLOAT32 | degC | Temperature |
| Gauge 2 status Gauge Status 0 good | 300027 | FLOAT32 | - | Status |
| Gauge 3 temperature Degrees F | 300031 | FLOAT32 | degC | Temperature |
| Gauge 3 status Gauge Status 0 good | 300033 | FLOAT32 | - | Status |
| Gauge 4 temperature Degrees F | 300037 | FLOAT32 | degC | Temperature |
| Gauge 4 status Gauge Status 0 good | 300039 | FLOAT32 | - | Status |
| Gauge 5 temperature Degrees F | 300043 | FLOAT32 | degC | Temperature |
| Gauge 5 status Gauge Status 0 good | 300045 | FLOAT32 | - | Status |
| Gauge 6 temperature Degrees F | 300049 | FLOAT32 | degC | Temperature |

## Addressing and setup

Addresses and values above are copied from the public JSON preview. Confirm the exact model, firmware, register function, address base, word order, scaling and units against the manufacturer manual before polling. No manufacturer manual revision or hardware validation is established by this page.

## Use with Modbus Monitor XPF

Check the device-map catalog in your installed XPF version for current map availability and licensing. The software download link does not open this map.

[Get Modbus Monitor XPF](https://docs.quantumbitsolutions.com/downloads-purchase/) · [Request a map or correction](https://github.com/Modbus-Monitor/modbus-device-maps/issues/new/choose) · [Browse all previews](https://docs.quantumbitsolutions.com/modbus-device-maps/)

<script type="application/ld+json">{"@context": "https://schema.org", "@type": "Dataset", "name": "Baker Hughes SureSens SDA public register preview", "description": "Sample register addresses and data types; not a complete map or hardware verification.", "url": "https://docs.quantumbitsolutions.com/modbus-device-maps/previews/baker-hughes/suresens-sda/", "license": "https://modbus-monitor.github.io/modbus-device-maps/data-license/", "creator": {"@type": "Organization", "name": "Quantum Bit Solutions", "url": "https://quantumbitsolutions.com/"}, "distribution": {"@type": "DataDownload", "encodingFormat": "application/json", "contentUrl": "https://modbus-monitor.github.io/modbus-device-maps/maps/baker-hughes/suresens-sda.json"}}</script>
