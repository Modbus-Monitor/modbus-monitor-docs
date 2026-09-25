---
title: Siemens SICAM P Modbus Register Map
description: Siemens SICAM P Modbus map and register map with sample Modbus registers, register addresses, and power meter overview for engineers. Includes sample addresses and data types for review before use with Modbus Monitor XPF.
---

# Siemens SICAM P Modbus Register Map

The Siemens SICAM P is a power meter used for power monitoring, energy metering, and facility automation. This page provides a sample Modbus register map with addresses, data types, and signal categories to help engineers commission, troubleshoot, and monitor the device. For Siemens SICAM P deployments, teams often use this map to surface harmonics, power factor, and status data in industrial automation panels and building management systems.

This page shows a public register preview. Check the catalog in your installed XPF version for complete-map availability and licensing.

Confirm the exact model and firmware, address base, register function, word order, scaling and units against the manufacturer manual before polling. This preview does not establish hardware validation.

## Overview

- **Device:** Siemens SICAM P
- **Type:** Power Meter
- **Protocol:** Confirm the supported transport for the exact device and firmware in the manufacturer manual.
- **Use case:** power monitoring, energy metering, and facility automation
- **Works with:** Modbus Monitor XPF (import directly)

## Download Modbus Map

The sample below is a public preview. Check the catalog in your installed XPF version for current availability, access and licensing.

- [Get Modbus Monitor XPF](https://www.modbusmonitor.com/download)

[Public JSON preview](https://modbus-monitor.github.io/modbus-device-maps/maps/siemens/sicam-p.json) · [Preview data terms](https://modbus-monitor.github.io/modbus-device-maps/data-license/)

## Register Table (Sample)

Sample registers from the Siemens SICAM P Modbus map. Confirm the sample against the exact device and firmware before use.

| Signal | Address | Type | Units | Category |
|---|---:|---|---|---|
| PF L1 | 400258 | FLOAT32 | - | Power Factor |
| Status of Binary Outputs and Device | 400128 | BIT | - | Status |
| THDU L1 | 400280 | FLOAT32 | - | Harmonics |
| MLFB:16 | 400000 | STRING | - | General |
| Serial number:10 | 400019 | STRING | - | Identification |
| Status of Binary Inputs | 400129 | BIT | - | Status |
| Status of Overflow at Measuring | 400199 | BIT | - | Status |
| PF L2 | 400260 | FLOAT32 | - | Power Factor |
| PF L3 | 400262 | FLOAT32 | - | Power Factor |
| PF | 400264 | FLOAT32 | - | Power Factor |
| THDU L2 | 400282 | FLOAT32 | - | Harmonics |
| THDU L3 | 400284 | FLOAT32 | - | Harmonics |

## How to Use This Map

1. **Download Modbus Monitor XPF** — [Get the free version](https://www.modbusmonitor.com/download).
2. **Select the Siemens SICAM P device map** — check availability and access in the installed application catalog.
3. **Connect to your device** — confirm transport, addressing and data types before starting a read operation.
4. **Visualise and log** — build dashboards, trend data, and export readings without manual register entry.

## Why Use Pre-Built Maps

- **Saves time** — no need to manually look up or enter register addresses
- **Reduces errors** — reusable maps reduce repeated manual entry; validate addresses and data types for your device
- **Speeds commissioning** — connect and poll within minutes instead of hours
- **Reusable across projects** — use the same map across multiple sites and installations

## Data Categories Available

- Harmonics
- Power Factor
- Status

## Related Tools

- [Modbus Monitor XPF — Windows Modbus Tool](https://www.modbusmonitor.com/download)
- [Modbus HMI Builder](https://www.modbusmonitor.com/modbus-hmi)
- [Compare Modbus Monitor XPF with Other Tools](https://www.modbusmonitor.com/compare)

## Related Device Maps

- [Siemens PAC3200 Modbus Register Map](./sentron-pac-3200.md)
- [Siemens PAC4200 Modbus Register Map](./sentron-pac-4200.md)
- [Siemens PAC2200 Modbus Register Map](./sentron-pac-2200.md)
- [Siemens SEM3 Series Modbus Register Map](./sem3-series.md)
- [All Siemens Modbus Register Maps](./index.md)
- [All XPF Device Maps](../../../../modbus-device-maps/index.md)

<!-- public-preview-metadata -->
<script type="application/ld+json">{"@context": "https://schema.org", "@type": "Dataset", "name": "Siemens SICAM P public register preview", "description": "Sample register addresses and data types; not a complete map or hardware verification.", "url": "https://docs.quantumbitsolutions.com/products/xpf/device-maps/siemens/sicam-p/", "license": "https://modbus-monitor.github.io/modbus-device-maps/data-license/", "creator": {"@type": "Organization", "name": "Quantum Bit Solutions", "url": "https://quantumbitsolutions.com/"}, "distribution": {"@type": "DataDownload", "encodingFormat": "application/json", "contentUrl": "https://modbus-monitor.github.io/modbus-device-maps/maps/siemens/sicam-p.json"}}</script>
<!-- /public-preview-metadata -->
