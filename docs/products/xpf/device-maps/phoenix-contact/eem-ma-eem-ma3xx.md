---
title: Phoenix Contact EEM-MA,EEM-MA3xx Modbus Register Map
description: Phoenix Contact EEM-MA,EEM-MA3xx Modbus map and register map with sample Modbus registers, register addresses, and power meter overview for engineers. Works with Modbus Monitor XPF (import directly) and includes downloadable CSV access in-app.
---

# Phoenix Contact EEM-MA,EEM-MA3xx Modbus Register Map

The Phoenix Contact EEM-MA,EEM-MA3xx is a power meter used for power monitoring, energy metering, and facility automation. This page provides a sample Modbus register map with addresses, data types, and signal categories to help engineers commission, troubleshoot, and monitor the device. For Phoenix Contact EEM-MA,EEM-MA3xx deployments, teams often use this map to surface power, energy, and voltage data in facility metering, commissioning, and operational analytics.

This page shows a preview subset of the full device map available in Modbus Monitor XPF.

Engineers searching for Phoenix Contact EEM-MA,EEM-MA3xx Modbus map, Phoenix Contact EEM-MA,EEM-MA3xx register map, or Phoenix Contact EEM-MA,EEM-MA3xx Modbus registers can use this page as a compatibility snapshot before importing the full map into Modbus Monitor XPF.

## Overview

- **Device:** Phoenix Contact EEM-MA,EEM-MA3xx
- **Type:** Power Meter
- **Protocol:** Modbus RTU / Modbus TCP
- **Use case:** power monitoring, energy metering, and facility automation
- **Works with:** Modbus Monitor XPF (import directly)

## Download Modbus Map

The full Phoenix Contact EEM-MA,EEM-MA3xx Modbus register map is available inside Modbus Monitor XPF as a pre-built device map. Download the free feature-locked version to access and export the complete map.

- [Download Modbus Monitor XPF Free](https://www.modbusmonitor.com/download)

## Register Table (Sample)

Sample registers from the Phoenix Contact EEM-MA,EEM-MA3xx Modbus map. Import the full map in Modbus Monitor XPF to access all registers.

| Signal | Address | Type | Units | Category |
|---|---:|---|---|---|
| U12 conductor voltage V | 450514 | UINT32 | V | Voltage |
| I1 current A | 450528 | UINT32 | - | Current |
| Sum P total active power - W | 450536 | INT32 | kW | Power |
| Total active energy procurement system kWh | 450770 | UINT32 | kWh | Energy |
| F frequency Hz | 450526 | UINT32 | Hz | Frequency |
| Hour operating hours counter h | 450512 | UINT32 | - | General |
| U23 conductor voltage V | 450516 | UINT32 | V | Voltage |
| U31 conductor voltage V | 450518 | UINT32 | V | Voltage |
| V1 conductor voltage to N V | 450520 | UINT32 | V | Voltage |
| V2 conductor voltage to N V | 450522 | UINT32 | V | Voltage |
| V3 conductor voltage to N V | 450524 | UINT32 | V | Voltage |
| I2 current A | 450530 | UINT32 | - | Current |

## How to Use This Map

1. **Download Modbus Monitor XPF** — [Get the free version](https://www.modbusmonitor.com/download).
2. **Select the Phoenix Contact EEM-MA,EEM-MA3xx device map** — pre-built maps are bundled and ready to load.
3. **Connect to your device** — enter the device IP or COM port and start polling registers immediately.
4. **Visualise and log** — build dashboards, trend data, and export readings without manual register entry.

## Why Use Pre-Built Maps

- **Saves time** — no need to manually look up or enter register addresses
- **Reduces errors** — pre-validated maps eliminate mis-typed addresses and wrong data types
- **Speeds commissioning** — connect and poll within minutes instead of hours
- **Reusable across projects** — use the same map across multiple sites and installations

## Data Categories Available

- Power
- Energy
- Voltage
- Current
- Frequency

## Related Tools

- [Modbus Monitor XPF — Windows Modbus Tool](https://www.modbusmonitor.com/download)
- [Modbus HMI Builder](https://www.modbusmonitor.com/modbus-hmi)
- [Compare Modbus Monitor XPF with Other Tools](https://www.modbusmonitor.com/compare)

## Related Device Maps

- [Phoenix Contact EEM-EM3xx,EM325,EM355,EM375,EM327,EM357,EM377 Modbus Register Map](./eem-em3xx-em325-em355-em375-em327-em357-em377.md)
- [Phoenix Contact EEM-MA3xx Modbus Register Map](./eem-ma3xx.md)
- [All Phoenix Contact Modbus Register Maps](../index.md)
- [All XPF Device Maps](../../../../modbus-device-maps/index.md)
