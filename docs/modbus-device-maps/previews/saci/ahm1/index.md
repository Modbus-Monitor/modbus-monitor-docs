---
title: "Saci AHM1 Modbus register preview"
description: "Sample register addresses and data types for Saci AHM1. Public preview with JSON source and verification status."
---

# Saci AHM1 Modbus register preview

Public preview for **Saci AHM1** (Power Meter).
This sample is not a complete map or evidence of hardware testing.

## Preview details

- Catalog ID: `saci/ahm1`
- Map version: 1.0
- Verification: not-reviewed
- Protocols: RTU, TCP
- Public preview: 12 registers. Complete in-app availability is not established by this preview.

[JSON preview](https://modbus-monitor.github.io/modbus-device-maps/maps/saci/ahm1.json) · [Data terms](https://modbus-monitor.github.io/modbus-device-maps/data-license/)

## Register table (sample)

| Signal | Display address | Data type | Units | Category |
|---|---|---|---|---|
| Positive-sequence component of voltage V | 300518 | INT16 | V | Voltage |
| Average current A | 300064 | FLOAT32 | - | Current |
| P1 kW | 300026 | FLOAT32 | - | Power |
| Import active energy kWh | 300066 | FLOAT32 | kWh | Energy |
| F Hz | 300058 | FLOAT32 | - | Frequency |
| PF1 | 300050 | FLOAT32 | - | Power Factor |
| Max demand value -I1 A | 300238 | FLOAT32 | kW | Demand |
| State of digital input 0off 1on bit0DI1 bit1DI2 | 304676 | INT16 | - | Status |
| THD-V1 | 300528 | INT16 | - | Harmonics |
| V1 V | 300006 | FLOAT32 | - | General |
| P2 kW | 300028 | FLOAT32 | - | Power |
| P3 kW | 300030 | FLOAT32 | - | Power |

## Addressing and setup

Addresses and values above are copied from the public JSON preview. Confirm the exact model, firmware, register function, address base, word order, scaling and units against the manufacturer manual before polling. No manufacturer manual revision or hardware validation is established by this page.

## Use with Modbus Monitor XPF

Check the device-map catalog in your installed XPF version for current map availability and licensing. The software download link does not open this map.

[Get Modbus Monitor XPF](https://docs.quantumbitsolutions.com/downloads-purchase/) · [Request a map or correction](https://github.com/Modbus-Monitor/modbus-device-maps/issues/new/choose) · [Browse all previews](https://docs.quantumbitsolutions.com/modbus-device-maps/)

<script type="application/ld+json">{"@context": "https://schema.org", "@type": "Dataset", "name": "Saci AHM1 public register preview", "description": "Sample register addresses and data types; not a complete map or hardware verification.", "url": "https://docs.quantumbitsolutions.com/modbus-device-maps/previews/saci/ahm1/", "license": "https://modbus-monitor.github.io/modbus-device-maps/data-license/", "creator": {"@type": "Organization", "name": "Quantum Bit Solutions", "url": "https://quantumbitsolutions.com/"}, "distribution": {"@type": "DataDownload", "encodingFormat": "application/json", "contentUrl": "https://modbus-monitor.github.io/modbus-device-maps/maps/saci/ahm1.json"}}</script>
