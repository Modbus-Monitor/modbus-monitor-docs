---
title: Janitza UMG96 Modbus Register Map
description: Janitza UMG96 Modbus map and register map with sample Modbus registers, register addresses, and power meter overview for engineers. Includes sample addresses and data types for review before use with Modbus Monitor XPF.
---

# Janitza UMG96 Modbus Register Map

The Janitza UMG96 is a power meter used for power monitoring, energy metering, and facility automation. This page provides a sample Modbus register map with addresses, data types, and signal categories to help engineers commission, troubleshoot, and monitor the device. For Janitza UMG96 deployments, teams often use this map to surface energy, voltage, and current data in facility metering, commissioning, and operational analytics.

This page shows a public register preview. Check the catalog in your installed XPF version for complete-map availability and licensing.

Confirm the exact model and firmware, address base, register function, word order, scaling and units against the manufacturer manual before polling. This preview does not establish hardware validation.

## Overview

- **Device:** Janitza UMG96
- **Type:** Power Meter
- **Protocol:** Confirm the supported transport for the exact device and firmware in the manufacturer manual.
- **Use case:** power monitoring, energy metering, and facility automation
- **Works with:** Modbus Monitor XPF (import directly)

## Download Modbus Map

The sample below is a public preview. Check the catalog in your installed XPF version for current availability, access and licensing.

- [Get Modbus Monitor XPF](https://www.modbusmonitor.com/download)

[Public JSON preview](https://modbus-monitor.github.io/modbus-device-maps/maps/janitza/umg96.json) · [Preview data terms](https://modbus-monitor.github.io/modbus-device-maps/data-license/)

## Register Table (Sample)

Sample registers from the Janitza UMG96 Modbus map. Confirm the sample against the exact device and firmware before use.

| Signal | Address | Type | Units | Category |
|---|---:|---|---|---|
| voltage L1 N V | 419000 | FLOAT32 | V | Voltage |
| current L1 A | 419012 | FLOAT32 | A | Current |
| active power L1 W | 419020 | FLOAT32 | kW | Power |
| active energy L1 Wh | 419054 | FLOAT32 | kWh | Energy |
| measured frequency Hz | 419050 | FLOAT32 | Hz | Frequency |
| harmonic THD U L1 N % | 419110 | FLOAT32 | - | Harmonics |
| rotation field 1 right CW 0 none -1 left CCW | 419052 | INT32 | - | General |
| Parameter device address 0 255 | 400000 | INT16 | - | Communication |
| voltage L2 N V | 419002 | FLOAT32 | V | Voltage |
| voltage L3 N V | 419004 | FLOAT32 | V | Voltage |
| voltage L1 L2 V | 419006 | FLOAT32 | V | Voltage |
| voltage L2 L3 V | 419008 | FLOAT32 | V | Voltage |

## How to Use This Map

1. **Download Modbus Monitor XPF** — [Get the free version](https://www.modbusmonitor.com/download).
2. **Select the Janitza UMG96 device map** — check availability and access in the installed application catalog.
3. **Connect to your device** — confirm transport, addressing and data types before starting a read operation.
4. **Visualise and log** — build dashboards, trend data, and export readings without manual register entry.

## Why Use Pre-Built Maps

- **Saves time** — no need to manually look up or enter register addresses
- **Reduces errors** — reusable maps reduce repeated manual entry; validate addresses and data types for your device
- **Speeds commissioning** — connect and poll within minutes instead of hours
- **Reusable across projects** — use the same map across multiple sites and installations

## Data Categories Available

- Energy
- Voltage
- Current
- Power
- Harmonics
- Frequency

## Related Tools

- [Modbus Monitor XPF — Windows Modbus Tool](https://www.modbusmonitor.com/download)
- [Modbus HMI Builder](https://www.modbusmonitor.com/modbus-hmi)
- [Compare Modbus Monitor XPF with Other Tools](https://www.modbusmonitor.com/compare)

## Related Device Maps

- [Janitza UMG104 Modbus Register Map](./umg104.md)
- [Janitza UMG605 Modbus Register Map](./umg605.md)
- [Janitza UMG604 Modbus Register Map](./umg604.md)
- [Janitza UMG103 Modbus Register Map](./umg103.md)
- [All Janitza Modbus Register Maps](./index.md)
- [All XPF Device Maps](../../../../modbus-device-maps/index.md)

<!-- public-preview-metadata -->
<script type="application/ld+json">{"@context": "https://schema.org", "@type": "Dataset", "name": "Janitza UMG96 public register preview", "description": "Sample register addresses and data types; not a complete map or hardware verification.", "url": "https://docs.quantumbitsolutions.com/products/xpf/device-maps/janitza/umg96/", "license": "https://modbus-monitor.github.io/modbus-device-maps/data-license/", "creator": {"@type": "Organization", "name": "Quantum Bit Solutions", "url": "https://quantumbitsolutions.com/"}, "distribution": {"@type": "DataDownload", "encodingFormat": "application/json", "contentUrl": "https://modbus-monitor.github.io/modbus-device-maps/maps/janitza/umg96.json"}}</script>
<!-- /public-preview-metadata -->
