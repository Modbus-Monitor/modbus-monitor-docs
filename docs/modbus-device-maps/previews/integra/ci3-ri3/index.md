---
title: "Integra Ci3, Ri3 Modbus register preview"
description: "Sample register addresses and data types for Integra Ci3, Ri3. Public preview with JSON source and verification status."
---

# Integra Ci3, Ri3 Modbus register preview

Public preview for **Integra Ci3, Ri3** (Power Meter).
This sample is not a complete map or evidence of hardware testing.

## Preview details

- Catalog ID: `integra/ci3-ri3`
- Map version: 1.0
- Verification: not-reviewed
- Protocols: RTU, TCP
- Public preview: 12 registers. Complete in-app availability is not established by this preview.

[JSON preview](https://modbus-monitor.github.io/modbus-device-maps/maps/integra/ci3-ri3.json) · [Data terms](https://modbus-monitor.github.io/modbus-device-maps/data-license/)

## Register table (sample)

| Signal | Display address | Data type | Units | Category |
|---|---|---|---|---|
| Kp1 kW | 400007 | UINT16 | - | Power |
| Loegyimppow kWh | 400036 | UINT16 | kWh | Energy |
| Freq Hz | 400035 | UINT16 | - | Frequency |
| V1thd | 400060 | UINT16 | - | Harmonics |
| V1 V | 400001 | UINT16 | - | General |
| Kp2 kW | 400008 | UINT16 | - | Power |
| Kp3 kW | 400009 | UINT16 | - | Power |
| Kva1 kVA | 400010 | UINT16 | - | Power |
| Kva2 kVA | 400011 | UINT16 | - | Power |
| Kva3 kVA | 400012 | UINT16 | - | Power |
| Kvar1 kVAr | 400013 | UINT16 | - | Power |
| Kvar2 kVAr | 400014 | UINT16 | - | Power |

## Addressing and setup

Addresses and values above are copied from the public JSON preview. Confirm the exact model, firmware, register function, address base, word order, scaling and units against the manufacturer manual before polling. No manufacturer manual revision or hardware validation is established by this page.

## Use with Modbus Monitor XPF

Check the device-map catalog in your installed XPF version for current map availability and licensing. The software download link does not open this map.

[Get Modbus Monitor XPF](https://docs.quantumbitsolutions.com/downloads-purchase/) · [Request a map or correction](https://github.com/Modbus-Monitor/modbus-device-maps/issues/new/choose) · [Browse all previews](https://docs.quantumbitsolutions.com/modbus-device-maps/)

<script type="application/ld+json">{"@context": "https://schema.org", "@type": "Dataset", "name": "Integra Ci3, Ri3 public register preview", "description": "Sample register addresses and data types; not a complete map or hardware verification.", "url": "https://docs.quantumbitsolutions.com/modbus-device-maps/previews/integra/ci3-ri3/", "license": "https://modbus-monitor.github.io/modbus-device-maps/data-license/", "creator": {"@type": "Organization", "name": "Quantum Bit Solutions", "url": "https://quantumbitsolutions.com/"}, "distribution": {"@type": "DataDownload", "encodingFormat": "application/json", "contentUrl": "https://modbus-monitor.github.io/modbus-device-maps/maps/integra/ci3-ri3.json"}}</script>
