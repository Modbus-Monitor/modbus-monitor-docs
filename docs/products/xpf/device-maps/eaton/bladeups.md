---
title: Eaton BladeUPS Modbus Register Map
description: Eaton BladeUPS Modbus map and register map with sample Modbus registers, register addresses, and ups overview for engineers. Works with Modbus Monitor XPF (import directly) and includes downloadable CSV access in-app.
---

# Eaton BladeUPS Modbus Register Map

The Eaton BladeUPS is a ups used for power continuity monitoring, alarm review, and resilience planning. This page provides a sample Modbus register map with addresses, data types, and signal categories to help engineers commission, troubleshoot, and monitor the device. For Eaton BladeUPS deployments, teams often use this map to surface voltage, status, and power data in UPS infrastructure, backup power systems, and resilience programs.

This page shows a preview subset of the full device map available in Modbus Monitor XPF.

Engineers searching for Eaton BladeUPS Modbus map, Eaton BladeUPS register map, or Eaton BladeUPS Modbus registers can use this page as a compatibility snapshot before importing the full map into Modbus Monitor XPF.

## Overview

- **Device:** Eaton BladeUPS
- **Type:** UPS
- **Protocol:** Modbus RTU / Modbus TCP
- **Use case:** power continuity monitoring, alarm review, and resilience planning
- **Works with:** Modbus Monitor XPF (import directly)

## Download Modbus Map

The full Eaton BladeUPS Modbus register map is available inside Modbus Monitor XPF as a pre-built device map. Download the free feature-locked version to access and export the complete map.

- [Download Modbus Monitor XPF Free](https://www.modbusmonitor.com/download)

## Register Table (Sample)

Sample registers from the Eaton BladeUPS Modbus map. Import the full map in Modbus Monitor XPF to access all registers.

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
2. **Select the Eaton BladeUPS device map** — pre-built maps are bundled and ready to load.
3. **Connect to your device** — enter the device IP or COM port and start polling registers immediately.
4. **Visualise and log** — build dashboards, trend data, and export readings without manual register entry.

## Why Use Pre-Built Maps

- **Saves time** — no need to manually look up or enter register addresses
- **Reduces errors** — pre-validated maps eliminate mis-typed addresses and wrong data types
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
- [All Eaton Modbus Register Maps](../index.md)
- [All XPF Device Maps](../../index.md)
