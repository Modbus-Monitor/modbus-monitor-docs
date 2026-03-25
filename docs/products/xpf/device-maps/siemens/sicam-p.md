---
title: Siemens SICAM P Modbus Map
description: Pre-built Siemens SICAM P Modbus map for Modbus Monitor XPF with register preview, device overview, and setup guidance.
---

# Siemens SICAM P Modbus Map

This Siemens SICAM P Modbus map is supported in Modbus Monitor XPF, allowing engineers to quickly test, monitor, and visualize device data without manual register mapping.

This page shows a preview subset of the full device map available in Modbus Monitor XPF.

For Siemens SICAM P deployments, teams often use this map to surface harmonics, power factor, and status data in industrial automation panels and building management systems.

## Use This Device Map in Modbus Monitor XPF

Start using this device map in minutes - no manual register mapping required.

- [Download Modbus Monitor XPF Free Trial](https://www.modbusmonitor.com/download)
- [Compare Modbus Monitor XPF with Other Tools](https://www.modbusmonitor.com/compare)
- [Modbus Tester for Windows](https://www.modbusmonitor.com/modbus-tester)

## Quick Facts

- **Manufacturer:** Siemens
- **Model:** SICAM P
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

## Common Data Categories

- Harmonics
- Power Factor
- Status

## Typical Use Cases

- Commissioning new devices with a known-good register baseline
- Troubleshooting Modbus communication and addressing issues
- Building HMI dashboards for operational visibility
- Logging device telemetry for analysis and reporting

## Related Device Maps

- [Siemens PAC4200 Modbus Map](./sentron-pac-4200.md)
- [Siemens PAC2200 Modbus Map](./sentron-pac-2200.md)
- [Siemens SEM3 Series Modbus Map](./sem3-series.md)
- [All Siemens Device Maps](../index.md)
- [All XPF Device Maps](../../index.md)

## Use This Device Map in Modbus Monitor XPF

Start using this device map in minutes - no manual register mapping required.

- [Download Modbus Monitor XPF Free Trial](https://www.modbusmonitor.com/download)
- [Compare Modbus Monitor XPF with Other Tools](https://www.modbusmonitor.com/compare)
- [Modbus Tester for Windows](https://www.modbusmonitor.com/modbus-tester)
