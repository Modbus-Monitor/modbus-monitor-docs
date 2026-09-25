---
title: "Selec EM2M-1P Modbus register preview"
description: "Sample register addresses and data types for Selec EM2M-1P. Public preview with JSON source and verification status."
---

# Selec EM2M-1P Modbus register preview

Public preview for **Selec EM2M-1P** (Power Meter).
This sample is not a complete map or evidence of hardware testing.

## Preview details

- Catalog ID: `selec/em2m-1p`
- Map version: 1.0
- Verification: not-reviewed
- Protocols: RTU, TCP
- Public preview: 12 registers. Complete in-app availability is not established by this preview.

[JSON preview](https://modbus-monitor.github.io/modbus-device-maps/maps/selec/em2m-1p.json) · [Data terms](https://modbus-monitor.github.io/modbus-device-maps/data-license/)

## Register table (sample)

| Signal | Display address | Data type | Units | Category |
|---|---|---|---|---|
| Voltage L-N | 300020 | FLOAT32 | V | Voltage |
| Current | 300022 | FLOAT32 | - | Current |
| Active power | 300014 | FLOAT32 | kW | Power |
| Total active energy | 300000 | FLOAT32 | kWh | Energy |
| Frequency | 300026 | FLOAT32 | Hz | Frequency |
| Import active energy | 300002 | FLOAT32 | kWh | Energy |
| Export active energy | 300004 | FLOAT32 | kWh | Energy |
| Total reactive energy | 300006 | FLOAT32 | kWh | Energy |
| Import reactive energy | 300008 | FLOAT32 | kWh | Energy |
| Export reactive energy | 300010 | FLOAT32 | kWh | Energy |
| Apparent energy | 300012 | FLOAT32 | kWh | Energy |
| Reactive power | 300016 | FLOAT32 | kW | Power |

## Addressing and setup

Addresses and values above are copied from the public JSON preview. Confirm the exact model, firmware, register function, address base, word order, scaling and units against the manufacturer manual before polling. No manufacturer manual revision or hardware validation is established by this page.

## Use with Modbus Monitor XPF

Check the device-map catalog in your installed XPF version for current map availability and licensing. The software download link does not open this map.

[Get Modbus Monitor XPF](https://docs.quantumbitsolutions.com/downloads-purchase/) · [Request a map or correction](https://github.com/Modbus-Monitor/modbus-device-maps/issues/new/choose) · [Browse all previews](https://docs.quantumbitsolutions.com/modbus-device-maps/)

<script type="application/ld+json">{"@context": "https://schema.org", "@type": "Dataset", "name": "Selec EM2M-1P public register preview", "description": "Sample register addresses and data types; not a complete map or hardware verification.", "url": "https://docs.quantumbitsolutions.com/modbus-device-maps/previews/selec/em2m-1p/", "license": "https://modbus-monitor.github.io/modbus-device-maps/data-license/", "creator": {"@type": "Organization", "name": "Quantum Bit Solutions", "url": "https://quantumbitsolutions.com/"}, "distribution": {"@type": "DataDownload", "encodingFormat": "application/json", "contentUrl": "https://modbus-monitor.github.io/modbus-device-maps/maps/selec/em2m-1p.json"}}</script>
