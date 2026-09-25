---
title: "Meatrol ME437 Modbus register preview"
description: "Sample register addresses and data types for Meatrol ME437. Public preview with JSON source and verification status."
---

# Meatrol ME437 Modbus register preview

Public preview for **Meatrol ME437** (Power Meter).
This sample is not a complete map or evidence of hardware testing.

## Preview details

- Catalog ID: `meatrol/me437`
- Map version: 1.0
- Verification: not-reviewed
- Protocols: RTU, TCP
- Public preview: 12 registers. Complete in-app availability is not established by this preview.

[JSON preview](https://modbus-monitor.github.io/modbus-device-maps/maps/meatrol/me437.json) · [Data terms](https://modbus-monitor.github.io/modbus-device-maps/data-license/)

## Register table (sample)

| Signal | Display address | Data type | Units | Category |
|---|---|---|---|---|
| Phase 1 X times harmonics voltage distortion | 402083 | FLOAT32 | V | Voltage |
| Phase 1 X times harmonics current distortion | 402027 | FLOAT32 | - | Current |
| Phase 1 power factor | 402000 | FLOAT32 | PF | Power |
| Active energy import phase 1 kWh | 404000 | UINT32 | kWh | Energy |
| Phase 1 frequency Hz | 402016 | FLOAT32 | Hz | Frequency |
| Average of PF1 PF2 PF3 | 402006 | FLOAT32 | - | Power Factor |
| Average of I1THDx I2THDx I3THDx | 402033 | FLOAT32 | - | Harmonics |
| Range2-52 | 402024 | UINT16 | - | General |
| Phase 2 power factor | 402002 | FLOAT32 | PF | Power |
| Phase 3 power factor | 402004 | FLOAT32 | PF | Power |
| Phase 1 displacement power factor | 402008 | FLOAT32 | PF | Power |
| Phase 2 displacement power factor | 402010 | FLOAT32 | PF | Power |

## Addressing and setup

Addresses and values above are copied from the public JSON preview. Confirm the exact model, firmware, register function, address base, word order, scaling and units against the manufacturer manual before polling. No manufacturer manual revision or hardware validation is established by this page.

## Use with Modbus Monitor XPF

Check the device-map catalog in your installed XPF version for current map availability and licensing. The software download link does not open this map.

[Get Modbus Monitor XPF](https://docs.quantumbitsolutions.com/downloads-purchase/) · [Request a map or correction](https://github.com/Modbus-Monitor/modbus-device-maps/issues/new/choose) · [Browse all previews](https://docs.quantumbitsolutions.com/modbus-device-maps/)

<script type="application/ld+json">{"@context": "https://schema.org", "@type": "Dataset", "name": "Meatrol ME437 public register preview", "description": "Sample register addresses and data types; not a complete map or hardware verification.", "url": "https://docs.quantumbitsolutions.com/modbus-device-maps/previews/meatrol/me437/", "license": "https://modbus-monitor.github.io/modbus-device-maps/data-license/", "creator": {"@type": "Organization", "name": "Quantum Bit Solutions", "url": "https://quantumbitsolutions.com/"}, "distribution": {"@type": "DataDownload", "encodingFormat": "application/json", "contentUrl": "https://modbus-monitor.github.io/modbus-device-maps/maps/meatrol/me437.json"}}</script>
