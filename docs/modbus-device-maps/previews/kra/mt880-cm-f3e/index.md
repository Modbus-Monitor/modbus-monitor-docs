---
title: "kra MT880,CM-f3e Modbus register preview"
description: "Sample register addresses and data types for kra MT880,CM-f3e. Public preview with JSON source and verification status."
---

# kra MT880,CM-f3e Modbus register preview

Public preview for **kra MT880,CM-f3e** (Power Meter).
This sample is not a complete map or evidence of hardware testing.

## Preview details

- Catalog ID: `kra/mt880-cm-f3e`
- Map version: 1.0
- Verification: not-reviewed
- Protocols: RTU, TCP
- Public preview: 12 registers. Complete in-app availability is not established by this preview.

[JSON preview](https://modbus-monitor.github.io/modbus-device-maps/maps/kra/mt880-cm-f3e.json) · [Data terms](https://modbus-monitor.github.io/modbus-device-maps/data-license/)

## Register table (sample)

| Signal | Display address | Data type | Units | Category |
|---|---|---|---|---|
| Instantaneous voltage L1 | 400296 | FLOAT32 | V | Voltage |
| Current system time | 400002 | INT32 | - | Current |
| Instantaneous active power a a | 400168 | FLOAT32 | kW | Power |
| Active energy import a | 400008 | FLOAT64 | kWh | Energy |
| Instantaneous net frequency | 400250 | FLOAT32 | Hz | Frequency |
| Device id 1 manufacturing number | 400000 | INT32 | - | General |
| Current system date | 400005 | INT32 | - | Current |
| Active energy export a | 400012 | FLOAT64 | kWh | Energy |
| Reactive energy import r | 400016 | FLOAT64 | kWh | Energy |
| Reactive energy export r | 400020 | FLOAT64 | kWh | Energy |
| Reactive energy Q1 ri | 400024 | FLOAT64 | kWh | Energy |
| Reactive energy Q2 rc | 400028 | FLOAT64 | kWh | Energy |

## Addressing and setup

Addresses and values above are copied from the public JSON preview. Confirm the exact model, firmware, register function, address base, word order, scaling and units against the manufacturer manual before polling. No manufacturer manual revision or hardware validation is established by this page.

## Use with Modbus Monitor XPF

Check the device-map catalog in your installed XPF version for current map availability and licensing. The software download link does not open this map.

[Get Modbus Monitor XPF](https://docs.quantumbitsolutions.com/downloads-purchase/) · [Request a map or correction](https://github.com/Modbus-Monitor/modbus-device-maps/issues/new/choose) · [Browse all previews](https://docs.quantumbitsolutions.com/modbus-device-maps/)

<script type="application/ld+json">{"@context": "https://schema.org", "@type": "Dataset", "name": "kra MT880,CM-f3e public register preview", "description": "Sample register addresses and data types; not a complete map or hardware verification.", "url": "https://docs.quantumbitsolutions.com/modbus-device-maps/previews/kra/mt880-cm-f3e/", "license": "https://modbus-monitor.github.io/modbus-device-maps/data-license/", "creator": {"@type": "Organization", "name": "Quantum Bit Solutions", "url": "https://quantumbitsolutions.com/"}, "distribution": {"@type": "DataDownload", "encodingFormat": "application/json", "contentUrl": "https://modbus-monitor.github.io/modbus-device-maps/maps/kra/mt880-cm-f3e.json"}}</script>
