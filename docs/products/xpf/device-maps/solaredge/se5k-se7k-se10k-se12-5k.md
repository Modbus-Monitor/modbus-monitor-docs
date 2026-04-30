---
title: SolarEdge SE5K / SE7K / SE10K / SE12.5K Modbus Register Map
description: SolarEdge SE5K / SE7K / SE10K / SE12.5K Modbus map and register map with sample Modbus registers, register addresses, and solar inverter overview for engineers. Works with Modbus Monitor XPF (import directly) and includes downloadable CSV access in-app.
---

# SolarEdge SE5K / SE7K / SE10K / SE12.5K Modbus Register Map

The SolarEdge SE5K / SE7K / SE10K / SE12.5K is a solar inverter used for PV production monitoring, inverter diagnostics, and energy analytics. This page provides a sample Modbus register map with addresses, data types, and signal categories to help engineers commission, troubleshoot, and monitor the device. For SolarEdge SE5K / SE7K / SE10K / SE12.5K deployments, teams often use this map to surface voltage, current, and power data in solar inverter monitoring and renewable energy systems.

This page shows a preview subset of the full device map available in Modbus Monitor XPF.

Engineers searching for SolarEdge SE5K / SE7K / SE10K / SE12.5K Modbus map, SolarEdge SE5K / SE7K / SE10K / SE12.5K register map, or SolarEdge SE5K / SE7K / SE10K / SE12.5K Modbus registers can use this page as a compatibility snapshot before importing the full map into Modbus Monitor XPF.

## Overview

- **Device:** SolarEdge SE5K / SE7K / SE10K / SE12.5K
- **Type:** Solar Inverter
- **Protocol:** Modbus RTU / Modbus TCP
- **Use case:** PV production monitoring, inverter diagnostics, and energy analytics
- **Works with:** Modbus Monitor XPF (import directly)

## Download Modbus Map

The full SolarEdge SE5K / SE7K / SE10K / SE12.5K Modbus register map is available inside Modbus Monitor XPF as a pre-built device map. Download the free feature-locked version to access and export the complete map.

- [Download Modbus Monitor XPF Free](/download)

## Register Table (Sample)

Sample registers from the SolarEdge SE5K / SE7K / SE10K / SE12.5K Modbus map. Import the full map in Modbus Monitor XPF to access all registers.

| Signal | Address | Type | Units | Category |
|---|---:|---|---|---|
| I AC VoltageAB | 440077 | UINT16 | V | Voltage |
| I AC Current | 440072 | UINT16 | - | Current |
| I AC Power | 440084 | INT16 | kW | Power |
| I AC Energy WH | 440094 | UINT32 | kWh | Energy |
| I AC Frequency | 440086 | UINT16 | Hz | Frequency |
| I AC PF1 | 440092 | INT16 | - | Power Factor |
| I Status | 440108 | UINT16 | - | Status |
| I Temp Sink | 440104 | INT16 | - | Temperature |
| C SunSpec ID | 440001 | UINT32 | - | General |
| C Model:16 | 440021 | STRING | - | Identification |
| M Exported | 440227 | UINT32 | - | Communication |
| I AC CurrentA | 440073 | UINT16 | - | Current |

## How to Use This Map

1. **Download Modbus Monitor XPF** — [Get the free version](/download).
2. **Select the SolarEdge SE5K / SE7K / SE10K / SE12.5K device map** — pre-built maps are bundled and ready to load.
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
- Power Factor
- Energy
- Status

## Related Tools

- [Modbus Monitor XPF — Windows Modbus Tool](https://www.modbusmonitor.com/download)
- [Modbus HMI Builder](https://www.modbusmonitor.com/modbus-hmi)
- [Compare Modbus Monitor XPF with Other Tools](https://www.modbusmonitor.com/compare)

## Related Device Maps

- [SolarEdge SE5000 Modbus Register Map](./se5000.md)
- [SolarEdge SE3000H Modbus Register Map](./se3000h.md)
- [SolarEdge SE6000 Modbus Register Map](./se6000.md)
- [SolarEdge SE10K Modbus Register Map](./se10k.md)
- [All SolarEdge Modbus Register Maps](../index.md)
- [All XPF Device Maps](../../index.md)
