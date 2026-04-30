---
title: Schneider Electric Symmetra PX Modbus Register Map
description: Schneider Electric Symmetra PX Modbus map and register map with sample Modbus registers, register addresses, and ups overview for engineers. Works with Modbus Monitor XPF (import directly) and includes downloadable CSV access in-app.
---

# Schneider Electric Symmetra PX Modbus Register Map

The Schneider Electric Symmetra PX is a ups used for power continuity monitoring, alarm review, and resilience planning. This page provides a sample Modbus register map with addresses, data types, and signal categories to help engineers commission, troubleshoot, and monitor the device. For Schneider Electric Symmetra PX deployments, teams often use this map to surface power, current, and status data in data centers, switchgear lineups, and advanced power monitoring projects.

This page shows a preview subset of the full device map available in Modbus Monitor XPF.

Engineers searching for Schneider Electric Symmetra PX Modbus map, Schneider Electric Symmetra PX register map, or Schneider Electric Symmetra PX Modbus registers can use this page as a compatibility snapshot before importing the full map into Modbus Monitor XPF.

## Overview

- **Device:** Schneider Electric Symmetra PX
- **Type:** UPS
- **Protocol:** Modbus RTU / Modbus TCP
- **Use case:** power continuity monitoring, alarm review, and resilience planning
- **Works with:** Modbus Monitor XPF (import directly)

## Download Modbus Map

The full Schneider Electric Symmetra PX Modbus register map is available inside Modbus Monitor XPF as a pre-built device map. Download the free feature-locked version to access and export the complete map.

- [Download Modbus Monitor XPF Free](https://www.modbusmonitor.com/download)

## Register Table (Sample)

Sample registers from the Schneider Electric Symmetra PX Modbus map. Import the full map in Modbus Monitor XPF to access all registers.

| Signal | Address | Type | Units | Category |
|---|---:|---|---|---|
| Battery Voltage | 404359 | UINT16 | V | Voltage |
| Battery Current | 404361 | UINT16 | - | Current |
| Battery Power | 404369 | UINT16 | kW | Power |
| Energy Meter kwH | 405167 | UINT16 | kWh | Energy |
| Frequency | 404608 | UINT16 | Hz | Frequency |
| UPS Status | 400000 | BIT | - | Status |
| BatterySystem Temperature | 404367 | INT16 | degC | Temperature |
| UPS Serial Number:6 | 404145 | STRING | - | Identification |
| Time on battery | 404352 | UINT32 | - | General |
| Alarm Register | 400002 | INT16 | - | Status |
| Alarm Register | 400003 | INT16 | - | Status |
| Alarm Register | 400004 | INT16 | - | Status |

## How to Use This Map

1. **Download Modbus Monitor XPF** — [Get the free version](https://www.modbusmonitor.com/download).
2. **Select the Schneider Electric Symmetra PX device map** — pre-built maps are bundled and ready to load.
3. **Connect to your device** — enter the device IP or COM port and start polling registers immediately.
4. **Visualise and log** — build dashboards, trend data, and export readings without manual register entry.

## Why Use Pre-Built Maps

- **Saves time** — no need to manually look up or enter register addresses
- **Reduces errors** — pre-validated maps eliminate mis-typed addresses and wrong data types
- **Speeds commissioning** — connect and poll within minutes instead of hours
- **Reusable across projects** — use the same map across multiple sites and installations

## Data Categories Available

- Power
- Current
- Status
- Voltage
- Frequency
- Temperature

## Related Tools

- [Modbus Monitor XPF — Windows Modbus Tool](https://www.modbusmonitor.com/download)
- [Modbus HMI Builder](https://www.modbusmonitor.com/modbus-hmi)
- [Compare Modbus Monitor XPF with Other Tools](https://www.modbusmonitor.com/compare)

## Related Device Maps

- [Schneider Electric PM8000 Modbus Register Map](./pm8000.md)
- [Schneider Electric ION9000 Modbus Register Map](./ion9000.md)
- [Schneider Electric PM5000 / PM5100 / PM5300 Modbus Register Map](./pm5000-pm5100-pm5300.md)
- [Schneider Electric PM5500 / PM5560 / PM5580 Modbus Register Map](./pm5500-pm5560-pm5580.md)
- [All Schneider Electric Modbus Register Maps](../index.md)
- [All XPF Device Maps](../../index.md)
