---
title: "ENTES EPR04 Modbus register preview"
description: "Sample register addresses and data types for ENTES EPR04. Public preview with JSON source and verification status."
---

# ENTES EPR04 Modbus register preview

Public preview for **ENTES EPR04** (Power Meter).
This sample is not a complete map or evidence of hardware testing.

## Preview details

- Catalog ID: `entes/epr04`
- Map version: 1.0
- Verification: not-reviewed
- Protocols: RTU, TCP
- Public preview: 12 registers. Complete in-app availability is not established by this preview.

[JSON preview](https://modbus-monitor.github.io/modbus-device-maps/maps/entes/epr04.json) · [Data terms](https://modbus-monitor.github.io/modbus-device-maps/data-license/)

## Register table (sample)

| Signal | Display address | Data type | Units | Category |
|---|---|---|---|---|
| Voltage transformer ratio | 432768 | INT16 | V | Voltage |
| Current transformer ratio | 432769 | INT16 | - | Current |
| L1 phase active power Watt | 400020 | INT32 | kW | Power |
| Import active energy 1 Wh | 400088 | INT64 | kWh | Energy |
| Frequency Hz | 400058 | UINT32 | Hz | Frequency |
| Demand time minute | 432771 | INT16 | kW | Demand |
| L1 phase cos | 400038 | INT32 | - | General |
| Communication address | 432777 | INT16 | - | Communication |
| L2 phase active power Watt | 400022 | INT32 | kW | Power |
| L3 phase active power Watt | 400024 | INT32 | kW | Power |
| L1 phase reactive power Var | 400026 | INT32 | kW | Power |
| L2 phase reactive power Var | 400028 | INT32 | kW | Power |

## Addressing and setup

Addresses and values above are copied from the public JSON preview. Confirm the exact model, firmware, register function, address base, word order, scaling and units against the manufacturer manual before polling. No manufacturer manual revision or hardware validation is established by this page.

## Use with Modbus Monitor XPF

Check the device-map catalog in your installed XPF version for current map availability and licensing. The software download link does not open this map.

[Get Modbus Monitor XPF](https://docs.quantumbitsolutions.com/downloads-purchase/) · [Request a map or correction](https://github.com/Modbus-Monitor/modbus-device-maps/issues/new/choose) · [Browse all previews](https://docs.quantumbitsolutions.com/modbus-device-maps/)

<script type="application/ld+json">{"@context": "https://schema.org", "@type": "Dataset", "name": "ENTES EPR04 public register preview", "description": "Sample register addresses and data types; not a complete map or hardware verification.", "url": "https://docs.quantumbitsolutions.com/modbus-device-maps/previews/entes/epr04/", "license": "https://modbus-monitor.github.io/modbus-device-maps/data-license/", "creator": {"@type": "Organization", "name": "Quantum Bit Solutions", "url": "https://quantumbitsolutions.com/"}, "distribution": {"@type": "DataDownload", "encodingFormat": "application/json", "contentUrl": "https://modbus-monitor.github.io/modbus-device-maps/maps/entes/epr04.json"}}</script>
