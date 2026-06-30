---
title: Janitza ECS Modbus Register Map
description: Janitza ECS Modbus map and register map with sample Modbus registers, register addresses, and power meter overview for engineers. Works with Modbus Monitor XPF (import directly) and includes downloadable CSV access in-app. Common searches: Janitza ECS Modbus register, Janitza ECS Modbus address list.
---

# Janitza ECS Modbus Register Map

The Janitza ECS is a power meter used for power monitoring, energy metering, and facility automation. This page provides a sample Modbus register map with addresses, data types, and signal categories to help engineers commission, troubleshoot, and monitor the device. For Janitza ECS deployments, teams often use this map to surface harmonics, energy, and power data in facility metering, commissioning, and operational analytics.

This page shows a preview subset of the full device map available in Modbus Monitor XPF.

Engineers searching for Janitza ECS Modbus map, Janitza ECS register map, or Janitza ECS Modbus registers can use this page as a compatibility snapshot before importing the full map into Modbus Monitor XPF. Also aligns to search intent around Janitza ECS Modbus register, Janitza ECS Modbus address list.

## Overview

- **Device:** Janitza ECS
- **Type:** Power Meter
- **Protocol:** Modbus RTU / Modbus TCP
- **Use case:** power monitoring, energy metering, and facility automation
- **Works with:** Modbus Monitor XPF (import directly)

## Download Modbus Map

The full Janitza ECS Modbus register map is available inside Modbus Monitor XPF as a pre-built device map. Download the free feature-locked version to access and export the complete map.

- [Download Modbus Monitor XPF Free](https://www.modbusmonitor.com/download)

## Register Table (Sample)

Sample registers from the Janitza ECS Modbus map. Import the full map in Modbus Monitor XPF to access all registers.

| Signal | Address | Type | Units | Category |
|---|---:|---|---|---|
| Voltage L1 N V | 419000 | FLOAT32 | V | Voltage |
| Apparent current L1 A | 419012 | FLOAT32 | A | Current |
| Real power L1 W | 419020 | FLOAT32 | kW | Power |
| Real energy l1l3 Wh | 419060 | FLOAT32 | kWh | Energy |
| Measured frequency Hz | 419050 | FLOAT32 | Hz | Frequency |
| Harmonic thd u L1 N | 419110 | FLOAT32 | - | Harmonics |
| Vector sum ini1i2i3 A | 419018 | FLOAT32 | - | General |
| Serial number | 400911 | INT32 | - | Identification |
| Voltage L2 N V | 419002 | FLOAT32 | V | Voltage |
| Voltage L3 N V | 419004 | FLOAT32 | V | Voltage |
| Voltage L1 L2 V | 419006 | FLOAT32 | V | Voltage |
| Voltage L2 L3 V | 419008 | FLOAT32 | V | Voltage |

## How to Use This Map

1. **Download Modbus Monitor XPF** — [Get the free version](https://www.modbusmonitor.com/download).
2. **Select the Janitza ECS device map** — pre-built maps are bundled and ready to load.
3. **Connect to your device** — enter the device IP or COM port and start polling registers immediately.
4. **Visualise and log** — build dashboards, trend data, and export readings without manual register entry.

## Why Use Pre-Built Maps

- **Saves time** — no need to manually look up or enter register addresses
- **Reduces errors** — pre-validated maps eliminate mis-typed addresses and wrong data types
- **Speeds commissioning** — connect and poll within minutes instead of hours
- **Reusable across projects** — use the same map across multiple sites and installations

## Data Categories Available

- Harmonics
- Energy
- Power
- Voltage
- Current
- Frequency

## Related Tools

- [Modbus Monitor XPF — Windows Modbus Tool](https://www.modbusmonitor.com/download)
- [Modbus HMI Builder](https://www.modbusmonitor.com/modbus-hmi)
- [Compare Modbus Monitor XPF with Other Tools](https://www.modbusmonitor.com/compare)

## Related Device Maps

- [Janitza UMG104 Modbus Register Map](./umg104.md)
- [Janitza UMG605 Modbus Register Map](./umg605.md)
- [Janitza UMG604 Modbus Register Map](./umg604.md)
- [Janitza UMG96 Modbus Register Map](./umg96.md)
- [All Janitza Modbus Register Maps](../index.md)
- [All XPF Device Maps](../../../../modbus-device-maps/index.md)
