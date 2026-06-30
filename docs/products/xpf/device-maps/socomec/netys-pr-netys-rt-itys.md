---
title: Socomec NETYS PR,NETYS RT,ITYS Modbus Register Map
description: Socomec NETYS PR,NETYS RT,ITYS Modbus map and register map with sample Modbus registers, register addresses, and ups overview for engineers. Works with Modbus Monitor XPF (import directly) and includes downloadable CSV access in-app. Common searches: Socomec NETYS PR,NETYS RT,ITYS Modbus register list, Socomec NETYS PR,NETYS RT,ITYS Modbus table.
---

# Socomec NETYS PR,NETYS RT,ITYS Modbus Register Map

The Socomec NETYS PR,NETYS RT,ITYS is a ups used for power continuity monitoring, alarm review, and resilience planning. This page provides a sample Modbus register map with addresses, data types, and signal categories to help engineers commission, troubleshoot, and monitor the device. For Socomec NETYS PR,NETYS RT,ITYS deployments, teams often use this map to surface voltage, frequency, and current data in backup power systems and critical infrastructure monitoring.

This page shows a preview subset of the full device map available in Modbus Monitor XPF.

Engineers searching for Socomec NETYS PR,NETYS RT,ITYS Modbus map, Socomec NETYS PR,NETYS RT,ITYS register map, or Socomec NETYS PR,NETYS RT,ITYS Modbus registers can use this page as a compatibility snapshot before importing the full map into Modbus Monitor XPF. Also aligns to search intent around Socomec NETYS PR,NETYS RT,ITYS Modbus register list, Socomec NETYS PR,NETYS RT,ITYS Modbus table.

## Overview

- **Device:** Socomec NETYS PR,NETYS RT,ITYS
- **Type:** UPS
- **Protocol:** Modbus RTU / Modbus TCP
- **Use case:** power continuity monitoring, alarm review, and resilience planning
- **Works with:** Modbus Monitor XPF (import directly)

## Download Modbus Map

The full Socomec NETYS PR,NETYS RT,ITYS Modbus register map is available inside Modbus Monitor XPF as a pre-built device map. Download the free feature-locked version to access and export the complete map.

- [Download Modbus Monitor XPF Free](https://www.modbusmonitor.com/download)

## Register Table (Sample)

Sample registers from the Socomec NETYS PR,NETYS RT,ITYS Modbus map. Import the full map in Modbus Monitor XPF to access all registers.

| Signal | Address | Type | Units | Category |
|---|---:|---|---|---|
| Phase Voltage AB V | 440074 | UINT16 | V | Voltage |
| AC Current A | 440069 | UINT16 | - | Current |
| AC Power W | 440081 | INT16 | kW | Power |
| AC Energy Wh | 440091 | UINT32 | kWh | Energy |
| Line Frequency Hz | 440083 | UINT16 | Hz | Frequency |
| Scale factor PFSF | 440090 | INT16 | - | Power Factor |
| Enumerated value Operating state | 440105 | UINT16 | - | Status |
| Cabinet Temperature C | 440100 | INT16 | degC | Temperature |
| Scale factor ASF | 440073 | INT16 | - | General |
| Phase A Current A | 440070 | UINT16 | - | Current |
| Phase B Current A | 440071 | UINT16 | - | Current |
| Phase C Current A | 440072 | UINT16 | - | Current |

## How to Use This Map

1. **Download Modbus Monitor XPF** — [Get the free version](https://www.modbusmonitor.com/download).
2. **Select the Socomec NETYS PR,NETYS RT,ITYS device map** — pre-built maps are bundled and ready to load.
3. **Connect to your device** — enter the device IP or COM port and start polling registers immediately.
4. **Visualise and log** — build dashboards, trend data, and export readings without manual register entry.

## Why Use Pre-Built Maps

- **Saves time** — no need to manually look up or enter register addresses
- **Reduces errors** — pre-validated maps eliminate mis-typed addresses and wrong data types
- **Speeds commissioning** — connect and poll within minutes instead of hours
- **Reusable across projects** — use the same map across multiple sites and installations

## Data Categories Available

- Voltage
- Frequency
- Current
- Temperature
- Power
- Status

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
