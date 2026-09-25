---
title: "NZIF SET-4TM Modbus register preview"
description: "Sample register addresses and data types for NZIF SET-4TM. Public preview with JSON source and verification status."
---

# NZIF SET-4TM Modbus register preview

Public preview for **NZIF SET-4TM** (Power Meter).
This sample is not a complete map or evidence of hardware testing.

## Preview details

- Catalog ID: `nzif/set-4tm`
- Map version: 1.0
- Verification: not-reviewed
- Protocols: RTU, TCP
- Public preview: 12 registers. Complete in-app availability is not established by this preview.

[JSON preview](https://modbus-monitor.github.io/modbus-device-maps/maps/nzif/set-4tm.json) · [Data terms](https://modbus-monitor.github.io/modbus-device-maps/data-license/)

## Register table (sample)

| Signal | Display address | Data type | Units | Category |
|---|---|---|---|---|
| Device 1 Voltage A | 404361 | UINT16 | V | Voltage |
| Device 1 Active power A | 404364 | UINT32 | kW | Power |
| Device 1 Total active energy | 404371 | UINT32 | kWh | Energy |
| Device 1 Connection state | 404352 | UINT16 | - | Status |
| Device 1 Temperature | 404370 | UINT16 | degC | Temperature |
| Device 1 Address | 404353 | UINT16 | - | Communication |
| Device 1 Timestamp | 404357 | INT16 | - | General |
| Device 1 Voltage B | 404362 | UINT16 | V | Voltage |
| Device 1 Voltage C | 404363 | UINT16 | V | Voltage |
| Device 1 Active power B | 404366 | UINT32 | kW | Power |
| Device 1 Active power C | 404368 | UINT32 | kW | Power |
| Device 1 Total reactive energy | 404373 | UINT32 | kWh | Energy |

## Addressing and setup

Addresses and values above are copied from the public JSON preview. Confirm the exact model, firmware, register function, address base, word order, scaling and units against the manufacturer manual before polling. No manufacturer manual revision or hardware validation is established by this page.

## Use with Modbus Monitor XPF

Check the device-map catalog in your installed XPF version for current map availability and licensing. The software download link does not open this map.

[Get Modbus Monitor XPF](https://docs.quantumbitsolutions.com/downloads-purchase/) · [Request a map or correction](https://github.com/Modbus-Monitor/modbus-device-maps/issues/new/choose) · [Browse all previews](https://docs.quantumbitsolutions.com/modbus-device-maps/)

<script type="application/ld+json">{"@context": "https://schema.org", "@type": "Dataset", "name": "NZIF SET-4TM public register preview", "description": "Sample register addresses and data types; not a complete map or hardware verification.", "url": "https://docs.quantumbitsolutions.com/modbus-device-maps/previews/nzif/set-4tm/", "license": "https://modbus-monitor.github.io/modbus-device-maps/data-license/", "creator": {"@type": "Organization", "name": "Quantum Bit Solutions", "url": "https://quantumbitsolutions.com/"}, "distribution": {"@type": "DataDownload", "encodingFormat": "application/json", "contentUrl": "https://modbus-monitor.github.io/modbus-device-maps/maps/nzif/set-4tm.json"}}</script>
