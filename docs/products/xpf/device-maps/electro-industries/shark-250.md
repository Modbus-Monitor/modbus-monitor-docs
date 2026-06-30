---
title: Electro Industries Shark 250 Modbus Register Map
description: Electro Industries Shark 250 Modbus map and register map with sample Modbus registers, register addresses, and power meter overview for engineers. Works with Modbus Monitor XPF (import directly) and includes downloadable CSV access in-app.
---

# Electro Industries Shark 250 Modbus Register Map

The Electro Industries Shark 250 is a power meter used for power monitoring, energy metering, and facility automation. This page provides a sample Modbus register map with addresses, data types, and signal categories to help engineers commission, troubleshoot, and monitor the device. For Electro Industries Shark 250 deployments, teams often use this map to surface demand, power factor, and current data in facility metering, commissioning, and operational analytics.

This page shows a preview subset of the full device map available in Modbus Monitor XPF.

Engineers searching for Electro Industries Shark 250 Modbus map, Electro Industries Shark 250 register map, or Electro Industries Shark 250 Modbus registers can use this page as a compatibility snapshot before importing the full map into Modbus Monitor XPF.

## Overview

- **Device:** Electro Industries Shark 250
- **Type:** Power Meter
- **Protocol:** Modbus RTU / Modbus TCP
- **Use case:** power monitoring, energy metering, and facility automation
- **Works with:** Modbus Monitor XPF (import directly)

## Download Modbus Map

The full Electro Industries Shark 250 Modbus register map is available inside Modbus Monitor XPF as a pre-built device map. Download the free feature-locked version to access and export the complete map.

- [Download Modbus Monitor XPF Free](https://www.modbusmonitor.com/download)

## Register Table (Sample)

Sample registers from the Electro Industries Shark 250 Modbus map. Import the full map in Modbus Monitor XPF to access all registers.

| Signal | Address | Type | Units | Category |
|---|---:|---|---|---|
| Voltage Unbalance zero sequence component component | 401062 | UINT16 | V | Voltage |
| Current Unbalance | 401064 | UINT16 | - | Current |
| Pulse Output Test Power | 410074 | UINT16 | kW | Power |
| Save Energy to File | 413993 | UINT16 | kWh | Energy |
| Frequency | 401025 | FLOAT32 | Hz | Frequency |
| PF Total | 401023 | FLOAT32 | - | Power Factor |
| Demand Interval End Timestamp | 401996 | UINT16 | kW | Demand |
| Meter Status | 404500 | UINT16 | - | Status |
| Unit Lifetime Data MaxTemperature | 404536 | FLOAT32 | degC | Temperature |
| V A N THD Minimum | 408077 | UINT16 | - | Harmonics |
| Meter Name:8 | 400000 | STRING | - | Identification |
| Meter Type | 400016 | UINT16 | - | General |

## How to Use This Map

1. **Download Modbus Monitor XPF** — [Get the free version](https://www.modbusmonitor.com/download).
2. **Select the Electro Industries Shark 250 device map** — pre-built maps are bundled and ready to load.
3. **Connect to your device** — enter the device IP or COM port and start polling registers immediately.
4. **Visualise and log** — build dashboards, trend data, and export readings without manual register entry.

## Why Use Pre-Built Maps

- **Saves time** — no need to manually look up or enter register addresses
- **Reduces errors** — pre-validated maps eliminate mis-typed addresses and wrong data types
- **Speeds commissioning** — connect and poll within minutes instead of hours
- **Reusable across projects** — use the same map across multiple sites and installations

## Data Categories Available

- Demand
- Power Factor
- Current
- Harmonics
- Status
- Voltage

## Related Tools

- [Modbus Monitor XPF — Windows Modbus Tool](https://www.modbusmonitor.com/download)
- [Modbus HMI Builder](https://www.modbusmonitor.com/modbus-hmi)
- [Compare Modbus Monitor XPF with Other Tools](https://www.modbusmonitor.com/compare)

## Related Device Maps

- [Electro Industries Shark 200 / 200T Modbus Register Map](./shark-200-200t.md)
- [Electro Industries Shark 200 Modbus Register Map](./shark-200.md)
- [Electro Industries Shark 50 Modbus Register Map](./shark-50.md)
- [All Electro Industries Modbus Register Maps](../index.md)
- [All XPF Device Maps](../../../../modbus-device-maps/index.md)
