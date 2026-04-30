---
title: Siemens SEM3 Series Modbus Register Map
description: Siemens SEM3 Series Modbus map and register map with sample Modbus registers, register addresses, and power meter overview for engineers. Works with Modbus Monitor XPF (import directly) and includes downloadable CSV access in-app.
---

# Siemens SEM3 Series Modbus Register Map

The Siemens SEM3 Series is a power meter used for power monitoring, energy metering, and facility automation. This page provides a sample Modbus register map with addresses, data types, and signal categories to help engineers commission, troubleshoot, and monitor the device. For Siemens SEM3 Series deployments, teams often use this map to surface current, power, and status data in industrial automation panels and building management systems.

This page shows a preview subset of the full device map available in Modbus Monitor XPF.

Engineers searching for Siemens SEM3 Series Modbus map, Siemens SEM3 Series register map, or Siemens SEM3 Series Modbus registers can use this page as a compatibility snapshot before importing the full map into Modbus Monitor XPF.

## Overview

- **Device:** Siemens SEM3 Series
- **Type:** Power Meter
- **Protocol:** Modbus RTU / Modbus TCP
- **Use case:** power monitoring, energy metering, and facility automation
- **Works with:** Modbus Monitor XPF (import directly)

## Download Modbus Map

The full Siemens SEM3 Series Modbus register map is available inside Modbus Monitor XPF as a pre-built device map. Download the free feature-locked version to access and export the complete map.

- [Download Modbus Monitor XPF Free](https://www.modbusmonitor.com/download)

## Register Table (Sample)

Sample registers from the Siemens SEM3 Series Modbus map. Import the full map in Modbus Monitor XPF to access all registers.

| Signal | Address | Type | Units | Category |
|---|---:|---|---|---|
| Monitor 1 current phase 1 Amps | 411906 | FLOAT32 | A | Current |
| Monitor 1 power factor phase 1 1 | 411930 | FLOAT32 | PF | Power |
| Monitor 1 alarm flags | 400200 | UINT16 | - | Status |
| Monitor 1 volts phase 1 Volts | 411900 | FLOAT32 | - | General |
| Monitor 2 alarm flags | 400201 | UINT16 | - | Status |
| Monitor 3 alarm flags | 400202 | UINT16 | - | Status |
| Monitor 4 alarm flags | 400203 | UINT16 | - | Status |
| Monitor 5 alarm flags | 400204 | UINT16 | - | Status |
| Monitor 6 alarm flags | 400205 | UINT16 | - | Status |
| Monitor 7 alarm flags | 400206 | UINT16 | - | Status |
| Monitor 8 alarm flags | 400207 | UINT16 | - | Status |
| Monitor 9 alarm flags | 400208 | UINT16 | - | Status |

## How to Use This Map

1. **Download Modbus Monitor XPF** — [Get the free version](https://www.modbusmonitor.com/download).
2. **Select the Siemens SEM3 Series device map** — pre-built maps are bundled and ready to load.
3. **Connect to your device** — enter the device IP or COM port and start polling registers immediately.
4. **Visualise and log** — build dashboards, trend data, and export readings without manual register entry.

## Why Use Pre-Built Maps

- **Saves time** — no need to manually look up or enter register addresses
- **Reduces errors** — pre-validated maps eliminate mis-typed addresses and wrong data types
- **Speeds commissioning** — connect and poll within minutes instead of hours
- **Reusable across projects** — use the same map across multiple sites and installations

## Data Categories Available

- Current
- Power
- Status

## Related Tools

- [Modbus Monitor XPF — Windows Modbus Tool](https://www.modbusmonitor.com/download)
- [Modbus HMI Builder](https://www.modbusmonitor.com/modbus-hmi)
- [Compare Modbus Monitor XPF with Other Tools](https://www.modbusmonitor.com/compare)

## Related Device Maps

- [Siemens PAC3200 Modbus Register Map](./sentron-pac-3200.md)
- [Siemens PAC4200 Modbus Register Map](./sentron-pac-4200.md)
- [Siemens PAC2200 Modbus Register Map](./sentron-pac-2200.md)
- [Siemens SICAM P Modbus Register Map](./sicam-p.md)
- [All Siemens Modbus Register Maps](../index.md)
- [All XPF Device Maps](../../index.md)
