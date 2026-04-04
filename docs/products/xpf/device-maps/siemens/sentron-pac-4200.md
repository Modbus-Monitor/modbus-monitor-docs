---
title: Siemens PAC4200 Modbus Map
description: Siemens PAC4200 Modbus map with register preview, power meter overview, common data categories, and ready-to-use setup guidance for Modbus Monitor XPF.
---

# Siemens PAC4200 Modbus Map

This Siemens PAC4200 Modbus map is supported in Modbus Monitor XPF, allowing engineers to quickly test, monitor, and visualize device data without manual register mapping.

This page shows a preview subset of the full device map available in Modbus Monitor XPF.

Common in industrial automation and building management systems.

## Use This Device Map in Modbus Monitor XPF

Start using this device map in minutes - no manual register mapping required.

- [Download Modbus Monitor XPF Free Trial](https://www.modbusmonitor.com/download)
- [Compare Modbus Monitor XPF with Other Tools](https://www.modbusmonitor.com/compare)
- [Modbus Tester for Windows](https://www.modbusmonitor.com/modbus-tester)

## Quick Facts

- **Manufacturer:** Siemens
- **Model:** PAC4200
- **Device Type:** Power Meter
- **Protocol:** Modbus
- **Typical Use:** power monitoring, energy metering, and facility automation
- **Available in:** Modbus Monitor XPF

## Why This Map Matters

Instead of manually decoding registers and building your setup from scratch, Modbus Monitor XPF provides a pre-built device map to help engineers test, monitor, and visualize data faster.

Browse all [XPF device maps](../../index.md) for the full library, explore [Siemens device maps](../index.md) to compare related models, and use [Compare Modbus Monitor XPF with Other Tools](https://www.modbusmonitor.com/compare) when evaluating fit across your stack.

## Register Preview

| Signal | Address | Type | Units | Category |
|---|---:|---|---|---|
| Voltage L1 N | 400001 | FLOAT32 | V | Voltage |
| Current L1 | 400013 | FLOAT32 | A | Current |
| Apparent power L1 | 400019 | FLOAT32 | kW | Power |
| Line Frequency | 400055 | FLOAT32 | Hz | Frequency |
| Sliding Window Demand Active Pow er L1 | 400325 | FLOAT32 | kW | Demand |
| PMD Diagnostics and Status | 400205 | UINT16 | - | Status |
| Maximum 3 Phase Average Volt age L N | 400131 | FLOAT32 | - | General |
| Voltage L2 N | 400003 | FLOAT32 | V | Voltage |
| Voltage L3 N | 400005 | FLOAT32 | V | Voltage |
| Voltage L1 L2 | 400007 | FLOAT32 | V | Voltage |
| Voltage L2 L3 | 400009 | FLOAT32 | V | Voltage |
| Voltage L3 L1 | 400011 | FLOAT32 | V | Voltage |

## Common Data Categories

- Power
- Voltage
- Current
- Status
- Demand
- Frequency

## Typical Use Cases

- Commissioning new devices with a known-good register baseline
- Troubleshooting Modbus communication and addressing issues
- Building HMI dashboards for operational visibility
- Logging device telemetry for analysis and reporting

## Related Device Maps

- [Siemens PAC2200 Modbus Map](./sentron-pac-2200.md)
- [Siemens SICAM P Modbus Map](./sicam-p.md)
- [Siemens SEM3 Series Modbus Map](./sem3-series.md)
- [All Siemens Device Maps](../index.md)
- [All XPF Device Maps](../../index.md)

## Use This Device Map in Modbus Monitor XPF

Start using this device map in minutes - no manual register mapping required.

- [Download Modbus Monitor XPF Free Trial](https://www.modbusmonitor.com/download)
- [Compare Modbus Monitor XPF with Other Tools](https://www.modbusmonitor.com/compare)
- [Modbus Tester for Windows](https://www.modbusmonitor.com/modbus-tester)
