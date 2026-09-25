---
title: "Electrex Est Modbus register preview"
description: "Sample register addresses and data types for Electrex Est. Public preview with JSON source and verification status."
---

# Electrex Est Modbus register preview

Public preview for **Electrex Est** (Power Meter).
This sample is not a complete map or evidence of hardware testing.

## Preview details

- Catalog ID: `electrex/est`
- Map version: 1.0
- Verification: not-reviewed
- Protocols: RTU, TCP
- Public preview: 12 registers. Complete in-app availability is not established by this preview.

[JSON preview](https://modbus-monitor.github.io/modbus-device-maps/maps/electrex/est.json) · [Data terms](https://modbus-monitor.github.io/modbus-device-maps/data-license/)

## Register table (sample)

| Signal | Display address | Data type | Units | Category |
|---|---|---|---|---|
| Voltage | 300000 | INT16 | V | Voltage |
| Current | 300002 | INT16 | - | Current |
| Active Power | 300004 | INT16 | kW | Power |
| Active Energy total | 300020 | INT16 | kWh | Energy |
| Frequency | 300046 | INT16 | Hz | Frequency |
| Pm | 300012 | INT16 | - | General |
| Reactive Power | 300006 | INT16 | kW | Power |
| Apparent Power | 300008 | INT16 | kW | Power |
| Power factor | 300010 | INT16 | PF | Power |
| Active Power Maximum Demand | 300016 | INT16 | kW | Power |
| Reactive Power Maximum Demand | 300018 | INT16 | kW | Power |
| Reactive Energy total | 300023 | INT16 | kWh | Energy |

## Addressing and setup

Addresses and values above are copied from the public JSON preview. Confirm the exact model, firmware, register function, address base, word order, scaling and units against the manufacturer manual before polling. No manufacturer manual revision or hardware validation is established by this page.

## Use with Modbus Monitor XPF

Check the device-map catalog in your installed XPF version for current map availability and licensing. The software download link does not open this map.

[Get Modbus Monitor XPF](https://docs.quantumbitsolutions.com/downloads-purchase/) · [Request a map or correction](https://github.com/Modbus-Monitor/modbus-device-maps/issues/new/choose) · [Browse all previews](https://docs.quantumbitsolutions.com/modbus-device-maps/)

<script type="application/ld+json">{"@context": "https://schema.org", "@type": "Dataset", "name": "Electrex Est public register preview", "description": "Sample register addresses and data types; not a complete map or hardware verification.", "url": "https://docs.quantumbitsolutions.com/modbus-device-maps/previews/electrex/est/", "license": "https://modbus-monitor.github.io/modbus-device-maps/data-license/", "creator": {"@type": "Organization", "name": "Quantum Bit Solutions", "url": "https://quantumbitsolutions.com/"}, "distribution": {"@type": "DataDownload", "encodingFormat": "application/json", "contentUrl": "https://modbus-monitor.github.io/modbus-device-maps/maps/electrex/est.json"}}</script>
