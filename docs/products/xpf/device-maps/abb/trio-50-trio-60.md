---
title: ABB Trio 50 / Trio 60 Modbus Register Map
description: ABB Trio 50 / Trio 60 Modbus map and register map with sample Modbus registers, register addresses, and solar inverter overview for engineers. Includes sample addresses and data types for review before use with Modbus Monitor XPF.
---

# ABB Trio 50 / Trio 60 Modbus Register Map

The ABB Trio 50 / Trio 60 is a solar inverter used for PV production monitoring, inverter diagnostics, and energy analytics. This page provides a sample Modbus register map with addresses, data types, and signal categories to help engineers commission, troubleshoot, and monitor the device. For ABB Trio 50 / Trio 60 deployments, teams often use this map to surface power, status, and current data in switchboards, facility power distribution, and commercial energy monitoring.

This page shows a public register preview. Check the catalog in your installed XPF version for complete-map availability and licensing.

Confirm the exact model and firmware, address base, register function, word order, scaling and units against the manufacturer manual before polling. This preview does not establish hardware validation.

## Overview

- **Device:** ABB Trio 50 / Trio 60
- **Type:** Solar Inverter
- **Protocol:** Confirm the supported transport for the exact device and firmware in the manufacturer manual.
- **Use case:** PV production monitoring, inverter diagnostics, and energy analytics
- **Works with:** Modbus Monitor XPF (import directly)

## Download Modbus Map

The sample below is a public preview. Check the catalog in your installed XPF version for current availability, access and licensing.

- [Get Modbus Monitor XPF](https://www.modbusmonitor.com/download)

[Public JSON preview](https://modbus-monitor.github.io/modbus-device-maps/maps/abb/trio-50-trio-60.json) · [Preview data terms](https://modbus-monitor.github.io/modbus-device-maps/data-license/)

## Register Table (Sample)

Sample registers from the ABB Trio 50 / Trio 60 Modbus map. Confirm the sample against the exact device and firmware before use.

| Signal | Address | Type | Units | Category |
|---|---:|---|---|---|
| Inverter Grid Voltage V | 400304 | FLOAT32 | V | Voltage |
| Inverter Grid Current A | 400308 | FLOAT32 | - | Current |
| Dynamic Mode Power Factor Set Point Reactive Power expressed as fixed Power Factor | 400201 | FLOAT32 | PF | Power |
| Daily Energy Wh | 401071 | UINT32 | kWh | Energy |
| Mean Grid Frequency Hz | 401107 | FLOAT32 | Hz | Frequency |
| Global State | 401051 | UINT16 | - | Status |
| Internal Temperature C | 401121 | FLOAT32 | degC | Temperature |
| Remote On Off | 400181 | UINT16 | - | General |
| Accuracy Set unit for Modbus Data Addresses 0507 0508 0511 and 0512 or | 400502 | UINT16 | - | Communication |
| Set communication protocol for serial line RS485 1 | 401007 | UINT16 | - | Identification |
| Permanent Mode Power Factor Set Point Reactive Power expressed as fixed Power Factor | 400203 | FLOAT32 | PF | Power |
| Dynamic Mode Active Power Set Point Active Power Curtailment expressed as percentage of Nominal Power in steps | 400211 | UINT16 | kW | Power |

## How to Use This Map

1. **Download Modbus Monitor XPF** — [Get the free version](https://www.modbusmonitor.com/download).
2. **Select the ABB Trio 50 / Trio 60 device map** — check availability and access in the installed application catalog.
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

- [ABB M4M Modbus Register Map](./m4m.md)
- [ABB B23 / B24 Modbus Register Map](./b23-b24.md)
- [ABB A41 / A42 Modbus Register Map](./a41-a42.md)
- [All ABB Modbus Register Maps](./index.md)
- [All XPF Device Maps](../../../../modbus-device-maps/index.md)

<!-- public-preview-metadata -->
<script type="application/ld+json">{"@context": "https://schema.org", "@type": "Dataset", "name": "ABB Trio 50 / Trio 60 public register preview", "description": "Sample register addresses and data types; not a complete map or hardware verification.", "url": "https://docs.quantumbitsolutions.com/products/xpf/device-maps/abb/trio-50-trio-60/", "license": "https://modbus-monitor.github.io/modbus-device-maps/data-license/", "creator": {"@type": "Organization", "name": "Quantum Bit Solutions", "url": "https://quantumbitsolutions.com/"}, "distribution": {"@type": "DataDownload", "encodingFormat": "application/json", "contentUrl": "https://modbus-monitor.github.io/modbus-device-maps/maps/abb/trio-50-trio-60.json"}}</script>
<!-- /public-preview-metadata -->
