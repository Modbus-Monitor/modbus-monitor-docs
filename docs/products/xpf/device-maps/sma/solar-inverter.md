---
title: SMA Solar Inverter Modbus Register Map
description: SMA Solar Inverter Modbus map and register map with sample Modbus registers, register addresses, and power meter overview for engineers. Includes sample addresses and data types for review before use with Modbus Monitor XPF.
---

# SMA Solar Inverter Modbus Register Map

The SMA Solar Inverter is a power meter used for power monitoring, energy metering, and facility automation. This page provides a sample Modbus register map with addresses, data types, and signal categories to help engineers commission, troubleshoot, and monitor the device. For SMA Solar Inverter deployments, teams often use this map to surface power, voltage, and current data in facility metering, commissioning, and operational analytics.

This page shows a public register preview. Check the catalog in your installed XPF version for complete-map availability and licensing.

Confirm the exact model and firmware, address base, register function, word order, scaling and units against the manufacturer manual before polling. This preview does not establish hardware validation.

## Overview

- **Device:** SMA Solar Inverter
- **Type:** Power Meter
- **Protocol:** Confirm the supported transport for the exact device and firmware in the manufacturer manual.
- **Use case:** power monitoring, energy metering, and facility automation
- **Works with:** Modbus Monitor XPF (import directly)

## Download Modbus Map

The sample below is a public preview. Check the catalog in your installed XPF version for current availability, access and licensing.

- [Get Modbus Monitor XPF](https://www.modbusmonitor.com/download)

[Public JSON preview](https://modbus-monitor.github.io/modbus-device-maps/maps/sma/solar-inverter.json) · [Preview data terms](https://modbus-monitor.github.io/modbus-device-maps/data-license/)

## Register Table (Sample)

Sample registers from the SMA Solar Inverter Modbus map. Confirm the sample against the exact device and firmware before use.

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
2. **Select the SMA Solar Inverter device map** — check availability and access in the installed application catalog.
3. **Connect to your device** — confirm transport, addressing and data types before starting a read operation.
4. **Visualise and log** — build dashboards, trend data, and export readings without manual register entry.

## Why Use Pre-Built Maps

- **Saves time** — no need to manually look up or enter register addresses
- **Reduces errors** — reusable maps reduce repeated manual entry; validate addresses and data types for your device
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

- [All SMA Modbus Register Maps](./index.md)
- [All XPF Device Maps](../../../../modbus-device-maps/index.md)

<!-- public-preview-metadata -->
<script type="application/ld+json">{"@context": "https://schema.org", "@type": "Dataset", "name": "SMA Solar Inverter public register preview", "description": "Sample register addresses and data types; not a complete map or hardware verification.", "url": "https://docs.quantumbitsolutions.com/products/xpf/device-maps/sma/solar-inverter/", "license": "https://modbus-monitor.github.io/modbus-device-maps/data-license/", "creator": {"@type": "Organization", "name": "Quantum Bit Solutions", "url": "https://quantumbitsolutions.com/"}, "distribution": {"@type": "DataDownload", "encodingFormat": "application/json", "contentUrl": "https://modbus-monitor.github.io/modbus-device-maps/maps/sma/solar-inverter.json"}}</script>
<!-- /public-preview-metadata -->
