---
title: "ENTES MPR7 Se ries Modbus register preview"
description: "Sample register addresses and data types for ENTES MPR7 Se ries. Public preview with JSON source and verification status."
---

# ENTES MPR7 Se ries Modbus register preview

Public preview for **ENTES MPR7 Se ries** (Power Meter).
This sample is not a complete map or evidence of hardware testing.

## Preview details

- Catalog ID: `entes/mpr7-se-ries`
- Map version: 1.0
- Verification: not-reviewed
- Protocols: RTU, TCP
- Public preview: 12 registers. Complete in-app availability is not established by this preview.

[JSON preview](https://modbus-monitor.github.io/modbus-device-maps/maps/entes/mpr7-se-ries.json) · [Data terms](https://modbus-monitor.github.io/modbus-device-maps/data-license/)

## Register table (sample)

| Signal | Display address | Data type | Units | Category |
|---|---|---|---|---|
| L1 phase voltage Vot | 400000 | UINT32 | V | Voltage |
| L1 phase current Amper | 400006 | UINT32 | - | Current |
| L1 phase active power Watt | 400020 | INT32 | kW | Power |
| Import active energy 1 Wh | 400088 | UINT32 | kWh | Energy |
| Frequency Hz | 400058 | UINT32 | Hz | Frequency |
| L1 phase cos | 400038 | INT32 | - | General |
| L2 phase voltage Vot | 400002 | UINT32 | V | Voltage |
| L3 phase voltage Vot | 400004 | UINT32 | V | Voltage |
| L2 phase current Amper | 400008 | UINT32 | - | Current |
| L3 phase current Amper | 400010 | UINT32 | - | Current |
| Neutral current Amper | 400012 | UINT32 | - | Current |
| L1 L2 phase phase voltage Vot | 400014 | UINT32 | V | Voltage |

## Addressing and setup

Addresses and values above are copied from the public JSON preview. Confirm the exact model, firmware, register function, address base, word order, scaling and units against the manufacturer manual before polling. No manufacturer manual revision or hardware validation is established by this page.

## Use with Modbus Monitor XPF

Check the device-map catalog in your installed XPF version for current map availability and licensing. The software download link does not open this map.

[Get Modbus Monitor XPF](https://docs.quantumbitsolutions.com/downloads-purchase/) · [Request a map or correction](https://github.com/Modbus-Monitor/modbus-device-maps/issues/new/choose) · [Browse all previews](https://docs.quantumbitsolutions.com/modbus-device-maps/)

<script type="application/ld+json">{"@context": "https://schema.org", "@type": "Dataset", "name": "ENTES MPR7 Se ries public register preview", "description": "Sample register addresses and data types; not a complete map or hardware verification.", "url": "https://docs.quantumbitsolutions.com/modbus-device-maps/previews/entes/mpr7-se-ries/", "license": "https://modbus-monitor.github.io/modbus-device-maps/data-license/", "creator": {"@type": "Organization", "name": "Quantum Bit Solutions", "url": "https://quantumbitsolutions.com/"}, "distribution": {"@type": "DataDownload", "encodingFormat": "application/json", "contentUrl": "https://modbus-monitor.github.io/modbus-device-maps/maps/entes/mpr7-se-ries.json"}}</script>
