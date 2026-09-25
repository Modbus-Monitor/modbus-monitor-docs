---
title: "Veris E51 Modbus register preview"
description: "Sample register addresses and data types for Veris E51. Public preview with JSON source and verification status."
---

# Veris E51 Modbus register preview

Public preview for **Veris E51** (Power Meter).
This sample is not a complete map or evidence of hardware testing.

## Preview details

- Catalog ID: `veris/e51`
- Map version: 1.0
- Verification: not-reviewed
- Protocols: RTU, TCP
- Public preview: 12 registers. Complete in-app availability is not established by this preview.

[JSON preview](https://modbus-monitor.github.io/modbus-device-maps/maps/veris/e51.json) · [Data terms](https://modbus-monitor.github.io/modbus-device-maps/data-license/)

## Register table (sample)

| Signal | Display address | Data type | Units | Category |
|---|---|---|---|---|
| Voltage L-L average of active phases yolt | 300025 | UINT16 | V | Voltage |
| Current average of active phases Amp | 300027 | UINT16 | A | Current |
| Apparent Q1-4 import kVAh | 300017 | UINT32 | - | Power |
| Real energy diet import-export kWh | 300001 | UINT32 | kWh | Energy |
| Frequency Hz | 300028 | UINT16 | Hz | Frequency |
| Ct ratio secondary | 300132 | UINT16 | - | General |
| Real energy Q1-4 import kWh | 300003 | UINT32 | kWh | Energy |
| Real energy Q2-3 import kWh | 300005 | UINT32 | kWh | Energy |
| Reactive energy Q1 kVARh | 300007 | UINT32 | kWh | Energy |
| Reactive energy Q2 kVARh | 300009 | UINT32 | kWh | Energy |
| Reactive energy Q3 kVARh | 300011 | UINT32 | kWh | Energy |
| Reactive energy Q4 kVARh | 300013 | UINT32 | kWh | Energy |

## Addressing and setup

Addresses and values above are copied from the public JSON preview. Confirm the exact model, firmware, register function, address base, word order, scaling and units against the manufacturer manual before polling. No manufacturer manual revision or hardware validation is established by this page.

## Use with Modbus Monitor XPF

Check the device-map catalog in your installed XPF version for current map availability and licensing. The software download link does not open this map.

[Get Modbus Monitor XPF](https://docs.quantumbitsolutions.com/downloads-purchase/) · [Request a map or correction](https://github.com/Modbus-Monitor/modbus-device-maps/issues/new/choose) · [Browse all previews](https://docs.quantumbitsolutions.com/modbus-device-maps/)

<script type="application/ld+json">{"@context": "https://schema.org", "@type": "Dataset", "name": "Veris E51 public register preview", "description": "Sample register addresses and data types; not a complete map or hardware verification.", "url": "https://docs.quantumbitsolutions.com/modbus-device-maps/previews/veris/e51/", "license": "https://modbus-monitor.github.io/modbus-device-maps/data-license/", "creator": {"@type": "Organization", "name": "Quantum Bit Solutions", "url": "https://quantumbitsolutions.com/"}, "distribution": {"@type": "DataDownload", "encodingFormat": "application/json", "contentUrl": "https://modbus-monitor.github.io/modbus-device-maps/maps/veris/e51.json"}}</script>
