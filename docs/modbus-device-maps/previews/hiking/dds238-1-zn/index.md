---
title: "Hiking DDS238-1-ZN Modbus register preview"
description: "Sample register addresses and data types for Hiking DDS238-1-ZN. Public preview with JSON source and verification status."
---

# Hiking DDS238-1-ZN Modbus register preview

Public preview for **Hiking DDS238-1-ZN** (Power Meter).
This sample is not a complete map or evidence of hardware testing.

## Preview details

- Catalog ID: `hiking/dds238-1-zn`
- Map version: 1.0
- Verification: not-reviewed
- Protocols: RTU, TCP
- Public preview: 8 registers. Complete in-app availability is not established by this preview.

[JSON preview](https://modbus-monitor.github.io/modbus-device-maps/maps/hiking/dds238-1-zn.json) · [Data terms](https://modbus-monitor.github.io/modbus-device-maps/data-license/)

## Register table (sample)

| Signal | Display address | Data type | Units | Category |
|---|---|---|---|---|
| Voltage V | 400012 | UINT16 | V | Voltage |
| Current A | 400013 | UINT16 | - | Current |
| Reactive power VAr | 400015 | UINT16 | kW | Power |
| Total energy kWh | 400000 | UINT32 | kWh | Energy |
| Frequency Hz | 400017 | UINT16 | Hz | Frequency |
| Export energy kWh | 400008 | UINT32 | kWh | Energy |
| Import energy kWh | 400010 | UINT32 | kWh | Energy |
| Power factor | 400016 | UINT16 | PF | Power |

## Addressing and setup

Addresses and values above are copied from the public JSON preview. Confirm the exact model, firmware, register function, address base, word order, scaling and units against the manufacturer manual before polling. No manufacturer manual revision or hardware validation is established by this page.

## Use with Modbus Monitor XPF

Check the device-map catalog in your installed XPF version for current map availability and licensing. The software download link does not open this map.

[Get Modbus Monitor XPF](https://docs.quantumbitsolutions.com/downloads-purchase/) · [Request a map or correction](https://github.com/Modbus-Monitor/modbus-device-maps/issues/new/choose) · [Browse all previews](https://docs.quantumbitsolutions.com/modbus-device-maps/)

<script type="application/ld+json">{"@context": "https://schema.org", "@type": "Dataset", "name": "Hiking DDS238-1-ZN public register preview", "description": "Sample register addresses and data types; not a complete map or hardware verification.", "url": "https://docs.quantumbitsolutions.com/modbus-device-maps/previews/hiking/dds238-1-zn/", "license": "https://modbus-monitor.github.io/modbus-device-maps/data-license/", "creator": {"@type": "Organization", "name": "Quantum Bit Solutions", "url": "https://quantumbitsolutions.com/"}, "distribution": {"@type": "DataDownload", "encodingFormat": "application/json", "contentUrl": "https://modbus-monitor.github.io/modbus-device-maps/maps/hiking/dds238-1-zn.json"}}</script>
