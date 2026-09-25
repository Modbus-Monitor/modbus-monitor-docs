---
title: "Owen Brothers OB115 Modbus register preview"
description: "Sample register addresses and data types for Owen Brothers OB115. Public preview with JSON source and verification status."
---

# Owen Brothers OB115 Modbus register preview

Public preview for **Owen Brothers OB115** (Power Meter).
This sample is not a complete map or evidence of hardware testing.

## Preview details

- Catalog ID: `owen-brothers/ob115`
- Map version: 1.0
- Verification: not-reviewed
- Protocols: RTU, TCP
- Public preview: 12 registers. Complete in-app availability is not established by this preview.

[JSON preview](https://modbus-monitor.github.io/modbus-device-maps/maps/owen-brothers/ob115.json) · [Data terms](https://modbus-monitor.github.io/modbus-device-maps/data-license/)

## Register table (sample)

| Signal | Display address | Data type | Units | Category |
|---|---|---|---|---|
| Voltage | 400002 | UINT32 | V | Voltage |
| Current | 400006 | UINT32 | - | Current |
| Active power | 400008 | UINT32 | kW | Power |
| Import active energy | 400352 | UINT32 | kWh | Energy |
| Frequency | 400004 | UINT32 | Hz | Frequency |
| Reserve default 0 | 400356 | UINT32 | - | General |
| Apparent power | 400010 | UINT32 | kW | Power |
| Reactive power | 400012 | UINT32 | kW | Power |
| Power factor | 400014 | UINT32 | PF | Power |
| Import reactive energy | 400354 | UINT32 | kWh | Energy |
| Export active energy | 400358 | UINT32 | kWh | Energy |
| Export reactive energy | 400360 | UINT32 | kWh | Energy |

## Addressing and setup

Addresses and values above are copied from the public JSON preview. Confirm the exact model, firmware, register function, address base, word order, scaling and units against the manufacturer manual before polling. No manufacturer manual revision or hardware validation is established by this page.

## Use with Modbus Monitor XPF

Check the device-map catalog in your installed XPF version for current map availability and licensing. The software download link does not open this map.

[Get Modbus Monitor XPF](https://docs.quantumbitsolutions.com/downloads-purchase/) · [Request a map or correction](https://github.com/Modbus-Monitor/modbus-device-maps/issues/new/choose) · [Browse all previews](https://docs.quantumbitsolutions.com/modbus-device-maps/)

<script type="application/ld+json">{"@context": "https://schema.org", "@type": "Dataset", "name": "Owen Brothers OB115 public register preview", "description": "Sample register addresses and data types; not a complete map or hardware verification.", "url": "https://docs.quantumbitsolutions.com/modbus-device-maps/previews/owen-brothers/ob115/", "license": "https://modbus-monitor.github.io/modbus-device-maps/data-license/", "creator": {"@type": "Organization", "name": "Quantum Bit Solutions", "url": "https://quantumbitsolutions.com/"}, "distribution": {"@type": "DataDownload", "encodingFormat": "application/json", "contentUrl": "https://modbus-monitor.github.io/modbus-device-maps/maps/owen-brothers/ob115.json"}}</script>
