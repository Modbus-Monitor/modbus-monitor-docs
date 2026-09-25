---
title: "Ginlong Solis PV Modbus register preview"
description: "Sample register addresses and data types for Ginlong Solis PV. Public preview with JSON source and verification status."
---

# Ginlong Solis PV Modbus register preview

Public preview for **Ginlong Solis PV** (Solar Inverter).
This sample is not a complete map or evidence of hardware testing.

## Preview details

- Catalog ID: `ginlong-solis/pv`
- Map version: 1.0
- Verification: not-reviewed
- Protocols: RTU, TCP
- Public preview: 12 registers. Complete in-app availability is not established by this preview.

[JSON preview](https://modbus-monitor.github.io/modbus-device-maps/maps/ginlong-solis/pv.json) · [Data terms](https://modbus-monitor.github.io/modbus-device-maps/data-license/)

## Register table (sample)

| Signal | Display address | Data type | Units | Category |
|---|---|---|---|---|
| Dc voltage 1 V | 303048 | UINT16 | V | Voltage |
| Dc current 1 A | 303049 | UINT16 | - | Current |
| Inverter total power generation kW | 303028 | UINT32 | kW | Power |
| Energy storage control switch | 303131 | UINT16 | kWh | Energy |
| Grid frequency Hz | 303093 | UINT16 | Hz | Frequency |
| Inverter temperature | 303092 | UINT16 | degC | Temperature |
| System time year a | 303021 | UINT16 | - | General |
| Inverter power generation in the month kW | 303030 | UINT32 | kW | Power |
| Inverted last months power generation kW | 303032 | UINT32 | kW | Power |
| Inverter power generation today kW | 303034 | UINT16 | kW | Power |
| Inverter yesterdays power generation kW | 303035 | UINT16 | kW | Power |
| Inverter power generation this year kW | 303036 | UINT32 | kW | Power |

## Addressing and setup

Addresses and values above are copied from the public JSON preview. Confirm the exact model, firmware, register function, address base, word order, scaling and units against the manufacturer manual before polling. No manufacturer manual revision or hardware validation is established by this page.

## Use with Modbus Monitor XPF

Check the device-map catalog in your installed XPF version for current map availability and licensing. The software download link does not open this map.

[Get Modbus Monitor XPF](https://docs.quantumbitsolutions.com/downloads-purchase/) · [Request a map or correction](https://github.com/Modbus-Monitor/modbus-device-maps/issues/new/choose) · [Browse all previews](https://docs.quantumbitsolutions.com/modbus-device-maps/)

<script type="application/ld+json">{"@context": "https://schema.org", "@type": "Dataset", "name": "Ginlong Solis PV public register preview", "description": "Sample register addresses and data types; not a complete map or hardware verification.", "url": "https://docs.quantumbitsolutions.com/modbus-device-maps/previews/ginlong-solis/pv/", "license": "https://modbus-monitor.github.io/modbus-device-maps/data-license/", "creator": {"@type": "Organization", "name": "Quantum Bit Solutions", "url": "https://quantumbitsolutions.com/"}, "distribution": {"@type": "DataDownload", "encodingFormat": "application/json", "contentUrl": "https://modbus-monitor.github.io/modbus-device-maps/maps/ginlong-solis/pv.json"}}</script>
