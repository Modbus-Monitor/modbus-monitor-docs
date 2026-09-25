---
title: "Continental Control Systems WattNode Modbus register preview"
description: "Sample register addresses and data types for Continental Control Systems WattNode. Public preview with JSON source and verification status."
---

# Continental Control Systems WattNode Modbus register preview

Public preview for **Continental Control Systems WattNode** (Power Meter).
This sample is not a complete map or evidence of hardware testing.

## Preview details

- Catalog ID: `continental-control-systems/wattnode`
- Map version: 1.0
- Verification: not-reviewed
- Protocols: RTU, TCP
- Public preview: 12 registers. Complete in-app availability is not established by this preview.

[JSON preview](https://modbus-monitor.github.io/modbus-device-maps/maps/continental-control-systems/wattnode.json) · [Data terms](https://modbus-monitor.github.io/modbus-device-maps/data-license/)

## Register table (sample)

| Signal | Display address | Data type | Units | Category |
|---|---|---|---|---|
| Average phase to neutral voltage V | 401017 | FLOAT32 | V | Voltage |
| Rms current phase A A | 401163 | FLOAT32 | A | Current |
| Real power sum of active phases W | 401009 | FLOAT32 | kW | Power |
| Total net bidirectional energy kWh | 401001 | FLOAT32 | kWh | Energy |
| Total positive energy kWh | 401003 | FLOAT32 | kWh | Energy |
| Real power phase A W | 401011 | FLOAT32 | kW | Power |
| Real power phase B W | 401013 | FLOAT32 | kW | Power |
| Real power phase C W | 401015 | FLOAT32 | kW | Power |
| Rms voltage phase A to neutral V | 401019 | FLOAT32 | V | Voltage |
| Rms voltage phase B to neutral V | 401021 | FLOAT32 | V | Voltage |
| Rms voltage phase C to neutral V | 401023 | FLOAT32 | V | Voltage |
| Average line to line voltage V | 401025 | FLOAT32 | V | Voltage |

## Addressing and setup

Addresses and values above are copied from the public JSON preview. Confirm the exact model, firmware, register function, address base, word order, scaling and units against the manufacturer manual before polling. No manufacturer manual revision or hardware validation is established by this page.

## Use with Modbus Monitor XPF

Check the device-map catalog in your installed XPF version for current map availability and licensing. The software download link does not open this map.

[Get Modbus Monitor XPF](https://docs.quantumbitsolutions.com/downloads-purchase/) · [Request a map or correction](https://github.com/Modbus-Monitor/modbus-device-maps/issues/new/choose) · [Browse all previews](https://docs.quantumbitsolutions.com/modbus-device-maps/)

<script type="application/ld+json">{"@context": "https://schema.org", "@type": "Dataset", "name": "Continental Control Systems WattNode public register preview", "description": "Sample register addresses and data types; not a complete map or hardware verification.", "url": "https://docs.quantumbitsolutions.com/modbus-device-maps/previews/continental-control-systems/wattnode/", "license": "https://modbus-monitor.github.io/modbus-device-maps/data-license/", "creator": {"@type": "Organization", "name": "Quantum Bit Solutions", "url": "https://quantumbitsolutions.com/"}, "distribution": {"@type": "DataDownload", "encodingFormat": "application/json", "contentUrl": "https://modbus-monitor.github.io/modbus-device-maps/maps/continental-control-systems/wattnode.json"}}</script>
