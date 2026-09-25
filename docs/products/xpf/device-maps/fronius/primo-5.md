---
title: Fronius Primo 5 Modbus Register Map
description: Fronius Primo 5 Modbus map and register map with sample Modbus registers, register addresses, and solar inverter overview for engineers. Includes sample addresses and data types for review before use with Modbus Monitor XPF.
---

# Fronius Primo 5 Modbus Register Map

The Fronius Primo 5 is a solar inverter used for PV production monitoring, inverter diagnostics, and energy analytics. This page provides a sample Modbus register map with addresses, data types, and signal categories to help engineers commission, troubleshoot, and monitor the device. For Fronius Primo 5 deployments, teams often use this map to surface power, voltage, and current data in solar inverter monitoring and renewable energy systems.

This page shows a public register preview. Check the catalog in your installed XPF version for complete-map availability and licensing.

Confirm the exact model and firmware, address base, register function, word order, scaling and units against the manufacturer manual before polling. This preview does not establish hardware validation.

## Overview

- **Device:** Fronius Primo 5
- **Type:** Solar Inverter
- **Protocol:** Confirm the supported transport for the exact device and firmware in the manufacturer manual.
- **Use case:** PV production monitoring, inverter diagnostics, and energy analytics
- **Works with:** Modbus Monitor XPF (import directly)

## Download Modbus Map

The sample below is a public preview. Check the catalog in your installed XPF version for current availability, access and licensing.

- [Get Modbus Monitor XPF](https://www.modbusmonitor.com/download)

[Public JSON preview](https://modbus-monitor.github.io/modbus-device-maps/maps/fronius/primo-5.json) · [Preview data terms](https://modbus-monitor.github.io/modbus-device-maps/data-license/)

## Register Table (Sample)

Sample registers from the Fronius Primo 5 Modbus map. Confirm the sample against the exact device and firmware before use.

| Signal | Address | Type | Units | Category |
|---|---:|---|---|---|
| Phase Voltage AB V | 440077 | FLOAT32 | V | Voltage |
| AC Current A | 440069 | FLOAT32 | - | Current |
| AC Power W | 440089 | FLOAT32 | kW | Power |
| AC Energy Wh | 440099 | FLOAT32 | kWh | Energy |
| Line Frequency Hz | 440091 | FLOAT32 | Hz | Frequency |
| Enumerated value Operating state | 440115 | UINT16 | - | Status |
| Cabinet Temperature C | 440107 | FLOAT32 | degC | Temperature |
| Bitmask value Event fields | 440117 | UINT32 | - | General |
| Phase A Current A | 440071 | FLOAT32 | - | Current |
| Phase B Current A | 440073 | FLOAT32 | - | Current |
| Phase C Current A | 440075 | FLOAT32 | - | Current |
| Phase Voltage BC V | 440079 | FLOAT32 | V | Voltage |

## How to Use This Map

1. **Download Modbus Monitor XPF** — [Get the free version](https://www.modbusmonitor.com/download).
2. **Select the Fronius Primo 5 device map** — check availability and access in the installed application catalog.
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
- Energy
- Status
- Temperature

## Related Tools

- [Modbus Monitor XPF — Windows Modbus Tool](https://www.modbusmonitor.com/download)
- [Modbus HMI Builder](https://www.modbusmonitor.com/modbus-hmi)
- [Compare Modbus Monitor XPF with Other Tools](https://www.modbusmonitor.com/compare)

## Related Device Maps

- [Fronius Primo 4 Modbus Register Map](./primo-4.md)
- [Fronius Symo 6 Modbus Register Map](./symo-6.md)
- [All Fronius Modbus Register Maps](./index.md)
- [All XPF Device Maps](../../../../modbus-device-maps/index.md)

<!-- public-preview-metadata -->
<script type="application/ld+json">{"@context": "https://schema.org", "@type": "Dataset", "name": "Fronius Primo 5 public register preview", "description": "Sample register addresses and data types; not a complete map or hardware verification.", "url": "https://docs.quantumbitsolutions.com/products/xpf/device-maps/fronius/primo-5/", "license": "https://modbus-monitor.github.io/modbus-device-maps/data-license/", "creator": {"@type": "Organization", "name": "Quantum Bit Solutions", "url": "https://quantumbitsolutions.com/"}, "distribution": {"@type": "DataDownload", "encodingFormat": "application/json", "contentUrl": "https://modbus-monitor.github.io/modbus-device-maps/maps/fronius/primo-5.json"}}</script>
<!-- /public-preview-metadata -->
