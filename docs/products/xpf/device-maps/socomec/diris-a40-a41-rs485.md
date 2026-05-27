---
title: Socomec DIRIS A40 / A41 RS485 Modbus Register Map
description: Socomec DIRIS A40 / A41 RS485 Modbus map and register map with sample Modbus registers, register addresses, and power meter overview for engineers. Works with Modbus Monitor XPF (import directly) and includes downloadable CSV access in-app. Common searches: Socomec DIRIS A40 / A41 RS485 Modbus register list, Socomec DIRIS A40 / A41 RS485 Modbus table.
---

# Socomec DIRIS A40 / A41 RS485 Modbus Register Map

The Socomec DIRIS A40 / A41 RS485 is a power meter used for power monitoring, energy metering, and facility automation. This page provides a sample Modbus register map with addresses, data types, and signal categories to help engineers commission, troubleshoot, and monitor the device. For Socomec DIRIS A40 / A41 RS485 deployments, teams often use this map to surface harmonics, power, and voltage data in facility metering, commissioning, and operational analytics.

This page shows a preview subset of the full device map available in Modbus Monitor XPF.

Engineers searching for Socomec DIRIS A40 / A41 RS485 Modbus map, Socomec DIRIS A40 / A41 RS485 register map, or Socomec DIRIS A40 / A41 RS485 Modbus registers can use this page as a compatibility snapshot before importing the full map into Modbus Monitor XPF. Also aligns to search intent around Socomec DIRIS A40 / A41 RS485 Modbus register list, Socomec DIRIS A40 / A41 RS485 Modbus table.

## Overview

- **Device:** Socomec DIRIS A40 / A41 RS485
- **Type:** Power Meter
- **Protocol:** Modbus RTU / Modbus TCP
- **Use case:** power monitoring, energy metering, and facility automation
- **Works with:** Modbus Monitor XPF (import directly)

## Download Modbus Map

The full Socomec DIRIS A40 / A41 RS485 Modbus register map is available inside Modbus Monitor XPF as a pre-built device map. Download the free feature-locked version to access and export the complete map.

- [Download Modbus Monitor XPF Free](https://www.modbusmonitor.com/download)

## Register Table (Sample)

Sample registers from the Socomec DIRIS A40 / A41 RS485 Modbus map. Import the full map in Modbus Monitor XPF to access all registers.

| Signal | Address | Type | Units | Category |
|---|---:|---|---|---|
| Phase to phase voltage u12 V | 410513 | UINT32 | V | Voltage |
| Phase current 1 | 410527 | UINT32 | - | Current |
| active power kW | 410535 | UINT32 | kW | Power |
| Active energy | 410769 | UINT32 | kWh | Energy |
| Frequency Hz | 410525 | UINT32 | Hz | Frequency |
| Internal temperature sensor present | 411455 | UINT16 | degC | Temperature |
| Thd u12 | 411535 | UINT16 | - | Harmonics |
| Hour meter 1 | 410511 | UINT32 | - | General |
| Phase to phase voltage u23 V | 410515 | UINT32 | V | Voltage |
| Phase to phase voltage u31 V | 410517 | UINT32 | V | Voltage |
| Phase to neutral voltage phase 1 V | 410519 | UINT32 | V | Voltage |
| Phase to neutral voltage phase 2 V | 410521 | UINT32 | V | Voltage |

## How to Use This Map

1. **Download Modbus Monitor XPF** — [Get the free version](https://www.modbusmonitor.com/download).
2. **Select the Socomec DIRIS A40 / A41 RS485 device map** — pre-built maps are bundled and ready to load.
3. **Connect to your device** — enter the device IP or COM port and start polling registers immediately.
4. **Visualise and log** — build dashboards, trend data, and export readings without manual register entry.

## Why Use Pre-Built Maps

- **Saves time** — no need to manually look up or enter register addresses
- **Reduces errors** — pre-validated maps eliminate mis-typed addresses and wrong data types
- **Speeds commissioning** — connect and poll within minutes instead of hours
- **Reusable across projects** — use the same map across multiple sites and installations

## Data Categories Available

- Harmonics
- Power
- Voltage
- Current
- Temperature
- Frequency

## Related Tools

- [Modbus Monitor XPF — Windows Modbus Tool](https://www.modbusmonitor.com/download)
- [Modbus HMI Builder](https://www.modbusmonitor.com/modbus-hmi)
- [Compare Modbus Monitor XPF with Other Tools](https://www.modbusmonitor.com/compare)

## Related Device Maps

- [Socomec DIRIS I31 Modbus Register Map](./diris-i31.md)
- [Socomec DIRIS U30 Modbus Register Map](./diris-u30.md)
- [Socomec Countis ECI3 Modbus Register Map](./countis-eci3.md)
- [Socomec Countis ECI2 Modbus Register Map](./countis-eci2.md)
- [All Socomec Modbus Register Maps](../index.md)
- [All XPF Device Maps](../../../../modbus-device-maps/index.md)
