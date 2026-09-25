---
title: "National Meter Industries Series 3000, Series 4000 Modbus register preview"
description: "Sample register addresses and data types for National Meter Industries Series 3000, Series 4000. Public preview with JSON source and verification status."
---

# National Meter Industries Series 3000, Series 4000 Modbus register preview

Public preview for **National Meter Industries Series 3000, Series 4000** (Power Meter).
This sample is not a complete map or evidence of hardware testing.

## Preview details

- Catalog ID: `national-meter-industries/series-3000-series-4000`
- Map version: 1.0
- Verification: not-reviewed
- Protocols: RTU, TCP
- Public preview: 11 registers. Complete in-app availability is not established by this preview.

[JSON preview](https://modbus-monitor.github.io/modbus-device-maps/maps/national-meter-industries/series-3000-series-4000.json) · [Data terms](https://modbus-monitor.github.io/modbus-device-maps/data-license/)

## Register table (sample)

| Signal | Display address | Data type | Units | Category |
|---|---|---|---|---|
| Current phase 1 mA | 400003 | UINT32 | A | Current |
| Active power phase 1 W | 400005 | UINT32 | kW | Power |
| Active energy Wh | 400019 | UINT32 | kWh | Energy |
| Voltaje phase 1 V | 400001 | UINT32 | - | General |
| Current phase 2 mA | 400009 | UINT32 | A | Current |
| Active power phase 2 W | 400011 | UINT32 | kW | Power |
| Active power phase 3 W | 400017 | UINT32 | kW | Power |
| Voltaje phase 2 V | 400007 | UINT32 | - | General |
| Voltaje phase 3 V | 400013 | UINT32 | - | General |
| Corrent phase 3 mA | 400015 | UINT32 | - | General |
| Max maximum | 400021 | UINT32 | - | General |

## Addressing and setup

Addresses and values above are copied from the public JSON preview. Confirm the exact model, firmware, register function, address base, word order, scaling and units against the manufacturer manual before polling. No manufacturer manual revision or hardware validation is established by this page.

## Use with Modbus Monitor XPF

Check the device-map catalog in your installed XPF version for current map availability and licensing. The software download link does not open this map.

[Get Modbus Monitor XPF](https://docs.quantumbitsolutions.com/downloads-purchase/) · [Request a map or correction](https://github.com/Modbus-Monitor/modbus-device-maps/issues/new/choose) · [Browse all previews](https://docs.quantumbitsolutions.com/modbus-device-maps/)

<script type="application/ld+json">{"@context": "https://schema.org", "@type": "Dataset", "name": "National Meter Industries Series 3000, Series 4000 public register preview", "description": "Sample register addresses and data types; not a complete map or hardware verification.", "url": "https://docs.quantumbitsolutions.com/modbus-device-maps/previews/national-meter-industries/series-3000-series-4000/", "license": "https://modbus-monitor.github.io/modbus-device-maps/data-license/", "creator": {"@type": "Organization", "name": "Quantum Bit Solutions", "url": "https://quantumbitsolutions.com/"}, "distribution": {"@type": "DataDownload", "encodingFormat": "application/json", "contentUrl": "https://modbus-monitor.github.io/modbus-device-maps/maps/national-meter-industries/series-3000-series-4000.json"}}</script>
