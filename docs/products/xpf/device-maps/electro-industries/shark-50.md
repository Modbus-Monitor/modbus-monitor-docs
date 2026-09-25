---
title: Electro Industries Shark 50 Modbus Register Map
description: Electro Industries Shark 50 Modbus map and register map with sample Modbus registers, register addresses, and power meter overview for engineers. Includes sample addresses and data types for review before use with Modbus Monitor XPF.
---

# Electro Industries Shark 50 Modbus Register Map

The Electro Industries Shark 50 is a power meter used for power monitoring, energy metering, and facility automation. This page provides a sample Modbus register map with addresses, data types, and signal categories to help engineers commission, troubleshoot, and monitor the device. For Electro Industries Shark 50 deployments, teams often use this map to surface current, demand, and power data in facility metering, commissioning, and operational analytics.

This page shows a public register preview. Check the catalog in your installed XPF version for complete-map availability and licensing.

Confirm the exact model and firmware, address base, register function, word order, scaling and units against the manufacturer manual before polling. This preview does not establish hardware validation.

## Overview

- **Device:** Electro Industries Shark 50
- **Type:** Power Meter
- **Protocol:** Confirm the supported transport for the exact device and firmware in the manufacturer manual.
- **Use case:** power monitoring, energy metering, and facility automation
- **Works with:** Modbus Monitor XPF (import directly)

## Download Modbus Map

The sample below is a public preview. Check the catalog in your installed XPF version for current availability, access and licensing.

- [Get Modbus Monitor XPF](https://www.modbusmonitor.com/download)

[Public JSON preview](https://modbus-monitor.github.io/modbus-device-maps/maps/electro-industries/shark-50.json) · [Preview data terms](https://modbus-monitor.github.io/modbus-device-maps/data-license/)

## Register Table (Sample)

Sample registers from the Electro Industries Shark 50 Modbus map. Confirm the sample against the exact device and firmware before use.

| Signal | Address | Type | Units | Category |
|---|---:|---|---|---|
| Amps A | 401011 | FLOAT32 | A | Current |
| Power Factor 3 Ph total | 401023 | FLOAT32 | PF | Power |
| Power Energy Format | 430005 | UINT16 | kWh | Energy |
| Frequency | 401025 | FLOAT32 | Hz | Frequency |
| Positive PF 3 Ph Average | 402015 | FLOAT32 | - | Power Factor |
| Positive Watts 3 Ph Minimum Avg Demand | 403017 | FLOAT32 | kW | Demand |
| Meter Status | 404999 | UINT16 | - | Status |
| Meter Name:8 | 400000 | STRING | - | Identification |
| Meter Type | 400016 | UINT16 | - | General |
| Communication port setup | 430025 | UINT16 | - | Communication |
| Amps B | 401013 | FLOAT32 | A | Current |
| Amps C | 401015 | FLOAT32 | A | Current |

## How to Use This Map

1. **Download Modbus Monitor XPF** — [Get the free version](https://www.modbusmonitor.com/download).
2. **Select the Electro Industries Shark 50 device map** — check availability and access in the installed application catalog.
3. **Connect to your device** — confirm transport, addressing and data types before starting a read operation.
4. **Visualise and log** — build dashboards, trend data, and export readings without manual register entry.

## Why Use Pre-Built Maps

- **Saves time** — no need to manually look up or enter register addresses
- **Reduces errors** — reusable maps reduce repeated manual entry; validate addresses and data types for your device
- **Speeds commissioning** — connect and poll within minutes instead of hours
- **Reusable across projects** — use the same map across multiple sites and installations

## Data Categories Available

- Current
- Demand
- Power
- Frequency
- Energy
- Power Factor

## Related Tools

- [Modbus Monitor XPF — Windows Modbus Tool](https://www.modbusmonitor.com/download)
- [Modbus HMI Builder](https://www.modbusmonitor.com/modbus-hmi)
- [Compare Modbus Monitor XPF with Other Tools](https://www.modbusmonitor.com/compare)

## Related Device Maps

- [Electro Industries Shark 200 / 200T Modbus Register Map](./shark-200-200t.md)
- [Electro Industries Shark 250 Modbus Register Map](./shark-250.md)
- [Electro Industries Shark 200 Modbus Register Map](./shark-200.md)
- [All Electro Industries Modbus Register Maps](./index.md)
- [All XPF Device Maps](../../../../modbus-device-maps/index.md)

<!-- public-preview-metadata -->
<script type="application/ld+json">{"@context": "https://schema.org", "@type": "Dataset", "name": "Electro Industries Shark 50 public register preview", "description": "Sample register addresses and data types; not a complete map or hardware verification.", "url": "https://docs.quantumbitsolutions.com/products/xpf/device-maps/electro-industries/shark-50/", "license": "https://modbus-monitor.github.io/modbus-device-maps/data-license/", "creator": {"@type": "Organization", "name": "Quantum Bit Solutions", "url": "https://quantumbitsolutions.com/"}, "distribution": {"@type": "DataDownload", "encodingFormat": "application/json", "contentUrl": "https://modbus-monitor.github.io/modbus-device-maps/maps/electro-industries/shark-50.json"}}</script>
<!-- /public-preview-metadata -->
