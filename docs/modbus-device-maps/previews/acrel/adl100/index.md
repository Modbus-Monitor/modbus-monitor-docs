---
title: "Acrel ADL100 Modbus register preview"
description: "Sample register addresses and data types for Acrel ADL100. Public preview with JSON source and verification status."
---

# Acrel ADL100 Modbus register preview

Public preview for **Acrel ADL100** (Power Meter).
This sample is not a complete map or evidence of hardware testing.

## Preview details

- Catalog ID: `acrel/adl100`
- Map version: 1.0
- Verification: not-reviewed
- Protocols: RTU, TCP
- Public preview: 12 registers. Complete in-app availability is not established by this preview.

[JSON preview](https://modbus-monitor.github.io/modbus-device-maps/maps/acrel/adl100.json) · [Data terms](https://modbus-monitor.github.io/modbus-device-maps/data-license/)

## Register table (sample)

| Signal | Display address | Data type | Units | Category |
|---|---|---|---|---|
| Voltage | 400012 | UINT16 | V | Voltage |
| Current total kwh | 400000 | UINT32 | kWh | Current |
| Negative kwh | 400008 | UINT32 | kWh | Energy |
| Frequency | 400017 | UINT16 | Hz | Frequency |
| Q | 400015 | UINT16 | - | General |
| Current peak kwh | 400002 | UINT32 | kWh | Current |
| Current valley kwh | 400006 | UINT32 | kWh | Current |
| Reactive kwh | 400010 | UINT32 | kWh | Energy |
| Current | 400013 | UINT16 | - | Current |
| Total kwh this month | 400034 | UINT32 | kWh | Energy |
| Peak kwh this month | 400036 | UINT32 | kWh | Energy |
| Flat kwh this month | 400038 | UINT32 | kWh | Energy |

## Addressing and setup

Addresses and values above are copied from the public JSON preview. Confirm the exact model, firmware, register function, address base, word order, scaling and units against the manufacturer manual before polling. No manufacturer manual revision or hardware validation is established by this page.

## Use with Modbus Monitor XPF

Check the device-map catalog in your installed XPF version for current map availability and licensing. The software download link does not open this map.

[Get Modbus Monitor XPF](https://docs.quantumbitsolutions.com/downloads-purchase/) · [Request a map or correction](https://github.com/Modbus-Monitor/modbus-device-maps/issues/new/choose) · [Browse all previews](https://docs.quantumbitsolutions.com/modbus-device-maps/)

<script type="application/ld+json">{"@context": "https://schema.org", "@type": "Dataset", "name": "Acrel ADL100 public register preview", "description": "Sample register addresses and data types; not a complete map or hardware verification.", "url": "https://docs.quantumbitsolutions.com/modbus-device-maps/previews/acrel/adl100/", "license": "https://modbus-monitor.github.io/modbus-device-maps/data-license/", "creator": {"@type": "Organization", "name": "Quantum Bit Solutions", "url": "https://quantumbitsolutions.com/"}, "distribution": {"@type": "DataDownload", "encodingFormat": "application/json", "contentUrl": "https://modbus-monitor.github.io/modbus-device-maps/maps/acrel/adl100.json"}}</script>
