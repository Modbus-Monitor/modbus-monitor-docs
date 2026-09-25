---
title: "Electrex Plus Modbus register preview"
description: "Sample register addresses and data types for Electrex Plus. Public preview with JSON source and verification status."
---

# Electrex Plus Modbus register preview

Public preview for **Electrex Plus** (Power Meter).
This sample is not a complete map or evidence of hardware testing.

## Preview details

- Catalog ID: `electrex/plus`
- Map version: 1.0
- Verification: not-reviewed
- Protocols: RTU, TCP
- Public preview: 12 registers. Complete in-app availability is not established by this preview.

[JSON preview](https://modbus-monitor.github.io/modbus-device-maps/maps/electrex/plus.json) · [Data terms](https://modbus-monitor.github.io/modbus-device-maps/data-license/)

## Register table (sample)

| Signal | Display address | Data type | Units | Category |
|---|---|---|---|---|
| Voltage | 300000 | INT16 | V | Voltage |
| Current | 300002 | INT16 | - | Current |
| Active Power | 300004 | INT16 | kW | Power |
| Active Energy total | 300020 | INT16 | kWh | Energy |
| Power factor | 300010 | INT16 | PF | Power |
| Reactive Energy total | 300023 | INT16 | kWh | Energy |
| Voltage L1 | 300028 | INT16 | V | Voltage |
| Voltage L2 | 300030 | INT16 | V | Voltage |
| Voltage L3 | 300032 | INT16 | V | Voltage |
| Current L1 | 300034 | INT16 | A | Current |
| Current L2 | 300036 | INT16 | A | Current |
| Current L3 | 300038 | INT16 | A | Current |

## Addressing and setup

Addresses and values above are copied from the public JSON preview. Confirm the exact model, firmware, register function, address base, word order, scaling and units against the manufacturer manual before polling. No manufacturer manual revision or hardware validation is established by this page.

## Use with Modbus Monitor XPF

Check the device-map catalog in your installed XPF version for current map availability and licensing. The software download link does not open this map.

[Get Modbus Monitor XPF](https://docs.quantumbitsolutions.com/downloads-purchase/) · [Request a map or correction](https://github.com/Modbus-Monitor/modbus-device-maps/issues/new/choose) · [Browse all previews](https://docs.quantumbitsolutions.com/modbus-device-maps/)

<script type="application/ld+json">{"@context": "https://schema.org", "@type": "Dataset", "name": "Electrex Plus public register preview", "description": "Sample register addresses and data types; not a complete map or hardware verification.", "url": "https://docs.quantumbitsolutions.com/modbus-device-maps/previews/electrex/plus/", "license": "https://modbus-monitor.github.io/modbus-device-maps/data-license/", "creator": {"@type": "Organization", "name": "Quantum Bit Solutions", "url": "https://quantumbitsolutions.com/"}, "distribution": {"@type": "DataDownload", "encodingFormat": "application/json", "contentUrl": "https://modbus-monitor.github.io/modbus-device-maps/maps/electrex/plus.json"}}</script>
