---
title: ABB Trio 50 / Trio 60 Modbus Map
description: Pre-built ABB Trio 50 / Trio 60 Modbus map for Modbus Monitor XPF with register preview, device overview, and setup guidance.
---

# ABB Trio 50 / Trio 60 Modbus Map

Use this pre-built ABB Trio 50 / Trio 60 Modbus map in Modbus Monitor XPF to reduce setup time and start monitoring faster. This page provides a technical preview of the supported solar inverter map, common data categories, and typical use cases.

## Use This Device Map in Modbus Monitor XPF

- [Download Modbus Monitor XPF](https://www.modbusmonitor.com/download)
- [Compare Modbus Monitor XPF with Other Tools](https://www.modbusmonitor.com/compare)
- [Modbus Tester for Windows](https://www.modbusmonitor.com/modbus-tester)

## Quick Facts

- **Manufacturer:** ABB
- **Model:** Trio 50 / Trio 60
- **Device Type:** Solar Inverter
- **Protocol:** Modbus
- **Typical Use:** PV production monitoring, inverter diagnostics, and energy analytics
- **Available in:** Modbus Monitor XPF

## Why This Map Matters

Instead of manually decoding registers and building your setup from scratch, Modbus Monitor XPF provides a pre-built device map to help engineers test, monitor, and visualize data faster.

See all [ABB device maps](../) to compare related models, and use [Compare Modbus Monitor XPF with Other Tools](https://www.modbusmonitor.com/compare) when evaluating fit across your stack.

## Register Preview

| Signal | Address | Type | Units | Category |
|---|---:|---|---|---|
| Inverter Grid Voltage V | 400304 | FLOAT32 | V | Voltage |
| Inverter Grid Current A | 400308 | FLOAT32 | - | Current |
| Dynamic Mode Power Factor Set Point Reactive Power expressed as fixed Power Factor | 400201 | FLOAT32 | PF | Power |
| Daily Energy Wh | 401071 | UINT32 | kWh | Energy |
| Mean Grid Frequency Hz | 401107 | FLOAT32 | Hz | Frequency |
| Global State | 401051 | UINT16 | - | Status |
| Internal Temperature C | 401121 | FLOAT32 | degC | Temperature |
| Remote On Off | 400181 | UINT16 | - | General |
| Accuracy Set unit for Modbus Data Addresses 0507 0508 0511 and 0512 or | 400502 | UINT16 | - | Communication |
| Set communication protocol for serial line RS485 1 | 401007 | UINT16 | - | Identification |
| Permanent Mode Power Factor Set Point Reactive Power expressed as fixed Power Factor | 400203 | FLOAT32 | PF | Power |
| Dynamic Mode Active Power Set Point Active Power Curtailment expressed as percentage of Nominal Power in steps | 400211 | UINT16 | kW | Power |

> This page shows a preview subset of the full device map available in Modbus Monitor XPF.

## Common Data Categories

- Power
- Status
- Current
- Energy
- Voltage
- Temperature

## Typical Use Cases

- Commissioning new devices with a known-good register baseline
- Troubleshooting Modbus communication and addressing issues
- Building HMI dashboards for operational visibility
- Logging device telemetry for analysis and reporting

## Related Device Maps

- [ABB M4M Modbus Map](../m4m/)
- [ABB B23 / B24 Modbus Map](../b23-b24/)
- [ABB A41 / A42 Modbus Map](../a41-a42/)
- [All ABB Device Maps](../)

## Use This Device Map in Modbus Monitor XPF

- [Download Modbus Monitor XPF](https://www.modbusmonitor.com/download)
- [Compare Modbus Monitor XPF with Other Tools](https://www.modbusmonitor.com/compare)
- [Modbus Tester for Windows](https://www.modbusmonitor.com/modbus-tester)
