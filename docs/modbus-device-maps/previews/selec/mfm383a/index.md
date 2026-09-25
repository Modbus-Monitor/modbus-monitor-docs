---
title: "Selec MFM383A Modbus register preview"
description: "Sample register addresses and data types for Selec MFM383A. Public preview with JSON source and verification status."
---

# Selec MFM383A Modbus register preview

Public preview for **Selec MFM383A** (Power Meter).
This sample is not a complete map or evidence of hardware testing.

## Preview details

- Catalog ID: `selec/mfm383a`
- Map version: 1.0
- Verification: not-reviewed
- Protocols: RTU, TCP
- Public preview: 12 registers. Complete in-app availability is not established by this preview.

[JSON preview](https://modbus-monitor.github.io/modbus-device-maps/maps/selec/mfm383a.json) · [Data terms](https://modbus-monitor.github.io/modbus-device-maps/data-license/)

## Register table (sample)

| Signal | Display address | Data type | Units | Category |
|---|---|---|---|---|
| Voltage v1n | 300000 | FLOAT32 | V | Voltage |
| Current 11 | 300016 | FLOAT32 | - | Current |
| kW1 | 300024 | FLOAT32 | - | Power |
| Kwh | 300058 | FLOAT32 | kWh | Energy |
| Frequency | 300056 | FLOAT32 | Hz | Frequency |
| PF1 | 300048 | FLOAT32 | - | Power Factor |
| Voltage v2n | 300002 | FLOAT32 | V | Voltage |
| Average voltage ln | 300006 | FLOAT32 | V | Voltage |
| Voltage V12 | 300008 | FLOAT32 | V | Voltage |
| Average voltage ll | 300014 | FLOAT32 | V | Voltage |
| Current 12 | 300018 | FLOAT32 | - | Current |
| Current I3 | 300020 | FLOAT32 | - | Current |

## Addressing and setup

Addresses and values above are copied from the public JSON preview. Confirm the exact model, firmware, register function, address base, word order, scaling and units against the manufacturer manual before polling. No manufacturer manual revision or hardware validation is established by this page.

## Use with Modbus Monitor XPF

Check the device-map catalog in your installed XPF version for current map availability and licensing. The software download link does not open this map.

[Get Modbus Monitor XPF](https://docs.quantumbitsolutions.com/downloads-purchase/) · [Request a map or correction](https://github.com/Modbus-Monitor/modbus-device-maps/issues/new/choose) · [Browse all previews](https://docs.quantumbitsolutions.com/modbus-device-maps/)

<script type="application/ld+json">{"@context": "https://schema.org", "@type": "Dataset", "name": "Selec MFM383A public register preview", "description": "Sample register addresses and data types; not a complete map or hardware verification.", "url": "https://docs.quantumbitsolutions.com/modbus-device-maps/previews/selec/mfm383a/", "license": "https://modbus-monitor.github.io/modbus-device-maps/data-license/", "creator": {"@type": "Organization", "name": "Quantum Bit Solutions", "url": "https://quantumbitsolutions.com/"}, "distribution": {"@type": "DataDownload", "encodingFormat": "application/json", "contentUrl": "https://modbus-monitor.github.io/modbus-device-maps/maps/selec/mfm383a.json"}}</script>
