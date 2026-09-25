---
title: "Meatrol MP440 Modbus register preview"
description: "Sample register addresses and data types for Meatrol MP440. Public preview with JSON source and verification status."
---

# Meatrol MP440 Modbus register preview

Public preview for **Meatrol MP440** (Power Meter).
This sample is not a complete map or evidence of hardware testing.

## Preview details

- Catalog ID: `meatrol/mp440`
- Map version: 1.0
- Verification: not-reviewed
- Protocols: RTU, TCP
- Public preview: 12 registers. Complete in-app availability is not established by this preview.

[JSON preview](https://modbus-monitor.github.io/modbus-device-maps/maps/meatrol/mp440.json) · [Data terms](https://modbus-monitor.github.io/modbus-device-maps/data-license/)

## Register table (sample)

| Signal | Display address | Data type | Units | Category |
|---|---|---|---|---|
| Voltage UA-UN V | 401010 | FLOAT32 | V | Voltage |
| Rated current A | 300777 | UINT16 | - | Current |
| Actual power con- sumption W | 300783 | UINT32 | kW | Power |
| Active energy import phase A kWh | 402000 | UINT32 | kWh | Energy |
| Frequency phase A Hz | 401068 | FLOAT32 | Hz | Frequency |
| CP state | 300770 | UINT16 | - | Status |
| HMI temperature internal | 300768 | INT16 | degC | Temperature |
| HCC3 error code | 300772 | UINT16 | - | General |
| Serial number | 300779 | UINT32 | - | Identification |
| HMI temperature external | 300769 | INT16 | degC | Temperature |
| PP state | 300771 | UINT16 | - | Status |
| State | 300773 | UINT16 | - | Status |

## Addressing and setup

Addresses and values above are copied from the public JSON preview. Confirm the exact model, firmware, register function, address base, word order, scaling and units against the manufacturer manual before polling. No manufacturer manual revision or hardware validation is established by this page.

## Use with Modbus Monitor XPF

Check the device-map catalog in your installed XPF version for current map availability and licensing. The software download link does not open this map.

[Get Modbus Monitor XPF](https://docs.quantumbitsolutions.com/downloads-purchase/) · [Request a map or correction](https://github.com/Modbus-Monitor/modbus-device-maps/issues/new/choose) · [Browse all previews](https://docs.quantumbitsolutions.com/modbus-device-maps/)

<script type="application/ld+json">{"@context": "https://schema.org", "@type": "Dataset", "name": "Meatrol MP440 public register preview", "description": "Sample register addresses and data types; not a complete map or hardware verification.", "url": "https://docs.quantumbitsolutions.com/modbus-device-maps/previews/meatrol/mp440/", "license": "https://modbus-monitor.github.io/modbus-device-maps/data-license/", "creator": {"@type": "Organization", "name": "Quantum Bit Solutions", "url": "https://quantumbitsolutions.com/"}, "distribution": {"@type": "DataDownload", "encodingFormat": "application/json", "contentUrl": "https://modbus-monitor.github.io/modbus-device-maps/maps/meatrol/mp440.json"}}</script>
