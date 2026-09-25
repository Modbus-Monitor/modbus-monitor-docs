---
title: Huawei SmartLogger Modbus Register Map
description: Huawei SmartLogger Modbus map and register map with sample Modbus registers, register addresses, and solar inverter overview for engineers. Includes sample addresses and data types for review before use with Modbus Monitor XPF.
---

# Huawei SmartLogger Modbus Register Map

The Huawei SmartLogger is a solar inverter used for PV production monitoring, inverter diagnostics, and energy analytics. This page provides a sample Modbus register map with addresses, data types, and signal categories to help engineers commission, troubleshoot, and monitor the device. For Huawei SmartLogger deployments, teams often use this map to surface power, status, and current data in solar inverter monitoring and renewable energy systems.

This page shows a public register preview. Check the catalog in your installed XPF version for complete-map availability and licensing.

Confirm the exact model and firmware, address base, register function, word order, scaling and units against the manufacturer manual before polling. This preview does not establish hardware validation.

## Overview

- **Device:** Huawei SmartLogger
- **Type:** Solar Inverter
- **Protocol:** Confirm the supported transport for the exact device and firmware in the manufacturer manual.
- **Use case:** PV production monitoring, inverter diagnostics, and energy analytics
- **Works with:** Modbus Monitor XPF (import directly)

## Download Modbus Map

The sample below is a public preview. Check the catalog in your installed XPF version for current availability, access and licensing.

- [Get Modbus Monitor XPF](https://www.modbusmonitor.com/download)

[Public JSON preview](https://modbus-monitor.github.io/modbus-device-maps/maps/huawei/smartlogger.json) · [Preview data terms](https://modbus-monitor.github.io/modbus-device-maps/data-license/)

## Register Table (Sample)

Sample registers from the Huawei SmartLogger Modbus map. Confirm the sample against the exact device and firmware before use.

| Signal | Address | Type | Units | Category |
|---|---:|---|---|---|
| Grid A phase voltage | 432260 | INT32 | V | Voltage |
| Grid A phase current | 432272 | INT32 | - | Current |
| Grid-tied Active Power | 432278 | INT32 | kW | Power |
| Energy Yield Daily | 440562 | UINT32 | kWh | Energy |
| ESS Battery Status | 437000 | UINT16 | - | Status |
| Battery1 Inv3 Temperature | 437022 | UINT16 | degC | Temperature |
| Solar Producion Now | 440521 | INT32 | - | General |
| Conversion coefficient | 441940 | UINT32 | - | Identification |
| Communication abnormal shutdown | 441947 | UINT16 | - | Communication |
| Battery Inv3 Charge/Discharge Power | 437765 | INT32 | kW | Power |
| Grid B Phase current | 432274 | INT32 | - | Current |
| Grid C Phase Current | 432276 | INT32 | - | Current |

## How to Use This Map

1. **Download Modbus Monitor XPF** — [Get the free version](https://www.modbusmonitor.com/download).
2. **Select the Huawei SmartLogger device map** — check availability and access in the installed application catalog.
3. **Connect to your device** — confirm transport, addressing and data types before starting a read operation.
4. **Visualise and log** — build dashboards, trend data, and export readings without manual register entry.

## Why Use Pre-Built Maps

- **Saves time** — no need to manually look up or enter register addresses
- **Reduces errors** — reusable maps reduce repeated manual entry; validate addresses and data types for your device
- **Speeds commissioning** — connect and poll within minutes instead of hours
- **Reusable across projects** — use the same map across multiple sites and installations

## Data Categories Available

- Power
- Status
- Current
- Energy
- Voltage
- Temperature

## Related Tools

- [Modbus Monitor XPF — Windows Modbus Tool](https://www.modbusmonitor.com/download)
- [Modbus HMI Builder](https://www.modbusmonitor.com/modbus-hmi)
- [Compare Modbus Monitor XPF with Other Tools](https://www.modbusmonitor.com/compare)

## Related Device Maps

- [Huawei Sun2000 Modbus Register Map](./sun2000.md)
- [Huawei Solar Inverter Modbus Register Map](./solar-inverter.md)
- [Huawei Sun2000 -env Modbus Register Map](./sun2000-env.md)
- [All Huawei Modbus Register Maps](./index.md)
- [All XPF Device Maps](../../../../modbus-device-maps/index.md)

<!-- public-preview-metadata -->
<script type="application/ld+json">{"@context": "https://schema.org", "@type": "Dataset", "name": "Huawei SmartLogger public register preview", "description": "Sample register addresses and data types; not a complete map or hardware verification.", "url": "https://docs.quantumbitsolutions.com/products/xpf/device-maps/huawei/smartlogger/", "license": "https://modbus-monitor.github.io/modbus-device-maps/data-license/", "creator": {"@type": "Organization", "name": "Quantum Bit Solutions", "url": "https://quantumbitsolutions.com/"}, "distribution": {"@type": "DataDownload", "encodingFormat": "application/json", "contentUrl": "https://modbus-monitor.github.io/modbus-device-maps/maps/huawei/smartlogger.json"}}</script>
<!-- /public-preview-metadata -->
