---
title: "Acrel PZ72-E3,P80-E3,PZ96-E3 Modbus register preview"
description: "Sample register addresses and data types for Acrel PZ72-E3,P80-E3,PZ96-E3. Public preview with JSON source and verification status."
---

# Acrel PZ72-E3,P80-E3,PZ96-E3 Modbus register preview

Public preview for **Acrel PZ72-E3,P80-E3,PZ96-E3** (Power Meter).
This sample is not a complete map or evidence of hardware testing.

## Preview details

- Catalog ID: `acrel/pz72-e3-p80-e3-pz96-e3`
- Map version: 1.0
- Verification: not-reviewed
- Protocols: RTU, TCP
- Public preview: 12 registers. Complete in-app availability is not established by this preview.

[JSON preview](https://modbus-monitor.github.io/modbus-device-maps/maps/acrel/pz72-e3-p80-e3-pz96-e3.json) · [Data terms](https://modbus-monitor.github.io/modbus-device-maps/data-license/)

## Register table (sample)

| Signal | Display address | Data type | Units | Category |
|---|---|---|---|---|
| Phase voltage A V | 400037 | UINT16 | V | Voltage |
| Measued im kwh | 400063 | UINT32 | kWh | Energy |
| Frequency F | 400062 | UINT16 | Hz | Frequency |
| The statement of relays | 400034 | UINT16 | - | Status |
| Ia A | 400043 | UINT16 | - | General |
| Phase voltage B V | 400038 | UINT16 | V | Voltage |
| Phase voltage C V | 400039 | UINT16 | V | Voltage |
| Line voltage AB V | 400040 | UINT16 | V | Voltage |
| Line voltage BC V | 400041 | UINT16 | V | Voltage |
| Line voltage AC V | 400042 | UINT16 | V | Voltage |
| Measued export kwh | 400065 | UINT32 | kWh | Energy |
| Measued import kvarh | 400067 | UINT32 | kWh | Energy |

## Addressing and setup

Addresses and values above are copied from the public JSON preview. Confirm the exact model, firmware, register function, address base, word order, scaling and units against the manufacturer manual before polling. No manufacturer manual revision or hardware validation is established by this page.

## Use with Modbus Monitor XPF

Check the device-map catalog in your installed XPF version for current map availability and licensing. The software download link does not open this map.

[Get Modbus Monitor XPF](https://docs.quantumbitsolutions.com/downloads-purchase/) · [Request a map or correction](https://github.com/Modbus-Monitor/modbus-device-maps/issues/new/choose) · [Browse all previews](https://docs.quantumbitsolutions.com/modbus-device-maps/)

<script type="application/ld+json">{"@context": "https://schema.org", "@type": "Dataset", "name": "Acrel PZ72-E3,P80-E3,PZ96-E3 public register preview", "description": "Sample register addresses and data types; not a complete map or hardware verification.", "url": "https://docs.quantumbitsolutions.com/modbus-device-maps/previews/acrel/pz72-e3-p80-e3-pz96-e3/", "license": "https://modbus-monitor.github.io/modbus-device-maps/data-license/", "creator": {"@type": "Organization", "name": "Quantum Bit Solutions", "url": "https://quantumbitsolutions.com/"}, "distribution": {"@type": "DataDownload", "encodingFormat": "application/json", "contentUrl": "https://modbus-monitor.github.io/modbus-device-maps/maps/acrel/pz72-e3-p80-e3-pz96-e3.json"}}</script>
