---
title: Phoenix Contact EEM-MA3xx Modbus Register Map
description: Phoenix Contact EEM-MA3xx Modbus map and register map with sample Modbus registers, register addresses, and power meter overview for engineers. Includes sample addresses and data types for review before use with Modbus Monitor XPF.
---

# Phoenix Contact EEM-MA3xx Modbus Register Map

The Phoenix Contact EEM-MA3xx is a power meter used for power monitoring, energy metering, and facility automation. This page provides a sample Modbus register map with addresses, data types, and signal categories to help engineers commission, troubleshoot, and monitor the device. For Phoenix Contact EEM-MA3xx deployments, teams often use this map to surface power, energy, and voltage data in facility metering, commissioning, and operational analytics.

This page shows a public register preview. Check the catalog in your installed XPF version for complete-map availability and licensing.

Confirm the exact model and firmware, address base, register function, word order, scaling and units against the manufacturer manual before polling. This preview does not establish hardware validation.

## Overview

- **Device:** Phoenix Contact EEM-MA3xx
- **Type:** Power Meter
- **Protocol:** Confirm the supported transport for the exact device and firmware in the manufacturer manual.
- **Use case:** power monitoring, energy metering, and facility automation
- **Works with:** Modbus Monitor XPF (import directly)

## Download Modbus Map

The sample below is a public preview. Check the catalog in your installed XPF version for current availability, access and licensing.

- [Get Modbus Monitor XPF](https://www.modbusmonitor.com/download)

[Public JSON preview](https://modbus-monitor.github.io/modbus-device-maps/maps/phoenix-contact/eem-ma3xx.json) · [Preview data terms](https://modbus-monitor.github.io/modbus-device-maps/data-license/)

## Register Table (Sample)

Sample registers from the Phoenix Contact EEM-MA3xx Modbus map. Confirm the sample against the exact device and firmware before use.

| Signal | Address | Type | Units | Category |
|---|---:|---|---|---|
| U12 conductor voltage V | 450514 | UINT32 | V | Voltage |
| I1 current A | 450528 | UINT32 | - | Current |
| Sum P total active power - W | 450536 | INT32 | kW | Power |
| Total active energy procurement system kWh | 450770 | UINT32 | kWh | Energy |
| F frequency Hz | 450526 | UINT32 | Hz | Frequency |
| Hour operating hours counter h | 450512 | UINT32 | - | General |
| U23 conductor voltage V | 450516 | UINT32 | V | Voltage |
| U31 conductor voltage V | 450518 | UINT32 | V | Voltage |
| V1 conductor voltage to N V | 450520 | UINT32 | V | Voltage |
| V2 conductor voltage to N V | 450522 | UINT32 | V | Voltage |
| V3 conductor voltage to N V | 450524 | UINT32 | V | Voltage |
| I2 current A | 450530 | UINT32 | - | Current |

## How to Use This Map

1. **Download Modbus Monitor XPF** — [Get the free version](https://www.modbusmonitor.com/download).
2. **Select the Phoenix Contact EEM-MA3xx device map** — check availability and access in the installed application catalog.
3. **Connect to your device** — confirm transport, addressing and data types before starting a read operation.
4. **Visualise and log** — build dashboards, trend data, and export readings without manual register entry.

## Why Use Pre-Built Maps

- **Saves time** — no need to manually look up or enter register addresses
- **Reduces errors** — reusable maps reduce repeated manual entry; validate addresses and data types for your device
- **Speeds commissioning** — connect and poll within minutes instead of hours
- **Reusable across projects** — use the same map across multiple sites and installations

## Data Categories Available

- Power
- Energy
- Voltage
- Current
- Frequency

## Related Tools

- [Modbus Monitor XPF — Windows Modbus Tool](https://www.modbusmonitor.com/download)
- [Modbus HMI Builder](https://www.modbusmonitor.com/modbus-hmi)
- [Compare Modbus Monitor XPF with Other Tools](https://www.modbusmonitor.com/compare)

## Related Device Maps

- [Phoenix Contact EEM-EM3xx,EM325,EM355,EM375,EM327,EM357,EM377 Modbus Register Map](./eem-em3xx-em325-em355-em375-em327-em357-em377.md)
- [Phoenix Contact EEM-MA,EEM-MA3xx Modbus Register Map](./eem-ma-eem-ma3xx.md)
- [All Phoenix Contact Modbus Register Maps](./index.md)
- [All XPF Device Maps](../../../../modbus-device-maps/index.md)

<!-- public-preview-metadata -->
<script type="application/ld+json">{"@context": "https://schema.org", "@type": "Dataset", "name": "Phoenix Contact EEM-MA3xx public register preview", "description": "Sample register addresses and data types; not a complete map or hardware verification.", "url": "https://docs.quantumbitsolutions.com/products/xpf/device-maps/phoenix-contact/eem-ma3xx/", "license": "https://modbus-monitor.github.io/modbus-device-maps/data-license/", "creator": {"@type": "Organization", "name": "Quantum Bit Solutions", "url": "https://quantumbitsolutions.com/"}, "distribution": {"@type": "DataDownload", "encodingFormat": "application/json", "contentUrl": "https://modbus-monitor.github.io/modbus-device-maps/maps/phoenix-contact/eem-ma3xx.json"}}</script>
<!-- /public-preview-metadata -->
