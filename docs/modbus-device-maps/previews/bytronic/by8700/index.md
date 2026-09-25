---
title: "Bytronic By8700 Modbus register preview"
description: "Sample register addresses and data types for Bytronic By8700. Public preview with JSON source and verification status."
---

# Bytronic By8700 Modbus register preview

Public preview for **Bytronic By8700** (Power Meter).
This sample is not a complete map or evidence of hardware testing.

## Preview details

- Catalog ID: `bytronic/by8700`
- Map version: 1.0
- Verification: not-reviewed
- Protocols: RTU, TCP
- Public preview: 12 registers. Complete in-app availability is not established by this preview.

[JSON preview](https://modbus-monitor.github.io/modbus-device-maps/maps/bytronic/by8700.json) · [Data terms](https://modbus-monitor.github.io/modbus-device-maps/data-license/)

## Register table (sample)

| Signal | Display address | Data type | Units | Category |
|---|---|---|---|---|
| Ampere-ora positivi Ah | 400593 | UINT32 | A | Current |
| Energia attiva consumata kWh | 400570 | UINT32 | kWh | Energy |
| Famiglia strumento | 400512 | UINT32 | - | General |
| Versione | 400513 | UINT32 | - | Identification |
| Energia attiva prodotta kWh | 400572 | UINT32 | kWh | Energy |
| Ampere-ora negativi Ah | 400595 | UINT32 | A | Current |
| Tipo strumento | 400512 | UINT32 | - | General |
| Revisione | 400513 | UINT32 | - | General |
| KRMSFACTOR | 400514 | UINT32 | - | General |
| Valore calibrazione fondoscala irms | 400515 | UINT32 | - | General |
| Valore calibrazione fondoscala vrms | 400518 | UINT32 | - | General |
| Valore fondoscala V Volt | 400524 | UINT32 | - | General |

## Addressing and setup

Addresses and values above are copied from the public JSON preview. Confirm the exact model, firmware, register function, address base, word order, scaling and units against the manufacturer manual before polling. No manufacturer manual revision or hardware validation is established by this page.

## Use with Modbus Monitor XPF

Check the device-map catalog in your installed XPF version for current map availability and licensing. The software download link does not open this map.

[Get Modbus Monitor XPF](https://docs.quantumbitsolutions.com/downloads-purchase/) · [Request a map or correction](https://github.com/Modbus-Monitor/modbus-device-maps/issues/new/choose) · [Browse all previews](https://docs.quantumbitsolutions.com/modbus-device-maps/)

<script type="application/ld+json">{"@context": "https://schema.org", "@type": "Dataset", "name": "Bytronic By8700 public register preview", "description": "Sample register addresses and data types; not a complete map or hardware verification.", "url": "https://docs.quantumbitsolutions.com/modbus-device-maps/previews/bytronic/by8700/", "license": "https://modbus-monitor.github.io/modbus-device-maps/data-license/", "creator": {"@type": "Organization", "name": "Quantum Bit Solutions", "url": "https://quantumbitsolutions.com/"}, "distribution": {"@type": "DataDownload", "encodingFormat": "application/json", "contentUrl": "https://modbus-monitor.github.io/modbus-device-maps/maps/bytronic/by8700.json"}}</script>
