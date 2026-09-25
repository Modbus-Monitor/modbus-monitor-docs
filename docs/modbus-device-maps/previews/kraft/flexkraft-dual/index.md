---
title: "Kraft FlexKraft Dual Modbus register preview"
description: "Sample register addresses and data types for Kraft FlexKraft Dual. Public preview with JSON source and verification status."
---

# Kraft FlexKraft Dual Modbus register preview

Public preview for **Kraft FlexKraft Dual** (Power Meter).
This sample is not a complete map or evidence of hardware testing.

## Preview details

- Catalog ID: `kraft/flexkraft-dual`
- Map version: 1.0
- Verification: not-reviewed
- Protocols: RTU, TCP
- Public preview: 12 registers. Complete in-app availability is not established by this preview.

[JSON preview](https://modbus-monitor.github.io/modbus-device-maps/maps/kraft/flexkraft-dual.json) · [Data terms](https://modbus-monitor.github.io/modbus-device-maps/data-license/)

## Register table (sample)

| Signal | Display address | Data type | Units | Category |
|---|---|---|---|---|
| Output voltage V | 300004 | INT16 | V | Voltage |
| Output current A | 300005 | INT16 | - | Current |
| Status register | 300001 | UINT16 | - | Status |
| Warnings register | 300002 | UINT16 | - | General |
| Alarms register | 300003 | UINT16 | - | Status |
| Output voltage A V | 300004 | INT16 | V | Voltage |
| Output current A A | 300005 | INT16 | - | Current |
| Output voltage B V | 300006 | INT16 | V | Voltage |
| Output current B A | 300007 | INT16 | - | Current |
| Process time s | 300006 | UINT32 | - | General |
| Ah Ah | 300008 | UINT32 | - | General |
| Process time s | 300008 | UINT32 | - | General |

## Addressing and setup

Addresses and values above are copied from the public JSON preview. Confirm the exact model, firmware, register function, address base, word order, scaling and units against the manufacturer manual before polling. No manufacturer manual revision or hardware validation is established by this page.

## Use with Modbus Monitor XPF

Check the device-map catalog in your installed XPF version for current map availability and licensing. The software download link does not open this map.

[Get Modbus Monitor XPF](https://docs.quantumbitsolutions.com/downloads-purchase/) · [Request a map or correction](https://github.com/Modbus-Monitor/modbus-device-maps/issues/new/choose) · [Browse all previews](https://docs.quantumbitsolutions.com/modbus-device-maps/)

<script type="application/ld+json">{"@context": "https://schema.org", "@type": "Dataset", "name": "Kraft FlexKraft Dual public register preview", "description": "Sample register addresses and data types; not a complete map or hardware verification.", "url": "https://docs.quantumbitsolutions.com/modbus-device-maps/previews/kraft/flexkraft-dual/", "license": "https://modbus-monitor.github.io/modbus-device-maps/data-license/", "creator": {"@type": "Organization", "name": "Quantum Bit Solutions", "url": "https://quantumbitsolutions.com/"}, "distribution": {"@type": "DataDownload", "encodingFormat": "application/json", "contentUrl": "https://modbus-monitor.github.io/modbus-device-maps/maps/kraft/flexkraft-dual.json"}}</script>
