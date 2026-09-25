---
title: Fronius Inverter Common Modbus Register Map
description: Fronius Inverter Common Modbus map and register map with sample Modbus registers, register addresses, and power meter overview for engineers. Includes sample addresses and data types for review before use with Modbus Monitor XPF.
---

# Fronius Inverter Common Modbus Register Map

The Fronius Inverter Common is a power meter used for power monitoring, energy metering, and facility automation. This page provides a sample Modbus register map with addresses, data types, and signal categories to help engineers commission, troubleshoot, and monitor the device. For Fronius Inverter Common deployments, teams often use this map to surface power, voltage, and current data in facility metering, commissioning, and operational analytics.

This page shows a public register preview. Check the catalog in your installed XPF version for complete-map availability and licensing.

Confirm the exact model and firmware, address base, register function, word order, scaling and units against the manufacturer manual before polling. This preview does not establish hardware validation.

## Overview

- **Device:** Fronius Inverter Common
- **Type:** Power Meter
- **Protocol:** Confirm the supported transport for the exact device and firmware in the manufacturer manual.
- **Use case:** power monitoring, energy metering, and facility automation
- **Works with:** Modbus Monitor XPF (import directly)

## Download Modbus Map

The sample below is a public preview. Check the catalog in your installed XPF version for current availability, access and licensing.

- [Get Modbus Monitor XPF](https://www.modbusmonitor.com/download)

[Public JSON preview](https://modbus-monitor.github.io/modbus-device-maps/maps/fronius-inverter/common.json) · [Preview data terms](https://modbus-monitor.github.io/modbus-device-maps/data-license/)

## Register Table (Sample)

Sample registers from the Fronius Inverter Common Modbus map. Confirm the sample against the exact device and firmware before use.

| Signal | Address | Type | Units | Category |
|---|---:|---|---|---|
| AC voltage phase AB V | 440076 | UINT16 | V | Voltage |
| Total AC current A | 440071 | UINT16 | - | Current |
| AC in feed power W | 440083 | INT16 | kW | Power |
| Total fed-in energy Wh | 440093 | UINT32 | kWh | Energy |
| AC frequency Hz | 440085 | UINT16 | Hz | Frequency |
| Housing temperature C | 440102 | INT16 | degC | Temperature |
| Operating mode Bitmask | 440107 | UINT16 | - | General |
| AC current phase A A | 440072 | UINT16 | A | Current |
| AC current phase B A | 440073 | UINT16 | A | Current |
| AC current phase C A | 440074 | UINT16 | A | Current |
| Scale factor AC current SF | 440075 | INT16 | - | Current |
| AC voltage phase BC V | 440077 | UINT16 | V | Voltage |

## How to Use This Map

1. **Download Modbus Monitor XPF** — [Get the free version](https://www.modbusmonitor.com/download).
2. **Select the Fronius Inverter Common device map** — check availability and access in the installed application catalog.
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
- Temperature
- Frequency
- Energy

## Related Tools

- [Modbus Monitor XPF — Windows Modbus Tool](https://www.modbusmonitor.com/download)
- [Modbus HMI Builder](https://www.modbusmonitor.com/modbus-hmi)
- [Compare Modbus Monitor XPF with Other Tools](https://www.modbusmonitor.com/compare)

## Related Device Maps

- [Fronius Inverter 110,111.112,113 Modbus Register Map](./110-111-112-113.md)
- [All Fronius Inverter Modbus Register Maps](./index.md)
- [All XPF Device Maps](../../../../modbus-device-maps/index.md)

<!-- public-preview-metadata -->
<script type="application/ld+json">{"@context": "https://schema.org", "@type": "Dataset", "name": "Fronius Inverter Common public register preview", "description": "Sample register addresses and data types; not a complete map or hardware verification.", "url": "https://docs.quantumbitsolutions.com/products/xpf/device-maps/fronius-inverter/common/", "license": "https://modbus-monitor.github.io/modbus-device-maps/data-license/", "creator": {"@type": "Organization", "name": "Quantum Bit Solutions", "url": "https://quantumbitsolutions.com/"}, "distribution": {"@type": "DataDownload", "encodingFormat": "application/json", "contentUrl": "https://modbus-monitor.github.io/modbus-device-maps/maps/fronius-inverter/common.json"}}</script>
<!-- /public-preview-metadata -->
