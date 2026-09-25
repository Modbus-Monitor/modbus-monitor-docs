---
title: "OutBack Power MATE3S Modbus register preview"
description: "Sample register addresses and data types for OutBack Power MATE3S. Public preview with JSON source and verification status."
---

# OutBack Power MATE3S Modbus register preview

Public preview for **OutBack Power MATE3S** (Power Meter).
This sample is not a complete map or evidence of hardware testing.

## Preview details

- Catalog ID: `outback-power/mate3s`
- Map version: 1.0
- Verification: not-reviewed
- Protocols: RTU, TCP
- Public preview: 12 registers. Complete in-app availability is not established by this preview.

[JSON preview](https://modbus-monitor.github.io/modbus-device-maps/maps/outback-power/mate3s.json) · [Data terms](https://modbus-monitor.github.io/modbus-device-maps/data-license/)

## Register table (sample)

| Signal | Display address | Data type | Units | Category |
|---|---|---|---|---|
| Phase Voltage AB V | 440525 | UINT16 | V | Voltage |
| AC Current A | 440520 | UINT16 | - | Current |
| AC Power W | 440532 | INT16 | kW | Power |
| AC Energy Wh | 440542 | UINT32 | kWh | Energy |
| Line Frequency Hz | 440534 | UINT16 | Hz | Frequency |
| Scale factor PFSF | 440541 | INT16 | - | Power Factor |
| Enumerated value Operating state | 440556 | UINT16 | - | Status |
| Cabinet Temperature C | 440551 | INT16 | degC | Temperature |
| Scale factor ASF | 440524 | INT16 | - | General |
| Number of curves supported recommend 4 | 440793 | UINT16 | - | Communication |
| Phase A Current A | 440521 | UINT16 | - | Current |
| Phase B Current A | 440522 | UINT16 | - | Current |

## Addressing and setup

Addresses and values above are copied from the public JSON preview. Confirm the exact model, firmware, register function, address base, word order, scaling and units against the manufacturer manual before polling. No manufacturer manual revision or hardware validation is established by this page.

## Use with Modbus Monitor XPF

Check the device-map catalog in your installed XPF version for current map availability and licensing. The software download link does not open this map.

[Get Modbus Monitor XPF](https://docs.quantumbitsolutions.com/downloads-purchase/) · [Request a map or correction](https://github.com/Modbus-Monitor/modbus-device-maps/issues/new/choose) · [Browse all previews](https://docs.quantumbitsolutions.com/modbus-device-maps/)

<script type="application/ld+json">{"@context": "https://schema.org", "@type": "Dataset", "name": "OutBack Power MATE3S public register preview", "description": "Sample register addresses and data types; not a complete map or hardware verification.", "url": "https://docs.quantumbitsolutions.com/modbus-device-maps/previews/outback-power/mate3s/", "license": "https://modbus-monitor.github.io/modbus-device-maps/data-license/", "creator": {"@type": "Organization", "name": "Quantum Bit Solutions", "url": "https://quantumbitsolutions.com/"}, "distribution": {"@type": "DataDownload", "encodingFormat": "application/json", "contentUrl": "https://modbus-monitor.github.io/modbus-device-maps/maps/outback-power/mate3s.json"}}</script>
