---
title: SEL SEL-751A Modbus Register Map
description: SEL SEL-751A Modbus map and register map with sample Modbus registers, register addresses, and relay overview for engineers. Works with Modbus Monitor XPF (import directly) and includes downloadable CSV access in-app.
---

# SEL SEL-751A Modbus Register Map

The SEL SEL-751A is a relay used for commissioning, troubleshooting, and operational monitoring. This page provides a sample Modbus register map with addresses, data types, and signal categories to help engineers commission, troubleshoot, and monitor the device. For SEL SEL-751A deployments, teams often use this map to surface demand, power factor, and energy data in utility metering, substations, and power quality analysis.

This page shows a preview subset of the full device map available in Modbus Monitor XPF.

Engineers searching for SEL SEL-751A Modbus map, SEL SEL-751A register map, or SEL SEL-751A Modbus registers can use this page as a compatibility snapshot before importing the full map into Modbus Monitor XPF.

## Overview

- **Device:** SEL SEL-751A
- **Type:** Relay
- **Protocol:** Modbus RTU / Modbus TCP
- **Use case:** commissioning, troubleshooting, and operational monitoring
- **Works with:** Modbus Monitor XPF (import directly)

## Download Modbus Map

The full SEL SEL-751A Modbus register map is available inside Modbus Monitor XPF as a pre-built device map. Download the free feature-locked version to access and export the complete map.

- [Download Modbus Monitor XPF Free](/download)

## Register Table (Sample)

Sample registers from the SEL SEL-751A Modbus map. Import the full map in Modbus Monitor XPF to access all registers.

| Signal | Address | Type | Units | Category |
|---|---:|---|---|---|
| PercentVoltageUnbalance | 300685 | FLOAT32 | V | Voltage |
| PercentCurrentUnbalance | 300664 | FLOAT32 | - | Current |
| ReverseEnergy | 300691 | FLOAT32 | kWh | Energy |
| PFapparentTotal | 300689 | FLOAT32 | - | Power Factor |
| DemandIa | 301690 | FLOAT32 | kW | Demand |
| BFActive | 300267 | UINT16 | - | General |
| ForwardEnergy | 300705 | FLOAT32 | kWh | Energy |
| PFapparentA | 301485 | FLOAT32 | - | Power Factor |
| PFapparentB | 301489 | FLOAT32 | - | Power Factor |
| PFapparentC | 301493 | FLOAT32 | - | Power Factor |
| DemandIb | 301691 | FLOAT32 | kW | Demand |
| DemandIc | 301692 | FLOAT32 | kW | Demand |

## How to Use This Map

1. **Download Modbus Monitor XPF** — [Get the free version](/download).
2. **Select the SEL SEL-751A device map** — pre-built maps are bundled and ready to load.
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
- Energy
- Current
- Voltage

## Related Tools

- [Modbus Monitor XPF — Windows Modbus Tool](https://www.modbusmonitor.com/download)
- [Modbus HMI Builder](https://www.modbusmonitor.com/modbus-hmi)
- [Compare Modbus Monitor XPF with Other Tools](https://www.modbusmonitor.com/compare)

## Related Device Maps

- [SEL SEL-735 Modbus Register Map](./sel-735.md)
- [SEL SEL-351A Modbus Register Map](./sel-351a.md)
- [SEL SEL-710 Modbus Register Map](./sel-710.md)
- [All SEL Modbus Register Maps](../index.md)
- [All XPF Device Maps](../../index.md)
