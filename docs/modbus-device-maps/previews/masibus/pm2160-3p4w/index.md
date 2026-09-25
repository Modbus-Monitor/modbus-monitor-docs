---
title: "Masibus PM2160-3P4W Modbus register preview"
description: "Sample register addresses and data types for Masibus PM2160-3P4W. Public preview with JSON source and verification status."
---

# Masibus PM2160-3P4W Modbus register preview

Public preview for **Masibus PM2160-3P4W** (Power Meter).
This sample is not a complete map or evidence of hardware testing.

## Preview details

- Catalog ID: `masibus/pm2160-3p4w`
- Map version: 1.0
- Verification: not-reviewed
- Protocols: RTU, TCP
- Public preview: 12 registers. Complete in-app availability is not established by this preview.

[JSON preview](https://modbus-monitor.github.io/modbus-device-maps/maps/masibus/pm2160-3p4w.json) · [Data terms](https://modbus-monitor.github.io/modbus-device-maps/data-license/)

## Register table (sample)

| Signal | Display address | Data type | Units | Category |
|---|---|---|---|---|
| Frequency | 300000 | UINT32 | Hz | Frequency |
| 1 Pf | 300002 | UINT32 | - | Power Factor |
| Rising demand | 300098 | UINT32 | kW | Demand |
| Total vrthd | 300213 | UINT32 | - | Harmonics |
| 1 Vrms | 300010 | UINT32 | - | General |
| 1wh import | 300058 | UINT32 | kWh | Communication |
| 2 Pf | 300004 | UINT32 | - | Power Factor |
| 3 Pf | 300006 | UINT32 | - | Power Factor |
| A Pf | 300008 | UINT32 | - | Power Factor |
| Maximum demand | 300104 | UINT32 | kW | Demand |
| Total vythd | 300229 | UINT32 | - | Harmonics |
| Total vbthd | 300245 | UINT32 | - | Harmonics |

## Addressing and setup

Addresses and values above are copied from the public JSON preview. Confirm the exact model, firmware, register function, address base, word order, scaling and units against the manufacturer manual before polling. No manufacturer manual revision or hardware validation is established by this page.

## Use with Modbus Monitor XPF

Check the device-map catalog in your installed XPF version for current map availability and licensing. The software download link does not open this map.

[Get Modbus Monitor XPF](https://docs.quantumbitsolutions.com/downloads-purchase/) · [Request a map or correction](https://github.com/Modbus-Monitor/modbus-device-maps/issues/new/choose) · [Browse all previews](https://docs.quantumbitsolutions.com/modbus-device-maps/)

<script type="application/ld+json">{"@context": "https://schema.org", "@type": "Dataset", "name": "Masibus PM2160-3P4W public register preview", "description": "Sample register addresses and data types; not a complete map or hardware verification.", "url": "https://docs.quantumbitsolutions.com/modbus-device-maps/previews/masibus/pm2160-3p4w/", "license": "https://modbus-monitor.github.io/modbus-device-maps/data-license/", "creator": {"@type": "Organization", "name": "Quantum Bit Solutions", "url": "https://quantumbitsolutions.com/"}, "distribution": {"@type": "DataDownload", "encodingFormat": "application/json", "contentUrl": "https://modbus-monitor.github.io/modbus-device-maps/maps/masibus/pm2160-3p4w.json"}}</script>
