---
title: Socomec Multis L20, Multis L40 Modbus Register Map
description: Socomec Multis L20, Multis L40 Modbus map and register map with sample Modbus registers, register addresses, and power meter overview for engineers. Works with Modbus Monitor XPF (import directly) and includes downloadable CSV access in-app. Common searches: Socomec Multis L20, Multis L40 Modbus register list, Socomec Multis L20, Multis L40 Modbus table.
---

# Socomec Multis L20, Multis L40 Modbus Register Map

The Socomec Multis L20, Multis L40 is a power meter used for power monitoring, energy metering, and facility automation. This page provides a sample Modbus register map with addresses, data types, and signal categories to help engineers commission, troubleshoot, and monitor the device. For Socomec Multis L20, Multis L40 deployments, teams often use this map to surface power, voltage, and current data in facility metering, commissioning, and operational analytics.

This page shows a preview subset of the full device map available in Modbus Monitor XPF.

Engineers searching for Socomec Multis L20, Multis L40 Modbus map, Socomec Multis L20, Multis L40 register map, or Socomec Multis L20, Multis L40 Modbus registers can use this page as a compatibility snapshot before importing the full map into Modbus Monitor XPF. Also aligns to search intent around Socomec Multis L20, Multis L40 Modbus register list, Socomec Multis L20, Multis L40 Modbus table.

## Overview

- **Device:** Socomec Multis L20, Multis L40
- **Type:** Power Meter
- **Protocol:** Modbus RTU / Modbus TCP
- **Use case:** power monitoring, energy metering, and facility automation
- **Works with:** Modbus Monitor XPF (import directly)

## Download Modbus Map

The full Socomec Multis L20, Multis L40 Modbus register map is available inside Modbus Monitor XPF as a pre-built device map. Download the free feature-locked version to access and export the complete map.

- [Download Modbus Monitor XPF Free](https://www.modbusmonitor.com/download)

## Register Table (Sample)

Sample registers from the Socomec Multis L20, Multis L40 Modbus map. Import the full map in Modbus Monitor XPF to access all registers.

| Signal | Address | Type | Units | Category |
|---|---:|---|---|---|
| Voltage L1 V | 400000 | UINT32 | V | Voltage |
| Current L1 A | 400006 | UINT32 | A | Current |
| Active power L1 W | 400020 | INT32 | kW | Power |
| Import active energy 1 Wh | 400086 | INT64 | kWh | Energy |
| Frequency Hz | 400058 | INT32 | Hz | Frequency |
| Average inductive CosF Var | 400054 | INT32 | - | General |
| Voltage L2 V | 400002 | UINT32 | V | Voltage |
| Voltage L3 V | 400004 | UINT32 | V | Voltage |
| Current L2 A | 400008 | UINT32 | A | Current |
| Current L3 A | 400010 | UINT32 | A | Current |
| Current L-N A | 400012 | UINT32 | A | Current |
| Voltage L1-L2 V | 400014 | UINT32 | V | Voltage |

## How to Use This Map

1. **Download Modbus Monitor XPF** — [Get the free version](https://www.modbusmonitor.com/download).
2. **Select the Socomec Multis L20, Multis L40 device map** — pre-built maps are bundled and ready to load.
3. **Connect to your device** — enter the device IP or COM port and start polling registers immediately.
4. **Visualise and log** — build dashboards, trend data, and export readings without manual register entry.

## Why Use Pre-Built Maps

- **Saves time** — no need to manually look up or enter register addresses
- **Reduces errors** — pre-validated maps eliminate mis-typed addresses and wrong data types
- **Speeds commissioning** — connect and poll within minutes instead of hours
- **Reusable across projects** — use the same map across multiple sites and installations

## Data Categories Available

- Power
- Voltage
- Current
- Energy
- Frequency

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
