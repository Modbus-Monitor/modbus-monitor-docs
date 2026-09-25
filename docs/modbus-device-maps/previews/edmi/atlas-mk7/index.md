---
title: "EDMI Atlas MK7 Modbus register preview"
description: "Sample register addresses and data types for EDMI Atlas MK7. Public preview with JSON source and verification status."
---

# EDMI Atlas MK7 Modbus register preview

Public preview for **EDMI Atlas MK7** (Power Meter).
This sample is not a complete map or evidence of hardware testing.

## Preview details

- Catalog ID: `edmi/atlas-mk7`
- Map version: 1.0
- Verification: not-reviewed
- Protocols: RTU, TCP
- Public preview: 12 registers. Complete in-app availability is not established by this preview.

[JSON preview](https://modbus-monitor.github.io/modbus-device-maps/maps/edmi/atlas-mk7.json) · [Data terms](https://modbus-monitor.github.io/modbus-device-maps/data-license/)

## Register table (sample)

| Signal | Display address | Data type | Units | Category |
|---|---|---|---|---|
| Power factor | 400061 | FLOAT32 | PF | Power |
| Frequency | 400059 | FLOAT32 | Hz | Frequency |
| Serial number | 400001 | INT32 | - | Identification |
| Export wh total ch0 | 400003 | FLOAT32 | kWh | Communication |
| Va | 400011 | FLOAT32 | - | General |
| Import wh total ch1 | 400005 | FLOAT32 | kWh | Communication |
| Export varh total ch2 | 400007 | FLOAT32 | - | Communication |
| Import varh total ch3 | 400009 | FLOAT32 | - | Communication |
| Ia | 400017 | FLOAT32 | - | General |
| Angle a | 400023 | FLOAT32 | - | General |
| Va ia angle | 400029 | FLOAT32 | - | General |
| Va va angle | 400035 | FLOAT32 | - | General |

## Addressing and setup

Addresses and values above are copied from the public JSON preview. Confirm the exact model, firmware, register function, address base, word order, scaling and units against the manufacturer manual before polling. No manufacturer manual revision or hardware validation is established by this page.

## Use with Modbus Monitor XPF

Check the device-map catalog in your installed XPF version for current map availability and licensing. The software download link does not open this map.

[Get Modbus Monitor XPF](https://docs.quantumbitsolutions.com/downloads-purchase/) · [Request a map or correction](https://github.com/Modbus-Monitor/modbus-device-maps/issues/new/choose) · [Browse all previews](https://docs.quantumbitsolutions.com/modbus-device-maps/)

<script type="application/ld+json">{"@context": "https://schema.org", "@type": "Dataset", "name": "EDMI Atlas MK7 public register preview", "description": "Sample register addresses and data types; not a complete map or hardware verification.", "url": "https://docs.quantumbitsolutions.com/modbus-device-maps/previews/edmi/atlas-mk7/", "license": "https://modbus-monitor.github.io/modbus-device-maps/data-license/", "creator": {"@type": "Organization", "name": "Quantum Bit Solutions", "url": "https://quantumbitsolutions.com/"}, "distribution": {"@type": "DataDownload", "encodingFormat": "application/json", "contentUrl": "https://modbus-monitor.github.io/modbus-device-maps/maps/edmi/atlas-mk7.json"}}</script>
