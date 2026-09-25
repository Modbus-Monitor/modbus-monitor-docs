---
title: "Tyco Electronics Integra 1630 Modbus register preview"
description: "Sample register addresses and data types for Tyco Electronics Integra 1630. Public preview with JSON source and verification status."
---

# Tyco Electronics Integra 1630 Modbus register preview

Public preview for **Tyco Electronics Integra 1630** (Power Meter).
This sample is not a complete map or evidence of hardware testing.

## Preview details

- Catalog ID: `tyco-electronics/integra-1630`
- Map version: 1.0
- Verification: not-reviewed
- Protocols: RTU, TCP
- Public preview: 12 registers. Complete in-app availability is not established by this preview.

[JSON preview](https://modbus-monitor.github.io/modbus-device-maps/maps/tyco-electronics/integra-1630.json) · [Data terms](https://modbus-monitor.github.io/modbus-device-maps/data-license/)

## Register table (sample)

| Signal | Display address | Data type | Units | Category |
|---|---|---|---|---|
| V L1 L2 | 300200 | FLOAT32 | - | Voltage |
| Current 1 | 300006 | FLOAT32 | - | Current |
| Power factor phase 1 | 300030 | FLOAT32 | PF | Power |
| Frequency | 300070 | FLOAT32 | Hz | Frequency |
| W demand import | 300084 | FLOAT32 | kW | Demand |
| Thd volts 1 | 300234 | FLOAT32 | - | Harmonics |
| Volts 1 L1 N 4w or L1 L2 3w | 300000 | FLOAT32 | - | General |
| Wh import | 300072 | FLOAT32 | kWh | Communication |
| Current 2 | 300008 | FLOAT32 | - | Current |
| Current 3 | 300010 | FLOAT32 | - | Current |
| Power factor phase 2 | 300032 | FLOAT32 | PF | Power |
| Power factor phase 3 | 300034 | FLOAT32 | PF | Power |

## Addressing and setup

Addresses and values above are copied from the public JSON preview. Confirm the exact model, firmware, register function, address base, word order, scaling and units against the manufacturer manual before polling. No manufacturer manual revision or hardware validation is established by this page.

## Use with Modbus Monitor XPF

Check the device-map catalog in your installed XPF version for current map availability and licensing. The software download link does not open this map.

[Get Modbus Monitor XPF](https://docs.quantumbitsolutions.com/downloads-purchase/) · [Request a map or correction](https://github.com/Modbus-Monitor/modbus-device-maps/issues/new/choose) · [Browse all previews](https://docs.quantumbitsolutions.com/modbus-device-maps/)

<script type="application/ld+json">{"@context": "https://schema.org", "@type": "Dataset", "name": "Tyco Electronics Integra 1630 public register preview", "description": "Sample register addresses and data types; not a complete map or hardware verification.", "url": "https://docs.quantumbitsolutions.com/modbus-device-maps/previews/tyco-electronics/integra-1630/", "license": "https://modbus-monitor.github.io/modbus-device-maps/data-license/", "creator": {"@type": "Organization", "name": "Quantum Bit Solutions", "url": "https://quantumbitsolutions.com/"}, "distribution": {"@type": "DataDownload", "encodingFormat": "application/json", "contentUrl": "https://modbus-monitor.github.io/modbus-device-maps/maps/tyco-electronics/integra-1630.json"}}</script>
