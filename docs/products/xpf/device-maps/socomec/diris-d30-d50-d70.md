---
title: Socomec DIRIS,D30,D50,D70 _ Modbus Register Map
description: Socomec DIRIS,D30,D50,D70 _ Modbus map and register map with sample Modbus registers, register addresses, and power meter overview for engineers. Includes sample addresses and data types for review before use with Modbus Monitor XPF.
---

# Socomec DIRIS,D30,D50,D70 _ Modbus Register Map

The Socomec DIRIS,D30,D50,D70 _ is a power meter used for power monitoring, energy metering, and facility automation. This page provides a sample Modbus register map with addresses, data types, and signal categories to help engineers commission, troubleshoot, and monitor the device. For Socomec DIRIS,D30,D50,D70 _ deployments, teams often use this map to surface energy, voltage, and current data in facility metering, commissioning, and operational analytics.

This page shows a public register preview. Check the catalog in your installed XPF version for complete-map availability and licensing.

Confirm the exact model and firmware, address base, register function, word order, scaling and units against the manufacturer manual before polling. This preview does not establish hardware validation.

## Overview

- **Device:** Socomec DIRIS,D30,D50,D70 _
- **Type:** Power Meter
- **Protocol:** Confirm the supported transport for the exact device and firmware in the manufacturer manual.
- **Use case:** power monitoring, energy metering, and facility automation
- **Works with:** Modbus Monitor XPF (import directly)

## Download Modbus Map

The sample below is a public preview. Check the catalog in your installed XPF version for current availability, access and licensing.

- [Get Modbus Monitor XPF](https://www.modbusmonitor.com/download)

[Public JSON preview](https://modbus-monitor.github.io/modbus-device-maps/maps/socomec/diris-d30-d50-d70.json) · [Preview data terms](https://modbus-monitor.github.io/modbus-device-maps/data-license/)

## Register Table (Sample)

Sample registers from the Socomec DIRIS,D30,D50,D70 _ Modbus map. Confirm the sample against the exact device and firmware before use.

| Signal | Address | Type | Units | Category |
|---|---:|---|---|---|
| Inst Measurement Load 1 Ph N voltage V1 V | 418444 | UINT32 | V | Voltage |
| Inst Measurement Load 1 Current I1 A | 418458 | UINT32 | - | Current |
| Inst Measurement Load 1 Total active power W | 418476 | INT32 | kW | Power |
| Energy measurement Load 1 Total positive active energy ea Wh | 419841 | UINT32 | kWh | Energy |
| Inst Measurement Load 1 Frequency Hz | 418442 | UINT32 | Hz | Frequency |
| Acknowledgment of alarms Ack id | 439616 | UINT16 | - | Status |
| Inst Measurement Load 1 Date of last instance s | 418433 | UINT32 | - | General |
| Inst Measurement Load 1 Ph N voltage V2 V | 418446 | UINT32 | V | Voltage |
| Inst Measurement Load 1 Ph N voltage V3 V | 418448 | UINT32 | V | Voltage |
| Inst Measurement Load 1 Ph ph voltage U12 V | 418452 | UINT32 | V | Voltage |
| Inst Measurement Load 1 Ph ph voltage U23 V | 418454 | UINT32 | V | Voltage |
| Inst Measurement Load 1 Ph ph voltage U31 V | 418456 | UINT32 | V | Voltage |

## How to Use This Map

1. **Download Modbus Monitor XPF** — [Get the free version](https://www.modbusmonitor.com/download).
2. **Select the Socomec DIRIS,D30,D50,D70 _ device map** — check availability and access in the installed application catalog.
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
- Status
- Frequency

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
<script type="application/ld+json">{"@context": "https://schema.org", "@type": "Dataset", "name": "Socomec DIRIS,D30,D50,D70 public register preview", "description": "Sample register addresses and data types; not a complete map or hardware verification.", "url": "https://docs.quantumbitsolutions.com/products/xpf/device-maps/socomec/diris-d30-d50-d70/", "license": "https://modbus-monitor.github.io/modbus-device-maps/data-license/", "creator": {"@type": "Organization", "name": "Quantum Bit Solutions", "url": "https://quantumbitsolutions.com/"}, "distribution": {"@type": "DataDownload", "encodingFormat": "application/json", "contentUrl": "https://modbus-monitor.github.io/modbus-device-maps/maps/socomec/diris-d30-d50-d70.json"}}</script>
<!-- /public-preview-metadata -->
