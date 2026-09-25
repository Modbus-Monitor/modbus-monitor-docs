---
title: Socomec NETYS PR,NETYS RT,ITYS Modbus Register Map
description: Socomec NETYS PR,NETYS RT,ITYS Modbus map and register map with sample Modbus registers, register addresses, and ups overview for engineers. Includes sample addresses and data types for review before use with Modbus Monitor XPF.
---

# Socomec NETYS PR,NETYS RT,ITYS Modbus Register Map

The Socomec NETYS PR,NETYS RT,ITYS is a ups used for power continuity monitoring, alarm review, and resilience planning. This page provides a sample Modbus register map with addresses, data types, and signal categories to help engineers commission, troubleshoot, and monitor the device. For Socomec NETYS PR,NETYS RT,ITYS deployments, teams often use this map to surface voltage, frequency, and current data in backup power systems and critical infrastructure monitoring.

This page shows a public register preview. Check the catalog in your installed XPF version for complete-map availability and licensing.

Confirm the exact model and firmware, address base, register function, word order, scaling and units against the manufacturer manual before polling. This preview does not establish hardware validation.

## Overview

- **Device:** Socomec NETYS PR,NETYS RT,ITYS
- **Type:** UPS
- **Protocol:** Confirm the supported transport for the exact device and firmware in the manufacturer manual.
- **Use case:** power continuity monitoring, alarm review, and resilience planning
- **Works with:** Modbus Monitor XPF (import directly)

## Download Modbus Map

The sample below is a public preview. Check the catalog in your installed XPF version for current availability, access and licensing.

- [Get Modbus Monitor XPF](https://www.modbusmonitor.com/download)

[Public JSON preview](https://modbus-monitor.github.io/modbus-device-maps/maps/socomec/netys-pr-netys-rt-itys.json) · [Preview data terms](https://modbus-monitor.github.io/modbus-device-maps/data-license/)

## Register Table (Sample)

Sample registers from the Socomec NETYS PR,NETYS RT,ITYS Modbus map. Confirm the sample against the exact device and firmware before use.

| Signal | Address | Type | Units | Category |
|---|---:|---|---|---|
| Phase Voltage AB V | 440074 | UINT16 | V | Voltage |
| AC Current A | 440069 | UINT16 | - | Current |
| AC Power W | 440081 | INT16 | kW | Power |
| AC Energy Wh | 440091 | UINT32 | kWh | Energy |
| Line Frequency Hz | 440083 | UINT16 | Hz | Frequency |
| Scale factor PFSF | 440090 | INT16 | - | Power Factor |
| Enumerated value Operating state | 440105 | UINT16 | - | Status |
| Cabinet Temperature C | 440100 | INT16 | degC | Temperature |
| Scale factor ASF | 440073 | INT16 | - | General |
| Phase A Current A | 440070 | UINT16 | - | Current |
| Phase B Current A | 440071 | UINT16 | - | Current |
| Phase C Current A | 440072 | UINT16 | - | Current |

## How to Use This Map

1. **Download Modbus Monitor XPF** — [Get the free version](https://www.modbusmonitor.com/download).
2. **Select the Socomec NETYS PR,NETYS RT,ITYS device map** — check availability and access in the installed application catalog.
3. **Connect to your device** — confirm transport, addressing and data types before starting a read operation.
4. **Visualise and log** — build dashboards, trend data, and export readings without manual register entry.

## Why Use Pre-Built Maps

- **Saves time** — no need to manually look up or enter register addresses
- **Reduces errors** — reusable maps reduce repeated manual entry; validate addresses and data types for your device
- **Speeds commissioning** — connect and poll within minutes instead of hours
- **Reusable across projects** — use the same map across multiple sites and installations

## Data Categories Available

- Voltage
- Frequency
- Current
- Temperature
- Power
- Status

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
<script type="application/ld+json">{"@context": "https://schema.org", "@type": "Dataset", "name": "Socomec NETYS PR,NETYS RT,ITYS public register preview", "description": "Sample register addresses and data types; not a complete map or hardware verification.", "url": "https://docs.quantumbitsolutions.com/products/xpf/device-maps/socomec/netys-pr-netys-rt-itys/", "license": "https://modbus-monitor.github.io/modbus-device-maps/data-license/", "creator": {"@type": "Organization", "name": "Quantum Bit Solutions", "url": "https://quantumbitsolutions.com/"}, "distribution": {"@type": "DataDownload", "encodingFormat": "application/json", "contentUrl": "https://modbus-monitor.github.io/modbus-device-maps/maps/socomec/netys-pr-netys-rt-itys.json"}}</script>
<!-- /public-preview-metadata -->
