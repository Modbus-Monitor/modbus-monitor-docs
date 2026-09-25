---
title: Socomec DIRIS A40 / A41 RS485 Modbus Register Map
description: Socomec DIRIS A40 / A41 RS485 Modbus map and register map with sample Modbus registers, register addresses, and power meter overview for engineers. Includes sample addresses and data types for review before use with Modbus Monitor XPF.
---

# Socomec DIRIS A40 / A41 RS485 Modbus Register Map

The Socomec DIRIS A40 / A41 RS485 is a power meter used for power monitoring, energy metering, and facility automation. This page provides a sample Modbus register map with addresses, data types, and signal categories to help engineers commission, troubleshoot, and monitor the device. For Socomec DIRIS A40 / A41 RS485 deployments, teams often use this map to surface harmonics, power, and voltage data in facility metering, commissioning, and operational analytics.

This page shows a public register preview. Check the catalog in your installed XPF version for complete-map availability and licensing.

Confirm the exact model and firmware, address base, register function, word order, scaling and units against the manufacturer manual before polling. This preview does not establish hardware validation.

## Overview

- **Device:** Socomec DIRIS A40 / A41 RS485
- **Type:** Power Meter
- **Protocol:** Confirm the supported transport for the exact device and firmware in the manufacturer manual.
- **Use case:** power monitoring, energy metering, and facility automation
- **Works with:** Modbus Monitor XPF (import directly)

## Download Modbus Map

The sample below is a public preview. Check the catalog in your installed XPF version for current availability, access and licensing.

- [Get Modbus Monitor XPF](https://www.modbusmonitor.com/download)

[Public JSON preview](https://modbus-monitor.github.io/modbus-device-maps/maps/socomec/diris-a40-a41-rs485.json) · [Preview data terms](https://modbus-monitor.github.io/modbus-device-maps/data-license/)

## Register Table (Sample)

Sample registers from the Socomec DIRIS A40 / A41 RS485 Modbus map. Confirm the sample against the exact device and firmware before use.

| Signal | Address | Type | Units | Category |
|---|---:|---|---|---|
| Phase to phase voltage u12 V | 410513 | UINT32 | V | Voltage |
| Phase current 1 | 410527 | UINT32 | - | Current |
| active power kW | 410535 | UINT32 | kW | Power |
| Active energy | 410769 | UINT32 | kWh | Energy |
| Frequency Hz | 410525 | UINT32 | Hz | Frequency |
| Internal temperature sensor present | 411455 | UINT16 | degC | Temperature |
| Thd u12 | 411535 | UINT16 | - | Harmonics |
| Hour meter 1 | 410511 | UINT32 | - | General |
| Phase to phase voltage u23 V | 410515 | UINT32 | V | Voltage |
| Phase to phase voltage u31 V | 410517 | UINT32 | V | Voltage |
| Phase to neutral voltage phase 1 V | 410519 | UINT32 | V | Voltage |
| Phase to neutral voltage phase 2 V | 410521 | UINT32 | V | Voltage |

## How to Use This Map

1. **Download Modbus Monitor XPF** — [Get the free version](https://www.modbusmonitor.com/download).
2. **Select the Socomec DIRIS A40 / A41 RS485 device map** — check availability and access in the installed application catalog.
3. **Connect to your device** — confirm transport, addressing and data types before starting a read operation.
4. **Visualise and log** — build dashboards, trend data, and export readings without manual register entry.

## Why Use Pre-Built Maps

- **Saves time** — no need to manually look up or enter register addresses
- **Reduces errors** — reusable maps reduce repeated manual entry; validate addresses and data types for your device
- **Speeds commissioning** — connect and poll within minutes instead of hours
- **Reusable across projects** — use the same map across multiple sites and installations

## Data Categories Available

- Harmonics
- Power
- Voltage
- Current
- Temperature
- Frequency

## Related Tools

- [Modbus Monitor XPF — Windows Modbus Tool](https://www.modbusmonitor.com/download)
- [Modbus HMI Builder](https://www.modbusmonitor.com/modbus-hmi)
- [Compare Modbus Monitor XPF with Other Tools](https://www.modbusmonitor.com/compare)

## Related Device Maps

- [Socomec DIRIS I31 Modbus Register Map](./diris-i31.md)
- [Socomec DIRIS U30 Modbus Register Map](./diris-u30.md)
- [Socomec Countis ECI3 Modbus Register Map](./countis-eci3.md)
- [Socomec Countis ECI2 Modbus Register Map](./countis-eci2.md)
- [All Socomec Modbus Register Maps](./index.md)
- [All XPF Device Maps](../../../../modbus-device-maps/index.md)

<!-- public-preview-metadata -->
<script type="application/ld+json">{"@context": "https://schema.org", "@type": "Dataset", "name": "Socomec DIRIS A40, A41, RS485 public register preview", "description": "Sample register addresses and data types; not a complete map or hardware verification.", "url": "https://docs.quantumbitsolutions.com/products/xpf/device-maps/socomec/diris-a40-a41-rs485/", "license": "https://modbus-monitor.github.io/modbus-device-maps/data-license/", "creator": {"@type": "Organization", "name": "Quantum Bit Solutions", "url": "https://quantumbitsolutions.com/"}, "distribution": {"@type": "DataDownload", "encodingFormat": "application/json", "contentUrl": "https://modbus-monitor.github.io/modbus-device-maps/maps/socomec/diris-a40-a41-rs485.json"}}</script>
<!-- /public-preview-metadata -->
