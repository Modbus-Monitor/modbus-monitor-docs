---
title: Siemens SICAM P Modbus Register Map
description: Siemens SICAM P Modbus map and register map with sample Modbus registers, register addresses, and power meter overview for engineers. Works with Modbus Monitor XPF (import directly) and includes downloadable CSV access in-app.
---

# Siemens SICAM P Modbus Register Map

The Siemens SICAM P is a power meter used for power monitoring, energy metering, and facility automation. This page provides a sample Modbus register map with addresses, data types, and signal categories to help engineers commission, troubleshoot, and monitor the device. For Siemens SICAM P deployments, teams often use this map to surface harmonics, power factor, and status data in industrial automation panels and building management systems.

This page shows a preview subset of the full device map available in Modbus Monitor XPF.

Engineers searching for Siemens SICAM P Modbus map, Siemens SICAM P register map, or Siemens SICAM P Modbus registers can use this page as a compatibility snapshot before importing the full map into Modbus Monitor XPF.

## Overview

- **Device:** Siemens SICAM P
- **Type:** Power Meter
- **Protocol:** Modbus RTU / Modbus TCP
- **Use case:** power monitoring, energy metering, and facility automation
- **Works with:** Modbus Monitor XPF (import directly)

## Download Modbus Map

The full Siemens SICAM P Modbus register map is available inside Modbus Monitor XPF as a pre-built device map. Download the free feature-locked version to access and export the complete map.

- [Download Modbus Monitor XPF Free](/download)

## Register Table (Sample)

Sample registers from the Siemens SICAM P Modbus map. Import the full map in Modbus Monitor XPF to access all registers.

| Signal | Address | Type | Units | Category |
|---|---:|---|---|---|
| PF L1 | 400258 | FLOAT32 | - | Power Factor |
| Status of Binary Outputs and Device | 400128 | BIT | - | Status |
| THDU L1 | 400280 | FLOAT32 | - | Harmonics |
| MLFB:16 | 400000 | STRING | - | General |
| Serial number:10 | 400019 | STRING | - | Identification |
| Status of Binary Inputs | 400129 | BIT | - | Status |
| Status of Overflow at Measuring | 400199 | BIT | - | Status |
| PF L2 | 400260 | FLOAT32 | - | Power Factor |
| PF L3 | 400262 | FLOAT32 | - | Power Factor |
| PF | 400264 | FLOAT32 | - | Power Factor |
| THDU L2 | 400282 | FLOAT32 | - | Harmonics |
| THDU L3 | 400284 | FLOAT32 | - | Harmonics |

## How to Use This Map

1. **Download Modbus Monitor XPF** — [Get the free version](/download).
2. **Select the Siemens SICAM P device map** — pre-built maps are bundled and ready to load.
3. **Connect to your device** — enter the device IP or COM port and start polling registers immediately.
4. **Visualise and log** — build dashboards, trend data, and export readings without manual register entry.

## Why Use Pre-Built Maps

- **Saves time** — no need to manually look up or enter register addresses
- **Reduces errors** — pre-validated maps eliminate mis-typed addresses and wrong data types
- **Speeds commissioning** — connect and poll within minutes instead of hours
- **Reusable across projects** — use the same map across multiple sites and installations

## Data Categories Available

- Harmonics
- Power Factor
- Status

## Related Tools

- [Modbus Monitor XPF — Windows Modbus Tool](https://www.modbusmonitor.com/download)
- [Modbus HMI Builder](https://www.modbusmonitor.com/modbus-hmi)
- [Compare Modbus Monitor XPF with Other Tools](https://www.modbusmonitor.com/compare)

## Related Device Maps

- [Siemens PAC3200 Modbus Register Map](./sentron-pac-3200.md)
- [Siemens PAC4200 Modbus Register Map](./sentron-pac-4200.md)
- [Siemens PAC2200 Modbus Register Map](./sentron-pac-2200.md)
- [Siemens SEM3 Series Modbus Register Map](./sem3-series.md)
- [All Siemens Modbus Register Maps](../index.md)
- [All XPF Device Maps](../../index.md)
