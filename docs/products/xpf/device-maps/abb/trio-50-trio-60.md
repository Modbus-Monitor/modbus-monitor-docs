---
title: ABB Trio 50 / Trio 60 Modbus Register Map
description: ABB Trio 50 / Trio 60 Modbus map and register map with sample Modbus registers, register addresses, and solar inverter overview for engineers. Works with Modbus Monitor XPF (import directly) and includes downloadable CSV access in-app.
---

# ABB Trio 50 / Trio 60 Modbus Register Map

The ABB Trio 50 / Trio 60 is a solar inverter used for PV production monitoring, inverter diagnostics, and energy analytics. This page provides a sample Modbus register map with addresses, data types, and signal categories to help engineers commission, troubleshoot, and monitor the device. For ABB Trio 50 / Trio 60 deployments, teams often use this map to surface power, status, and current data in switchboards, facility power distribution, and commercial energy monitoring.

This page shows a preview subset of the full device map available in Modbus Monitor XPF.

Engineers searching for ABB Trio 50 / Trio 60 Modbus map, ABB Trio 50 / Trio 60 register map, or ABB Trio 50 / Trio 60 Modbus registers can use this page as a compatibility snapshot before importing the full map into Modbus Monitor XPF.

## Overview

- **Device:** ABB Trio 50 / Trio 60
- **Type:** Solar Inverter
- **Protocol:** Modbus RTU / Modbus TCP
- **Use case:** PV production monitoring, inverter diagnostics, and energy analytics
- **Works with:** Modbus Monitor XPF (import directly)

## Download Modbus Map

The full ABB Trio 50 / Trio 60 Modbus register map is available inside Modbus Monitor XPF as a pre-built device map. Download the free feature-locked version to access and export the complete map.

- [Download Modbus Monitor XPF Free](https://www.modbusmonitor.com/download)

## Register Table (Sample)

Sample registers from the ABB Trio 50 / Trio 60 Modbus map. Import the full map in Modbus Monitor XPF to access all registers.

| Signal | Address | Type | Units | Category |
|---|---:|---|---|---|
| Inverter Grid Voltage V | 400304 | FLOAT32 | V | Voltage |
| Inverter Grid Current A | 400308 | FLOAT32 | - | Current |
| Dynamic Mode Power Factor Set Point Reactive Power expressed as fixed Power Factor | 400201 | FLOAT32 | PF | Power |
| Daily Energy Wh | 401071 | UINT32 | kWh | Energy |
| Mean Grid Frequency Hz | 401107 | FLOAT32 | Hz | Frequency |
| Global State | 401051 | UINT16 | - | Status |
| Internal Temperature C | 401121 | FLOAT32 | degC | Temperature |
| Remote On Off | 400181 | UINT16 | - | General |
| Accuracy Set unit for Modbus Data Addresses 0507 0508 0511 and 0512 or | 400502 | UINT16 | - | Communication |
| Set communication protocol for serial line RS485 1 | 401007 | UINT16 | - | Identification |
| Permanent Mode Power Factor Set Point Reactive Power expressed as fixed Power Factor | 400203 | FLOAT32 | PF | Power |
| Dynamic Mode Active Power Set Point Active Power Curtailment expressed as percentage of Nominal Power in steps | 400211 | UINT16 | kW | Power |

## How to Use This Map

1. **Download Modbus Monitor XPF** — [Get the free version](https://www.modbusmonitor.com/download).
2. **Select the ABB Trio 50 / Trio 60 device map** — pre-built maps are bundled and ready to load.
3. **Connect to your device** — enter the device IP or COM port and start polling registers immediately.
4. **Visualise and log** — build dashboards, trend data, and export readings without manual register entry.

## Why Use Pre-Built Maps

- **Saves time** — no need to manually look up or enter register addresses
- **Reduces errors** — pre-validated maps eliminate mis-typed addresses and wrong data types
- **Speeds commissioning** — connect and poll within minutes instead of hours
- **Reusable across projects** — use the same map across multiple sites and installations

## Data Categories Available

- Power
- Status
- Current
- Energy
- Voltage
- Temperature

## Related Tools

- [Modbus Monitor XPF — Windows Modbus Tool](https://www.modbusmonitor.com/download)
- [Modbus HMI Builder](https://www.modbusmonitor.com/modbus-hmi)
- [Compare Modbus Monitor XPF with Other Tools](https://www.modbusmonitor.com/compare)

## Related Device Maps

- [ABB M4M Modbus Register Map](./m4m.md)
- [ABB B23 / B24 Modbus Register Map](./b23-b24.md)
- [ABB A41 / A42 Modbus Register Map](./a41-a42.md)
- [All ABB Modbus Register Maps](../index.md)
- [All XPF Device Maps](../../index.md)
