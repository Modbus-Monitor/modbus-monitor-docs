---
title: "Obvius A90DC-12 Modbus register preview"
description: "Sample register addresses and data types for Obvius A90DC-12. Public preview with JSON source and verification status."
---

# Obvius A90DC-12 Modbus register preview

Public preview for **Obvius A90DC-12** (Power Meter).
This sample is not a complete map or evidence of hardware testing.

## Preview details

- Catalog ID: `obvius/a90dc-12`
- Map version: 1.0
- Verification: not-reviewed
- Protocols: RTU, TCP
- Public preview: 12 registers. Complete in-app availability is not established by this preview.

[JSON preview](https://modbus-monitor.github.io/modbus-device-maps/maps/obvius/a90dc-12.json) · [Data terms](https://modbus-monitor.github.io/modbus-device-maps/data-license/)

## Register table (sample)

| Signal | Display address | Data type | Units | Category |
|---|---|---|---|---|
| Channel 1 current instantaneous A | 400010 | INT16 | - | Current |
| Input power supply V | 400009 | UINT16 | kW | Power |
| Pcb temperature deg F | 400008 | INT16 | degC | Temperature |
| Input 1 mode nvrw | 400044 | UINT16 | - | General |
| Channel 1 current long average A | 400011 | INT16 | A | Current |
| Channel 2 current instantaneous A | 400012 | INT16 | - | Current |
| Channel 2 current long average A | 400013 | INT16 | A | Current |
| Channel 3 current instantaneous A | 400014 | INT16 | - | Current |
| Channel 3 current long average A | 400015 | INT16 | A | Current |
| Channel 4 current instantaneous amps 100 A | 400016 | INT16 | A | Current |
| Channel 4 current long average A | 400017 | INT16 | A | Current |
| Channel 5 current instantaneous A | 400018 | INT16 | - | Current |

## Addressing and setup

Addresses and values above are copied from the public JSON preview. Confirm the exact model, firmware, register function, address base, word order, scaling and units against the manufacturer manual before polling. No manufacturer manual revision or hardware validation is established by this page.

## Use with Modbus Monitor XPF

Check the device-map catalog in your installed XPF version for current map availability and licensing. The software download link does not open this map.

[Get Modbus Monitor XPF](https://docs.quantumbitsolutions.com/downloads-purchase/) · [Request a map or correction](https://github.com/Modbus-Monitor/modbus-device-maps/issues/new/choose) · [Browse all previews](https://docs.quantumbitsolutions.com/modbus-device-maps/)

<script type="application/ld+json">{"@context": "https://schema.org", "@type": "Dataset", "name": "Obvius A90DC-12 public register preview", "description": "Sample register addresses and data types; not a complete map or hardware verification.", "url": "https://docs.quantumbitsolutions.com/modbus-device-maps/previews/obvius/a90dc-12/", "license": "https://modbus-monitor.github.io/modbus-device-maps/data-license/", "creator": {"@type": "Organization", "name": "Quantum Bit Solutions", "url": "https://quantumbitsolutions.com/"}, "distribution": {"@type": "DataDownload", "encodingFormat": "application/json", "contentUrl": "https://modbus-monitor.github.io/modbus-device-maps/maps/obvius/a90dc-12.json"}}</script>
