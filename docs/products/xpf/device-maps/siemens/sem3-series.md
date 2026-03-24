---
title: Siemens SEM3 Series Modbus Map
description: Pre-built Siemens SEM3 Series Modbus map for Modbus Monitor XPF with register preview, device overview, and setup guidance.
---

# Siemens SEM3 Series Modbus Map

Use this pre-built Siemens SEM3 Series Modbus map in Modbus Monitor XPF to reduce setup time and start monitoring faster. This page provides a technical preview of the supported power meter map, common data categories, and typical use cases.

## Use This Device Map in Modbus Monitor XPF

- [Download Modbus Monitor XPF](https://www.modbusmonitor.com/download)
- [Compare Modbus Monitor XPF with Other Tools](https://www.modbusmonitor.com/compare)
- [Modbus Tester for Windows](https://www.modbusmonitor.com/modbus-tester)

## Quick Facts

- **Manufacturer:** Siemens
- **Model:** SEM3 Series
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

> This page shows a preview subset of the full device map available in Modbus Monitor XPF.

## Common Data Categories

- Current
- Power
- Status

## Typical Use Cases

- Commissioning new devices with a known-good register baseline
- Troubleshooting Modbus communication and addressing issues
- Building HMI dashboards for operational visibility
- Logging device telemetry for analysis and reporting

## Related Device Maps

- [Siemens PAC4200 Modbus Map](../sentron-pac-4200/)
- [Siemens PAC2200 Modbus Map](../sentron-pac-2200/)
- [Siemens SICAM P Modbus Map](../sicam-p/)
- [All Siemens Device Maps](../)

## Use This Device Map in Modbus Monitor XPF

- [Download Modbus Monitor XPF](https://www.modbusmonitor.com/download)
- [Compare Modbus Monitor XPF with Other Tools](https://www.modbusmonitor.com/compare)
- [Modbus Tester for Windows](https://www.modbusmonitor.com/modbus-tester)
