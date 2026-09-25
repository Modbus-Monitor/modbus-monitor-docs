---
title: "Electrex Exa Modbus register preview"
description: "Sample register addresses and data types for Electrex Exa. Public preview with JSON source and verification status."
---

# Electrex Exa Modbus register preview

Public preview for **Electrex Exa** (Power Meter).
This sample is not a complete map or evidence of hardware testing.

## Preview details

- Catalog ID: `electrex/exa`
- Map version: 1.0
- Verification: not-reviewed
- Protocols: RTU, TCP
- Public preview: 12 registers. Complete in-app availability is not established by this preview.

[JSON preview](https://modbus-monitor.github.io/modbus-device-maps/maps/electrex/exa.json) · [Data terms](https://modbus-monitor.github.io/modbus-device-maps/data-license/)

## Register table (sample)

| Signal | Display address | Data type | Units | Category |
|---|---|---|---|---|
| Phase to neutral voltage thd | 400200 | FLOAT32 | V | Voltage |
| Phase current thd | 400212 | FLOAT32 | - | Current |
| Phase active power imp exp W | 400240 | FLOAT32 | kW | Power |
| Frequency of u1n Hz | 400218 | FLOAT32 | Hz | Frequency |
| External pulse counter with weight total counter or tariff T1 | 400376 | FLOAT32 | - | General |
| Phase to neutral voltage thd | 400202 | FLOAT32 | V | Voltage |
| Phase to neutral voltage thd | 400204 | FLOAT32 | V | Voltage |
| Phase to phase voltage thd | 400206 | FLOAT32 | V | Voltage |
| Phase to phase voltage thd | 400208 | FLOAT32 | V | Voltage |
| Phase to phase voltage thd | 400210 | FLOAT32 | V | Voltage |
| Phase current thd | 400214 | FLOAT32 | - | Current |
| Phase current thd | 400216 | FLOAT32 | - | Current |

## Addressing and setup

Addresses and values above are copied from the public JSON preview. Confirm the exact model, firmware, register function, address base, word order, scaling and units against the manufacturer manual before polling. No manufacturer manual revision or hardware validation is established by this page.

## Use with Modbus Monitor XPF

Check the device-map catalog in your installed XPF version for current map availability and licensing. The software download link does not open this map.

[Get Modbus Monitor XPF](https://docs.quantumbitsolutions.com/downloads-purchase/) · [Request a map or correction](https://github.com/Modbus-Monitor/modbus-device-maps/issues/new/choose) · [Browse all previews](https://docs.quantumbitsolutions.com/modbus-device-maps/)

<script type="application/ld+json">{"@context": "https://schema.org", "@type": "Dataset", "name": "Electrex Exa public register preview", "description": "Sample register addresses and data types; not a complete map or hardware verification.", "url": "https://docs.quantumbitsolutions.com/modbus-device-maps/previews/electrex/exa/", "license": "https://modbus-monitor.github.io/modbus-device-maps/data-license/", "creator": {"@type": "Organization", "name": "Quantum Bit Solutions", "url": "https://quantumbitsolutions.com/"}, "distribution": {"@type": "DataDownload", "encodingFormat": "application/json", "contentUrl": "https://modbus-monitor.github.io/modbus-device-maps/maps/electrex/exa.json"}}</script>
