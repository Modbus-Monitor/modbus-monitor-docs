---
title: "mega CN7200,CN7500,CN7600,CN7800 Modbus register preview"
description: "Sample register addresses and data types for mega CN7200,CN7500,CN7600,CN7800. Public preview with JSON source and verification status."
---

# mega CN7200,CN7500,CN7600,CN7800 Modbus register preview

Public preview for **mega CN7200,CN7500,CN7600,CN7800** (Power Meter).
This sample is not a complete map or evidence of hardware testing.

## Preview details

- Catalog ID: `mega/cn7200-cn7500-cn7600-cn7800`
- Map version: 1.0
- Verification: not-reviewed
- Protocols: RTU, TCP
- Public preview: 12 registers. Complete in-app availability is not established by this preview.

[JSON preview](https://modbus-monitor.github.io/modbus-device-maps/maps/mega/cn7200-cn7500-cn7600-cn7800.json) · [Data terms](https://modbus-monitor.github.io/modbus-device-maps/data-license/)

## Register table (sample)

| Signal | Display address | Data type | Units | Category |
|---|---|---|---|---|
| Alarm 1 type | 404127 | UINT16 | - | Status |
| Upper limit of temperature range | 404097 | UINT16 | degC | Temperature |
| Process value pv | 404095 | UINT16 | - | General |
| Pb proportional band | 404104 | UINT16 | - | Communication |
| Software version | 404142 | UINT16 | - | Identification |
| Lower limit of temperature range | 404098 | UINT16 | degC | Temperature |
| Input temperature sensor type | 404099 | UINT16 | degC | Temperature |
| Temperature regulation value | 404117 | UINT16 | degC | Temperature |
| Alarm 2 type | 404128 | UINT16 | - | Status |
| Alarm 3 type | 404129 | UINT16 | - | Status |
| Upper limit alarm 1 | 404131 | UINT16 | - | Status |
| Lower limit alarm 1 | 404132 | UINT16 | - | Status |

## Addressing and setup

Addresses and values above are copied from the public JSON preview. Confirm the exact model, firmware, register function, address base, word order, scaling and units against the manufacturer manual before polling. No manufacturer manual revision or hardware validation is established by this page.

## Use with Modbus Monitor XPF

Check the device-map catalog in your installed XPF version for current map availability and licensing. The software download link does not open this map.

[Get Modbus Monitor XPF](https://docs.quantumbitsolutions.com/downloads-purchase/) · [Request a map or correction](https://github.com/Modbus-Monitor/modbus-device-maps/issues/new/choose) · [Browse all previews](https://docs.quantumbitsolutions.com/modbus-device-maps/)

<script type="application/ld+json">{"@context": "https://schema.org", "@type": "Dataset", "name": "mega CN7200,CN7500,CN7600,CN7800 public register preview", "description": "Sample register addresses and data types; not a complete map or hardware verification.", "url": "https://docs.quantumbitsolutions.com/modbus-device-maps/previews/mega/cn7200-cn7500-cn7600-cn7800/", "license": "https://modbus-monitor.github.io/modbus-device-maps/data-license/", "creator": {"@type": "Organization", "name": "Quantum Bit Solutions", "url": "https://quantumbitsolutions.com/"}, "distribution": {"@type": "DataDownload", "encodingFormat": "application/json", "contentUrl": "https://modbus-monitor.github.io/modbus-device-maps/maps/mega/cn7200-cn7500-cn7600-cn7800.json"}}</script>
