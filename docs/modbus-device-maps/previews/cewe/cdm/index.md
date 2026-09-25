---
title: "Cewe CDM Modbus register preview"
description: "Sample register addresses and data types for Cewe CDM. Public preview with JSON source and verification status."
---

# Cewe CDM Modbus register preview

Public preview for **Cewe CDM** (Power Meter).
This sample is not a complete map or evidence of hardware testing.

## Preview details

- Catalog ID: `cewe/cdm`
- Map version: 1.0
- Verification: not-reviewed
- Protocols: RTU, TCP
- Public preview: 12 registers. Complete in-app availability is not established by this preview.

[JSON preview](https://modbus-monitor.github.io/modbus-device-maps/maps/cewe/cdm.json) · [Data terms](https://modbus-monitor.github.io/modbus-device-maps/data-license/)

## Register table (sample)

| Signal | Display address | Data type | Units | Category |
|---|---|---|---|---|
| V1 L N voltage phase 1 V | 404096 | FLOAT32 | V | Voltage |
| A1 phase 1 current A | 404110 | FLOAT32 | - | Current |
| PF1 phase 1 power factor | 404120 | FLOAT32 | PF | Power |
| kwh1 phase 1 imported active energy Wh | 404352 | FLOAT32 | kWh | Energy |
| F frequency Hz | 404152 | FLOAT32 | Hz | Frequency |
| V2 L N voltage phase 2 V | 404098 | FLOAT32 | V | Voltage |
| V3 L N voltage phase 3 V | 404100 | FLOAT32 | V | Voltage |
| V12 L L voltage line 12 V | 404102 | FLOAT32 | V | Voltage |
| V23 L L voltage line 23 V | 404104 | FLOAT32 | V | Voltage |
| V31 L L voltage line 31 V | 404106 | FLOAT32 | V | Voltage |
| V system voltage V | 404108 | FLOAT32 | V | Voltage |
| A2 phase 2 current A | 404112 | FLOAT32 | - | Current |

## Addressing and setup

Addresses and values above are copied from the public JSON preview. Confirm the exact model, firmware, register function, address base, word order, scaling and units against the manufacturer manual before polling. No manufacturer manual revision or hardware validation is established by this page.

## Use with Modbus Monitor XPF

Check the device-map catalog in your installed XPF version for current map availability and licensing. The software download link does not open this map.

[Get Modbus Monitor XPF](https://docs.quantumbitsolutions.com/downloads-purchase/) · [Request a map or correction](https://github.com/Modbus-Monitor/modbus-device-maps/issues/new/choose) · [Browse all previews](https://docs.quantumbitsolutions.com/modbus-device-maps/)

<script type="application/ld+json">{"@context": "https://schema.org", "@type": "Dataset", "name": "Cewe CDM public register preview", "description": "Sample register addresses and data types; not a complete map or hardware verification.", "url": "https://docs.quantumbitsolutions.com/modbus-device-maps/previews/cewe/cdm/", "license": "https://modbus-monitor.github.io/modbus-device-maps/data-license/", "creator": {"@type": "Organization", "name": "Quantum Bit Solutions", "url": "https://quantumbitsolutions.com/"}, "distribution": {"@type": "DataDownload", "encodingFormat": "application/json", "contentUrl": "https://modbus-monitor.github.io/modbus-device-maps/maps/cewe/cdm.json"}}</script>
