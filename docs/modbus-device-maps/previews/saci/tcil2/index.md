---
title: "Saci TCIL2 Modbus register preview"
description: "Sample register addresses and data types for Saci TCIL2. Public preview with JSON source and verification status."
---

# Saci TCIL2 Modbus register preview

Public preview for **Saci TCIL2** (Power Meter).
This sample is not a complete map or evidence of hardware testing.

## Preview details

- Catalog ID: `saci/tcil2`
- Map version: 1.0
- Verification: not-reviewed
- Protocols: RTU, TCP
- Public preview: 12 registers. Complete in-app availability is not established by this preview.

[JSON preview](https://modbus-monitor.github.io/modbus-device-maps/maps/saci/tcil2.json) · [Data terms](https://modbus-monitor.github.io/modbus-device-maps/data-license/)

## Register table (sample)

| Signal | Display address | Data type | Units | Category |
|---|---|---|---|---|
| Average value of three phase voltages V | 300096 | FLOAT32 | V | Voltage |
| Average value of three phase currents A | 300100 | FLOAT32 | - | Current |
| Total power factor | 300086 | FLOAT32 | PF | Power |
| EP kWh | 300102 | FLOAT32 | kWh | Energy |
| Grid frequency Hz | 300088 | FLOAT32 | Hz | Frequency |
| 2nd harmonic content - V1 | 301350 | INT16 | - | Harmonics |
| Three phase line average minimum V | 300888 | FLOAT32 | - | General |
| Average value of three line voltages V | 300098 | FLOAT32 | V | Voltage |
| EP- kWh | 300104 | FLOAT32 | kWh | Energy |
| EQ kvarh | 300112 | FLOAT32 | kWh | Energy |
| EQ- kvarh | 300114 | FLOAT32 | kWh | Energy |
| Apparent energy kVAh | 300116 | FLOAT32 | kWh | Energy |

## Addressing and setup

Addresses and values above are copied from the public JSON preview. Confirm the exact model, firmware, register function, address base, word order, scaling and units against the manufacturer manual before polling. No manufacturer manual revision or hardware validation is established by this page.

## Use with Modbus Monitor XPF

Check the device-map catalog in your installed XPF version for current map availability and licensing. The software download link does not open this map.

[Get Modbus Monitor XPF](https://docs.quantumbitsolutions.com/downloads-purchase/) · [Request a map or correction](https://github.com/Modbus-Monitor/modbus-device-maps/issues/new/choose) · [Browse all previews](https://docs.quantumbitsolutions.com/modbus-device-maps/)

<script type="application/ld+json">{"@context": "https://schema.org", "@type": "Dataset", "name": "Saci TCIL2 public register preview", "description": "Sample register addresses and data types; not a complete map or hardware verification.", "url": "https://docs.quantumbitsolutions.com/modbus-device-maps/previews/saci/tcil2/", "license": "https://modbus-monitor.github.io/modbus-device-maps/data-license/", "creator": {"@type": "Organization", "name": "Quantum Bit Solutions", "url": "https://quantumbitsolutions.com/"}, "distribution": {"@type": "DataDownload", "encodingFormat": "application/json", "contentUrl": "https://modbus-monitor.github.io/modbus-device-maps/maps/saci/tcil2.json"}}</script>
