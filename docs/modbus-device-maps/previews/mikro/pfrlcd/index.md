---
title: "Mikro PFRLCD Modbus register preview"
description: "Sample register addresses and data types for Mikro PFRLCD. Public preview with JSON source and verification status."
---

# Mikro PFRLCD Modbus register preview

Public preview for **Mikro PFRLCD** (Power Meter).
This sample is not a complete map or evidence of hardware testing.

## Preview details

- Catalog ID: `mikro/pfrlcd`
- Map version: 1.0
- Verification: not-reviewed
- Protocols: RTU, TCP
- Public preview: 12 registers. Complete in-app availability is not established by this preview.

[JSON preview](https://modbus-monitor.github.io/modbus-device-maps/maps/mikro/pfrlcd.json) · [Data terms](https://modbus-monitor.github.io/modbus-device-maps/data-license/)

## Register table (sample)

| Signal | Display address | Data type | Units | Category |
|---|---|---|---|---|
| Phase voltage A Vrms | 400019 | FLOAT32 | V | Voltage |
| Phase current A Irms | 400025 | FLOAT32 | - | Current |
| Active power phase A W | 400031 | FLOAT32 | kW | Power |
| Frequency Hz | 400017 | FLOAT32 | Hz | Frequency |
| Phase voltage B Vrms | 400021 | FLOAT32 | V | Voltage |
| Phase voltage C Vrms | 400023 | FLOAT32 | V | Voltage |
| Phase current B Irms | 400027 | FLOAT32 | - | Current |
| Phase current C Irms | 400029 | FLOAT32 | - | Current |
| Reactive power phase A VAR | 400033 | FLOAT32 | kW | Power |
| Apparent power phase A VA | 400035 | FLOAT32 | kW | Power |
| Power factor phase A | 400037 | FLOAT32 | PF | Power |
| Active power phase B W | 400039 | FLOAT32 | kW | Power |

## Addressing and setup

Addresses and values above are copied from the public JSON preview. Confirm the exact model, firmware, register function, address base, word order, scaling and units against the manufacturer manual before polling. No manufacturer manual revision or hardware validation is established by this page.

## Use with Modbus Monitor XPF

Check the device-map catalog in your installed XPF version for current map availability and licensing. The software download link does not open this map.

[Get Modbus Monitor XPF](https://docs.quantumbitsolutions.com/downloads-purchase/) · [Request a map or correction](https://github.com/Modbus-Monitor/modbus-device-maps/issues/new/choose) · [Browse all previews](https://docs.quantumbitsolutions.com/modbus-device-maps/)

<script type="application/ld+json">{"@context": "https://schema.org", "@type": "Dataset", "name": "Mikro PFRLCD public register preview", "description": "Sample register addresses and data types; not a complete map or hardware verification.", "url": "https://docs.quantumbitsolutions.com/modbus-device-maps/previews/mikro/pfrlcd/", "license": "https://modbus-monitor.github.io/modbus-device-maps/data-license/", "creator": {"@type": "Organization", "name": "Quantum Bit Solutions", "url": "https://quantumbitsolutions.com/"}, "distribution": {"@type": "DataDownload", "encodingFormat": "application/json", "contentUrl": "https://modbus-monitor.github.io/modbus-device-maps/maps/mikro/pfrlcd.json"}}</script>
