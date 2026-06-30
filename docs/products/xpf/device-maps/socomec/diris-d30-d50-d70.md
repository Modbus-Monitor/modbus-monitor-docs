---
title: Socomec DIRIS,D30,D50,D70 _ Modbus Register Map
description: Socomec DIRIS,D30,D50,D70 _ Modbus map and register map with sample Modbus registers, register addresses, and power meter overview for engineers. Works with Modbus Monitor XPF (import directly) and includes downloadable CSV access in-app. Common searches: Socomec DIRIS,D30,D50,D70 _ Modbus register list, Socomec DIRIS,D30,D50,D70 _ Modbus table.
---

# Socomec DIRIS,D30,D50,D70 _ Modbus Register Map

The Socomec DIRIS,D30,D50,D70 _ is a power meter used for power monitoring, energy metering, and facility automation. This page provides a sample Modbus register map with addresses, data types, and signal categories to help engineers commission, troubleshoot, and monitor the device. For Socomec DIRIS,D30,D50,D70 _ deployments, teams often use this map to surface energy, voltage, and current data in facility metering, commissioning, and operational analytics.

This page shows a preview subset of the full device map available in Modbus Monitor XPF.

Engineers searching for Socomec DIRIS,D30,D50,D70 _ Modbus map, Socomec DIRIS,D30,D50,D70 _ register map, or Socomec DIRIS,D30,D50,D70 _ Modbus registers can use this page as a compatibility snapshot before importing the full map into Modbus Monitor XPF. Also aligns to search intent around Socomec DIRIS,D30,D50,D70 _ Modbus register list, Socomec DIRIS,D30,D50,D70 _ Modbus table.

## Overview

- **Device:** Socomec DIRIS,D30,D50,D70 _
- **Type:** Power Meter
- **Protocol:** Modbus RTU / Modbus TCP
- **Use case:** power monitoring, energy metering, and facility automation
- **Works with:** Modbus Monitor XPF (import directly)

## Download Modbus Map

The full Socomec DIRIS,D30,D50,D70 _ Modbus register map is available inside Modbus Monitor XPF as a pre-built device map. Download the free feature-locked version to access and export the complete map.

- [Download Modbus Monitor XPF Free](https://www.modbusmonitor.com/download)

## Register Table (Sample)

Sample registers from the Socomec DIRIS,D30,D50,D70 _ Modbus map. Import the full map in Modbus Monitor XPF to access all registers.

| Signal | Address | Type | Units | Category |
|---|---:|---|---|---|
| Inst Measurement Load 1 Ph N voltage V1 V | 418444 | UINT32 | V | Voltage |
| Inst Measurement Load 1 Current I1 A | 418458 | UINT32 | - | Current |
| Inst Measurement Load 1 Total active power W | 418476 | INT32 | kW | Power |
| Energy measurement Load 1 Total positive active energy ea Wh | 419841 | UINT32 | kWh | Energy |
| Inst Measurement Load 1 Frequency Hz | 418442 | UINT32 | Hz | Frequency |
| Acknowledgment of alarms Ack id | 439616 | UINT16 | - | Status |
| Inst Measurement Load 1 Date of last instance s | 418433 | UINT32 | - | General |
| Inst Measurement Load 1 Ph N voltage V2 V | 418446 | UINT32 | V | Voltage |
| Inst Measurement Load 1 Ph N voltage V3 V | 418448 | UINT32 | V | Voltage |
| Inst Measurement Load 1 Ph ph voltage U12 V | 418452 | UINT32 | V | Voltage |
| Inst Measurement Load 1 Ph ph voltage U23 V | 418454 | UINT32 | V | Voltage |
| Inst Measurement Load 1 Ph ph voltage U31 V | 418456 | UINT32 | V | Voltage |

## How to Use This Map

1. **Download Modbus Monitor XPF** — [Get the free version](https://www.modbusmonitor.com/download).
2. **Select the Socomec DIRIS,D30,D50,D70 _ device map** — pre-built maps are bundled and ready to load.
3. **Connect to your device** — enter the device IP or COM port and start polling registers immediately.
4. **Visualise and log** — build dashboards, trend data, and export readings without manual register entry.

## Why Use Pre-Built Maps

- **Saves time** — no need to manually look up or enter register addresses
- **Reduces errors** — pre-validated maps eliminate mis-typed addresses and wrong data types
- **Speeds commissioning** — connect and poll within minutes instead of hours
- **Reusable across projects** — use the same map across multiple sites and installations

## Data Categories Available

- Energy
- Voltage
- Current
- Power
- Status
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
