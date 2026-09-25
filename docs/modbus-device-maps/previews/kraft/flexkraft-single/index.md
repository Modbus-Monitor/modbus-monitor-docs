---
title: "Kraft FlexKraft Single Modbus register preview"
description: "Sample register addresses and data types for Kraft FlexKraft Single. Public preview with JSON source and verification status."
---

# Kraft FlexKraft Single Modbus register preview

Public preview for **Kraft FlexKraft Single** (Power Meter).
This sample is not a complete map or evidence of hardware testing.

## Preview details

- Catalog ID: `kraft/flexkraft-single`
- Map version: 1.0
- Verification: not-reviewed
- Protocols: RTU, TCP
- Public preview: 8 registers. Complete in-app availability is not established by this preview.

[JSON preview](https://modbus-monitor.github.io/modbus-device-maps/maps/kraft/flexkraft-single.json) · [Data terms](https://modbus-monitor.github.io/modbus-device-maps/data-license/)

## Register table (sample)

| Signal | Display address | Data type | Units | Category |
|---|---|---|---|---|
| Long status sensor | 300016 | UINT32 | - | Status |
| Flow speed ms | 300000 | FLOAT32 | - | General |
| Long status device | 300018 | UINT32 | - | Status |
| Volume flow m3 s | 300002 | FLOAT32 | - | General |
| Mass flow kgs | 300004 | FLOAT32 | - | General |
| Operating time s | 300006 | FLOAT32 | - | General |
| Counter 1 m3 | 300008 | FLOAT64 | - | General |
| Counter 2 m3 | 300012 | FLOAT64 | - | General |

## Addressing and setup

Addresses and values above are copied from the public JSON preview. Confirm the exact model, firmware, register function, address base, word order, scaling and units against the manufacturer manual before polling. No manufacturer manual revision or hardware validation is established by this page.

## Use with Modbus Monitor XPF

Check the device-map catalog in your installed XPF version for current map availability and licensing. The software download link does not open this map.

[Get Modbus Monitor XPF](https://docs.quantumbitsolutions.com/downloads-purchase/) · [Request a map or correction](https://github.com/Modbus-Monitor/modbus-device-maps/issues/new/choose) · [Browse all previews](https://docs.quantumbitsolutions.com/modbus-device-maps/)

<script type="application/ld+json">{"@context": "https://schema.org", "@type": "Dataset", "name": "Kraft FlexKraft Single public register preview", "description": "Sample register addresses and data types; not a complete map or hardware verification.", "url": "https://docs.quantumbitsolutions.com/modbus-device-maps/previews/kraft/flexkraft-single/", "license": "https://modbus-monitor.github.io/modbus-device-maps/data-license/", "creator": {"@type": "Organization", "name": "Quantum Bit Solutions", "url": "https://quantumbitsolutions.com/"}, "distribution": {"@type": "DataDownload", "encodingFormat": "application/json", "contentUrl": "https://modbus-monitor.github.io/modbus-device-maps/maps/kraft/flexkraft-single.json"}}</script>
