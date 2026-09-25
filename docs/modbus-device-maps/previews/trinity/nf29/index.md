---
title: "Trinity NF29 Modbus register preview"
description: "Sample register addresses and data types for Trinity NF29. Public preview with JSON source and verification status."
---

# Trinity NF29 Modbus register preview

Public preview for **Trinity NF29** (Power Meter).
This sample is not a complete map or evidence of hardware testing.

## Preview details

- Catalog ID: `trinity/nf29`
- Map version: 1.0
- Verification: not-reviewed
- Protocols: RTU, TCP
- Public preview: 12 registers. Complete in-app availability is not established by this preview.

[JSON preview](https://modbus-monitor.github.io/modbus-device-maps/maps/trinity/nf29.json) · [Data terms](https://modbus-monitor.github.io/modbus-device-maps/data-license/)

## Register table (sample)

| Signal | Display address | Data type | Units | Category |
|---|---|---|---|---|
| 3-phase Average amps A | 403011 | UINT32 | A | Current |
| 3-phase KVA KVa | 402999 | UINT32 | - | Power |
| 3-phase KW KWh | 403001 | UINT32 | kWh | Energy |
| R-phase Frequency Hz | 403035 | UINT32 | Hz | Frequency |
| 3-phase Average VLL V | 403007 | UINT32 | - | General |
| 3-phase KVA KVar | 403003 | UINT32 | - | Power |
| 3-phase Power factor | 403005 | UINT32 | PF | Power |
| R-phase KWh KWh | 403029 | UINT32 | kWh | Energy |
| R-phase KVAh KVA | 403031 | UINT32 | - | Power |
| R-phase KVARh KVARh | 403033 | UINT32 | kWh | Energy |
| R-phase Power factor | 403043 | UINT32 | PF | Power |
| R-phase KVA KVA | 403119 | UINT32 | - | Power |

## Addressing and setup

Addresses and values above are copied from the public JSON preview. Confirm the exact model, firmware, register function, address base, word order, scaling and units against the manufacturer manual before polling. No manufacturer manual revision or hardware validation is established by this page.

## Use with Modbus Monitor XPF

Check the device-map catalog in your installed XPF version for current map availability and licensing. The software download link does not open this map.

[Get Modbus Monitor XPF](https://docs.quantumbitsolutions.com/downloads-purchase/) · [Request a map or correction](https://github.com/Modbus-Monitor/modbus-device-maps/issues/new/choose) · [Browse all previews](https://docs.quantumbitsolutions.com/modbus-device-maps/)

<script type="application/ld+json">{"@context": "https://schema.org", "@type": "Dataset", "name": "Trinity NF29 public register preview", "description": "Sample register addresses and data types; not a complete map or hardware verification.", "url": "https://docs.quantumbitsolutions.com/modbus-device-maps/previews/trinity/nf29/", "license": "https://modbus-monitor.github.io/modbus-device-maps/data-license/", "creator": {"@type": "Organization", "name": "Quantum Bit Solutions", "url": "https://quantumbitsolutions.com/"}, "distribution": {"@type": "DataDownload", "encodingFormat": "application/json", "contentUrl": "https://modbus-monitor.github.io/modbus-device-maps/maps/trinity/nf29.json"}}</script>
