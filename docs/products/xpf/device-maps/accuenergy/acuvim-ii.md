---
title: Accuenergy Acuvim II Modbus Map
description: Pre-built Accuenergy Acuvim II Modbus map for Modbus Monitor XPF with register preview, device overview, and setup guidance.
---

# Accuenergy Acuvim II Modbus Map

This Accuenergy Acuvim II Modbus map is supported in Modbus Monitor XPF, allowing engineers to quickly test, monitor, and visualize device data without manual register mapping.

This page shows a preview subset of the full device map available in Modbus Monitor XPF.

It is commonly used in power monitoring, energy metering, and facility automation.

## Use This Device Map in Modbus Monitor XPF

- [Download Modbus Monitor XPF](https://www.modbusmonitor.com/download)
- [Compare Modbus Monitor XPF with Other Tools](https://www.modbusmonitor.com/compare)
- [Modbus Tester for Windows](https://www.modbusmonitor.com/modbus-tester)

## Quick Facts

- **Manufacturer:** Accuenergy
- **Model:** Acuvim II
- **Device Type:** Power Meter
- **Protocol:** Modbus
- **Typical Use:** power monitoring, energy metering, and facility automation
- **Available in:** Modbus Monitor XPF

## Why This Map Matters

Instead of manually decoding registers and building your setup from scratch, Modbus Monitor XPF provides a pre-built device map to help engineers test, monitor, and visualize data faster.

See all [Accuenergy device maps](../) to compare related models, and use [Compare Modbus Monitor XPF with Other Tools](https://www.modbusmonitor.com/compare) when evaluating fit across your stack.

## Register Preview

| Signal | Address | Type | Units | Category |
|---|---:|---|---|---|
| Voltage Input Wiring Type 0 3LN 1 1LN 2 2LL 3 3LL 4 1LL | 404100 | UINT16 | V | Voltage |
| Current Input Wiring Type 0 3CT 1 1CT 2 2CT | 404101 | UINT16 | - | Current |
| Reactive Power Calculation Method 0 True Reactive Power 1 Generic Reactive Power | 404121 | UINT16 | kW | Power |
| kWh Pulse Constant 1 60000 | 404107 | UINT16 | kWh | Energy |
| Frequency Selection 0 50Hz 1 60Hz | 404094 | UINT16 | Hz | Frequency |
| VAR PF Convention 0 IEC 1 IEEE | 404118 | UINT16 | - | Power Factor |
| Demand Interval 1 30 | 404110 | UINT16 | kW | Demand |
| Seal Status 0x0A Sealed Other Unsealed | 404128 | UINT16 | - | Status |
| THD V1 V12 THD Rx 100 | 416475 | INT16 | - | Harmonics |
| Channel 1 Communication Protocol 0 Modbus 2 BACnet MS TP | 404095 | UINT16 | - | Communication |
| Channel 1 Parity 0 Even 1 Odd 2 None2 3 None1 | 404096 | UINT16 | - | General |
| kvarh Pulse Constant 1 60000 | 404108 | UINT16 | kWh | Energy |

## Common Data Categories

- Power
- Energy
- Current
- Voltage
- Harmonics
- Status

## Typical Use Cases

- Commissioning new devices with a known-good register baseline
- Troubleshooting Modbus communication and addressing issues
- Building HMI dashboards for operational visibility
- Logging device telemetry for analysis and reporting

## Related Device Maps

- [All Accuenergy Device Maps](../)

## Use This Device Map in Modbus Monitor XPF

- [Download Modbus Monitor XPF](https://www.modbusmonitor.com/download)
- [Compare Modbus Monitor XPF with Other Tools](https://www.modbusmonitor.com/compare)
- [Modbus Tester for Windows](https://www.modbusmonitor.com/modbus-tester)
