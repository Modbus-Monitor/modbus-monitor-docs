---
title: "Veris E34 Modbus register preview"
description: "Sample register addresses and data types for Veris E34. Public preview with JSON source and verification status."
---

# Veris E34 Modbus register preview

Public preview for **Veris E34** (Power Meter).
This sample is not a complete map or evidence of hardware testing.

## Preview details

- Catalog ID: `veris/e34`
- Map version: 1.0
- Verification: not-reviewed
- Protocols: RTU, TCP
- Public preview: 12 registers. Complete in-app availability is not established by this preview.

[JSON preview](https://modbus-monitor.github.io/modbus-device-maps/maps/veris/e34.json) · [Data terms](https://modbus-monitor.github.io/modbus-device-maps/data-license/)

## Register table (sample)

| Signal | Display address | Data type | Units | Category |
|---|---|---|---|---|
| Voltage L l average of 3 phases Volts | 310145 | FLOAT32 | V | Voltage |
| Average current Amperes | 310119 | FLOAT32 | A | Current |
| Total kw kW | 310109 | FLOAT32 | - | Power |
| Total kwh msw kWh | 310101 | FLOAT32 | kWh | Energy |
| Frequency derived from phase a Hertz | 310149 | FLOAT32 | Hz | Frequency |
| Total pf PF | 310115 | FLOAT32 | - | Power Factor |
| Total kva kVA | 310113 | FLOAT32 | - | Power |
| Present kw demand kW | 310121 | FLOAT32 | kW | Power |
| Present current demand Amperes | 310127 | FLOAT32 | A | Current |
| Max kw demand kW | 310129 | FLOAT32 | kW | Power |
| Max current demand Amperes | 310135 | FLOAT32 | A | Current |
| Max kw kW | 310137 | FLOAT32 | - | Power |

## Addressing and setup

Addresses and values above are copied from the public JSON preview. Confirm the exact model, firmware, register function, address base, word order, scaling and units against the manufacturer manual before polling. No manufacturer manual revision or hardware validation is established by this page.

## Use with Modbus Monitor XPF

Check the device-map catalog in your installed XPF version for current map availability and licensing. The software download link does not open this map.

[Get Modbus Monitor XPF](https://docs.quantumbitsolutions.com/downloads-purchase/) · [Request a map or correction](https://github.com/Modbus-Monitor/modbus-device-maps/issues/new/choose) · [Browse all previews](https://docs.quantumbitsolutions.com/modbus-device-maps/)

<script type="application/ld+json">{"@context": "https://schema.org", "@type": "Dataset", "name": "Veris E34 public register preview", "description": "Sample register addresses and data types; not a complete map or hardware verification.", "url": "https://docs.quantumbitsolutions.com/modbus-device-maps/previews/veris/e34/", "license": "https://modbus-monitor.github.io/modbus-device-maps/data-license/", "creator": {"@type": "Organization", "name": "Quantum Bit Solutions", "url": "https://quantumbitsolutions.com/"}, "distribution": {"@type": "DataDownload", "encodingFormat": "application/json", "contentUrl": "https://modbus-monitor.github.io/modbus-device-maps/maps/veris/e34.json"}}</script>
