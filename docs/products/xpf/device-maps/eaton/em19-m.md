---
title: Eaton EM19 M Modbus Register Map
description: Eaton EM19 M Modbus map and register map with sample Modbus registers, register addresses, and power meter overview for engineers. Works with Modbus Monitor XPF (import directly) and includes downloadable CSV access in-app.
---

# Eaton EM19 M Modbus Register Map

The Eaton EM19 M is a power meter used for power monitoring, energy metering, and facility automation. This page provides a sample Modbus register map with addresses, data types, and signal categories to help engineers commission, troubleshoot, and monitor the device. For Eaton EM19 M deployments, teams often use this map to surface demand, harmonics, and power factor data in critical power distribution and electrical monitoring systems.

This page shows a preview subset of the full device map available in Modbus Monitor XPF.

Engineers searching for Eaton EM19 M Modbus map, Eaton EM19 M register map, or Eaton EM19 M Modbus registers can use this page as a compatibility snapshot before importing the full map into Modbus Monitor XPF.

## Overview

- **Device:** Eaton EM19 M
- **Type:** Power Meter
- **Protocol:** Modbus RTU / Modbus TCP
- **Use case:** power monitoring, energy metering, and facility automation
- **Works with:** Modbus Monitor XPF (import directly)

## Download Modbus Map

The full Eaton EM19 M Modbus register map is available inside Modbus Monitor XPF as a pre-built device map. Download the free feature-locked version to access and export the complete map.

- [Download Modbus Monitor XPF Free](https://www.modbusmonitor.com/download)

## Register Table (Sample)

Sample registers from the Eaton EM19 M Modbus map. Import the full map in Modbus Monitor XPF to access all registers.

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
2. **Select the Eaton EM19 M device map** — pre-built maps are bundled and ready to load.
3. **Connect to your device** — enter the device IP or COM port and start polling registers immediately.
4. **Visualise and log** — build dashboards, trend data, and export readings without manual register entry.

## Why Use Pre-Built Maps

- **Saves time** — no need to manually look up or enter register addresses
- **Reduces errors** — pre-validated maps eliminate mis-typed addresses and wrong data types
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
- [All Eaton Modbus Register Maps](../index.md)
- [All XPF Device Maps](../../index.md)
