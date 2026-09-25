---
title: "Chint Instrument DSU666,DTSU666 Modbus register preview"
description: "Sample register addresses and data types for Chint Instrument DSU666,DTSU666. Public preview with JSON source and verification status."
---

# Chint Instrument DSU666,DTSU666 Modbus register preview

Public preview for **Chint Instrument DSU666,DTSU666** (Power Meter).
This sample is not a complete map or evidence of hardware testing.

## Preview details

- Catalog ID: `chint-instrument/dsu666-dtsu666`
- Map version: 1.0
- Verification: not-reviewed
- Protocols: RTU, TCP
- Public preview: 12 registers. Complete in-app availability is not established by this preview.

[JSON preview](https://modbus-monitor.github.io/modbus-device-maps/maps/chint-instrument/dsu666-dtsu666.json) · [Data terms](https://modbus-monitor.github.io/modbus-device-maps/data-license/)

## Register table (sample)

| Signal | Display address | Data type | Units | Category |
|---|---|---|---|---|
| Line line voltage uab V | 408192 | FLOAT32 | V | Voltage |
| Current transformer ratio irat | 400006 | INT16 | - | Current |
| Conjunction active power W | 408210 | FLOAT32 | kW | Power |
| Electric energy zero clearing clre | 400002 | INT16 | kWh | Energy |
| Frequency freq | 408260 | FLOAT32 | Hz | Frequency |
| Version rev | 400000 | INT16 | - | Identification |
| Potentia1 transformer ratio urat | 400007 | INT16 | - | General |
| Line line voltage ubc V | 408194 | FLOAT32 | V | Voltage |
| Line line voltage uca V | 408196 | FLOAT32 | V | Voltage |
| Phase phase voltage ua V | 408198 | FLOAT32 | V | Voltage |
| Phase phase voltage ub V | 408200 | FLOAT32 | V | Voltage |
| Phase phase voltage uc V | 408202 | FLOAT32 | V | Voltage |

## Addressing and setup

Addresses and values above are copied from the public JSON preview. Confirm the exact model, firmware, register function, address base, word order, scaling and units against the manufacturer manual before polling. No manufacturer manual revision or hardware validation is established by this page.

## Use with Modbus Monitor XPF

Check the device-map catalog in your installed XPF version for current map availability and licensing. The software download link does not open this map.

[Get Modbus Monitor XPF](https://docs.quantumbitsolutions.com/downloads-purchase/) · [Request a map or correction](https://github.com/Modbus-Monitor/modbus-device-maps/issues/new/choose) · [Browse all previews](https://docs.quantumbitsolutions.com/modbus-device-maps/)

<script type="application/ld+json">{"@context": "https://schema.org", "@type": "Dataset", "name": "Chint Instrument DSU666,DTSU666 public register preview", "description": "Sample register addresses and data types; not a complete map or hardware verification.", "url": "https://docs.quantumbitsolutions.com/modbus-device-maps/previews/chint-instrument/dsu666-dtsu666/", "license": "https://modbus-monitor.github.io/modbus-device-maps/data-license/", "creator": {"@type": "Organization", "name": "Quantum Bit Solutions", "url": "https://quantumbitsolutions.com/"}, "distribution": {"@type": "DataDownload", "encodingFormat": "application/json", "contentUrl": "https://modbus-monitor.github.io/modbus-device-maps/maps/chint-instrument/dsu666-dtsu666.json"}}</script>
