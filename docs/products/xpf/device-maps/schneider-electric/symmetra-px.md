---
title: Schneider Electric Symmetra PX Modbus Map
description: Pre-built Schneider Electric Symmetra PX Modbus map for Modbus Monitor XPF with register preview, device overview, and setup guidance.
---

# Schneider Electric Symmetra PX Modbus Map

This Schneider Electric Symmetra PX Modbus map is supported in Modbus Monitor XPF, allowing engineers to quickly test, monitor, and visualize device data without manual register mapping.

This page shows a preview subset of the full device map available in Modbus Monitor XPF.

For Schneider Electric Symmetra PX deployments, teams often use this map to surface power, current, and status data in data centers, switchgear lineups, and advanced power monitoring projects.

## Use This Device Map in Modbus Monitor XPF

Start using this device map in minutes - no manual register mapping required.

- [Download Modbus Monitor XPF Free Trial](https://www.modbusmonitor.com/download)
- [Compare Modbus Monitor XPF with Other Tools](https://www.modbusmonitor.com/compare)
- [Modbus Tester for Windows](https://www.modbusmonitor.com/modbus-tester)

## Quick Facts

- **Manufacturer:** Schneider Electric
- **Model:** Symmetra PX
- **Device Type:** UPS
- **Protocol:** Modbus
- **Typical Use:** power continuity monitoring, alarm review, and resilience planning
- **Available in:** Modbus Monitor XPF

## Why This Map Matters

Instead of manually decoding registers and building your setup from scratch, Modbus Monitor XPF provides a pre-built device map to help engineers test, monitor, and visualize data faster.

Browse all [XPF device maps](../../index.md) for the full library, explore [Schneider Electric device maps](../index.md) to compare related models, and use [Compare Modbus Monitor XPF with Other Tools](https://www.modbusmonitor.com/compare) when evaluating fit across your stack.

## Register Preview

| Signal | Address | Type | Units | Category |
|---|---:|---|---|---|
| Battery Voltage | 404359 | UINT16 | V | Voltage |
| Battery Current | 404361 | UINT16 | - | Current |
| Battery Power | 404369 | UINT16 | kW | Power |
| Energy Meter kwH | 405167 | UINT16 | kWh | Energy |
| Frequency | 404608 | UINT16 | Hz | Frequency |
| UPS Status | 400000 | BIT | - | Status |
| BatterySystem Temperature | 404367 | INT16 | degC | Temperature |
| UPS Serial Number:6 | 404145 | STRING | - | Identification |
| Time on battery | 404352 | UINT32 | - | General |
| Alarm Register | 400002 | INT16 | - | Status |
| Alarm Register | 400003 | INT16 | - | Status |
| Alarm Register | 400004 | INT16 | - | Status |

## Common Data Categories

- Power
- Current
- Status
- Voltage
- Frequency
- Temperature

## Typical Use Cases

- Commissioning new devices with a known-good register baseline
- Troubleshooting Modbus communication and addressing issues
- Building HMI dashboards for operational visibility
- Logging device telemetry for analysis and reporting

## Related Device Maps

- [Schneider Electric PM8000 Modbus Map](./pm8000.md)
- [Schneider Electric ION9000 Modbus Map](./ion9000.md)
- [Schneider Electric PM5000 / PM5100 / PM5300 Modbus Map](./pm5000-pm5100-pm5300.md)
- [All Schneider Electric Device Maps](../index.md)
- [All XPF Device Maps](../../index.md)

## Use This Device Map in Modbus Monitor XPF

Start using this device map in minutes - no manual register mapping required.

- [Download Modbus Monitor XPF Free Trial](https://www.modbusmonitor.com/download)
- [Compare Modbus Monitor XPF with Other Tools](https://www.modbusmonitor.com/compare)
- [Modbus Tester for Windows](https://www.modbusmonitor.com/modbus-tester)
