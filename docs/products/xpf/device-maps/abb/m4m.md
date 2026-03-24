---
title: ABB M4M Modbus Map
description: Pre-built ABB M4M Modbus map for Modbus Monitor XPF with register preview, device overview, and setup guidance.
---

# ABB M4M Modbus Map

Use this pre-built ABB M4M Modbus map in Modbus Monitor XPF to reduce setup time and start monitoring faster. This page provides a technical preview of the supported power meter map, common data categories, and typical use cases.

## Use This Device Map in Modbus Monitor XPF

- [Download Modbus Monitor XPF](https://www.modbusmonitor.com/download)
- [Compare Modbus Monitor XPF with Other Tools](https://www.modbusmonitor.com/compare)
- [Modbus Tester for Windows](https://www.modbusmonitor.com/modbus-tester)

## Quick Facts

- **Manufacturer:** ABB
- **Model:** M4M
- **Device Type:** Power Meter
- **Protocol:** Modbus
- **Typical Use:** power monitoring, energy metering, and facility automation
- **Available in:** Modbus Monitor XPF

## Why This Map Matters

Instead of manually decoding registers and building your setup from scratch, Modbus Monitor XPF provides a pre-built device map to help engineers test, monitor, and visualize data faster.

See all [ABB device maps](../) to compare related models, and use [Compare Modbus Monitor XPF with Other Tools](https://www.modbusmonitor.com/compare) when evaluating fit across your stack.

## Register Preview

| Signal | Address | Type | Units | Category |
|---|---:|---|---|---|
| Energy Trend Data block 1 0 | 433552 | UINT16 | kWh | Energy |
| Max Min Demand Data block 1 0 | 436738 | UINT16 | kW | Demand |
| Alarm number | 435936 | UINT16 | - | Status |
| Entry number | 432769 | UINT16 | - | General |
| I O port 1 | 435852 | UINT16 | - | Communication |
| Energy Trend Data block 1 1 | 433553 | UINT16 | kWh | Energy |
| Energy Trend Data block 1 2 | 433554 | UINT16 | kWh | Energy |
| Energy Trend Data block 1 3 | 433555 | UINT16 | kWh | Energy |
| Energy Trend Data block 1 4 | 433556 | UINT16 | kWh | Energy |
| Energy Trend Data block 1 5 | 433557 | UINT16 | kWh | Energy |
| Energy Trend Data block 1 6 | 433558 | UINT16 | kWh | Energy |
| Energy Trend Data block 1 7 | 433559 | UINT16 | kWh | Energy |

> This page shows a preview subset of the full device map available in Modbus Monitor XPF.

## Common Data Categories

- Demand
- Energy
- Status

## Typical Use Cases

- Commissioning new devices with a known-good register baseline
- Troubleshooting Modbus communication and addressing issues
- Building HMI dashboards for operational visibility
- Logging device telemetry for analysis and reporting

## Related Device Maps

- [ABB B23 / B24 Modbus Map](../b23-b24/)
- [ABB A41 / A42 Modbus Map](../a41-a42/)
- [ABB Trio 50 / Trio 60 Modbus Map](../trio-50-trio-60/)
- [All ABB Device Maps](../)

## Use This Device Map in Modbus Monitor XPF

- [Download Modbus Monitor XPF](https://www.modbusmonitor.com/download)
- [Compare Modbus Monitor XPF with Other Tools](https://www.modbusmonitor.com/compare)
- [Modbus Tester for Windows](https://www.modbusmonitor.com/modbus-tester)
