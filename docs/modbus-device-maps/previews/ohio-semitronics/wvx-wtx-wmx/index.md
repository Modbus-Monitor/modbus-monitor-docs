---
title: "Ohio Semitronics WVx,WTx,WMx Modbus register preview"
description: "Sample register addresses and data types for Ohio Semitronics WVx,WTx,WMx. Public preview with JSON source and verification status."
---

# Ohio Semitronics WVx,WTx,WMx Modbus register preview

Public preview for **Ohio Semitronics WVx,WTx,WMx** (Power Meter).
This sample is not a complete map or evidence of hardware testing.

## Preview details

- Catalog ID: `ohio-semitronics/wvx-wtx-wmx`
- Map version: 1.0
- Verification: not-reviewed
- Protocols: RTU, TCP
- Public preview: 12 registers. Complete in-app availability is not established by this preview.

[JSON preview](https://modbus-monitor.github.io/modbus-device-maps/maps/ohio-semitronics/wvx-wtx-wmx.json) · [Data terms](https://modbus-monitor.github.io/modbus-device-maps/data-license/)

## Register table (sample)

| Signal | Display address | Data type | Units | Category |
|---|---|---|---|---|
| Current L1 | 305220 | FLOAT32 | A | Current |
| Power factor -1 to 1 | 305206 | FLOAT32 | PF | Power |
| Frequency 0 to 1000 | 305232 | FLOAT32 | Hz | Frequency |
| Watts total | 305200 | FLOAT32 | - | General |
| Current L2 | 305222 | FLOAT32 | A | Current |
| Current L3 | 305224 | FLOAT32 | A | Current |
| Power factor l1 | 305246 | FLOAT32 | PF | Power |
| Power factor l2 | 305248 | FLOAT32 | PF | Power |
| Power factor l3 | 305250 | FLOAT32 | PF | Power |
| Va total | 305202 | FLOAT32 | - | General |
| Vars total | 305204 | FLOAT32 | - | General |
| Volts L1 L2 | 305208 | FLOAT32 | - | General |

## Addressing and setup

Addresses and values above are copied from the public JSON preview. Confirm the exact model, firmware, register function, address base, word order, scaling and units against the manufacturer manual before polling. No manufacturer manual revision or hardware validation is established by this page.

## Use with Modbus Monitor XPF

Check the device-map catalog in your installed XPF version for current map availability and licensing. The software download link does not open this map.

[Get Modbus Monitor XPF](https://docs.quantumbitsolutions.com/downloads-purchase/) · [Request a map or correction](https://github.com/Modbus-Monitor/modbus-device-maps/issues/new/choose) · [Browse all previews](https://docs.quantumbitsolutions.com/modbus-device-maps/)

<script type="application/ld+json">{"@context": "https://schema.org", "@type": "Dataset", "name": "Ohio Semitronics WVx,WTx,WMx public register preview", "description": "Sample register addresses and data types; not a complete map or hardware verification.", "url": "https://docs.quantumbitsolutions.com/modbus-device-maps/previews/ohio-semitronics/wvx-wtx-wmx/", "license": "https://modbus-monitor.github.io/modbus-device-maps/data-license/", "creator": {"@type": "Organization", "name": "Quantum Bit Solutions", "url": "https://quantumbitsolutions.com/"}, "distribution": {"@type": "DataDownload", "encodingFormat": "application/json", "contentUrl": "https://modbus-monitor.github.io/modbus-device-maps/maps/ohio-semitronics/wvx-wtx-wmx.json"}}</script>
