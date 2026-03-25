---
title: SolarEdge SE5K / SE7K / SE10K / SE12.5K Modbus Map
description: Pre-built SolarEdge SE5K / SE7K / SE10K / SE12.5K Modbus map for Modbus Monitor XPF with register preview, device overview, and setup guidance.
---

# SolarEdge SE5K / SE7K / SE10K / SE12.5K Modbus Map

This SolarEdge SE5K / SE7K / SE10K / SE12.5K Modbus map is supported in Modbus Monitor XPF, allowing engineers to quickly test, monitor, and visualize device data without manual register mapping.

This page shows a preview subset of the full device map available in Modbus Monitor XPF.

For SolarEdge SE5K / SE7K / SE10K / SE12.5K deployments, teams often use this map to surface voltage, current, and power data in solar inverter monitoring and renewable energy systems.

## Use This Device Map in Modbus Monitor XPF

Start using this device map in minutes - no manual register mapping required.

- [Download Modbus Monitor XPF Free Trial](https://www.modbusmonitor.com/download)
- [Compare Modbus Monitor XPF with Other Tools](https://www.modbusmonitor.com/compare)
- [Modbus Tester for Windows](https://www.modbusmonitor.com/modbus-tester)

## Quick Facts

- **Manufacturer:** SolarEdge
- **Model:** SE5K / SE7K / SE10K / SE12.5K
- **Device Type:** Solar Inverter
- **Protocol:** Modbus
- **Typical Use:** PV production monitoring, inverter diagnostics, and energy analytics
- **Available in:** Modbus Monitor XPF

## Why This Map Matters

Instead of manually decoding registers and building your setup from scratch, Modbus Monitor XPF provides a pre-built device map to help engineers test, monitor, and visualize data faster.

Browse all [XPF device maps](../../index.md) for the full library, explore [SolarEdge device maps](../index.md) to compare related models, and use [Compare Modbus Monitor XPF with Other Tools](https://www.modbusmonitor.com/compare) when evaluating fit across your stack.

## Register Preview

| Signal | Address | Type | Units | Category |
|---|---:|---|---|---|
| I AC VoltageAB | 440077 | UINT16 | V | Voltage |
| I AC Current | 440072 | UINT16 | - | Current |
| I AC Power | 440084 | INT16 | kW | Power |
| I AC Energy WH | 440094 | UINT32 | kWh | Energy |
| I AC Frequency | 440086 | UINT16 | Hz | Frequency |
| I AC PF1 | 440092 | INT16 | - | Power Factor |
| I Status | 440108 | UINT16 | - | Status |
| I Temp Sink | 440104 | INT16 | - | Temperature |
| C SunSpec ID | 440001 | UINT32 | - | General |
| C Model:16 | 440021 | STRING | - | Identification |
| M Exported | 440227 | UINT32 | - | Communication |
| I AC CurrentA | 440073 | UINT16 | - | Current |

## Common Data Categories

- Voltage
- Current
- Power
- Power Factor
- Energy
- Status

## Typical Use Cases

- Commissioning new devices with a known-good register baseline
- Troubleshooting Modbus communication and addressing issues
- Building HMI dashboards for operational visibility
- Logging device telemetry for analysis and reporting

## Related Device Maps

- [SolarEdge SE5000 Modbus Map](./se5000.md)
- [SolarEdge SE3000H Modbus Map](./se3000h.md)
- [All SolarEdge Device Maps](../index.md)
- [All XPF Device Maps](../../index.md)

## Use This Device Map in Modbus Monitor XPF

Start using this device map in minutes - no manual register mapping required.

- [Download Modbus Monitor XPF Free Trial](https://www.modbusmonitor.com/download)
- [Compare Modbus Monitor XPF with Other Tools](https://www.modbusmonitor.com/compare)
- [Modbus Tester for Windows](https://www.modbusmonitor.com/modbus-tester)
