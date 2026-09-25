---
title: "Inepro Metering PRO380 Modbus register preview"
description: "Sample register addresses and data types for Inepro Metering PRO380. Public preview with JSON source and verification status."
---

# Inepro Metering PRO380 Modbus register preview

Public preview for **Inepro Metering PRO380** (Power Meter).
This sample is not a complete map or evidence of hardware testing.

## Preview details

- Catalog ID: `inepro-metering/pro380`
- Map version: 1.0
- Verification: not-reviewed
- Protocols: RTU, TCP
- Public preview: 12 registers. Complete in-app availability is not established by this preview.

[JSON preview](https://modbus-monitor.github.io/modbus-device-maps/maps/inepro-metering/pro380.json) · [Data terms](https://modbus-monitor.github.io/modbus-device-maps/data-license/)

## Register table (sample)

| Signal | Display address | Data type | Units | Category |
|---|---|---|---|---|
| Voltage V | 420480 | FLOAT32 | V | Voltage |
| Meter amps A | 416395 | INT16 | A | Current |
| Power down counter | 416406 | INT16 | kW | Power |
| S0 output rate impkWh | 416397 | FLOAT32 | kWh | Energy |
| Grid frequency Hz | 420488 | FLOAT32 | Hz | Frequency |
| Modbus ID | 416387 | INT16 | - | Communication |
| Protocol version | 416389 | FLOAT32 | - | Identification |
| Combination code | 416399 | INT16 | - | General |
| Current direction | 416402 | STRING | - | Current |
| L2 current direction | 416403 | STRING | - | Current |
| L3 current direction | 416404 | STRING | - | Current |
| L1 voltage V | 420482 | FLOAT32 | V | Voltage |

## Addressing and setup

Addresses and values above are copied from the public JSON preview. Confirm the exact model, firmware, register function, address base, word order, scaling and units against the manufacturer manual before polling. No manufacturer manual revision or hardware validation is established by this page.

## Use with Modbus Monitor XPF

Check the device-map catalog in your installed XPF version for current map availability and licensing. The software download link does not open this map.

[Get Modbus Monitor XPF](https://docs.quantumbitsolutions.com/downloads-purchase/) · [Request a map or correction](https://github.com/Modbus-Monitor/modbus-device-maps/issues/new/choose) · [Browse all previews](https://docs.quantumbitsolutions.com/modbus-device-maps/)

<script type="application/ld+json">{"@context": "https://schema.org", "@type": "Dataset", "name": "Inepro Metering PRO380 public register preview", "description": "Sample register addresses and data types; not a complete map or hardware verification.", "url": "https://docs.quantumbitsolutions.com/modbus-device-maps/previews/inepro-metering/pro380/", "license": "https://modbus-monitor.github.io/modbus-device-maps/data-license/", "creator": {"@type": "Organization", "name": "Quantum Bit Solutions", "url": "https://quantumbitsolutions.com/"}, "distribution": {"@type": "DataDownload", "encodingFormat": "application/json", "contentUrl": "https://modbus-monitor.github.io/modbus-device-maps/maps/inepro-metering/pro380.json"}}</script>
