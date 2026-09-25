---
title: "Acrel PZ80 Modbus register preview"
description: "Sample register addresses and data types for Acrel PZ80. Public preview with JSON source and verification status."
---

# Acrel PZ80 Modbus register preview

Public preview for **Acrel PZ80** (Power Meter).
This sample is not a complete map or evidence of hardware testing.

## Preview details

- Catalog ID: `acrel/pz80`
- Map version: 1.0
- Verification: not-reviewed
- Protocols: RTU, TCP
- Public preview: 12 registers. Complete in-app availability is not established by this preview.

[JSON preview](https://modbus-monitor.github.io/modbus-device-maps/maps/acrel/pz80.json) · [Data terms](https://modbus-monitor.github.io/modbus-device-maps/data-license/)

## Register table (sample)

| Signal | Display address | Data type | Units | Category |
|---|---|---|---|---|
| Voltage effective value V | 400000 | UINT16 | V | Voltage |
| Current effective value A | 400002 | UINT16 | - | Current |
| Power factor effective value | 400006 | UINT16 | PF | Power |
| Active energy Wh | 400012 | UINT32 | kWh | Energy |
| Frequency effective value Hz | 400004 | UINT16 | Hz | Frequency |
| Alarm and IO | 400018 | UINT16 | - | Status |
| Pt ratio pt | 400016 | UINT16 | - | General |
| Voltage index | 400001 | UINT16 | V | Voltage |
| Current index | 400003 | UINT16 | - | Current |
| Frequency index | 400005 | UINT16 | Hz | Frequency |
| Power factor index | 400007 | UINT16 | PF | Power |
| Active power effective value W | 400008 | UINT16 | kW | Power |

## Addressing and setup

Addresses and values above are copied from the public JSON preview. Confirm the exact model, firmware, register function, address base, word order, scaling and units against the manufacturer manual before polling. No manufacturer manual revision or hardware validation is established by this page.

## Use with Modbus Monitor XPF

Check the device-map catalog in your installed XPF version for current map availability and licensing. The software download link does not open this map.

[Get Modbus Monitor XPF](https://docs.quantumbitsolutions.com/downloads-purchase/) · [Request a map or correction](https://github.com/Modbus-Monitor/modbus-device-maps/issues/new/choose) · [Browse all previews](https://docs.quantumbitsolutions.com/modbus-device-maps/)

<script type="application/ld+json">{"@context": "https://schema.org", "@type": "Dataset", "name": "Acrel PZ80 public register preview", "description": "Sample register addresses and data types; not a complete map or hardware verification.", "url": "https://docs.quantumbitsolutions.com/modbus-device-maps/previews/acrel/pz80/", "license": "https://modbus-monitor.github.io/modbus-device-maps/data-license/", "creator": {"@type": "Organization", "name": "Quantum Bit Solutions", "url": "https://quantumbitsolutions.com/"}, "distribution": {"@type": "DataDownload", "encodingFormat": "application/json", "contentUrl": "https://modbus-monitor.github.io/modbus-device-maps/maps/acrel/pz80.json"}}</script>
