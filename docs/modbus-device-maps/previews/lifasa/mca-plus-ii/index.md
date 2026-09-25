---
title: "Lifasa MCA PLUS II Modbus register preview"
description: "Sample register addresses and data types for Lifasa MCA PLUS II. Public preview with JSON source and verification status."
---

# Lifasa MCA PLUS II Modbus register preview

Public preview for **Lifasa MCA PLUS II** (Power Meter).
This sample is not a complete map or evidence of hardware testing.

## Preview details

- Catalog ID: `lifasa/mca-plus-ii`
- Map version: 1.0
- Verification: not-reviewed
- Protocols: RTU, TCP
- Public preview: 12 registers. Complete in-app availability is not established by this preview.

[JSON preview](https://modbus-monitor.github.io/modbus-device-maps/maps/lifasa/mca-plus-ii.json) · [Data terms](https://modbus-monitor.github.io/modbus-device-maps/data-license/)

## Register table (sample)

| Signal | Display address | Data type | Units | Category |
|---|---|---|---|---|
| L1 phase voltage V | 300000 | UINT32 | V | Voltage |
| L1 current mA | 300002 | UINT32 | - | Current |
| L1 active power W | 300004 | UINT32 | kW | Power |
| Consumed active energy kW DC-DD | 300094 | UINT32 | kWh | Energy |
| L1 frequency Hz | 300060 | UINT32 | Hz | Frequency |
| Maximum demand I AVG mA | 300086 | UINT32 | kW | Demand |
| 2nd order harmonic | 302634 | UINT32 | - | Harmonics |
| Cos L1 | 300014 | UINT32 | - | General |
| L1 inductive power var | 300006 | UINT32 | kW | Power |
| L1 capacitive power var | 300008 | UINT32 | kW | Power |
| L1 apparent power VA | 300010 | UINT32 | kW | Power |
| L1 power factor | 300012 | UINT32 | PF | Power |

## Addressing and setup

Addresses and values above are copied from the public JSON preview. Confirm the exact model, firmware, register function, address base, word order, scaling and units against the manufacturer manual before polling. No manufacturer manual revision or hardware validation is established by this page.

## Use with Modbus Monitor XPF

Check the device-map catalog in your installed XPF version for current map availability and licensing. The software download link does not open this map.

[Get Modbus Monitor XPF](https://docs.quantumbitsolutions.com/downloads-purchase/) · [Request a map or correction](https://github.com/Modbus-Monitor/modbus-device-maps/issues/new/choose) · [Browse all previews](https://docs.quantumbitsolutions.com/modbus-device-maps/)

<script type="application/ld+json">{"@context": "https://schema.org", "@type": "Dataset", "name": "Lifasa MCA PLUS II public register preview", "description": "Sample register addresses and data types; not a complete map or hardware verification.", "url": "https://docs.quantumbitsolutions.com/modbus-device-maps/previews/lifasa/mca-plus-ii/", "license": "https://modbus-monitor.github.io/modbus-device-maps/data-license/", "creator": {"@type": "Organization", "name": "Quantum Bit Solutions", "url": "https://quantumbitsolutions.com/"}, "distribution": {"@type": "DataDownload", "encodingFormat": "application/json", "contentUrl": "https://modbus-monitor.github.io/modbus-device-maps/maps/lifasa/mca-plus-ii.json"}}</script>
