---
title: "SAIA Energy Meter ALD1, ALE3, AWD3 Modbus register preview"
description: "Sample register addresses and data types for SAIA Energy Meter ALD1, ALE3, AWD3. Public preview with JSON source and verification status."
---

# SAIA Energy Meter ALD1, ALE3, AWD3 Modbus register preview

Public preview for **SAIA Energy Meter ALD1, ALE3, AWD3** (Power Meter).
This sample is not a complete map or evidence of hardware testing.

## Preview details

- Catalog ID: `saia-energy-meter/ald1-ale3-awd3`
- Map version: 1.0
- Verification: not-reviewed
- Protocols: RTU, TCP
- Public preview: 12 registers. Complete in-app availability is not established by this preview.

[JSON preview](https://modbus-monitor.github.io/modbus-device-maps/maps/saia-energy-meter/ald1-ale3-awd3.json) · [Data terms](https://modbus-monitor.github.io/modbus-device-maps/data-license/)

## Register table (sample)

| Signal | Display address | Data type | Units | Category |
|---|---|---|---|---|
| URMS phase 1 Effective Voltage of Phase 1 V | 400036 | UINT16 | V | Voltage |
| IRMS phase 1 Effective Current of Phase 1 A | 400037 | UINT16 | - | Current |
| PRMS phase 1 Effective active Power of Phase 1 kW | 400038 | UINT16 | kW | Power |
| WT1 total Counter Energy Total Tariff 1 kWh | 400028 | UINT32 | kWh | Energy |
| Status Protect | 400022 | UINT16 | - | Status |
| Modbus com Number of supported registers | 400002 | UINT16 | - | Communication |
| Not Used | 400006 | UINT16 | - | General |
| Serial number | 400016 | UINT32 | - | Identification |
| WT2 total Counter Energy Total Tariff 2 kWh | 400032 | UINT32 | kWh | Energy |
| QRMS phase 1 Effective reactive Power of Phase 1 kvar | 400039 | UINT16 | kW | Power |
| URMS phase 2 Effective Voltage of Phase 2 V | 400041 | UINT16 | V | Voltage |
| IRMS phase 2 Effective Current of Phase 2 A | 400042 | UINT16 | - | Current |

## Addressing and setup

Addresses and values above are copied from the public JSON preview. Confirm the exact model, firmware, register function, address base, word order, scaling and units against the manufacturer manual before polling. No manufacturer manual revision or hardware validation is established by this page.

## Use with Modbus Monitor XPF

Check the device-map catalog in your installed XPF version for current map availability and licensing. The software download link does not open this map.

[Get Modbus Monitor XPF](https://docs.quantumbitsolutions.com/downloads-purchase/) · [Request a map or correction](https://github.com/Modbus-Monitor/modbus-device-maps/issues/new/choose) · [Browse all previews](https://docs.quantumbitsolutions.com/modbus-device-maps/)

<script type="application/ld+json">{"@context": "https://schema.org", "@type": "Dataset", "name": "SAIA Energy Meter ALD1, ALE3, AWD3 public register preview", "description": "Sample register addresses and data types; not a complete map or hardware verification.", "url": "https://docs.quantumbitsolutions.com/modbus-device-maps/previews/saia-energy-meter/ald1-ale3-awd3/", "license": "https://modbus-monitor.github.io/modbus-device-maps/data-license/", "creator": {"@type": "Organization", "name": "Quantum Bit Solutions", "url": "https://quantumbitsolutions.com/"}, "distribution": {"@type": "DataDownload", "encodingFormat": "application/json", "contentUrl": "https://modbus-monitor.github.io/modbus-device-maps/maps/saia-energy-meter/ald1-ale3-awd3.json"}}</script>
