---
title: "Integra Ci1 Modbus register preview"
description: "Sample register addresses and data types for Integra Ci1. Public preview with JSON source and verification status."
---

# Integra Ci1 Modbus register preview

Public preview for **Integra Ci1** (Power Meter).
This sample is not a complete map or evidence of hardware testing.

## Preview details

- Catalog ID: `integra/ci1`
- Map version: 1.0
- Verification: not-reviewed
- Protocols: RTU, TCP
- Public preview: 8 registers. Complete in-app availability is not established by this preview.

[JSON preview](https://modbus-monitor.github.io/modbus-device-maps/maps/integra/ci1.json) · [Data terms](https://modbus-monitor.github.io/modbus-device-maps/data-license/)

## Register table (sample)

| Signal | Display address | Data type | Units | Category |
|---|---|---|---|---|
| Hiegyexppow kWh | 400004 | UINT16 | kWh | Energy |
| Loegyimppow Wh | 400001 | UINT16 | kWh | General |
| Hiegyimpvar kVArh | 400006 | UINT16 | kWh | Energy |
| Hiegyexpvar kVArh | 400008 | UINT16 | kWh | Energy |
| Hiegyimppow kh | 400002 | UINT16 | - | General |
| Loegyexppow Wh | 400003 | UINT16 | kWh | General |
| Loegyimpvar VArh | 400005 | UINT16 | - | General |
| Loegyexpvar VArh | 400007 | UINT16 | - | General |

## Addressing and setup

Addresses and values above are copied from the public JSON preview. Confirm the exact model, firmware, register function, address base, word order, scaling and units against the manufacturer manual before polling. No manufacturer manual revision or hardware validation is established by this page.

## Use with Modbus Monitor XPF

Check the device-map catalog in your installed XPF version for current map availability and licensing. The software download link does not open this map.

[Get Modbus Monitor XPF](https://docs.quantumbitsolutions.com/downloads-purchase/) · [Request a map or correction](https://github.com/Modbus-Monitor/modbus-device-maps/issues/new/choose) · [Browse all previews](https://docs.quantumbitsolutions.com/modbus-device-maps/)

<script type="application/ld+json">{"@context": "https://schema.org", "@type": "Dataset", "name": "Integra Ci1 public register preview", "description": "Sample register addresses and data types; not a complete map or hardware verification.", "url": "https://docs.quantumbitsolutions.com/modbus-device-maps/previews/integra/ci1/", "license": "https://modbus-monitor.github.io/modbus-device-maps/data-license/", "creator": {"@type": "Organization", "name": "Quantum Bit Solutions", "url": "https://quantumbitsolutions.com/"}, "distribution": {"@type": "DataDownload", "encodingFormat": "application/json", "contentUrl": "https://modbus-monitor.github.io/modbus-device-maps/maps/integra/ci1.json"}}</script>
