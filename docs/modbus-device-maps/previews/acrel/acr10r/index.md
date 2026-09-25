---
title: "Acrel ACR10R Modbus register preview"
description: "Sample register addresses and data types for Acrel ACR10R. Public preview with JSON source and verification status."
---

# Acrel ACR10R Modbus register preview

Public preview for **Acrel ACR10R** (Power Meter).
This sample is not a complete map or evidence of hardware testing.

## Preview details

- Catalog ID: `acrel/acr10r`
- Map version: 1.0
- Verification: not-reviewed
- Protocols: RTU, TCP
- Public preview: 12 registers. Complete in-app availability is not established by this preview.

[JSON preview](https://modbus-monitor.github.io/modbus-device-maps/maps/acrel/acr10r.json) · [Data terms](https://modbus-monitor.github.io/modbus-device-maps/data-license/)

## Register table (sample)

| Signal | Display address | Data type | Units | Category |
|---|---|---|---|---|
| Secondary side rated voltage ue V | 400004 | UINT16 | V | Voltage |
| Secondary side rated current value ie A | 400005 | UINT16 | - | Current |
| Power primary and secondary side coefficients | 400018 | UINT32 | kW | Power |
| This month active peak electric energy kWh | 400333 | UINT32 | kWh | Energy |
| Frequency F | 400252 | UINT16 | Hz | Frequency |
| Maximum demand | 400301 | UINT32 | kW | Demand |
| DIDO state | 401000 | UINT16 | - | Status |
| Communication speed bps | 400001 | UINT16 | - | Communication |
| Wiring mode wire | 400003 | UINT16 | - | General |
| Primary side rated voltage PU kV | 400006 | UINT16 | V | Voltage |
| Voltage primary side and | 400014 | UINT32 | V | Voltage |
| Primary side and secondary side coefficient of current | 400016 | UINT32 | - | Current |

## Addressing and setup

Addresses and values above are copied from the public JSON preview. Confirm the exact model, firmware, register function, address base, word order, scaling and units against the manufacturer manual before polling. No manufacturer manual revision or hardware validation is established by this page.

## Use with Modbus Monitor XPF

Check the device-map catalog in your installed XPF version for current map availability and licensing. The software download link does not open this map.

[Get Modbus Monitor XPF](https://docs.quantumbitsolutions.com/downloads-purchase/) · [Request a map or correction](https://github.com/Modbus-Monitor/modbus-device-maps/issues/new/choose) · [Browse all previews](https://docs.quantumbitsolutions.com/modbus-device-maps/)

<script type="application/ld+json">{"@context": "https://schema.org", "@type": "Dataset", "name": "Acrel ACR10R public register preview", "description": "Sample register addresses and data types; not a complete map or hardware verification.", "url": "https://docs.quantumbitsolutions.com/modbus-device-maps/previews/acrel/acr10r/", "license": "https://modbus-monitor.github.io/modbus-device-maps/data-license/", "creator": {"@type": "Organization", "name": "Quantum Bit Solutions", "url": "https://quantumbitsolutions.com/"}, "distribution": {"@type": "DataDownload", "encodingFormat": "application/json", "contentUrl": "https://modbus-monitor.github.io/modbus-device-maps/maps/acrel/acr10r.json"}}</script>
