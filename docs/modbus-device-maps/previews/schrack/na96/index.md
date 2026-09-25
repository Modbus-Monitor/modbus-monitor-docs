---
title: "Schrack NA96 Modbus register preview"
description: "Sample register addresses and data types for Schrack NA96. Public preview with JSON source and verification status."
---

# Schrack NA96 Modbus register preview

Public preview for **Schrack NA96** (Power Meter).
This sample is not a complete map or evidence of hardware testing.

## Preview details

- Catalog ID: `schrack/na96`
- Map version: 1.0
- Verification: not-reviewed
- Protocols: RTU, TCP
- Public preview: 12 registers. Complete in-app availability is not established by this preview.

[JSON preview](https://modbus-monitor.github.io/modbus-device-maps/maps/schrack/na96.json) · [Data terms](https://modbus-monitor.github.io/modbus-device-maps/data-license/)

## Register table (sample)

| Signal | Display address | Data type | Units | Category |
|---|---|---|---|---|
| Phase 1 phase voltage mV | 400769 | INT32 | V | Voltage |
| Phase 1 current mA | 400781 | INT32 | - | Current |
| 3phase active power | 400793 | INT32 | kW | Power |
| 3phase positive reactive energy | 400835 | INT32 | kWh | Energy |
| Frequency Hz | 400825 | UINT16 | Hz | Frequency |
| 3phase peak maximum demand | 400852 | INT32 | kW | Demand |
| Output relay status | 400833 | UINT16 | - | Status |
| Phase 1 thd vl | 400912 | UINT16 | - | Harmonics |
| 3phase positive active enerqy | 400805 | INT32 | - | General |
| Phase 2 phase voltage mV | 400773 | INT32 | V | Voltage |
| Phase 3 phase voltage mV | 400777 | INT32 | V | Voltage |
| Phase 2 current mA | 400785 | INT32 | - | Current |

## Addressing and setup

Addresses and values above are copied from the public JSON preview. Confirm the exact model, firmware, register function, address base, word order, scaling and units against the manufacturer manual before polling. No manufacturer manual revision or hardware validation is established by this page.

## Use with Modbus Monitor XPF

Check the device-map catalog in your installed XPF version for current map availability and licensing. The software download link does not open this map.

[Get Modbus Monitor XPF](https://docs.quantumbitsolutions.com/downloads-purchase/) · [Request a map or correction](https://github.com/Modbus-Monitor/modbus-device-maps/issues/new/choose) · [Browse all previews](https://docs.quantumbitsolutions.com/modbus-device-maps/)

<script type="application/ld+json">{"@context": "https://schema.org", "@type": "Dataset", "name": "Schrack NA96 public register preview", "description": "Sample register addresses and data types; not a complete map or hardware verification.", "url": "https://docs.quantumbitsolutions.com/modbus-device-maps/previews/schrack/na96/", "license": "https://modbus-monitor.github.io/modbus-device-maps/data-license/", "creator": {"@type": "Organization", "name": "Quantum Bit Solutions", "url": "https://quantumbitsolutions.com/"}, "distribution": {"@type": "DataDownload", "encodingFormat": "application/json", "contentUrl": "https://modbus-monitor.github.io/modbus-device-maps/maps/schrack/na96.json"}}</script>
