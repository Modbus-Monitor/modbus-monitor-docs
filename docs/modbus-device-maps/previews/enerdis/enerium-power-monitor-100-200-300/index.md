---
title: "Enerdis Enerium Power Monitor 100-200-300 Modbus register preview"
description: "Sample register addresses and data types for Enerdis Enerium Power Monitor 100-200-300. Public preview with JSON source and verification status."
---

# Enerdis Enerium Power Monitor 100-200-300 Modbus register preview

Public preview for **Enerdis Enerium Power Monitor 100-200-300** (Power Meter).
This sample is not a complete map or evidence of hardware testing.

## Preview details

- Catalog ID: `enerdis/enerium-power-monitor-100-200-300`
- Map version: 1.0
- Verification: not-reviewed
- Protocols: RTU, TCP
- Public preview: 12 registers. Complete in-app availability is not established by this preview.

[JSON preview](https://modbus-monitor.github.io/modbus-device-maps/maps/enerdis/enerium-power-monitor-100-200-300.json) · [Data terms](https://modbus-monitor.github.io/modbus-device-maps/data-license/)

## Register table (sample)

| Signal | Display address | Data type | Units | Category |
|---|---|---|---|---|
| Voltage unbalance | 401348 | INT16 | V | Voltage |
| Output 2 min Current | 427802 | INT16 | - | Current |
| Active energy receiver mode | 402454 | UINT32 | kWh | Energy |
| Frequency Hz | 401349 | UINT16 | Hz | Frequency |
| Maxima of mean thd V1 | 403072 | UINT32 | - | Harmonics |
| Output 2 min Quantity | 427798 | INT32 | - | General |
| Output 2 max Current | 427803 | INT16 | - | Current |
| Frequency Hz | 401352 | UINT16 | Hz | Frequency |
| Minima of frequency Hz | 402848 | UINT32 | Hz | Frequency |
| Date of minima of frequency | 402850 | UINT32 | Hz | Frequency |
| Maxima of frequency Hz | 402992 | UINT32 | Hz | Frequency |
| Date of maxima of frequency | 402994 | UINT32 | Hz | Frequency |

## Addressing and setup

Addresses and values above are copied from the public JSON preview. Confirm the exact model, firmware, register function, address base, word order, scaling and units against the manufacturer manual before polling. No manufacturer manual revision or hardware validation is established by this page.

## Use with Modbus Monitor XPF

Check the device-map catalog in your installed XPF version for current map availability and licensing. The software download link does not open this map.

[Get Modbus Monitor XPF](https://docs.quantumbitsolutions.com/downloads-purchase/) · [Request a map or correction](https://github.com/Modbus-Monitor/modbus-device-maps/issues/new/choose) · [Browse all previews](https://docs.quantumbitsolutions.com/modbus-device-maps/)

<script type="application/ld+json">{"@context": "https://schema.org", "@type": "Dataset", "name": "Enerdis Enerium Power Monitor 100-200-300 public register preview", "description": "Sample register addresses and data types; not a complete map or hardware verification.", "url": "https://docs.quantumbitsolutions.com/modbus-device-maps/previews/enerdis/enerium-power-monitor-100-200-300/", "license": "https://modbus-monitor.github.io/modbus-device-maps/data-license/", "creator": {"@type": "Organization", "name": "Quantum Bit Solutions", "url": "https://quantumbitsolutions.com/"}, "distribution": {"@type": "DataDownload", "encodingFormat": "application/json", "contentUrl": "https://modbus-monitor.github.io/modbus-device-maps/maps/enerdis/enerium-power-monitor-100-200-300.json"}}</script>
