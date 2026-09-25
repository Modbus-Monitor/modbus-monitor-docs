---
title: "Lifasa Master Control Var Modbus register preview"
description: "Sample register addresses and data types for Lifasa Master Control Var. Public preview with JSON source and verification status."
---

# Lifasa Master Control Var Modbus register preview

Public preview for **Lifasa Master Control Var** (Power Meter).
This sample is not a complete map or evidence of hardware testing.

## Preview details

- Catalog ID: `lifasa/master-control-var`
- Map version: 1.0
- Verification: not-reviewed
- Protocols: RTU, TCP
- Public preview: 12 registers. Complete in-app availability is not established by this preview.

[JSON preview](https://modbus-monitor.github.io/modbus-device-maps/maps/lifasa/master-control-var.json) · [Data terms](https://modbus-monitor.github.io/modbus-device-maps/data-license/)

## Register table (sample)

| Signal | Display address | Data type | Units | Category |
|---|---|---|---|---|
| L1 phase voltage V | 300000 | UINT32 | V | Voltage |
| L1 current mA | 300002 | UINT32 | - | Current |
| L1 active power W | 300004 | UINT32 | kW | Power |
| Active energy consumed kWh kWh | 300136 | UINT32 | kWh | Energy |
| Frequency Hz | 300104 | UINT32 | Hz | Frequency |
| Alarm variable | 301541 | UINT32 | - | Status |
| Temperature C | 300116 | UINT32 | degC | Temperature |
| L1 cos | 300020 | UINT32 | - | General |
| L1 inductive reactive power varL | 300006 | UINT32 | kW | Power |
| L1 capacitive reactive power varC | 300008 | UINT32 | kW | Power |
| L1 reactive power var | 300010 | UINT32 | kW | Power |
| L1 apparent power VA | 300012 | UINT32 | kW | Power |

## Addressing and setup

Addresses and values above are copied from the public JSON preview. Confirm the exact model, firmware, register function, address base, word order, scaling and units against the manufacturer manual before polling. No manufacturer manual revision or hardware validation is established by this page.

## Use with Modbus Monitor XPF

Check the device-map catalog in your installed XPF version for current map availability and licensing. The software download link does not open this map.

[Get Modbus Monitor XPF](https://docs.quantumbitsolutions.com/downloads-purchase/) · [Request a map or correction](https://github.com/Modbus-Monitor/modbus-device-maps/issues/new/choose) · [Browse all previews](https://docs.quantumbitsolutions.com/modbus-device-maps/)

<script type="application/ld+json">{"@context": "https://schema.org", "@type": "Dataset", "name": "Lifasa Master Control Var public register preview", "description": "Sample register addresses and data types; not a complete map or hardware verification.", "url": "https://docs.quantumbitsolutions.com/modbus-device-maps/previews/lifasa/master-control-var/", "license": "https://modbus-monitor.github.io/modbus-device-maps/data-license/", "creator": {"@type": "Organization", "name": "Quantum Bit Solutions", "url": "https://quantumbitsolutions.com/"}, "distribution": {"@type": "DataDownload", "encodingFormat": "application/json", "contentUrl": "https://modbus-monitor.github.io/modbus-device-maps/maps/lifasa/master-control-var.json"}}</script>
