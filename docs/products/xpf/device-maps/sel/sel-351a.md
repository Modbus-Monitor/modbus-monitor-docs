---
title: SEL SEL-351A Modbus Register Map
description: SEL SEL-351A Modbus map and register map with sample Modbus registers, register addresses, and relay overview for engineers. Works with Modbus Monitor XPF (import directly) and includes downloadable CSV access in-app.
---

# SEL SEL-351A Modbus Register Map

The SEL SEL-351A is a relay used for commissioning, troubleshooting, and operational monitoring. This page provides a sample Modbus register map with addresses, data types, and signal categories to help engineers commission, troubleshoot, and monitor the device. For SEL SEL-351A deployments, teams often use this map to surface energy and power factor data in utility metering, substations, and power quality analysis.

This page shows a preview subset of the full device map available in Modbus Monitor XPF.

Engineers searching for SEL SEL-351A Modbus map, SEL SEL-351A register map, or SEL SEL-351A Modbus registers can use this page as a compatibility snapshot before importing the full map into Modbus Monitor XPF.

## Overview

- **Device:** SEL SEL-351A
- **Type:** Relay
- **Protocol:** Modbus RTU / Modbus TCP
- **Use case:** commissioning, troubleshooting, and operational monitoring
- **Works with:** Modbus Monitor XPF (import directly)

## Download Modbus Map

The full SEL SEL-351A Modbus register map is available inside Modbus Monitor XPF as a pre-built device map. Download the free feature-locked version to access and export the complete map.

- [Download Modbus Monitor XPF Free](/download)

## Register Table (Sample)

Sample registers from the SEL SEL-351A Modbus map. Import the full map in Modbus Monitor XPF to access all registers.

| Signal | Address | Type | Units | Category |
|---|---:|---|---|---|
| ForwardEnergy | 300031 | FLOAT32 | kWh | Energy |
| PFapparentTotal | 300027 | FLOAT32 | - | Power Factor |
| Ptrip.6 | 100001 | BIT | - | General |
| ReverseEnergy | 300033 | FLOAT32 | kWh | Energy |
| 50A1pickup.7 | 100003 | BIT | - | General |
| 50A2pickup.4 | 100003 | BIT | - | General |
| 50A3pickup.1 | 100003 | BIT | - | General |
| 50B1pickup.6 | 100003 | BIT | - | General |
| 50B2pickup.3 | 100003 | BIT | - | General |
| 50B3pickup.0 | 100003 | BIT | - | General |
| 50C1pickup.5 | 100003 | BIT | - | General |
| 50C2pickup.2 | 100003 | BIT | - | General |

## How to Use This Map

1. **Download Modbus Monitor XPF** — [Get the free version](/download).
2. **Select the SEL SEL-351A device map** — pre-built maps are bundled and ready to load.
3. **Connect to your device** — enter the device IP or COM port and start polling registers immediately.
4. **Visualise and log** — build dashboards, trend data, and export readings without manual register entry.

## Why Use Pre-Built Maps

- **Saves time** — no need to manually look up or enter register addresses
- **Reduces errors** — pre-validated maps eliminate mis-typed addresses and wrong data types
- **Speeds commissioning** — connect and poll within minutes instead of hours
- **Reusable across projects** — use the same map across multiple sites and installations

## Data Categories Available

- Energy
- Power Factor

## Related Tools

- [Modbus Monitor XPF — Windows Modbus Tool](https://www.modbusmonitor.com/download)
- [Modbus HMI Builder](https://www.modbusmonitor.com/modbus-hmi)
- [Compare Modbus Monitor XPF with Other Tools](https://www.modbusmonitor.com/compare)

## Related Device Maps

- [SEL SEL-735 Modbus Register Map](./sel-735.md)
- [SEL SEL-751A Modbus Register Map](./sel-751a.md)
- [SEL SEL-710 Modbus Register Map](./sel-710.md)
- [All SEL Modbus Register Maps](../index.md)
- [All XPF Device Maps](../../index.md)
