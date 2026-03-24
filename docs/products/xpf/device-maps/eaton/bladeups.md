---
title: Eaton BladeUPS Modbus Map
description: Pre-built Eaton BladeUPS Modbus map for Modbus Monitor XPF with register preview, device overview, and setup guidance.
---

# Eaton BladeUPS Modbus Map

Use this pre-built Eaton BladeUPS Modbus map in Modbus Monitor XPF to reduce setup time and start monitoring faster. This page provides a technical preview of the supported ups map, common data categories, and typical use cases.

## Use This Device Map in Modbus Monitor XPF

- [Download Modbus Monitor XPF](https://www.modbusmonitor.com/download)
- [Compare Modbus Monitor XPF with Other Tools](https://www.modbusmonitor.com/compare)
- [Modbus Tester for Windows](https://www.modbusmonitor.com/modbus-tester)

## Quick Facts

- **Manufacturer:** Eaton
- **Model:** BladeUPS
- **Device Type:** UPS
- **Protocol:** Modbus
- **Typical Use:** power continuity monitoring, alarm review, and resilience planning
- **Available in:** Modbus Monitor XPF

## Why This Map Matters

Instead of manually decoding registers and building your setup from scratch, Modbus Monitor XPF provides a pre-built device map to help engineers test, monitor, and visualize data faster.

See all [Eaton device maps](../) to compare related models, and use [Compare Modbus Monitor XPF with Other Tools](https://www.modbusmonitor.com/compare) when evaluating fit across your stack.

## Register Preview

| Signal | Address | Type | Units | Category |
|---|---:|---|---|---|
| Nominal Input Voltage iDeviceVoltsInRatingValue | 301358 | UINT32 | V | Voltage |
| Output Current Rating iDeviceAmpsRatingValue | 301811 | UINT16 | A | Current |
| Power Strategy sPowerStrategyValue | 303004 | UINT16 | kW | Power |
| Output KW Hours mOutputKWHourValue | 307003 | FLOAT32 | kWh | Energy |
| Nominal Input Frequency iNominalInputFrequencyValue | 301670 | UINT16 | Hz | Frequency |
| Min Battery Capacity for Return iMinBattCapforReturnValue | 318490 | UINT16 | - | Power Factor |
| Low Runtime Alarm Setpoint iLowRuntimeSetpointValue | 301676 | UINT16 | - | Status |
| Ambient Temperature mTempAmbientValue | 312001 | FLOAT32 | degC | Temperature |
| Vendor Name VendorNameValue:32 | 301033 | STRING | - | Identification |
| Device Type iDeviceTypeValue:32 | 301129 | STRING | - | General |
| Nominal Output Voltage iDeviceVoltsOutRatingValue | 301360 | UINT32 | V | Voltage |
| Nominal Output Frequency iNominalOutputFrequencyValue | 301671 | UINT16 | Hz | Frequency |

> This page shows a preview subset of the full device map available in Modbus Monitor XPF.

## Common Data Categories

- Voltage
- Status
- Power
- Frequency
- Current
- Temperature

## Typical Use Cases

- Commissioning new devices with a known-good register baseline
- Troubleshooting Modbus communication and addressing issues
- Building HMI dashboards for operational visibility
- Logging device telemetry for analysis and reporting

## Related Device Maps

- [Eaton 93PM Modbus Map](../93pm/)
- [Eaton PXM2000 Modbus Map](../pxm2000/)
- [All Eaton Device Maps](../)

## Use This Device Map in Modbus Monitor XPF

- [Download Modbus Monitor XPF](https://www.modbusmonitor.com/download)
- [Compare Modbus Monitor XPF with Other Tools](https://www.modbusmonitor.com/compare)
- [Modbus Tester for Windows](https://www.modbusmonitor.com/modbus-tester)
