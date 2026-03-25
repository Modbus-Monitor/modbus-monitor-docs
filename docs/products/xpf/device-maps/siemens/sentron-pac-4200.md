---
title: Siemens PAC4200 Modbus Map
description: Pre-built Siemens PAC4200 Modbus map for Modbus Monitor XPF with register preview, device overview, and setup guidance.
---

# Siemens PAC4200 Modbus Map

This Siemens PAC4200 Modbus map is supported in Modbus Monitor XPF, allowing engineers to quickly test, monitor, and visualize device data without manual register mapping.

This page shows a preview subset of the full device map available in Modbus Monitor XPF.

It is commonly used in power monitoring, energy metering, and facility automation.

## Use This Device Map in Modbus Monitor XPF

- [Download Modbus Monitor XPF](https://www.modbusmonitor.com/download)
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

See all [Siemens device maps](../) to compare related models, and use [Compare Modbus Monitor XPF with Other Tools](https://www.modbusmonitor.com/compare) when evaluating fit across your stack.

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

- [Siemens PAC2200 Modbus Map](../sentron-pac-2200/)
- [Siemens SICAM P Modbus Map](../sicam-p/)
- [Siemens SEM3 Series Modbus Map](../sem3-series/)
- [All Siemens Device Maps](../)

## Use This Device Map in Modbus Monitor XPF

- [Download Modbus Monitor XPF](https://www.modbusmonitor.com/download)
- [Compare Modbus Monitor XPF with Other Tools](https://www.modbusmonitor.com/compare)
- [Modbus Tester for Windows](https://www.modbusmonitor.com/modbus-tester)
