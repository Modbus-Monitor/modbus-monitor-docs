---
title: "YTL 5300 Modbus register preview"
description: "Sample register addresses and data types for YTL 5300. Public preview with JSON source and verification status."
---

# YTL 5300 Modbus register preview

Public preview for **YTL 5300** (Power Meter).
This sample is not a complete map or evidence of hardware testing.

## Preview details

- Catalog ID: `ytl/5300`
- Map version: 1.0
- Verification: not-reviewed
- Protocols: RTU, TCP
- Public preview: 12 registers. Complete in-app availability is not established by this preview.

[JSON preview](https://modbus-monitor.github.io/modbus-device-maps/maps/ytl/5300.json) · [Data terms](https://modbus-monitor.github.io/modbus-device-maps/data-license/)

## Register table (sample)

| Signal | Display address | Data type | Units | Category |
|---|---|---|---|---|
| L1 voltage | 400014 | FLOAT32 | V | Voltage |
| L1 current | 400022 | FLOAT32 | - | Current |
| Total active power | 400028 | FLOAT32 | kW | Power |
| Total active energy | 400256 | FLOAT32 | kWh | Energy |
| Grid frequency | 400020 | FLOAT32 | Hz | Frequency |
| Serial number | 400000 | FLOAT32 | - | Identification |
| Meter ID | 400002 | FLOAT32 | - | General |
| Baud rate | 400003 | FLOAT32 | - | Communication |
| L2 voltage | 400016 | FLOAT32 | V | Voltage |
| L3 voltage | 400018 | FLOAT32 | V | Voltage |
| L2 current | 400024 | FLOAT32 | - | Current |
| L3 current | 400026 | FLOAT32 | - | Current |

## Addressing and setup

Addresses and values above are copied from the public JSON preview. Confirm the exact model, firmware, register function, address base, word order, scaling and units against the manufacturer manual before polling. No manufacturer manual revision or hardware validation is established by this page.

## Use with Modbus Monitor XPF

Check the device-map catalog in your installed XPF version for current map availability and licensing. The software download link does not open this map.

[Get Modbus Monitor XPF](https://docs.quantumbitsolutions.com/downloads-purchase/) · [Request a map or correction](https://github.com/Modbus-Monitor/modbus-device-maps/issues/new/choose) · [Browse all previews](https://docs.quantumbitsolutions.com/modbus-device-maps/)

<script type="application/ld+json">{"@context": "https://schema.org", "@type": "Dataset", "name": "YTL 5300 public register preview", "description": "Sample register addresses and data types; not a complete map or hardware verification.", "url": "https://docs.quantumbitsolutions.com/modbus-device-maps/previews/ytl/5300/", "license": "https://modbus-monitor.github.io/modbus-device-maps/data-license/", "creator": {"@type": "Organization", "name": "Quantum Bit Solutions", "url": "https://quantumbitsolutions.com/"}, "distribution": {"@type": "DataDownload", "encodingFormat": "application/json", "contentUrl": "https://modbus-monitor.github.io/modbus-device-maps/maps/ytl/5300.json"}}</script>
