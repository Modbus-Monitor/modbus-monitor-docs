---
title: Socomec DIRIS U20 Modbus Register Map
description: Socomec DIRIS U20 Modbus map and register map with sample Modbus registers, register addresses, and power meter overview for engineers. Works with Modbus Monitor XPF (import directly) and includes downloadable CSV access in-app. Common searches: Socomec DIRIS U20 Modbus register list, Socomec DIRIS U20 Modbus table.
---

# Socomec DIRIS U20 Modbus Register Map

The Socomec DIRIS U20 is a power meter used for power monitoring, energy metering, and facility automation. This page provides a sample Modbus register map with addresses, data types, and signal categories to help engineers commission, troubleshoot, and monitor the device. For Socomec DIRIS U20 deployments, teams often use this map to surface power, current, and voltage data in facility metering, commissioning, and operational analytics.

This page shows a preview subset of the full device map available in Modbus Monitor XPF.

Engineers searching for Socomec DIRIS U20 Modbus map, Socomec DIRIS U20 register map, or Socomec DIRIS U20 Modbus registers can use this page as a compatibility snapshot before importing the full map into Modbus Monitor XPF. Also aligns to search intent around Socomec DIRIS U20 Modbus register list, Socomec DIRIS U20 Modbus table.

## Overview

- **Device:** Socomec DIRIS U20
- **Type:** Power Meter
- **Protocol:** Modbus RTU / Modbus TCP
- **Use case:** power monitoring, energy metering, and facility automation
- **Works with:** Modbus Monitor XPF (import directly)

## Download Modbus Map

The full Socomec DIRIS U20 Modbus register map is available inside Modbus Monitor XPF as a pre-built device map. Download the free feature-locked version to access and export the complete map.

- [Download Modbus Monitor XPF Free](https://www.modbusmonitor.com/download)

## Register Table (Sample)

Sample registers from the Socomec DIRIS U20 Modbus map. Import the full map in Modbus Monitor XPF to access all registers.

| Signal | Address | Type | Units | Category |
|---|---:|---|---|---|
| Hour meter allocation1 Auxiliary power supply 2 Currents3 phase to phase voltage 4 Input 1 5 Input2 6 Input3 | 436361 | UINT16 | V | Voltage |
| Current Transformer secondary | 457345 | UINT16 | - | Current |
| Reactive Power Calculation | 436369 | UINT16 | kW | Power |
| OUT pulse output value 0 0 1 kWh kvarh1 1 kWh kvarh2 10 kWh kvarh3 100 kWh kvarh4 1000 kWh kvarh5 10000 kWh kvarh | 436359 | UINT16 | kWh | Energy |
| Frequency F Hz | 450526 | UINT32 | Hz | Frequency |
| Alarm Type 1 I2 In3 U4 V5 PP6 QP7 SP8 PFC9 PFL10 THDU11 THDV12 THDI13 HOUR14 F | 436363 | UINT16 | - | Power Factor |
| Alarm Specified time 1 999 s | 436364 | UINT16 | - | Status |
| thd U12 | 451536 | UINT16 | - | Harmonics |
| SOCO :4 | 450000 | STRING | - | General |
| JBUS Table Version EX 101 Version 1 01 | 450006 | UINT16 | - | Identification |
| Product option code bit field bit 1 Metering Optionbit 2 Communication optionbit 3 3 inputs 1 output option | 436096 | UINT16 | - | Communication |
| Current Transformer primary A | 457346 | UINT16 | - | Current |

## How to Use This Map

1. **Download Modbus Monitor XPF** — [Get the free version](https://www.modbusmonitor.com/download).
2. **Select the Socomec DIRIS U20 device map** — pre-built maps are bundled and ready to load.
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
- Voltage
- Energy
- Status
- Harmonics

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
