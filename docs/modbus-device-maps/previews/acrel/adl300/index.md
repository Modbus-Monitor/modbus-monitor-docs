---
title: "Acrel ADL300 Modbus register preview"
description: "Sample register addresses and data types for Acrel ADL300. Public preview with JSON source and verification status."
---

# Acrel ADL300 Modbus register preview

Public preview for **Acrel ADL300** (Power Meter).
This sample is not a complete map or evidence of hardware testing.

## Preview details

- Catalog ID: `acrel/adl300`
- Map version: 1.0
- Verification: not-reviewed
- Protocols: RTU, TCP
- Public preview: 12 registers. Complete in-app availability is not established by this preview.

[JSON preview](https://modbus-monitor.github.io/modbus-device-maps/maps/acrel/adl300.json) · [Data terms](https://modbus-monitor.github.io/modbus-device-maps/data-license/)

## Register table (sample)

| Signal | Display address | Data type | Units | Category |
|---|---|---|---|---|
| Current total kwh | 400000 | UINT32 | kWh | Current |
| Total kwh this month | 400027 | UINT32 | kWh | Energy |
| Year month | 400010 | UINT16 | - | General |
| Current spike kwh | 400002 | UINT32 | kWh | Current |
| Current flat kwh | 400006 | UINT32 | kWh | Current |
| Current valley kwh | 400008 | UINT16 | kWh | Current |
| Peak kwh this month | 400031 | UINT32 | kWh | Energy |
| Flat kwh this month | 400033 | UINT32 | kWh | Energy |
| Valley kwh this month | 400035 | UINT32 | kWh | Energy |
| Total kwh last month | 400038 | UINT32 | kWh | Energy |
| Spike kwh last month | 400040 | UINT32 | kWh | Energy |
| Peak kwh last month | 400042 | UINT32 | kWh | Energy |

## Addressing and setup

Addresses and values above are copied from the public JSON preview. Confirm the exact model, firmware, register function, address base, word order, scaling and units against the manufacturer manual before polling. No manufacturer manual revision or hardware validation is established by this page.

## Use with Modbus Monitor XPF

Check the device-map catalog in your installed XPF version for current map availability and licensing. The software download link does not open this map.

[Get Modbus Monitor XPF](https://docs.quantumbitsolutions.com/downloads-purchase/) · [Request a map or correction](https://github.com/Modbus-Monitor/modbus-device-maps/issues/new/choose) · [Browse all previews](https://docs.quantumbitsolutions.com/modbus-device-maps/)

<script type="application/ld+json">{"@context": "https://schema.org", "@type": "Dataset", "name": "Acrel ADL300 public register preview", "description": "Sample register addresses and data types; not a complete map or hardware verification.", "url": "https://docs.quantumbitsolutions.com/modbus-device-maps/previews/acrel/adl300/", "license": "https://modbus-monitor.github.io/modbus-device-maps/data-license/", "creator": {"@type": "Organization", "name": "Quantum Bit Solutions", "url": "https://quantumbitsolutions.com/"}, "distribution": {"@type": "DataDownload", "encodingFormat": "application/json", "contentUrl": "https://modbus-monitor.github.io/modbus-device-maps/maps/acrel/adl300.json"}}</script>
