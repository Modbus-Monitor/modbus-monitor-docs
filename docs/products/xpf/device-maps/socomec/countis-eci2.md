---
title: Socomec Countis ECI2 Modbus Register Map
description: Socomec Countis ECI2 Modbus map and register map with sample Modbus registers, register addresses, and power meter overview for engineers. Works with Modbus Monitor XPF (import directly) and includes downloadable CSV access in-app. Common searches: Socomec Countis ECI2 Modbus register list, Socomec Countis ECI2 Modbus table.
---

# Socomec Countis ECI2 Modbus Register Map

The Socomec Countis ECI2 is a power meter used for power monitoring, energy metering, and facility automation. This page provides a sample Modbus register map with addresses, data types, and signal categories to help engineers commission, troubleshoot, and monitor the device. For Socomec Countis ECI2 deployments, teams often use this map to surface current, frequency, and status data in facility metering, commissioning, and operational analytics.

This page shows a preview subset of the full device map available in Modbus Monitor XPF.

Engineers searching for Socomec Countis ECI2 Modbus map, Socomec Countis ECI2 register map, or Socomec Countis ECI2 Modbus registers can use this page as a compatibility snapshot before importing the full map into Modbus Monitor XPF. Also aligns to search intent around Socomec Countis ECI2 Modbus register list, Socomec Countis ECI2 Modbus table.

## Overview

- **Device:** Socomec Countis ECI2
- **Type:** Power Meter
- **Protocol:** Modbus RTU / Modbus TCP
- **Use case:** power monitoring, energy metering, and facility automation
- **Works with:** Modbus Monitor XPF (import directly)

## Download Modbus Map

The full Socomec Countis ECI2 Modbus register map is available inside Modbus Monitor XPF as a pre-built device map. Download the free feature-locked version to access and export the complete map.

- [Download Modbus Monitor XPF Free](https://www.modbusmonitor.com/download)

## Register Table (Sample)

Sample registers from the Socomec Countis ECI2 Modbus map. Import the full map in Modbus Monitor XPF to access all registers.

| Signal | Address | Type | Units | Category |
|---|---:|---|---|---|
| Date & Time Current s | 437120 | UINT16 | - | Current |
| Custom Meter Frequency | 439698 | UINT16 | Hz | Frequency |
| Status | 440981 | UINT16 | - | Status |
| Label of custom unit :2 | 437072 | STRING | - | General |
| Name :5 | 440192 | STRING | - | Identification |
| Address | 440448 | UINT16 | - | Communication |
| Custom Meter Frequency | 439725 | UINT16 | Hz | Frequency |
| Custom Meter Frequency | 439752 | UINT16 | Hz | Frequency |
| Custom Meter Frequency | 439779 | UINT16 | Hz | Frequency |
| Custom Meter Frequency | 439806 | UINT16 | Hz | Frequency |
| Custom Meter Frequency | 439833 | UINT16 | Hz | Frequency |
| Custom Meter Frequency | 439860 | UINT16 | Hz | Frequency |

## How to Use This Map

1. **Download Modbus Monitor XPF** — [Get the free version](https://www.modbusmonitor.com/download).
2. **Select the Socomec Countis ECI2 device map** — pre-built maps are bundled and ready to load.
3. **Connect to your device** — enter the device IP or COM port and start polling registers immediately.
4. **Visualise and log** — build dashboards, trend data, and export readings without manual register entry.

## Why Use Pre-Built Maps

- **Saves time** — no need to manually look up or enter register addresses
- **Reduces errors** — pre-validated maps eliminate mis-typed addresses and wrong data types
- **Speeds commissioning** — connect and poll within minutes instead of hours
- **Reusable across projects** — use the same map across multiple sites and installations

## Data Categories Available

- Current
- Frequency
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
