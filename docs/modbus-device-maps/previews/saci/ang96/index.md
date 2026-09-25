---
title: "Saci ANG96 Modbus register preview"
description: "Sample register addresses and data types for Saci ANG96. Public preview with JSON source and verification status."
---

# Saci ANG96 Modbus register preview

Public preview for **Saci ANG96** (Power Meter).
This sample is not a complete map or evidence of hardware testing.

## Preview details

- Catalog ID: `saci/ang96`
- Map version: 1.0
- Verification: not-reviewed
- Protocols: RTU, TCP
- Public preview: 12 registers. Complete in-app availability is not established by this preview.

[JSON preview](https://modbus-monitor.github.io/modbus-device-maps/maps/saci/ang96.json) · [Data terms](https://modbus-monitor.github.io/modbus-device-maps/data-license/)

## Register table (sample)

| Signal | Display address | Data type | Units | Category |
|---|---|---|---|---|
| Voltage V | 300000 | FLOAT32 | V | Voltage |
| Current L1 A | 300004 | FLOAT32 | A | Current |
| Active power L1 KW | 300016 | FLOAT32 | kW | Power |
| Import active energy kWh | 300102 | FLOAT32 | kWh | Energy |
| Frequency Hz | 300086 | FLOAT32 | Hz | Frequency |
| Generator model export active energy time counter | 300136 | UINT32 | kWh | Identification |
| Voltage V | 300002 | FLOAT32 | V | Voltage |
| THD current L1 | 300006 | FLOAT32 | A | Current |
| THD voltage | 300008 | FLOAT32 | V | Voltage |
| Power factor | 300018 | FLOAT32 | PF | Power |
| Reactive power L1 Kvar | 300020 | FLOAT32 | kW | Power |
| Apparent power L1 KVA | 300022 | FLOAT32 | kW | Power |

## Addressing and setup

Addresses and values above are copied from the public JSON preview. Confirm the exact model, firmware, register function, address base, word order, scaling and units against the manufacturer manual before polling. No manufacturer manual revision or hardware validation is established by this page.

## Use with Modbus Monitor XPF

Check the device-map catalog in your installed XPF version for current map availability and licensing. The software download link does not open this map.

[Get Modbus Monitor XPF](https://docs.quantumbitsolutions.com/downloads-purchase/) · [Request a map or correction](https://github.com/Modbus-Monitor/modbus-device-maps/issues/new/choose) · [Browse all previews](https://docs.quantumbitsolutions.com/modbus-device-maps/)

<script type="application/ld+json">{"@context": "https://schema.org", "@type": "Dataset", "name": "Saci ANG96 public register preview", "description": "Sample register addresses and data types; not a complete map or hardware verification.", "url": "https://docs.quantumbitsolutions.com/modbus-device-maps/previews/saci/ang96/", "license": "https://modbus-monitor.github.io/modbus-device-maps/data-license/", "creator": {"@type": "Organization", "name": "Quantum Bit Solutions", "url": "https://quantumbitsolutions.com/"}, "distribution": {"@type": "DataDownload", "encodingFormat": "application/json", "contentUrl": "https://modbus-monitor.github.io/modbus-device-maps/maps/saci/ang96.json"}}</script>
