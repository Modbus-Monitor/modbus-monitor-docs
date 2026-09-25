---
title: "Finder Series 7E,7E64,7E68,7E78,7E86 Modbus register preview"
description: "Sample register addresses and data types for Finder Series 7E,7E64,7E68,7E78,7E86. Public preview with JSON source and verification status."
---

# Finder Series 7E,7E64,7E68,7E78,7E86 Modbus register preview

Public preview for **Finder Series 7E,7E64,7E68,7E78,7E86** (Power Meter).
This sample is not a complete map or evidence of hardware testing.

## Preview details

- Catalog ID: `finder/series-7e-7e64-7e68-7e78-7e86`
- Map version: 1.0
- Verification: not-reviewed
- Protocols: RTU, TCP
- Public preview: 12 registers. Complete in-app availability is not established by this preview.

[JSON preview](https://modbus-monitor.github.io/modbus-device-maps/maps/finder/series-7e-7e64-7e68-7e78-7e86.json) · [Data terms](https://modbus-monitor.github.io/modbus-device-maps/data-license/)

## Register table (sample)

| Signal | Display address | Data type | Units | Category |
|---|---|---|---|---|
| Ph 1 N voltage V | 404096 | FLOAT32 | V | Voltage |
| Ph1 current A | 404110 | FLOAT32 | - | Current |
| Ph1 power factor | 404120 | FLOAT32 | PF | Power |
| Frequency Hz | 404152 | FLOAT32 | Hz | Frequency |
| Phase seque nce | 404154 | FLOAT32 | - | General |
| Ph 2 N voltage V | 404098 | FLOAT32 | V | Voltage |
| Ph 3 N voltage V | 404100 | FLOAT32 | V | Voltage |
| L 1 2 voltage V | 404102 | FLOAT32 | V | Voltage |
| L 2 3 voltage V | 404104 | FLOAT32 | V | Voltage |
| L 3 1 voltage V | 404106 | FLOAT32 | V | Voltage |
| System voltage V | 404108 | FLOAT32 | V | Voltage |
| Ph2 current A | 404112 | FLOAT32 | - | Current |

## Addressing and setup

Addresses and values above are copied from the public JSON preview. Confirm the exact model, firmware, register function, address base, word order, scaling and units against the manufacturer manual before polling. No manufacturer manual revision or hardware validation is established by this page.

## Use with Modbus Monitor XPF

Check the device-map catalog in your installed XPF version for current map availability and licensing. The software download link does not open this map.

[Get Modbus Monitor XPF](https://docs.quantumbitsolutions.com/downloads-purchase/) · [Request a map or correction](https://github.com/Modbus-Monitor/modbus-device-maps/issues/new/choose) · [Browse all previews](https://docs.quantumbitsolutions.com/modbus-device-maps/)

<script type="application/ld+json">{"@context": "https://schema.org", "@type": "Dataset", "name": "Finder Series 7E,7E64,7E68,7E78,7E86 public register preview", "description": "Sample register addresses and data types; not a complete map or hardware verification.", "url": "https://docs.quantumbitsolutions.com/modbus-device-maps/previews/finder/series-7e-7e64-7e68-7e78-7e86/", "license": "https://modbus-monitor.github.io/modbus-device-maps/data-license/", "creator": {"@type": "Organization", "name": "Quantum Bit Solutions", "url": "https://quantumbitsolutions.com/"}, "distribution": {"@type": "DataDownload", "encodingFormat": "application/json", "contentUrl": "https://modbus-monitor.github.io/modbus-device-maps/maps/finder/series-7e-7e64-7e68-7e78-7e86.json"}}</script>
