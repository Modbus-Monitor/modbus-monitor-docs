---
title: "Allen Bradley PowerMonitor 3000 Modbus register preview"
description: "Sample register addresses and data types for Allen Bradley PowerMonitor 3000. Public preview with JSON source and verification status."
---

# Allen Bradley PowerMonitor 3000 Modbus register preview

Public preview for **Allen Bradley PowerMonitor 3000** (Power Meter).
This sample is not a complete map or evidence of hardware testing.

## Preview details

- Catalog ID: `allen-bradley/powermonitor-3000`
- Map version: 1.0
- Verification: not-reviewed
- Protocols: RTU, TCP
- Public preview: 12 registers. Complete in-app availability is not established by this preview.

[JSON preview](https://modbus-monitor.github.io/modbus-device-maps/maps/allen-bradley/powermonitor-3000.json) · [Data terms](https://modbus-monitor.github.io/modbus-device-maps/data-license/)

## Register table (sample)

| Signal | Display address | Data type | Units | Category |
|---|---|---|---|---|
| L1 N voltage V | 300108 | UINT32 | V | Voltage |
| L1 current A | 300100 | UINT32 | - | Current |
| L1 real power VA | 300300 | UINT32 | kW | Power |
| Frequency last cycle Hz | 300124 | UINT32 | Hz | Frequency |
| Three phase true pf | 300506 | UINT32 | - | Power Factor |
| Projected demand I | 300408 | UINT32 | kW | Demand |
| Metering iteration | 300126 | UINT32 | - | General |
| L2 current A | 300102 | UINT32 | - | Current |
| L3 current A | 300104 | UINT32 | - | Current |
| Avg Current A | 300106 | UINT32 | - | Current |
| L2 N voltage V | 300110 | UINT32 | V | Voltage |
| L3 N voltage V | 300112 | UINT32 | V | Voltage |

## Addressing and setup

Addresses and values above are copied from the public JSON preview. Confirm the exact model, firmware, register function, address base, word order, scaling and units against the manufacturer manual before polling. No manufacturer manual revision or hardware validation is established by this page.

## Use with Modbus Monitor XPF

Check the device-map catalog in your installed XPF version for current map availability and licensing. The software download link does not open this map.

[Get Modbus Monitor XPF](https://docs.quantumbitsolutions.com/downloads-purchase/) · [Request a map or correction](https://github.com/Modbus-Monitor/modbus-device-maps/issues/new/choose) · [Browse all previews](https://docs.quantumbitsolutions.com/modbus-device-maps/)

<script type="application/ld+json">{"@context": "https://schema.org", "@type": "Dataset", "name": "Allen Bradley PowerMonitor 3000 public register preview", "description": "Sample register addresses and data types; not a complete map or hardware verification.", "url": "https://docs.quantumbitsolutions.com/modbus-device-maps/previews/allen-bradley/powermonitor-3000/", "license": "https://modbus-monitor.github.io/modbus-device-maps/data-license/", "creator": {"@type": "Organization", "name": "Quantum Bit Solutions", "url": "https://quantumbitsolutions.com/"}, "distribution": {"@type": "DataDownload", "encodingFormat": "application/json", "contentUrl": "https://modbus-monitor.github.io/modbus-device-maps/maps/allen-bradley/powermonitor-3000.json"}}</script>
