---
title: "Tense TPM 05 Modbus register preview"
description: "Sample register addresses and data types for Tense TPM 05. Public preview with JSON source and verification status."
---

# Tense TPM 05 Modbus register preview

Public preview for **Tense TPM 05** (Power Meter).
This sample is not a complete map or evidence of hardware testing.

## Preview details

- Catalog ID: `tense/tpm-05`
- Map version: 1.0
- Verification: not-reviewed
- Protocols: RTU, TCP
- Public preview: 12 registers. Complete in-app availability is not established by this preview.

[JSON preview](https://modbus-monitor.github.io/modbus-device-maps/maps/tense/tpm-05.json) · [Data terms](https://modbus-monitor.github.io/modbus-device-maps/data-license/)

## Register table (sample)

| Signal | Display address | Data type | Units | Category |
|---|---|---|---|---|
| L2 THDV | 402001 | UINT16 | - | Harmonics |
| L3 THDV | 402002 | UINT16 | - | Harmonics |
| 3P THDV | 402003 | UINT16 | - | Harmonics |
| L1 THDI | 402004 | UINT16 | - | Harmonics |
| L2 THDI | 402005 | UINT16 | - | Harmonics |
| L3 THDI | 402006 | UINT16 | - | Harmonics |
| 3P THDI | 402007 | UINT16 | - | Harmonics |
| VL1 harmonic 2 | 402011 | UINT16 | - | Harmonics |
| VL1 harmonic 3 | 402012 | UINT16 | - | Harmonics |
| VL1 harmonic 4 | 402013 | UINT16 | - | Harmonics |
| VL1 harmonic 63 | 402072 | UINT16 | - | Harmonics |
| VL2 harmonic 2 | 402073 | UINT16 | - | Harmonics |

## Addressing and setup

Addresses and values above are copied from the public JSON preview. Confirm the exact model, firmware, register function, address base, word order, scaling and units against the manufacturer manual before polling. No manufacturer manual revision or hardware validation is established by this page.

## Use with Modbus Monitor XPF

Check the device-map catalog in your installed XPF version for current map availability and licensing. The software download link does not open this map.

[Get Modbus Monitor XPF](https://docs.quantumbitsolutions.com/downloads-purchase/) · [Request a map or correction](https://github.com/Modbus-Monitor/modbus-device-maps/issues/new/choose) · [Browse all previews](https://docs.quantumbitsolutions.com/modbus-device-maps/)

<script type="application/ld+json">{"@context": "https://schema.org", "@type": "Dataset", "name": "Tense TPM 05 public register preview", "description": "Sample register addresses and data types; not a complete map or hardware verification.", "url": "https://docs.quantumbitsolutions.com/modbus-device-maps/previews/tense/tpm-05/", "license": "https://modbus-monitor.github.io/modbus-device-maps/data-license/", "creator": {"@type": "Organization", "name": "Quantum Bit Solutions", "url": "https://quantumbitsolutions.com/"}, "distribution": {"@type": "DataDownload", "encodingFormat": "application/json", "contentUrl": "https://modbus-monitor.github.io/modbus-device-maps/maps/tense/tpm-05.json"}}</script>
