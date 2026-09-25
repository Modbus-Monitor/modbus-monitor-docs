---
title: "Kostal Piko IQ,Plenticore Modbus register preview"
description: "Sample register addresses and data types for Kostal Piko IQ,Plenticore. Public preview with JSON source and verification status."
---

# Kostal Piko IQ,Plenticore Modbus register preview

Public preview for **Kostal Piko IQ,Plenticore** (Power Meter).
This sample is not a complete map or evidence of hardware testing.

## Preview details

- Catalog ID: `kostal/piko-iq-plenticore`
- Map version: 1.0
- Verification: not-reviewed
- Protocols: RTU, TCP
- Public preview: 12 registers. Complete in-app availability is not established by this preview.

[JSON preview](https://modbus-monitor.github.io/modbus-device-maps/maps/kostal/piko-iq-plenticore.json) · [Data terms](https://modbus-monitor.github.io/modbus-device-maps/data-license/)

## Register table (sample)

| Signal | Display address | Data type | Units | Category |
|---|---|---|---|---|
| Voltage phase 1 V | 400158 | FLOAT32 | V | Voltage |
| Current phase 1 A | 400154 | FLOAT32 | A | Current |
| Power id | 400054 | UINT16 | kW | Power |
| State of energy manager3 | 400104 | UINT32 | kWh | Energy |
| Grid frequency Hz | 400152 | FLOAT32 | Hz | Frequency |
| Inverter state2 | 400056 | UINT16 | - | Status |
| Battery temperature DC | 400214 | FLOAT32 | degC | Temperature |
| Modbus unit id | 400004 | UINT16 | - | Communication |
| Inverter article number | 400006 | STRING | - | General |
| Inverter serial number | 400014 | STRING | - | Identification |
| Total dc power W | 400100 | FLOAT32 | kW | Power |
| Power limit from evu | 400122 | FLOAT32 | kW | Power |

## Addressing and setup

Addresses and values above are copied from the public JSON preview. Confirm the exact model, firmware, register function, address base, word order, scaling and units against the manufacturer manual before polling. No manufacturer manual revision or hardware validation is established by this page.

## Use with Modbus Monitor XPF

Check the device-map catalog in your installed XPF version for current map availability and licensing. The software download link does not open this map.

[Get Modbus Monitor XPF](https://docs.quantumbitsolutions.com/downloads-purchase/) · [Request a map or correction](https://github.com/Modbus-Monitor/modbus-device-maps/issues/new/choose) · [Browse all previews](https://docs.quantumbitsolutions.com/modbus-device-maps/)

<script type="application/ld+json">{"@context": "https://schema.org", "@type": "Dataset", "name": "Kostal Piko IQ,Plenticore public register preview", "description": "Sample register addresses and data types; not a complete map or hardware verification.", "url": "https://docs.quantumbitsolutions.com/modbus-device-maps/previews/kostal/piko-iq-plenticore/", "license": "https://modbus-monitor.github.io/modbus-device-maps/data-license/", "creator": {"@type": "Organization", "name": "Quantum Bit Solutions", "url": "https://quantumbitsolutions.com/"}, "distribution": {"@type": "DataDownload", "encodingFormat": "application/json", "contentUrl": "https://modbus-monitor.github.io/modbus-device-maps/maps/kostal/piko-iq-plenticore.json"}}</script>
