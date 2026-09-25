---
title: "Saci M2DL2 Modbus register preview"
description: "Sample register addresses and data types for Saci M2DL2. Public preview with JSON source and verification status."
---

# Saci M2DL2 Modbus register preview

Public preview for **Saci M2DL2** (Power Meter).
This sample is not a complete map or evidence of hardware testing.

## Preview details

- Catalog ID: `saci/m2dl2`
- Map version: 1.0
- Verification: not-reviewed
- Protocols: RTU, TCP
- Public preview: 12 registers. Complete in-app availability is not established by this preview.

[JSON preview](https://modbus-monitor.github.io/modbus-device-maps/maps/saci/m2dl2.json) · [Data terms](https://modbus-monitor.github.io/modbus-device-maps/data-license/)

## Register table (sample)

| Signal | Display address | Data type | Units | Category |
|---|---|---|---|---|
| Voltage V | 300012 | UINT16 | V | Voltage |
| Current A | 300013 | UINT16 | - | Current |
| Active power W | 300014 | UINT16 | kW | Power |
| Global active energy accumulator kWh | 300000 | UINT32 | kWh | Energy |
| Frequency Hz | 300017 | UINT16 | Hz | Frequency |
| Export active energy accumulator kWh | 300008 | UINT32 | kWh | Energy |
| Import active energy accumulator kWh | 300010 | UINT32 | kWh | Energy |
| Reactive power W | 300015 | UINT16 | kW | Power |
| Power factor | 300016 | UINT16 | PF | Power |
| Import reactive energy accumulator Q1 Q2 kWh | 300256 | UINT32 | kWh | Energy |
| Export reactive energy accumulator Q3 Q4 kWh | 300258 | UINT32 | kWh | Energy |
| Q1 reactive energy accumulator kWh | 300260 | UINT32 | kWh | Energy |

## Addressing and setup

Addresses and values above are copied from the public JSON preview. Confirm the exact model, firmware, register function, address base, word order, scaling and units against the manufacturer manual before polling. No manufacturer manual revision or hardware validation is established by this page.

## Use with Modbus Monitor XPF

Check the device-map catalog in your installed XPF version for current map availability and licensing. The software download link does not open this map.

[Get Modbus Monitor XPF](https://docs.quantumbitsolutions.com/downloads-purchase/) · [Request a map or correction](https://github.com/Modbus-Monitor/modbus-device-maps/issues/new/choose) · [Browse all previews](https://docs.quantumbitsolutions.com/modbus-device-maps/)

<script type="application/ld+json">{"@context": "https://schema.org", "@type": "Dataset", "name": "Saci M2DL2 public register preview", "description": "Sample register addresses and data types; not a complete map or hardware verification.", "url": "https://docs.quantumbitsolutions.com/modbus-device-maps/previews/saci/m2dl2/", "license": "https://modbus-monitor.github.io/modbus-device-maps/data-license/", "creator": {"@type": "Organization", "name": "Quantum Bit Solutions", "url": "https://quantumbitsolutions.com/"}, "distribution": {"@type": "DataDownload", "encodingFormat": "application/json", "contentUrl": "https://modbus-monitor.github.io/modbus-device-maps/maps/saci/m2dl2.json"}}</script>
