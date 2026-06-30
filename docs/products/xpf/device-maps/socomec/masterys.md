---
title: Socomec Masterys Modbus Register Map
description: Socomec Masterys Modbus map and register map with sample Modbus registers, register addresses, and ups overview for engineers. Works with Modbus Monitor XPF (import directly) and includes downloadable CSV access in-app. Common searches: Socomec Masterys Modbus register list, Socomec Masterys Modbus table.
---

# Socomec Masterys Modbus Register Map

The Socomec Masterys is a ups used for power continuity monitoring, alarm review, and resilience planning. This page provides a sample Modbus register map with addresses, data types, and signal categories to help engineers commission, troubleshoot, and monitor the device. For Socomec Masterys deployments, teams often use this map to surface voltage, current, and power data in backup power systems and critical infrastructure monitoring.

This page shows a preview subset of the full device map available in Modbus Monitor XPF.

Engineers searching for Socomec Masterys Modbus map, Socomec Masterys register map, or Socomec Masterys Modbus registers can use this page as a compatibility snapshot before importing the full map into Modbus Monitor XPF. Also aligns to search intent around Socomec Masterys Modbus register list, Socomec Masterys Modbus table.

## Overview

- **Device:** Socomec Masterys
- **Type:** UPS
- **Protocol:** Modbus RTU / Modbus TCP
- **Use case:** power continuity monitoring, alarm review, and resilience planning
- **Works with:** Modbus Monitor XPF (import directly)

## Download Modbus Map

The full Socomec Masterys Modbus register map is available inside Modbus Monitor XPF as a pre-built device map. Download the free feature-locked version to access and export the complete map.

- [Download Modbus Monitor XPF Free](https://www.modbusmonitor.com/download)

## Register Table (Sample)

Sample registers from the Socomec Masterys Modbus map. Import the full map in Modbus Monitor XPF to access all registers.

| Signal | Address | Type | Units | Category |
|---|---:|---|---|---|
| Auxiliary mains star voltage v1 M06 V | 400102 | UINT16 | V | Voltage |
| Input current phase l1 M12 A | 400108 | UINT16 | A | Current |
| Output active power 4 M36 kW | 400132 | UINT16 | kW | Power |
| Auxiliary frequency M18 Hz | 400114 | UINT16 | Hz | Frequency |
| Internal UPS temperature M22 DC | 400118 | UINT16 | degC | Temperature |
| Load phase 1 M00 | 400096 | UINT16 | - | General |
| Auxiliary mains star voltage v2 M07 V | 400103 | UINT16 | V | Voltage |
| Auxiliary mains star voltage v3 M08 V | 400104 | UINT16 | V | Voltage |
| Output star voltage v1 M09 V | 400105 | UINT16 | V | Voltage |
| Output star voltage v2 M10 V | 400106 | UINT16 | V | Voltage |
| Output star voltage v3 M11 V | 400107 | UINT16 | V | Voltage |
| Input current phase l2 M13 A | 400109 | UINT16 | A | Current |

## How to Use This Map

1. **Download Modbus Monitor XPF** — [Get the free version](https://www.modbusmonitor.com/download).
2. **Select the Socomec Masterys device map** — pre-built maps are bundled and ready to load.
3. **Connect to your device** — enter the device IP or COM port and start polling registers immediately.
4. **Visualise and log** — build dashboards, trend data, and export readings without manual register entry.

## Why Use Pre-Built Maps

- **Saves time** — no need to manually look up or enter register addresses
- **Reduces errors** — pre-validated maps eliminate mis-typed addresses and wrong data types
- **Speeds commissioning** — connect and poll within minutes instead of hours
- **Reusable across projects** — use the same map across multiple sites and installations

## Data Categories Available

- Voltage
- Current
- Power
- Frequency
- Temperature

## Related Tools

- [Modbus Monitor XPF — Windows Modbus Tool](https://www.modbusmonitor.com/download)
- [Modbus HMI Builder](https://www.modbusmonitor.com/modbus-hmi)
- [Compare Modbus Monitor XPF with Other Tools](https://www.modbusmonitor.com/compare)

## Related Device Maps

- [Socomec DIRIS A40 / A41 RS485 Modbus Register Map](./diris-a40-a41-rs485.md)
- [Socomec DIRIS I31 Modbus Register Map](./diris-i31.md)
- [Socomec DIRIS U30 Modbus Register Map](./diris-u30.md)
- [Socomec Countis ECI3 Modbus Register Map](./countis-eci3.md)
- [All Socomec Modbus Register Maps](../index.md)
- [All XPF Device Maps](../../../../modbus-device-maps/index.md)
