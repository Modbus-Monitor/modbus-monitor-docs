---
title: Eaton IQ100 series,IQ130,IQ140,IQ150 Modbus Register Map
description: Eaton IQ100 series,IQ130,IQ140,IQ150 Modbus map and register map with sample Modbus registers, register addresses, and power meter overview for engineers. Works with Modbus Monitor XPF (import directly) and includes downloadable CSV access in-app.
---

# Eaton IQ100 series,IQ130,IQ140,IQ150 Modbus Register Map

The Eaton IQ100 series,IQ130,IQ140,IQ150 is a power meter used for power monitoring, energy metering, and facility automation. This page provides a sample Modbus register map with addresses, data types, and signal categories to help engineers commission, troubleshoot, and monitor the device. For Eaton IQ100 series,IQ130,IQ140,IQ150 deployments, teams often use this map to surface current, energy, and demand data in critical power distribution and electrical monitoring systems.

This page shows a preview subset of the full device map available in Modbus Monitor XPF.

Engineers searching for Eaton IQ100 series,IQ130,IQ140,IQ150 Modbus map, Eaton IQ100 series,IQ130,IQ140,IQ150 register map, or Eaton IQ100 series,IQ130,IQ140,IQ150 Modbus registers can use this page as a compatibility snapshot before importing the full map into Modbus Monitor XPF.

## Overview

- **Device:** Eaton IQ100 series,IQ130,IQ140,IQ150
- **Type:** Power Meter
- **Protocol:** Modbus RTU / Modbus TCP
- **Use case:** power monitoring, energy metering, and facility automation
- **Works with:** Modbus Monitor XPF (import directly)

## Download Modbus Map

The full Eaton IQ100 series,IQ130,IQ140,IQ150 Modbus register map is available inside Modbus Monitor XPF as a pre-built device map. Download the free feature-locked version to access and export the complete map.

- [Download Modbus Monitor XPF Free](https://www.modbusmonitor.com/download)

## Register Table (Sample)

Sample registers from the Eaton IQ100 series,IQ130,IQ140,IQ150 Modbus map. Import the full map in Modbus Monitor XPF to access all registers.

| Signal | Address | Type | Units | Category |
|---|---:|---|---|---|
| Amps A amps | 401011 | FLOAT32 | A | Current |
| Positive Power Factor 3 Ph Maximum Avg Demand none | 403127 | FLOAT32 | PF | Power |
| Power Energy Format pppp nn eee ddd | 430005 | UINT16 | kWh | Energy |
| Frequency Hz | 401025 | FLOAT32 | Hz | Frequency |
| Positive pf 3 ph average -100 to 100 | 402015 | FLOAT32 | - | Power Factor |
| Positive Watts 3 Ph Maximum Avg Demand watts | 403117 | FLOAT32 | kW | Demand |
| Meter status bit-mapped | 404999 | UINT16 | - | Status |
| Meter Serial Number:8 | 400008 | STRING | - | Identification |
| Meter type bit-mapped | 400016 | UINT16 | - | General |
| Amps B amps | 401013 | FLOAT32 | A | Current |
| Amps C amps | 401015 | FLOAT32 | A | Current |
| Neutral current amps | 401027 | FLOAT32 | A | Current |

## How to Use This Map

1. **Download Modbus Monitor XPF** — [Get the free version](https://www.modbusmonitor.com/download).
2. **Select the Eaton IQ100 series,IQ130,IQ140,IQ150 device map** — pre-built maps are bundled and ready to load.
3. **Connect to your device** — enter the device IP or COM port and start polling registers immediately.
4. **Visualise and log** — build dashboards, trend data, and export readings without manual register entry.

## Why Use Pre-Built Maps

- **Saves time** — no need to manually look up or enter register addresses
- **Reduces errors** — pre-validated maps eliminate mis-typed addresses and wrong data types
- **Speeds commissioning** — connect and poll within minutes instead of hours
- **Reusable across projects** — use the same map across multiple sites and installations

## Data Categories Available

- Current
- Energy
- Demand
- Frequency
- Power
- Power Factor

## Related Tools

- [Modbus Monitor XPF — Windows Modbus Tool](https://www.modbusmonitor.com/download)
- [Modbus HMI Builder](https://www.modbusmonitor.com/modbus-hmi)
- [Compare Modbus Monitor XPF with Other Tools](https://www.modbusmonitor.com/compare)

## Related Device Maps

- [Eaton 93PM Modbus Register Map](./93pm.md)
- [Eaton BladeUPS Modbus Register Map](./bladeups.md)
- [Eaton PXM2000 Modbus Register Map](./pxm2000.md)
- [Eaton EM19 M Modbus Register Map](./em19-m.md)
- [All Eaton Modbus Register Maps](../index.md)
- [All XPF Device Maps](../../../../modbus-device-maps/index.md)
