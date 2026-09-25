---
title: Eaton EM19 M Modbus Register Map
description: Eaton EM19 M Modbus map and register map with sample Modbus registers, register addresses, and power meter overview for engineers. Includes sample addresses and data types for review before use with Modbus Monitor XPF.
---

# Eaton EM19 M Modbus Register Map

The Eaton EM19 M is a power meter used for power monitoring, energy metering, and facility automation. This page provides a sample Modbus register map with addresses, data types, and signal categories to help engineers commission, troubleshoot, and monitor the device. For Eaton EM19 M deployments, teams often use this map to surface demand, harmonics, and power factor data in critical power distribution and electrical monitoring systems.

This page shows a public register preview. Check the catalog in your installed XPF version for complete-map availability and licensing.

Confirm the exact model and firmware, address base, register function, word order, scaling and units against the manufacturer manual before polling. This preview does not establish hardware validation.

## Overview

- **Device:** Eaton EM19 M
- **Type:** Power Meter
- **Protocol:** Confirm the supported transport for the exact device and firmware in the manufacturer manual.
- **Use case:** power monitoring, energy metering, and facility automation
- **Works with:** Modbus Monitor XPF (import directly)

## Download Modbus Map

The sample below is a public preview. Check the catalog in your installed XPF version for current availability, access and licensing.

- [Get Modbus Monitor XPF](https://www.modbusmonitor.com/download)

[Public JSON preview](https://modbus-monitor.github.io/modbus-device-maps/maps/eaton/em19-m.json) · [Preview data terms](https://modbus-monitor.github.io/modbus-device-maps/data-license/)

## Register Table (Sample)

Sample registers from the Eaton EM19 M Modbus map. Confirm the sample against the exact device and firmware before use.

| Signal | Address | Type | Units | Category |
|---|---:|---|---|---|
| ForwardEnergy | 400515 | FLOAT32 | kWh | Energy |
| PFapparentA | 407699 | FLOAT32 | - | Power Factor |
| PwrDemandWindowPeriod | 403336 | FLOAT32 | kW | Demand |
| VanPerTHD | 404353 | FLOAT32 | - | Harmonics |
| VAh | 400517 | FLOAT32 | - | General |
| ReverseEnergy | 400525 | FLOAT32 | kWh | Energy |
| CurDemandWindowPeriod | 403594 | FLOAT32 | kW | Demand |
| ACIAPeakDemand | 403841 | FLOAT32 | kW | Demand |
| ACIBPeakDemand | 403842 | FLOAT32 | kW | Demand |
| ACICPeakDemand | 403843 | FLOAT32 | kW | Demand |
| DemandACVanPeak | 403844 | FLOAT32 | kW | Demand |
| DemandACVbnPeak | 403845 | FLOAT32 | kW | Demand |

## How to Use This Map

1. **Download Modbus Monitor XPF** — [Get the free version](https://www.modbusmonitor.com/download).
2. **Select the Eaton EM19 M device map** — check availability and access in the installed application catalog.
3. **Connect to your device** — confirm transport, addressing and data types before starting a read operation.
4. **Visualise and log** — build dashboards, trend data, and export readings without manual register entry.

## Why Use Pre-Built Maps

- **Saves time** — no need to manually look up or enter register addresses
- **Reduces errors** — reusable maps reduce repeated manual entry; validate addresses and data types for your device
- **Speeds commissioning** — connect and poll within minutes instead of hours
- **Reusable across projects** — use the same map across multiple sites and installations

## Data Categories Available

- Demand
- Harmonics
- Power Factor
- Energy

## Related Tools

- [Modbus Monitor XPF — Windows Modbus Tool](https://www.modbusmonitor.com/download)
- [Modbus HMI Builder](https://www.modbusmonitor.com/modbus-hmi)
- [Compare Modbus Monitor XPF with Other Tools](https://www.modbusmonitor.com/compare)

## Related Device Maps

- [Eaton 93PM Modbus Register Map](./93pm.md)
- [Eaton BladeUPS Modbus Register Map](./bladeups.md)
- [Eaton PXM2000 Modbus Register Map](./pxm2000.md)
- [Eaton EM20 Modbus Register Map](./em20.md)
- [All Eaton Modbus Register Maps](./index.md)
- [All XPF Device Maps](../../../../modbus-device-maps/index.md)

<!-- public-preview-metadata -->
<script type="application/ld+json">{"@context": "https://schema.org", "@type": "Dataset", "name": "Eaton EM19 M public register preview", "description": "Sample register addresses and data types; not a complete map or hardware verification.", "url": "https://docs.quantumbitsolutions.com/products/xpf/device-maps/eaton/em19-m/", "license": "https://modbus-monitor.github.io/modbus-device-maps/data-license/", "creator": {"@type": "Organization", "name": "Quantum Bit Solutions", "url": "https://quantumbitsolutions.com/"}, "distribution": {"@type": "DataDownload", "encodingFormat": "application/json", "contentUrl": "https://modbus-monitor.github.io/modbus-device-maps/maps/eaton/em19-m.json"}}</script>
<!-- /public-preview-metadata -->
