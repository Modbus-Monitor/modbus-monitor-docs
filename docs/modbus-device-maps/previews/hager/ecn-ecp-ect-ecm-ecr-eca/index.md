---
title: "Hager ECN,ECP,ECT,ECM,ECR,ECA Modbus register preview"
description: "Sample register addresses and data types for Hager ECN,ECP,ECT,ECM,ECR,ECA. Public preview with JSON source and verification status."
---

# Hager ECN,ECP,ECT,ECM,ECR,ECA Modbus register preview

Public preview for **Hager ECN,ECP,ECT,ECM,ECR,ECA** (Power Meter).
This sample is not a complete map or evidence of hardware testing.

## Preview details

- Catalog ID: `hager/ecn-ecp-ect-ecm-ecr-eca`
- Map version: 1.0
- Verification: not-reviewed
- Protocols: RTU, TCP
- Public preview: 12 registers. Complete in-app availability is not established by this preview.

[JSON preview](https://modbus-monitor.github.io/modbus-device-maps/maps/hager/ecn-ecp-ect-ecm-ecr-eca.json) · [Data terms](https://modbus-monitor.github.io/modbus-device-maps/data-license/)

## Register table (sample)

| Signal | Display address | Data type | Units | Category |
|---|---|---|---|---|
| V L1 N V | 445056 | UINT16 | - | Voltage |
| P sum L KW | 445073 | INT32 | - | Power |
| Ea sum T kWh | 445152 | UINT32 | kWh | Energy |
| F Hz | 445062 | UINT16 | - | Frequency |
| Pf sum L iec | 445079 | INT16 | - | Power Factor |
| I L1 mA | 445065 | UINT32 | - | General |
| V L2 N V | 445057 | UINT16 | - | Voltage |
| V L3 N V | 445058 | UINT16 | - | Voltage |
| V L1 L2 V | 445059 | UINT16 | - | Voltage |
| V L2 L3 V | 445060 | UINT16 | - | Voltage |
| V L3 L1 V | 445061 | UINT16 | - | Voltage |
| Not used Hz | 445063 | UINT16 | - | Frequency |

## Addressing and setup

Addresses and values above are copied from the public JSON preview. Confirm the exact model, firmware, register function, address base, word order, scaling and units against the manufacturer manual before polling. No manufacturer manual revision or hardware validation is established by this page.

## Use with Modbus Monitor XPF

Check the device-map catalog in your installed XPF version for current map availability and licensing. The software download link does not open this map.

[Get Modbus Monitor XPF](https://docs.quantumbitsolutions.com/downloads-purchase/) · [Request a map or correction](https://github.com/Modbus-Monitor/modbus-device-maps/issues/new/choose) · [Browse all previews](https://docs.quantumbitsolutions.com/modbus-device-maps/)

<script type="application/ld+json">{"@context": "https://schema.org", "@type": "Dataset", "name": "Hager ECN,ECP,ECT,ECM,ECR,ECA public register preview", "description": "Sample register addresses and data types; not a complete map or hardware verification.", "url": "https://docs.quantumbitsolutions.com/modbus-device-maps/previews/hager/ecn-ecp-ect-ecm-ecr-eca/", "license": "https://modbus-monitor.github.io/modbus-device-maps/data-license/", "creator": {"@type": "Organization", "name": "Quantum Bit Solutions", "url": "https://quantumbitsolutions.com/"}, "distribution": {"@type": "DataDownload", "encodingFormat": "application/json", "contentUrl": "https://modbus-monitor.github.io/modbus-device-maps/maps/hager/ecn-ecp-ect-ecm-ecr-eca.json"}}</script>
