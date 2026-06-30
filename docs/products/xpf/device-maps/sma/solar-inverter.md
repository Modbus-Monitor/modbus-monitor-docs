---
title: SMA Solar Inverter Modbus Register Map
description: SMA Solar Inverter Modbus map and register map with sample Modbus registers, register addresses, and power meter overview for engineers. Works with Modbus Monitor XPF (import directly) and includes downloadable CSV access in-app.
---

# SMA Solar Inverter Modbus Register Map

The SMA Solar Inverter is a power meter used for power monitoring, energy metering, and facility automation. This page provides a sample Modbus register map with addresses, data types, and signal categories to help engineers commission, troubleshoot, and monitor the device. For SMA Solar Inverter deployments, teams often use this map to surface power, voltage, and current data in facility metering, commissioning, and operational analytics.

This page shows a preview subset of the full device map available in Modbus Monitor XPF.

Engineers searching for SMA Solar Inverter Modbus map, SMA Solar Inverter register map, or SMA Solar Inverter Modbus registers can use this page as a compatibility snapshot before importing the full map into Modbus Monitor XPF.

## Overview

- **Device:** SMA Solar Inverter
- **Type:** Power Meter
- **Protocol:** Modbus RTU / Modbus TCP
- **Use case:** power monitoring, energy metering, and facility automation
- **Works with:** Modbus Monitor XPF (import directly)

## Download Modbus Map

The full SMA Solar Inverter Modbus register map is available inside Modbus Monitor XPF as a pre-built device map. Download the free feature-locked version to access and export the complete map.

- [Download Modbus Monitor XPF Free](https://www.modbusmonitor.com/download)

## Register Table (Sample)

Sample registers from the SMA Solar Inverter Modbus map. Import the full map in Modbus Monitor XPF to access all registers.

| Signal | Address | Type | Units | Category |
|---|---:|---|---|---|
| Grid voltage phase L1 Metering GridMs PhV phsA V | 431252 | UINT32 | V | Voltage |
| Current charging power CmpBMS GetBatChaWh Wh | 432200 | INT64U | kWh | Current |
| External active power setpoint specification fallback value for active power setpoint specification Inverter WModCfg WCtlComCfg FlbWSpt W | 441214 | INT32 | kW | Power |
| Charge energy CmpBMS BatChaWh Wh | 441362 | UINT32 | kWh | Energy |
| Grid frequency Metering GridMs Hz Hz | 431446 | UINT32 | Hz | Frequency |
| Nominal cos phi PFMinQ1 Inverter PFMinQ1 0 to 1 | 444408 | UINT32 | - | Power Factor |
| Operating mode of multifunction relay MltFncSw OpMode 258 Switching status grid relay GriSwCpy | 440574 | UINT32 | - | Status |
| Ambient temperature Env TmpVal degC | 434608 | INT32 | degC | Temperature |
| Control of battery charging via communication available Bat ChaCtlComAval 1129 Yes Yes | 431060 | UINT32 | - | Communication |
| Battery charge BatChrg BatChrg Wh | 431396 | INT64U | kWh | General |
| Standard Daylight saving time conversion on DtTm DlSvIsOn 1129 Yes Yes | 440004 | UINT32 | - | Identification |
| Discharge energy CmpBMS BatDschWh Wh | 441364 | UINT32 | kWh | Energy |

## How to Use This Map

1. **Download Modbus Monitor XPF** — [Get the free version](https://www.modbusmonitor.com/download).
2. **Select the SMA Solar Inverter device map** — pre-built maps are bundled and ready to load.
3. **Connect to your device** — enter the device IP or COM port and start polling registers immediately.
4. **Visualise and log** — build dashboards, trend data, and export readings without manual register entry.

## Why Use Pre-Built Maps

- **Saves time** — no need to manually look up or enter register addresses
- **Reduces errors** — pre-validated maps eliminate mis-typed addresses and wrong data types
- **Speeds commissioning** — connect and poll within minutes instead of hours
- **Reusable across projects** — use the same map across multiple sites and installations

## Data Categories Available

- Power
- Voltage
- Current
- Frequency
- Power Factor
- Temperature

## Related Tools

- [Modbus Monitor XPF — Windows Modbus Tool](https://www.modbusmonitor.com/download)
- [Modbus HMI Builder](https://www.modbusmonitor.com/modbus-hmi)
- [Compare Modbus Monitor XPF with Other Tools](https://www.modbusmonitor.com/compare)

## Related Device Maps

- [All SMA Modbus Register Maps](../index.md)
- [All XPF Device Maps](../../../../modbus-device-maps/index.md)
