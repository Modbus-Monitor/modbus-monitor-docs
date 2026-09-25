---
title: Schneider Electric Symmetra PX Modbus Register Map
description: Schneider Electric Symmetra PX Modbus map and register map with sample Modbus registers, register addresses, and ups overview for engineers. Includes sample addresses and data types for review before use with Modbus Monitor XPF.
---

# Schneider Electric Symmetra PX Modbus Register Map

The Schneider Electric Symmetra PX is a ups used for power continuity monitoring, alarm review, and resilience planning. This page provides a sample Modbus register map with addresses, data types, and signal categories to help engineers commission, troubleshoot, and monitor the device. For Schneider Electric Symmetra PX deployments, teams often use this map to surface power, current, and status data in data centers, switchgear lineups, and advanced power monitoring projects.

This page shows a public register preview. Check the catalog in your installed XPF version for complete-map availability and licensing.

Confirm the exact model and firmware, address base, register function, word order, scaling and units against the manufacturer manual before polling. This preview does not establish hardware validation.

## Overview

- **Device:** Schneider Electric Symmetra PX
- **Type:** UPS
- **Protocol:** Confirm the supported transport for the exact device and firmware in the manufacturer manual.
- **Use case:** power continuity monitoring, alarm review, and resilience planning
- **Works with:** Modbus Monitor XPF (import directly)

## Download Modbus Map

The sample below is a public preview. Check the catalog in your installed XPF version for current availability, access and licensing.

- [Get Modbus Monitor XPF](https://www.modbusmonitor.com/download)

[Public JSON preview](https://modbus-monitor.github.io/modbus-device-maps/maps/schneider-electric/symmetra-px.json) · [Preview data terms](https://modbus-monitor.github.io/modbus-device-maps/data-license/)

## Register Table (Sample)

Sample registers from the Schneider Electric Symmetra PX Modbus map. Confirm the sample against the exact device and firmware before use.

| Signal | Address | Type | Units | Category |
|---|---:|---|---|---|
| Battery Voltage | 404359 | UINT16 | V | Voltage |
| Battery Current | 404361 | UINT16 | - | Current |
| Battery Power | 404369 | UINT16 | kW | Power |
| Energy Meter kwH | 405167 | UINT16 | kWh | Energy |
| Frequency | 404608 | UINT16 | Hz | Frequency |
| UPS Status | 400000 | BIT | - | Status |
| BatterySystem Temperature | 404367 | INT16 | degC | Temperature |
| UPS Serial Number:6 | 404145 | STRING | - | Identification |
| Time on battery | 404352 | UINT32 | - | General |
| Alarm Register | 400002 | INT16 | - | Status |
| Alarm Register | 400003 | INT16 | - | Status |
| Alarm Register | 400004 | INT16 | - | Status |

## How to Use This Map

1. **Download Modbus Monitor XPF** — [Get the free version](https://www.modbusmonitor.com/download).
2. **Select the Schneider Electric Symmetra PX device map** — check availability and access in the installed application catalog.
3. **Connect to your device** — confirm transport, addressing and data types before starting a read operation.
4. **Visualise and log** — build dashboards, trend data, and export readings without manual register entry.

## Why Use Pre-Built Maps

- **Saves time** — no need to manually look up or enter register addresses
- **Reduces errors** — reusable maps reduce repeated manual entry; validate addresses and data types for your device
- **Speeds commissioning** — connect and poll within minutes instead of hours
- **Reusable across projects** — use the same map across multiple sites and installations

## Data Categories Available

- Power
- Current
- Status
- Voltage
- Frequency
- Temperature

## Related Tools

- [Modbus Monitor XPF — Windows Modbus Tool](https://www.modbusmonitor.com/download)
- [Modbus HMI Builder](https://www.modbusmonitor.com/modbus-hmi)
- [Compare Modbus Monitor XPF with Other Tools](https://www.modbusmonitor.com/compare)

## Related Device Maps

- [Schneider Electric PM8000 Modbus Register Map](./pm8000.md)
- [Schneider Electric ION9000 Modbus Register Map](./ion9000.md)
- [Schneider Electric PM5000 / PM5100 / PM5300 Modbus Register Map](./pm5000-pm5100-pm5300.md)
- [Schneider Electric PM5500 / PM5560 / PM5580 Modbus Register Map](./pm5500-pm5560-pm5580.md)
- [All Schneider Electric Modbus Register Maps](./index.md)
- [All XPF Device Maps](../../../../modbus-device-maps/index.md)

<!-- public-preview-metadata -->
<script type="application/ld+json">{"@context": "https://schema.org", "@type": "Dataset", "name": "Schneider Electric Symmetra PX public register preview", "description": "Sample register addresses and data types; not a complete map or hardware verification.", "url": "https://docs.quantumbitsolutions.com/products/xpf/device-maps/schneider-electric/symmetra-px/", "license": "https://modbus-monitor.github.io/modbus-device-maps/data-license/", "creator": {"@type": "Organization", "name": "Quantum Bit Solutions", "url": "https://quantumbitsolutions.com/"}, "distribution": {"@type": "DataDownload", "encodingFormat": "application/json", "contentUrl": "https://modbus-monitor.github.io/modbus-device-maps/maps/schneider-electric/symmetra-px.json"}}</script>
<!-- /public-preview-metadata -->
