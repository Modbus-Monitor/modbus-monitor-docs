---
title: "Veris E50 Modbus register preview"
description: "Sample register addresses and data types for Veris E50. Public preview with JSON source and verification status."
---

# Veris E50 Modbus register preview

Public preview for **Veris E50** (Power Meter).
This sample is not a complete map or evidence of hardware testing.

## Preview details

- Catalog ID: `veris/e50`
- Map version: 1.0
- Verification: not-reviewed
- Protocols: RTU, TCP
- Public preview: 12 registers. Complete in-app availability is not established by this preview.

[JSON preview](https://modbus-monitor.github.io/modbus-device-maps/maps/veris/e50.json) · [Data terms](https://modbus-monitor.github.io/modbus-device-maps/data-license/)

## Register table (sample)

| Signal | Display address | Data type | Units | Category |
|---|---|---|---|---|
| Voltage L l average of 3 phases Volt | 300007 | UINT16 | V | Voltage |
| Current average of 3 phases Amp | 300009 | UINT16 | A | Current |
| Total instantaneous real power 3 phase total kW | 300003 | UINT16 | kW | Power |
| Real energy consumption kWh | 300001 | UINT32 | kWh | Energy |
| Frequency derived from phase A Hz | 300026 | UINT16 | Hz | Frequency |
| Ljrrent instantaneous phase C Amp | 300024 | UINT16 | - | General |
| Total instantaneous reactive power 3 phase total kVAR | 300004 | UINT16 | kW | Power |
| Total instantaneous apparent power 3 phase total KVA | 300005 | UINT16 | kW | Power |
| Total power factor total kw total kva Ratio | 300006 | UINT16 | PF | Power |
| Voltage L ii average of 3 phases Volt | 300008 | UINT16 | V | Voltage |
| Real power phase A kW | 300010 | UINT16 | kW | Power |
| Real power phase B kW | 300011 | UINT16 | kW | Power |

## Addressing and setup

Addresses and values above are copied from the public JSON preview. Confirm the exact model, firmware, register function, address base, word order, scaling and units against the manufacturer manual before polling. No manufacturer manual revision or hardware validation is established by this page.

## Use with Modbus Monitor XPF

Check the device-map catalog in your installed XPF version for current map availability and licensing. The software download link does not open this map.

[Get Modbus Monitor XPF](https://docs.quantumbitsolutions.com/downloads-purchase/) · [Request a map or correction](https://github.com/Modbus-Monitor/modbus-device-maps/issues/new/choose) · [Browse all previews](https://docs.quantumbitsolutions.com/modbus-device-maps/)

<script type="application/ld+json">{"@context": "https://schema.org", "@type": "Dataset", "name": "Veris E50 public register preview", "description": "Sample register addresses and data types; not a complete map or hardware verification.", "url": "https://docs.quantumbitsolutions.com/modbus-device-maps/previews/veris/e50/", "license": "https://modbus-monitor.github.io/modbus-device-maps/data-license/", "creator": {"@type": "Organization", "name": "Quantum Bit Solutions", "url": "https://quantumbitsolutions.com/"}, "distribution": {"@type": "DataDownload", "encodingFormat": "application/json", "contentUrl": "https://modbus-monitor.github.io/modbus-device-maps/maps/veris/e50.json"}}</script>
