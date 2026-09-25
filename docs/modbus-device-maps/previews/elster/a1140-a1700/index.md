---
title: "Elster A1140,A1700 Modbus register preview"
description: "Sample register addresses and data types for Elster A1140,A1700. Public preview with JSON source and verification status."
---

# Elster A1140,A1700 Modbus register preview

Public preview for **Elster A1140,A1700** (Power Meter).
This sample is not a complete map or evidence of hardware testing.

## Preview details

- Catalog ID: `elster/a1140-a1700`
- Map version: 1.0
- Verification: not-reviewed
- Protocols: RTU, TCP
- Public preview: 12 registers. Complete in-app availability is not established by this preview.

[JSON preview](https://modbus-monitor.github.io/modbus-device-maps/maps/elster/a1140-a1700.json) · [Data terms](https://modbus-monitor.github.io/modbus-device-maps/data-license/)

## Register table (sample)

| Signal | Display address | Data type | Units | Category |
|---|---|---|---|---|
| kWhTotalExport | 300053 | INT32 | kWh | Energy |
| Pfa | 300031 | FLOAT32 | - | Power Factor |
| Va | 300001 | FLOAT32 | - | General |
| Pfb | 300033 | FLOAT32 | - | Power Factor |
| Pfc | 300035 | FLOAT32 | - | Power Factor |
| pfsUM | 300043 | FLOAT32 | - | Power Factor |
| kVarhImportLag | 300055 | INT32 | kWh | Energy |
| kVarhImportLead | 300057 | INT32 | kWh | Energy |
| kVarhExportLag | 300059 | INT32 | kWh | Energy |
| LastEnergyRead | 300095 | UINT16 | kWh | Energy |
| HIST kWhTotalImport | 300097 | INT32 | kWh | Energy |
| HIST kWhTotalExport | 300099 | INT32 | kWh | Energy |

## Addressing and setup

Addresses and values above are copied from the public JSON preview. Confirm the exact model, firmware, register function, address base, word order, scaling and units against the manufacturer manual before polling. No manufacturer manual revision or hardware validation is established by this page.

## Use with Modbus Monitor XPF

Check the device-map catalog in your installed XPF version for current map availability and licensing. The software download link does not open this map.

[Get Modbus Monitor XPF](https://docs.quantumbitsolutions.com/downloads-purchase/) · [Request a map or correction](https://github.com/Modbus-Monitor/modbus-device-maps/issues/new/choose) · [Browse all previews](https://docs.quantumbitsolutions.com/modbus-device-maps/)

<script type="application/ld+json">{"@context": "https://schema.org", "@type": "Dataset", "name": "Elster A1140,A1700 public register preview", "description": "Sample register addresses and data types; not a complete map or hardware verification.", "url": "https://docs.quantumbitsolutions.com/modbus-device-maps/previews/elster/a1140-a1700/", "license": "https://modbus-monitor.github.io/modbus-device-maps/data-license/", "creator": {"@type": "Organization", "name": "Quantum Bit Solutions", "url": "https://quantumbitsolutions.com/"}, "distribution": {"@type": "DataDownload", "encodingFormat": "application/json", "contentUrl": "https://modbus-monitor.github.io/modbus-device-maps/maps/elster/a1140-a1700.json"}}</script>
