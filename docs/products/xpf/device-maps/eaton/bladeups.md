---
title: Eaton BladeUPS Modbus Register Map
description: Eaton BladeUPS Modbus map and register map with sample Modbus registers, register addresses, and ups overview for engineers. Includes sample addresses and data types for review before use with Modbus Monitor XPF.
---

# Eaton BladeUPS Modbus Register Map

The Eaton BladeUPS is a ups used for power continuity monitoring, alarm review, and resilience planning. This page provides a sample Modbus register map with addresses, data types, and signal categories to help engineers commission, troubleshoot, and monitor the device. For Eaton BladeUPS deployments, teams often use this map to surface voltage, status, and power data in UPS infrastructure, backup power systems, and resilience programs.

This page shows a public register preview. Check the catalog in your installed XPF version for complete-map availability and licensing.

Confirm the exact model and firmware, address base, register function, word order, scaling and units against the manufacturer manual before polling. This preview does not establish hardware validation.

## Overview

- **Device:** Eaton BladeUPS
- **Type:** UPS
- **Protocol:** Confirm the supported transport for the exact device and firmware in the manufacturer manual.
- **Use case:** power continuity monitoring, alarm review, and resilience planning
- **Works with:** Modbus Monitor XPF (import directly)

## Download Modbus Map

The sample below is a public preview. Check the catalog in your installed XPF version for current availability, access and licensing.

- [Get Modbus Monitor XPF](https://www.modbusmonitor.com/download)

[Public JSON preview](https://modbus-monitor.github.io/modbus-device-maps/maps/eaton/bladeups.json) · [Preview data terms](https://modbus-monitor.github.io/modbus-device-maps/data-license/)

## Register Table (Sample)

Sample registers from the Eaton BladeUPS Modbus map. Confirm the sample against the exact device and firmware before use.

| Signal | Address | Type | Units | Category |
|---|---:|---|---|---|
| Nominal Input Voltage iDeviceVoltsInRatingValue | 301358 | UINT32 | V | Voltage |
| Output Current Rating iDeviceAmpsRatingValue | 301811 | UINT16 | A | Current |
| Power Strategy sPowerStrategyValue | 303004 | UINT16 | kW | Power |
| Output KW Hours mOutputKWHourValue | 307003 | FLOAT32 | kWh | Energy |
| Nominal Input Frequency iNominalInputFrequencyValue | 301670 | UINT16 | Hz | Frequency |
| Min Battery Capacity for Return iMinBattCapforReturnValue | 318490 | UINT16 | - | Power Factor |
| Low Runtime Alarm Setpoint iLowRuntimeSetpointValue | 301676 | UINT16 | - | Status |
| Ambient Temperature mTempAmbientValue | 312001 | FLOAT32 | degC | Temperature |
| Vendor Name VendorNameValue:32 | 301033 | STRING | - | Identification |
| Device Type iDeviceTypeValue:32 | 301129 | STRING | - | General |
| Nominal Output Voltage iDeviceVoltsOutRatingValue | 301360 | UINT32 | V | Voltage |
| Nominal Output Frequency iNominalOutputFrequencyValue | 301671 | UINT16 | Hz | Frequency |

## How to Use This Map

1. **Download Modbus Monitor XPF** — [Get the free version](https://www.modbusmonitor.com/download).
2. **Select the Eaton BladeUPS device map** — check availability and access in the installed application catalog.
3. **Connect to your device** — confirm transport, addressing and data types before starting a read operation.
4. **Visualise and log** — build dashboards, trend data, and export readings without manual register entry.

## Why Use Pre-Built Maps

- **Saves time** — no need to manually look up or enter register addresses
- **Reduces errors** — reusable maps reduce repeated manual entry; validate addresses and data types for your device
- **Speeds commissioning** — connect and poll within minutes instead of hours
- **Reusable across projects** — use the same map across multiple sites and installations

## Data Categories Available

- Voltage
- Status
- Power
- Frequency
- Current
- Temperature

## Related Tools

- [Modbus Monitor XPF — Windows Modbus Tool](https://www.modbusmonitor.com/download)
- [Modbus HMI Builder](https://www.modbusmonitor.com/modbus-hmi)
- [Compare Modbus Monitor XPF with Other Tools](https://www.modbusmonitor.com/compare)

## Related Device Maps

- [Eaton 93PM Modbus Register Map](./93pm.md)
- [Eaton PXM2000 Modbus Register Map](./pxm2000.md)
- [Eaton EM19 M Modbus Register Map](./em19-m.md)
- [Eaton EM20 Modbus Register Map](./em20.md)
- [All Eaton Modbus Register Maps](./index.md)
- [All XPF Device Maps](../../../../modbus-device-maps/index.md)

<!-- public-preview-metadata -->
<script type="application/ld+json">{"@context": "https://schema.org", "@type": "Dataset", "name": "Eaton BladeUPS public register preview", "description": "Sample register addresses and data types; not a complete map or hardware verification.", "url": "https://docs.quantumbitsolutions.com/products/xpf/device-maps/eaton/bladeups/", "license": "https://modbus-monitor.github.io/modbus-device-maps/data-license/", "creator": {"@type": "Organization", "name": "Quantum Bit Solutions", "url": "https://quantumbitsolutions.com/"}, "distribution": {"@type": "DataDownload", "encodingFormat": "application/json", "contentUrl": "https://modbus-monitor.github.io/modbus-device-maps/maps/eaton/bladeups.json"}}</script>
<!-- /public-preview-metadata -->
