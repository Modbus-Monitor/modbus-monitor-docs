---
title: Eaton EM22-DIN Modbus Register Map
description: Eaton EM22-DIN Modbus map and register map with sample Modbus registers, register addresses, and power meter overview for engineers. Includes sample addresses and data types for review before use with Modbus Monitor XPF.
---

# Eaton EM22-DIN Modbus Register Map

The Eaton EM22-DIN is a power meter used for power monitoring, energy metering, and facility automation. This page provides a sample Modbus register map with addresses, data types, and signal categories to help engineers commission, troubleshoot, and monitor the device. For Eaton EM22-DIN deployments, teams often use this map to surface demand and energy data in critical power distribution and electrical monitoring systems.

This page shows a public register preview. Check the catalog in your installed XPF version for complete-map availability and licensing.

Confirm the exact model and firmware, address base, register function, word order, scaling and units against the manufacturer manual before polling. This preview does not establish hardware validation.

## Overview

- **Device:** Eaton EM22-DIN
- **Type:** Power Meter
- **Protocol:** Confirm the supported transport for the exact device and firmware in the manufacturer manual.
- **Use case:** power monitoring, energy metering, and facility automation
- **Works with:** Modbus Monitor XPF (import directly)

## Download Modbus Map

The sample below is a public preview. Check the catalog in your installed XPF version for current availability, access and licensing.

- [Get Modbus Monitor XPF](https://www.modbusmonitor.com/download)

[Public JSON preview](https://modbus-monitor.github.io/modbus-device-maps/maps/eaton/em22-din.json) · [Preview data terms](https://modbus-monitor.github.io/modbus-device-maps/data-license/)

## Register Table (Sample)

Sample registers from the Eaton EM22-DIN Modbus map. Confirm the sample against the exact device and firmware before use.

| Signal | Address | Type | Units | Category |
|---|---:|---|---|---|
| TotalEnergy | 400035 | FLOAT32 | kWh | Energy |
| DemandTotalWatts | 400027 | FLOAT32 | kW | Demand |
| ACVAN | 400001 | FLOAT32 | - | General |
| PeakDemandWatts | 400029 | FLOAT32 | kW | Demand |
| DemandVAs | 400031 | FLOAT32 | kW | Demand |
| PeakDemandVAs | 400033 | FLOAT32 | kW | Demand |
| TotalEnergyA | 400037 | FLOAT32 | kWh | Energy |
| TotalEnergyB | 400039 | FLOAT32 | kWh | Energy |
| DemandWindow | 404357 | UINT16 | kW | Demand |
| ACIout1A | 400003 | FLOAT32 | - | General |
| ACIout2A | 400005 | FLOAT32 | - | General |
| ACIA | 400007 | FLOAT32 | - | General |

## How to Use This Map

1. **Download Modbus Monitor XPF** — [Get the free version](https://www.modbusmonitor.com/download).
2. **Select the Eaton EM22-DIN device map** — check availability and access in the installed application catalog.
3. **Connect to your device** — confirm transport, addressing and data types before starting a read operation.
4. **Visualise and log** — build dashboards, trend data, and export readings without manual register entry.

## Why Use Pre-Built Maps

- **Saves time** — no need to manually look up or enter register addresses
- **Reduces errors** — reusable maps reduce repeated manual entry; validate addresses and data types for your device
- **Speeds commissioning** — connect and poll within minutes instead of hours
- **Reusable across projects** — use the same map across multiple sites and installations

## Data Categories Available

- Demand
- Energy

## Related Tools

- [Modbus Monitor XPF — Windows Modbus Tool](https://www.modbusmonitor.com/download)
- [Modbus HMI Builder](https://www.modbusmonitor.com/modbus-hmi)
- [Compare Modbus Monitor XPF with Other Tools](https://www.modbusmonitor.com/compare)

## Related Device Maps

- [Eaton 93PM Modbus Register Map](./93pm.md)
- [Eaton BladeUPS Modbus Register Map](./bladeups.md)
- [Eaton PXM2000 Modbus Register Map](./pxm2000.md)
- [Eaton EM19 M Modbus Register Map](./em19-m.md)
- [All Eaton Modbus Register Maps](./index.md)
- [All XPF Device Maps](../../../../modbus-device-maps/index.md)

<!-- public-preview-metadata -->
<script type="application/ld+json">{"@context": "https://schema.org", "@type": "Dataset", "name": "Eaton EM22-DIN public register preview", "description": "Sample register addresses and data types; not a complete map or hardware verification.", "url": "https://docs.quantumbitsolutions.com/products/xpf/device-maps/eaton/em22-din/", "license": "https://modbus-monitor.github.io/modbus-device-maps/data-license/", "creator": {"@type": "Organization", "name": "Quantum Bit Solutions", "url": "https://quantumbitsolutions.com/"}, "distribution": {"@type": "DataDownload", "encodingFormat": "application/json", "contentUrl": "https://modbus-monitor.github.io/modbus-device-maps/maps/eaton/em22-din.json"}}</script>
<!-- /public-preview-metadata -->
