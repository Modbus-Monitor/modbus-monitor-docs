---
title: "Owen Brothers OB737 Modbus register preview"
description: "Sample register addresses and data types for Owen Brothers OB737. Public preview with JSON source and verification status."
---

# Owen Brothers OB737 Modbus register preview

Public preview for **Owen Brothers OB737** (Power Meter).
This sample is not a complete map or evidence of hardware testing.

## Preview details

- Catalog ID: `owen-brothers/ob737`
- Map version: 1.0
- Verification: not-reviewed
- Protocols: RTU, TCP
- Public preview: 12 registers. Complete in-app availability is not established by this preview.

[JSON preview](https://modbus-monitor.github.io/modbus-device-maps/maps/owen-brothers/ob737.json) · [Data terms](https://modbus-monitor.github.io/modbus-device-maps/data-license/)

## Register table (sample)

| Signal | Display address | Data type | Units | Category |
|---|---|---|---|---|
| Conductor voltage to N U1 V | 404096 | FLOAT32 | V | Voltage |
| Current in conductor I1 A | 404110 | FLOAT32 | - | Current |
| Power factor phase 1 - | 404120 | FLOAT32 | PF | Power |
| Total active energy procurement L1 Wh | 404352 | FLOAT32 | kWh | Energy |
| Frequency Hz | 404152 | FLOAT32 | Hz | Frequency |
| Phase sequence 0123 | 404154 | FLOAT32 | - | General |
| Conductor voltage to N U2 V | 404098 | FLOAT32 | V | Voltage |
| Conductor voltage to N U3 V | 404100 | FLOAT32 | V | Voltage |
| Conductor voltage to conductor U12 V | 404102 | FLOAT32 | V | Voltage |
| Conductor voltage to conductor U23 V | 404104 | FLOAT32 | V | Voltage |
| Conductor voltage to conductor U31 V | 404106 | FLOAT32 | V | Voltage |
| External conductor voltage system V | 404108 | FLOAT32 | V | Voltage |

## Addressing and setup

Addresses and values above are copied from the public JSON preview. Confirm the exact model, firmware, register function, address base, word order, scaling and units against the manufacturer manual before polling. No manufacturer manual revision or hardware validation is established by this page.

## Use with Modbus Monitor XPF

Check the device-map catalog in your installed XPF version for current map availability and licensing. The software download link does not open this map.

[Get Modbus Monitor XPF](https://docs.quantumbitsolutions.com/downloads-purchase/) · [Request a map or correction](https://github.com/Modbus-Monitor/modbus-device-maps/issues/new/choose) · [Browse all previews](https://docs.quantumbitsolutions.com/modbus-device-maps/)

<script type="application/ld+json">{"@context": "https://schema.org", "@type": "Dataset", "name": "Owen Brothers OB737 public register preview", "description": "Sample register addresses and data types; not a complete map or hardware verification.", "url": "https://docs.quantumbitsolutions.com/modbus-device-maps/previews/owen-brothers/ob737/", "license": "https://modbus-monitor.github.io/modbus-device-maps/data-license/", "creator": {"@type": "Organization", "name": "Quantum Bit Solutions", "url": "https://quantumbitsolutions.com/"}, "distribution": {"@type": "DataDownload", "encodingFormat": "application/json", "contentUrl": "https://modbus-monitor.github.io/modbus-device-maps/maps/owen-brothers/ob737.json"}}</script>
