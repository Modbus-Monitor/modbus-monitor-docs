---
title: "Larsen Toubro Quasar Modbus register preview"
description: "Sample register addresses and data types for Larsen Toubro Quasar. Public preview with JSON source and verification status."
---

# Larsen Toubro Quasar Modbus register preview

Public preview for **Larsen Toubro Quasar** (Power Meter).
This sample is not a complete map or evidence of hardware testing.

## Preview details

- Catalog ID: `larsen-toubro/quasar`
- Map version: 1.0
- Verification: not-reviewed
- Protocols: RTU, TCP
- Public preview: 12 registers. Complete in-app availability is not established by this preview.

[JSON preview](https://modbus-monitor.github.io/modbus-device-maps/maps/larsen-toubro/quasar.json) · [Data terms](https://modbus-monitor.github.io/modbus-device-maps/data-license/)

## Register table (sample)

| Signal | Display address | Data type | Units | Category |
|---|---|---|---|---|
| Phase 1 voltage | 300000 | UINT32 | V | Voltage |
| Phase 1 current | 300006 | UINT32 | - | Current |
| Phase 1 active power | 300012 | UINT32 | kW | Power |
| Cumulative energy forward kVAh | 300512 | UINT32 | kWh | Energy |
| Phase 2 voltage | 300002 | UINT32 | V | Voltage |
| Phase 3 voltage | 300004 | UINT32 | V | Voltage |
| Phase 2 current | 300008 | UINT32 | - | Current |
| Phase 3 current | 300010 | UINT32 | - | Current |
| Phase 2 active power | 300014 | UINT32 | kW | Power |
| Phase 3 active power | 300016 | UINT32 | kW | Power |
| Phase 1 reactive power | 300018 | UINT32 | kW | Power |
| Phase 2 reactive power | 300020 | UINT32 | kW | Power |

## Addressing and setup

Addresses and values above are copied from the public JSON preview. Confirm the exact model, firmware, register function, address base, word order, scaling and units against the manufacturer manual before polling. No manufacturer manual revision or hardware validation is established by this page.

## Use with Modbus Monitor XPF

Check the device-map catalog in your installed XPF version for current map availability and licensing. The software download link does not open this map.

[Get Modbus Monitor XPF](https://docs.quantumbitsolutions.com/downloads-purchase/) · [Request a map or correction](https://github.com/Modbus-Monitor/modbus-device-maps/issues/new/choose) · [Browse all previews](https://docs.quantumbitsolutions.com/modbus-device-maps/)

<script type="application/ld+json">{"@context": "https://schema.org", "@type": "Dataset", "name": "Larsen Toubro Quasar public register preview", "description": "Sample register addresses and data types; not a complete map or hardware verification.", "url": "https://docs.quantumbitsolutions.com/modbus-device-maps/previews/larsen-toubro/quasar/", "license": "https://modbus-monitor.github.io/modbus-device-maps/data-license/", "creator": {"@type": "Organization", "name": "Quantum Bit Solutions", "url": "https://quantumbitsolutions.com/"}, "distribution": {"@type": "DataDownload", "encodingFormat": "application/json", "contentUrl": "https://modbus-monitor.github.io/modbus-device-maps/maps/larsen-toubro/quasar.json"}}</script>
