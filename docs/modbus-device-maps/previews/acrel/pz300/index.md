---
title: "Acrel PZ300 Modbus register preview"
description: "Sample register addresses and data types for Acrel PZ300. Public preview with JSON source and verification status."
---

# Acrel PZ300 Modbus register preview

Public preview for **Acrel PZ300** (Power Meter).
This sample is not a complete map or evidence of hardware testing.

## Preview details

- Catalog ID: `acrel/pz300`
- Map version: 1.0
- Verification: not-reviewed
- Protocols: RTU, TCP
- Public preview: 12 registers. Complete in-app availability is not established by this preview.

[JSON preview](https://modbus-monitor.github.io/modbus-device-maps/maps/acrel/pz300.json) · [Data terms](https://modbus-monitor.github.io/modbus-device-maps/data-license/)

## Register table (sample)

| Signal | Display address | Data type | Units | Category |
|---|---|---|---|---|
| 1 voltage effective value V | 400000 | INT16 | V | Voltage |
| 1 current effective value A | 400008 | INT16 | - | Current |
| 1 active power effective value W | 400016 | INT16 | kW | Power |
| 1 active electric energy | 400052 | UINT32 | kWh | Energy |
| Frequency effective value Hz | 400048 | INT16 | Hz | Frequency |
| Pt ratio | 400050 | UINT16 | - | General |
| 2 voltage effective value | 400002 | INT16 | V | Voltage |
| 3 voltage effective value | 400004 | INT16 | V | Voltage |
| Average voltage effective value | 400006 | INT16 | V | Voltage |
| 2 current effective value | 400010 | INT16 | - | Current |
| 3 current effective value | 400012 | INT16 | - | Current |
| Total current effective value | 400014 | INT16 | - | Current |

## Addressing and setup

Addresses and values above are copied from the public JSON preview. Confirm the exact model, firmware, register function, address base, word order, scaling and units against the manufacturer manual before polling. No manufacturer manual revision or hardware validation is established by this page.

## Use with Modbus Monitor XPF

Check the device-map catalog in your installed XPF version for current map availability and licensing. The software download link does not open this map.

[Get Modbus Monitor XPF](https://docs.quantumbitsolutions.com/downloads-purchase/) · [Request a map or correction](https://github.com/Modbus-Monitor/modbus-device-maps/issues/new/choose) · [Browse all previews](https://docs.quantumbitsolutions.com/modbus-device-maps/)

<script type="application/ld+json">{"@context": "https://schema.org", "@type": "Dataset", "name": "Acrel PZ300 public register preview", "description": "Sample register addresses and data types; not a complete map or hardware verification.", "url": "https://docs.quantumbitsolutions.com/modbus-device-maps/previews/acrel/pz300/", "license": "https://modbus-monitor.github.io/modbus-device-maps/data-license/", "creator": {"@type": "Organization", "name": "Quantum Bit Solutions", "url": "https://quantumbitsolutions.com/"}, "distribution": {"@type": "DataDownload", "encodingFormat": "application/json", "contentUrl": "https://modbus-monitor.github.io/modbus-device-maps/maps/acrel/pz300.json"}}</script>
