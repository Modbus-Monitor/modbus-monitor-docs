---
title: "EDME Genius Mk6 Modbus register preview"
description: "Sample register addresses and data types for EDME Genius Mk6. Public preview with JSON source and verification status."
---

# EDME Genius Mk6 Modbus register preview

Public preview for **EDME Genius Mk6** (Power Meter).
This sample is not a complete map or evidence of hardware testing.

## Preview details

- Catalog ID: `edme/genius-mk6`
- Map version: 1.0
- Verification: not-reviewed
- Protocols: RTU, TCP
- Public preview: 12 registers. Complete in-app availability is not established by this preview.

[JSON preview](https://modbus-monitor.github.io/modbus-device-maps/maps/edme/genius-mk6.json) · [Data terms](https://modbus-monitor.github.io/modbus-device-maps/data-license/)

## Register table (sample)

| Signal | Display address | Data type | Units | Category |
|---|---|---|---|---|
| Phase A voltage | 309001 | FLOAT32 | V | Voltage |
| Phase A current | 309007 | FLOAT32 | - | Current |
| Power factor | 309043 | FLOAT32 | PF | Power |
| Frequency | 309037 | FLOAT32 | Hz | Frequency |
| Phase angle of A phase | 309013 | FLOAT32 | - | General |
| Phase B voltage | 309003 | FLOAT32 | V | Voltage |
| Phase C voltage | 309005 | FLOAT32 | V | Voltage |
| Phase B current | 309009 | FLOAT32 | - | Current |
| Phase C current | 309011 | FLOAT32 | - | Current |
| Phase angle of B phase | 309015 | FLOAT32 | - | General |
| Phase angle of C phase | 309017 | FLOAT32 | - | General |
| Phase A watts | 309019 | FLOAT32 | - | General |

## Addressing and setup

Addresses and values above are copied from the public JSON preview. Confirm the exact model, firmware, register function, address base, word order, scaling and units against the manufacturer manual before polling. No manufacturer manual revision or hardware validation is established by this page.

## Use with Modbus Monitor XPF

Check the device-map catalog in your installed XPF version for current map availability and licensing. The software download link does not open this map.

[Get Modbus Monitor XPF](https://docs.quantumbitsolutions.com/downloads-purchase/) · [Request a map or correction](https://github.com/Modbus-Monitor/modbus-device-maps/issues/new/choose) · [Browse all previews](https://docs.quantumbitsolutions.com/modbus-device-maps/)

<script type="application/ld+json">{"@context": "https://schema.org", "@type": "Dataset", "name": "EDME Genius Mk6 public register preview", "description": "Sample register addresses and data types; not a complete map or hardware verification.", "url": "https://docs.quantumbitsolutions.com/modbus-device-maps/previews/edme/genius-mk6/", "license": "https://modbus-monitor.github.io/modbus-device-maps/data-license/", "creator": {"@type": "Organization", "name": "Quantum Bit Solutions", "url": "https://quantumbitsolutions.com/"}, "distribution": {"@type": "DataDownload", "encodingFormat": "application/json", "contentUrl": "https://modbus-monitor.github.io/modbus-device-maps/maps/edme/genius-mk6.json"}}</script>
