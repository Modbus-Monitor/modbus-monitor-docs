---
title: "I-Real WS0101 Modbus register preview"
description: "Sample register addresses and data types for I-Real WS0101. Public preview with JSON source and verification status."
---

# I-Real WS0101 Modbus register preview

Public preview for **I-Real WS0101** (Power Meter).
This sample is not a complete map or evidence of hardware testing.

## Preview details

- Catalog ID: `i-real/ws0101`
- Map version: 1.0
- Verification: not-reviewed
- Protocols: RTU, TCP
- Public preview: 12 registers. Complete in-app availability is not established by this preview.

[JSON preview](https://modbus-monitor.github.io/modbus-device-maps/maps/i-real/ws0101.json) · [Data terms](https://modbus-monitor.github.io/modbus-device-maps/data-license/)

## Register table (sample)

| Signal | Display address | Data type | Units | Category |
|---|---|---|---|---|
| Current active tariff | 300132 | UINT16 | - | Current |
| Active power total Pt | 300089 | UINT16 | kW | Power |
| Energy counter 1 exponent | 300036 | INT16 | kWh | Energy |
| Internal temperature | 300125 | UINT16 | degC | Temperature |
| Software reference | 300012 | UINT16 | - | General |
| Modbus max register read at once | 300013 | UINT16 | - | Communication |
| Energy counter 2 exponent | 300037 | INT16 | kWh | Energy |
| Energy counter 3 exponent | 300038 | INT16 | kWh | Energy |
| Energy counter 4 exponent | 300039 | INT16 | kWh | Energy |
| Reactive power total Qt | 300097 | UINT16 | kW | Power |
| Apparent power total St | 300105 | INT16 | kW | Power |
| Energy counter 1 | 300133 | INT32 | kWh | Energy |

## Addressing and setup

Addresses and values above are copied from the public JSON preview. Confirm the exact model, firmware, register function, address base, word order, scaling and units against the manufacturer manual before polling. No manufacturer manual revision or hardware validation is established by this page.

## Use with Modbus Monitor XPF

Check the device-map catalog in your installed XPF version for current map availability and licensing. The software download link does not open this map.

[Get Modbus Monitor XPF](https://docs.quantumbitsolutions.com/downloads-purchase/) · [Request a map or correction](https://github.com/Modbus-Monitor/modbus-device-maps/issues/new/choose) · [Browse all previews](https://docs.quantumbitsolutions.com/modbus-device-maps/)

<script type="application/ld+json">{"@context": "https://schema.org", "@type": "Dataset", "name": "I-Real WS0101 public register preview", "description": "Sample register addresses and data types; not a complete map or hardware verification.", "url": "https://docs.quantumbitsolutions.com/modbus-device-maps/previews/i-real/ws0101/", "license": "https://modbus-monitor.github.io/modbus-device-maps/data-license/", "creator": {"@type": "Organization", "name": "Quantum Bit Solutions", "url": "https://quantumbitsolutions.com/"}, "distribution": {"@type": "DataDownload", "encodingFormat": "application/json", "contentUrl": "https://modbus-monitor.github.io/modbus-device-maps/maps/i-real/ws0101.json"}}</script>
