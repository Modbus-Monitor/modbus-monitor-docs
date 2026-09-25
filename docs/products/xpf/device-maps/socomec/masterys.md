---
title: Socomec Masterys Modbus Register Map
description: Socomec Masterys Modbus map and register map with sample Modbus registers, register addresses, and ups overview for engineers. Includes sample addresses and data types for review before use with Modbus Monitor XPF.
---

# Socomec Masterys Modbus Register Map

The Socomec Masterys is a ups used for power continuity monitoring, alarm review, and resilience planning. This page provides a sample Modbus register map with addresses, data types, and signal categories to help engineers commission, troubleshoot, and monitor the device. For Socomec Masterys deployments, teams often use this map to surface voltage, current, and power data in backup power systems and critical infrastructure monitoring.

This page shows a public register preview. Check the catalog in your installed XPF version for complete-map availability and licensing.

Confirm the exact model and firmware, address base, register function, word order, scaling and units against the manufacturer manual before polling. This preview does not establish hardware validation.

## Overview

- **Device:** Socomec Masterys
- **Type:** UPS
- **Protocol:** Confirm the supported transport for the exact device and firmware in the manufacturer manual.
- **Use case:** power continuity monitoring, alarm review, and resilience planning
- **Works with:** Modbus Monitor XPF (import directly)

## Download Modbus Map

The sample below is a public preview. Check the catalog in your installed XPF version for current availability, access and licensing.

- [Get Modbus Monitor XPF](https://www.modbusmonitor.com/download)

[Public JSON preview](https://modbus-monitor.github.io/modbus-device-maps/maps/socomec/masterys.json) · [Preview data terms](https://modbus-monitor.github.io/modbus-device-maps/data-license/)

## Register Table (Sample)

Sample registers from the Socomec Masterys Modbus map. Confirm the sample against the exact device and firmware before use.

| Signal | Address | Type | Units | Category |
|---|---:|---|---|---|
| Auxiliary mains star voltage v1 M06 V | 400102 | UINT16 | V | Voltage |
| Input current phase l1 M12 A | 400108 | UINT16 | A | Current |
| Output active power 4 M36 kW | 400132 | UINT16 | kW | Power |
| Auxiliary frequency M18 Hz | 400114 | UINT16 | Hz | Frequency |
| Internal UPS temperature M22 DC | 400118 | UINT16 | degC | Temperature |
| Load phase 1 M00 | 400096 | UINT16 | - | General |
| Auxiliary mains star voltage v2 M07 V | 400103 | UINT16 | V | Voltage |
| Auxiliary mains star voltage v3 M08 V | 400104 | UINT16 | V | Voltage |
| Output star voltage v1 M09 V | 400105 | UINT16 | V | Voltage |
| Output star voltage v2 M10 V | 400106 | UINT16 | V | Voltage |
| Output star voltage v3 M11 V | 400107 | UINT16 | V | Voltage |
| Input current phase l2 M13 A | 400109 | UINT16 | A | Current |

## How to Use This Map

1. **Download Modbus Monitor XPF** — [Get the free version](https://www.modbusmonitor.com/download).
2. **Select the Socomec Masterys device map** — check availability and access in the installed application catalog.
3. **Connect to your device** — confirm transport, addressing and data types before starting a read operation.
4. **Visualise and log** — build dashboards, trend data, and export readings without manual register entry.

## Why Use Pre-Built Maps

- **Saves time** — no need to manually look up or enter register addresses
- **Reduces errors** — reusable maps reduce repeated manual entry; validate addresses and data types for your device
- **Speeds commissioning** — connect and poll within minutes instead of hours
- **Reusable across projects** — use the same map across multiple sites and installations

## Data Categories Available

- Voltage
- Current
- Power
- Frequency
- Temperature

## Related Tools

- [Modbus Monitor XPF — Windows Modbus Tool](https://www.modbusmonitor.com/download)
- [Modbus HMI Builder](https://www.modbusmonitor.com/modbus-hmi)
- [Compare Modbus Monitor XPF with Other Tools](https://www.modbusmonitor.com/compare)

## Related Device Maps

- [Socomec DIRIS A40 / A41 RS485 Modbus Register Map](./diris-a40-a41-rs485.md)
- [Socomec DIRIS I31 Modbus Register Map](./diris-i31.md)
- [Socomec DIRIS U30 Modbus Register Map](./diris-u30.md)
- [Socomec Countis ECI3 Modbus Register Map](./countis-eci3.md)
- [All Socomec Modbus Register Maps](./index.md)
- [All XPF Device Maps](../../../../modbus-device-maps/index.md)

<!-- public-preview-metadata -->
<script type="application/ld+json">{"@context": "https://schema.org", "@type": "Dataset", "name": "Socomec Masterys public register preview", "description": "Sample register addresses and data types; not a complete map or hardware verification.", "url": "https://docs.quantumbitsolutions.com/products/xpf/device-maps/socomec/masterys/", "license": "https://modbus-monitor.github.io/modbus-device-maps/data-license/", "creator": {"@type": "Organization", "name": "Quantum Bit Solutions", "url": "https://quantumbitsolutions.com/"}, "distribution": {"@type": "DataDownload", "encodingFormat": "application/json", "contentUrl": "https://modbus-monitor.github.io/modbus-device-maps/maps/socomec/masterys.json"}}</script>
<!-- /public-preview-metadata -->
