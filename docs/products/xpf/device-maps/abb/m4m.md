---
title: ABB M4M Modbus Register Map
description: ABB M4M Modbus map and register map with sample Modbus registers, register addresses, and power meter overview for engineers. Includes sample addresses and data types for review before use with Modbus Monitor XPF.
---

# ABB M4M Modbus Register Map

The ABB M4M is a power meter used for power monitoring, energy metering, and facility automation. This page provides a sample Modbus register map with addresses, data types, and signal categories to help engineers commission, troubleshoot, and monitor the device. Often deployed in switchboards and compact power monitoring panels.

This page shows a public register preview. Check the catalog in your installed XPF version for complete-map availability and licensing.

Confirm the exact model and firmware, address base, register function, word order, scaling and units against the manufacturer manual before polling. This preview does not establish hardware validation.

## Overview

- **Device:** ABB M4M
- **Type:** Power Meter
- **Protocol:** Confirm the supported transport for the exact device and firmware in the manufacturer manual.
- **Use case:** power monitoring, energy metering, and facility automation
- **Works with:** Modbus Monitor XPF (import directly)

## Download Modbus Map

The sample below is a public preview. Check the catalog in your installed XPF version for current availability, access and licensing.

- [Get Modbus Monitor XPF](https://www.modbusmonitor.com/download)

[Public JSON preview](https://modbus-monitor.github.io/modbus-device-maps/maps/abb/m4m.json) · [Preview data terms](https://modbus-monitor.github.io/modbus-device-maps/data-license/)

## Register Table (Sample)

Sample registers from the ABB M4M Modbus map. Confirm the sample against the exact device and firmware before use.

| Signal | Address | Type | Units | Category |
|---|---:|---|---|---|
| Energy Trend Data block 1 0 | 433552 | UINT16 | kWh | Energy |
| Max Min Demand Data block 1 0 | 436738 | UINT16 | kW | Demand |
| Alarm number | 435936 | UINT16 | - | Status |
| Entry number | 432769 | UINT16 | - | General |
| I O port 1 | 435852 | UINT16 | - | Communication |
| Energy Trend Data block 1 1 | 433553 | UINT16 | kWh | Energy |
| Energy Trend Data block 1 2 | 433554 | UINT16 | kWh | Energy |
| Energy Trend Data block 1 3 | 433555 | UINT16 | kWh | Energy |
| Energy Trend Data block 1 4 | 433556 | UINT16 | kWh | Energy |
| Energy Trend Data block 1 5 | 433557 | UINT16 | kWh | Energy |
| Energy Trend Data block 1 6 | 433558 | UINT16 | kWh | Energy |
| Energy Trend Data block 1 7 | 433559 | UINT16 | kWh | Energy |

## How to Use This Map

1. **Download Modbus Monitor XPF** — [Get the free version](https://www.modbusmonitor.com/download).
2. **Select the ABB M4M device map** — check availability and access in the installed application catalog.
3. **Connect to your device** — confirm transport, addressing and data types before starting a read operation.
4. **Visualise and log** — build dashboards, trend data, and export readings without manual register entry.

## Why Use Pre-Built Maps

- **Saves time** — no need to manually look up or enter register addresses
- **Reduces errors** — reusable maps reduce repeated manual entry; validate addresses and data types for your device
- **Speeds commissioning** — connect and poll within minutes instead of hours
- **Reusable across projects** — use the same map across multiple sites and installations

## Data Categories Available

- Demand
- Energy
- Status

## Related Tools

- [Modbus Monitor XPF — Windows Modbus Tool](https://www.modbusmonitor.com/download)
- [Modbus HMI Builder](https://www.modbusmonitor.com/modbus-hmi)
- [Compare Modbus Monitor XPF with Other Tools](https://www.modbusmonitor.com/compare)

## Related Device Maps

- [ABB B23 / B24 Modbus Register Map](./b23-b24.md)
- [ABB A41 / A42 Modbus Register Map](./a41-a42.md)
- [ABB Trio 50 / Trio 60 Modbus Register Map](./trio-50-trio-60.md)
- [All ABB Modbus Register Maps](./index.md)
- [All XPF Device Maps](../../../../modbus-device-maps/index.md)

<!-- public-preview-metadata -->
<script type="application/ld+json">{"@context": "https://schema.org", "@type": "Dataset", "name": "ABB M4M public register preview", "description": "Sample register addresses and data types; not a complete map or hardware verification.", "url": "https://docs.quantumbitsolutions.com/products/xpf/device-maps/abb/m4m/", "license": "https://modbus-monitor.github.io/modbus-device-maps/data-license/", "creator": {"@type": "Organization", "name": "Quantum Bit Solutions", "url": "https://quantumbitsolutions.com/"}, "distribution": {"@type": "DataDownload", "encodingFormat": "application/json", "contentUrl": "https://modbus-monitor.github.io/modbus-device-maps/maps/abb/m4m.json"}}</script>
<!-- /public-preview-metadata -->
