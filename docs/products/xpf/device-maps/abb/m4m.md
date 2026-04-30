---
title: ABB M4M Modbus Register Map
description: ABB M4M Modbus map and register map with sample Modbus registers, register addresses, and power meter overview for engineers. Works with Modbus Monitor XPF (import directly) and includes downloadable CSV access in-app.
---

# ABB M4M Modbus Register Map

The ABB M4M is a power meter used for power monitoring, energy metering, and facility automation. This page provides a sample Modbus register map with addresses, data types, and signal categories to help engineers commission, troubleshoot, and monitor the device. Often deployed in switchboards and compact power monitoring panels.

This page shows a preview subset of the full device map available in Modbus Monitor XPF.

Engineers searching for ABB M4M Modbus map, ABB M4M register map, or ABB M4M Modbus registers can use this page as a compatibility snapshot before importing the full map into Modbus Monitor XPF.

## Overview

- **Device:** ABB M4M
- **Type:** Power Meter
- **Protocol:** Modbus RTU / Modbus TCP
- **Use case:** power monitoring, energy metering, and facility automation
- **Works with:** Modbus Monitor XPF (import directly)

## Download Modbus Map

The full ABB M4M Modbus register map is available inside Modbus Monitor XPF as a pre-built device map. Download the free feature-locked version to access and export the complete map.

- [Download Modbus Monitor XPF Free](/download)

## Register Table (Sample)

Sample registers from the ABB M4M Modbus map. Import the full map in Modbus Monitor XPF to access all registers.

| Signal | Address | Type | Units | Category |
|---|---:|---|---|---|
| Energy Trend Data block 1 0 | 433552 | UINT16 | kWh | Energy |
| Max Min Demand Data block 1 0 | 436738 | UINT16 | kW | Demand |
| Alarm number | 435936 | UINT16 | - | Status |
| Entry number | 432769 | UINT16 | - | General |
| I O port 1 | 435852 | UINT16 | - | Communication |
| Energy Trend Data block 1 1 | 433553 | UINT16 | kWh | Energy |
| Energy Trend Data block 1 2 | 433554 | UINT16 | kWh | Energy |
| Energy Trend Data block 1 3 | 433555 | UINT16 | kWh | Energy |
| Energy Trend Data block 1 4 | 433556 | UINT16 | kWh | Energy |
| Energy Trend Data block 1 5 | 433557 | UINT16 | kWh | Energy |
| Energy Trend Data block 1 6 | 433558 | UINT16 | kWh | Energy |
| Energy Trend Data block 1 7 | 433559 | UINT16 | kWh | Energy |

## How to Use This Map

1. **Download Modbus Monitor XPF** — [Get the free version](/download).
2. **Select the ABB M4M device map** — pre-built maps are bundled and ready to load.
3. **Connect to your device** — enter the device IP or COM port and start polling registers immediately.
4. **Visualise and log** — build dashboards, trend data, and export readings without manual register entry.

## Why Use Pre-Built Maps

- **Saves time** — no need to manually look up or enter register addresses
- **Reduces errors** — pre-validated maps eliminate mis-typed addresses and wrong data types
- **Speeds commissioning** — connect and poll within minutes instead of hours
- **Reusable across projects** — use the same map across multiple sites and installations

## Data Categories Available

- Demand
- Energy
- Status

## Related Tools

- [Modbus Monitor XPF — Windows Modbus Tool](https://www.modbusmonitor.com/download)
- [Modbus HMI Builder](https://www.modbusmonitor.com/modbus-hmi)
- [Compare Modbus Monitor XPF with Other Tools](https://www.modbusmonitor.com/compare)

## Related Device Maps

- [ABB B23 / B24 Modbus Register Map](./b23-b24.md)
- [ABB A41 / A42 Modbus Register Map](./a41-a42.md)
- [ABB Trio 50 / Trio 60 Modbus Register Map](./trio-50-trio-60.md)
- [All ABB Modbus Register Maps](../index.md)
- [All XPF Device Maps](../../index.md)
