---
title: Siemens PAC2200 Modbus Map
description: Pre-built Siemens PAC2200 Modbus map for Modbus Monitor XPF with register preview, device overview, and setup guidance.
---

# Siemens PAC2200 Modbus Map

Use this pre-built Siemens PAC2200 Modbus map in Modbus Monitor XPF to reduce setup time and start monitoring faster. This page provides a technical preview of the supported power meter map, common data categories, and typical use cases.

## Use This Device Map in Modbus Monitor XPF

- [Download Modbus Monitor XPF](https://www.modbusmonitor.com/download)
- [Compare Modbus Monitor XPF with Other Tools](https://www.modbusmonitor.com/compare)
- [Modbus Tester for Windows](https://www.modbusmonitor.com/modbus-tester)

## Quick Facts

- **Manufacturer:** Siemens
- **Model:** PAC2200
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
| Voltage UL1 N | 400002 | FLOAT32 | V | Voltage |
| Current L1 | 400014 | FLOAT32 | A | Current |
| Apparent power L1 | 400020 | FLOAT32 | kW | Power |
| Secondary total of active energy im port | 400962 | DOUBLE64 | kWh | Energy |
| Frequency | 400056 | FLOAT32 | Hz | Frequency |
| Device diagnostics and device status | 400206 | UINT32 | - | Status |
| Active tariff | 400212 | UINT32 | - | General |
| Voltage UL2 N | 400004 | FLOAT32 | V | Voltage |
| Voltage UL3 N | 400006 | FLOAT32 | V | Voltage |
| Voltage UL1 L2 | 400008 | FLOAT32 | V | Voltage |
| Voltage UL2 L3 | 400010 | FLOAT32 | V | Voltage |
| Voltage UL3 L1 | 400012 | FLOAT32 | V | Voltage |

> This page shows a preview subset of the full device map available in Modbus Monitor XPF.

## Common Data Categories

- Power
- Current
- Voltage
- Energy
- Status
- Frequency

## Typical Use Cases

- Commissioning new devices with a known-good register baseline
- Troubleshooting Modbus communication and addressing issues
- Building HMI dashboards for operational visibility
- Logging device telemetry for analysis and reporting

## Related Device Maps

- [Siemens PAC4200 Modbus Map](../sentron-pac-4200/)
- [Siemens SICAM P Modbus Map](../sicam-p/)
- [Siemens SEM3 Series Modbus Map](../sem3-series/)
- [All Siemens Device Maps](../)

## Use This Device Map in Modbus Monitor XPF

- [Download Modbus Monitor XPF](https://www.modbusmonitor.com/download)
- [Compare Modbus Monitor XPF with Other Tools](https://www.modbusmonitor.com/compare)
- [Modbus Tester for Windows](https://www.modbusmonitor.com/modbus-tester)
