---
title: "Chint Power CPS Modbus register preview"
description: "Sample register addresses and data types for Chint Power CPS. Public preview with JSON source and verification status."
---

# Chint Power CPS Modbus register preview

Public preview for **Chint Power CPS** (Power Meter).
This sample is not a complete map or evidence of hardware testing.

## Preview details

- Catalog ID: `chint-power/cps`
- Map version: 1.0
- Verification: not-reviewed
- Protocols: RTU, TCP
- Public preview: 12 registers. Complete in-app availability is not established by this preview.

[JSON preview](https://modbus-monitor.github.io/modbus-device-maps/maps/chint-power/cps.json) · [Data terms](https://modbus-monitor.github.io/modbus-device-maps/data-license/)

## Register table (sample)

| Signal | Display address | Data type | Units | Category |
|---|---|---|---|---|
| Grid voltage uab V | 300031 | UINT16 | V | Voltage |
| Grid A phase current A | 300034 | UINT16 | - | Current |
| Maximum active ac power during the day kW | 300027 | UINT16 | kW | Power |
| Grid frequency Hz | 300043 | UINT16 | Hz | Frequency |
| Permanent fault pfault | 300052 | UINT16 | - | Power Factor |
| Inverter operation state | 300047 | UINT16 | - | Status |
| Internal inverter temperature C | 300045 | INT16 | degC | Temperature |
| Error timestamp | 300048 | INT64 | - | General |
| Active ac power reading kW | 300029 | UINT16 | kW | Power |
| Apparent ac power reading kVA | 300030 | UINT16 | kW | Power |
| Grid voltage ubc V | 300032 | UINT16 | V | Voltage |
| Grid voltage uca V | 300033 | UINT16 | V | Voltage |

## Addressing and setup

Addresses and values above are copied from the public JSON preview. Confirm the exact model, firmware, register function, address base, word order, scaling and units against the manufacturer manual before polling. No manufacturer manual revision or hardware validation is established by this page.

## Use with Modbus Monitor XPF

Check the device-map catalog in your installed XPF version for current map availability and licensing. The software download link does not open this map.

[Get Modbus Monitor XPF](https://docs.quantumbitsolutions.com/downloads-purchase/) · [Request a map or correction](https://github.com/Modbus-Monitor/modbus-device-maps/issues/new/choose) · [Browse all previews](https://docs.quantumbitsolutions.com/modbus-device-maps/)

<script type="application/ld+json">{"@context": "https://schema.org", "@type": "Dataset", "name": "Chint Power CPS public register preview", "description": "Sample register addresses and data types; not a complete map or hardware verification.", "url": "https://docs.quantumbitsolutions.com/modbus-device-maps/previews/chint-power/cps/", "license": "https://modbus-monitor.github.io/modbus-device-maps/data-license/", "creator": {"@type": "Organization", "name": "Quantum Bit Solutions", "url": "https://quantumbitsolutions.com/"}, "distribution": {"@type": "DataDownload", "encodingFormat": "application/json", "contentUrl": "https://modbus-monitor.github.io/modbus-device-maps/maps/chint-power/cps.json"}}</script>
