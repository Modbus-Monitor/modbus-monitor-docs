---
title: "Delta DPM 530 Modbus register preview"
description: "Sample register addresses and data types for Delta DPM 530. Public preview with JSON source and verification status."
---

# Delta DPM 530 Modbus register preview

Public preview for **Delta DPM 530** (Power Meter).
This sample is not a complete map or evidence of hardware testing.

## Preview details

- Catalog ID: `delta/dpm-530`
- Map version: 1.0
- Verification: not-reviewed
- Protocols: RTU, TCP
- Public preview: 12 registers. Complete in-app availability is not established by this preview.

[JSON preview](https://modbus-monitor.github.io/modbus-device-maps/maps/delta/dpm-530.json) · [Data terms](https://modbus-monitor.github.io/modbus-device-maps/data-license/)

## Register table (sample)

| Signal | Display address | Data type | Units | Category |
|---|---|---|---|---|
| Voltage A N V | 400256 | FLOAT32 | V | Voltage |
| Current A A | 400288 | FLOAT32 | - | Current |
| Power factor total | 400306 | FLOAT32 | PF | Power |
| Active energy delivered Wh | 400348 | FLOAT32 | kWh | Energy |
| Frequency Hz | 400322 | FLOAT32 | Hz | Frequency |
| Over phase loss alarm status | 401168 | UINT16 | - | Status |
| Floor area | 401280 | UINT16 | - | General |
| Voltage B N V | 400258 | FLOAT32 | V | Voltage |
| Voltage C N V | 400260 | FLOAT32 | V | Voltage |
| Voltage L N avg V | 400262 | FLOAT32 | V | Voltage |
| Voltage A B V | 400264 | FLOAT32 | V | Voltage |
| Voltage B C V | 400266 | FLOAT32 | V | Voltage |

## Addressing and setup

Addresses and values above are copied from the public JSON preview. Confirm the exact model, firmware, register function, address base, word order, scaling and units against the manufacturer manual before polling. No manufacturer manual revision or hardware validation is established by this page.

## Use with Modbus Monitor XPF

Check the device-map catalog in your installed XPF version for current map availability and licensing. The software download link does not open this map.

[Get Modbus Monitor XPF](https://docs.quantumbitsolutions.com/downloads-purchase/) · [Request a map or correction](https://github.com/Modbus-Monitor/modbus-device-maps/issues/new/choose) · [Browse all previews](https://docs.quantumbitsolutions.com/modbus-device-maps/)

<script type="application/ld+json">{"@context": "https://schema.org", "@type": "Dataset", "name": "Delta DPM 530 public register preview", "description": "Sample register addresses and data types; not a complete map or hardware verification.", "url": "https://docs.quantumbitsolutions.com/modbus-device-maps/previews/delta/dpm-530/", "license": "https://modbus-monitor.github.io/modbus-device-maps/data-license/", "creator": {"@type": "Organization", "name": "Quantum Bit Solutions", "url": "https://quantumbitsolutions.com/"}, "distribution": {"@type": "DataDownload", "encodingFormat": "application/json", "contentUrl": "https://modbus-monitor.github.io/modbus-device-maps/maps/delta/dpm-530.json"}}</script>
