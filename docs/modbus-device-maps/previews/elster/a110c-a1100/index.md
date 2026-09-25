---
title: "Elster A110C,A1100 Modbus register preview"
description: "Sample register addresses and data types for Elster A110C,A1100. Public preview with JSON source and verification status."
---

# Elster A110C,A1100 Modbus register preview

Public preview for **Elster A110C,A1100** (Power Meter).
This sample is not a complete map or evidence of hardware testing.

## Preview details

- Catalog ID: `elster/a110c-a1100`
- Map version: 1.0
- Verification: not-reviewed
- Protocols: RTU, TCP
- Public preview: 12 registers. Complete in-app availability is not established by this preview.

[JSON preview](https://modbus-monitor.github.io/modbus-device-maps/maps/elster/a110c-a1100.json) · [Data terms](https://modbus-monitor.github.io/modbus-device-maps/data-license/)

## Register table (sample)

| Signal | Display address | Data type | Units | Category |
|---|---|---|---|---|
| Meter1 import rate1 | 300001 | INT32 | - | Communication |
| Meter1 export rate1 | 300003 | INT32 | - | Communication |
| Meter1 import rate2 | 300005 | INT32 | - | Communication |
| Meter1 export rate2 | 300007 | INT32 | - | Communication |
| Meter2 import rate1 | 300009 | INT32 | - | Communication |
| Meter2 export rate1 | 300011 | INT32 | - | Communication |
| Meter2 import rate2 | 300013 | INT32 | - | Communication |
| Meter2 export rate2 | 300015 | INT32 | - | Communication |
| Meter1 import rate1 | 300017 | FLOAT32 | - | Communication |
| Meter1 export rate1 | 300019 | FLOAT32 | - | Communication |
| Meter1 import rate2 | 300021 | FLOAT32 | - | Communication |
| Meterl export rate1 | 300023 | FLOAT32 | - | Communication |

## Addressing and setup

Addresses and values above are copied from the public JSON preview. Confirm the exact model, firmware, register function, address base, word order, scaling and units against the manufacturer manual before polling. No manufacturer manual revision or hardware validation is established by this page.

## Use with Modbus Monitor XPF

Check the device-map catalog in your installed XPF version for current map availability and licensing. The software download link does not open this map.

[Get Modbus Monitor XPF](https://docs.quantumbitsolutions.com/downloads-purchase/) · [Request a map or correction](https://github.com/Modbus-Monitor/modbus-device-maps/issues/new/choose) · [Browse all previews](https://docs.quantumbitsolutions.com/modbus-device-maps/)

<script type="application/ld+json">{"@context": "https://schema.org", "@type": "Dataset", "name": "Elster A110C,A1100 public register preview", "description": "Sample register addresses and data types; not a complete map or hardware verification.", "url": "https://docs.quantumbitsolutions.com/modbus-device-maps/previews/elster/a110c-a1100/", "license": "https://modbus-monitor.github.io/modbus-device-maps/data-license/", "creator": {"@type": "Organization", "name": "Quantum Bit Solutions", "url": "https://quantumbitsolutions.com/"}, "distribution": {"@type": "DataDownload", "encodingFormat": "application/json", "contentUrl": "https://modbus-monitor.github.io/modbus-device-maps/maps/elster/a110c-a1100.json"}}</script>
