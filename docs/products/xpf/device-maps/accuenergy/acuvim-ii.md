---
title: Accuenergy Acuvim II Modbus Register Map
description: Accuenergy Acuvim II Modbus map and register map with sample Modbus registers, register addresses, and power meter overview for engineers. Includes sample addresses and data types for review before use with Modbus Monitor XPF.
---

# Accuenergy Acuvim II Modbus Register Map

The Accuenergy Acuvim II is a power meter used for power monitoring, energy metering, and facility automation. This page provides a sample Modbus register map with addresses, data types, and signal categories to help engineers commission, troubleshoot, and monitor the device. For Accuenergy Acuvim II deployments, teams often use this map to surface power, energy, and current data in multi-circuit energy monitoring, tenant billing, and branch circuit analytics.

This page shows a public register preview. Check the catalog in your installed XPF version for complete-map availability and licensing.

Confirm the exact model and firmware, address base, register function, word order, scaling and units against the manufacturer manual before polling. This preview does not establish hardware validation.

## Overview

- **Device:** Accuenergy Acuvim II
- **Type:** Power Meter
- **Protocol:** Confirm the supported transport for the exact device and firmware in the manufacturer manual.
- **Use case:** power monitoring, energy metering, and facility automation
- **Works with:** Modbus Monitor XPF (import directly)

## Download Modbus Map

The sample below is a public preview. Check the catalog in your installed XPF version for current availability, access and licensing.

- [Get Modbus Monitor XPF](https://www.modbusmonitor.com/download)

[Public JSON preview](https://modbus-monitor.github.io/modbus-device-maps/maps/accuenergy/acuvim-ii.json) · [Preview data terms](https://modbus-monitor.github.io/modbus-device-maps/data-license/)

## Register Table (Sample)

Sample registers from the Accuenergy Acuvim II Modbus map. Confirm the sample against the exact device and firmware before use.

| Signal | Address | Type | Units | Category |
|---|---:|---|---|---|
| Voltage Input Wiring Type 0 3LN 1 1LN 2 2LL 3 3LL 4 1LL | 404100 | UINT16 | V | Voltage |
| Current Input Wiring Type 0 3CT 1 1CT 2 2CT | 404101 | UINT16 | - | Current |
| Reactive Power Calculation Method 0 True Reactive Power 1 Generic Reactive Power | 404121 | UINT16 | kW | Power |
| kWh Pulse Constant 1 60000 | 404107 | UINT16 | kWh | Energy |
| Frequency Selection 0 50Hz 1 60Hz | 404094 | UINT16 | Hz | Frequency |
| VAR PF Convention 0 IEC 1 IEEE | 404118 | UINT16 | - | Power Factor |
| Demand Interval 1 30 | 404110 | UINT16 | kW | Demand |
| Seal Status 0x0A Sealed Other Unsealed | 404128 | UINT16 | - | Status |
| THD V1 V12 THD Rx 100 | 416475 | INT16 | - | Harmonics |
| Channel 1 Communication Protocol 0 Modbus 2 BACnet MS TP | 404095 | UINT16 | - | Communication |
| Channel 1 Parity 0 Even 1 Odd 2 None2 3 None1 | 404096 | UINT16 | - | General |
| kvarh Pulse Constant 1 60000 | 404108 | UINT16 | kWh | Energy |

## How to Use This Map

1. **Download Modbus Monitor XPF** — [Get the free version](https://www.modbusmonitor.com/download).
2. **Select the Accuenergy Acuvim II device map** — check availability and access in the installed application catalog.
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
- Current
- Voltage
- Harmonics
- Status

## Related Tools

- [Modbus Monitor XPF — Windows Modbus Tool](https://www.modbusmonitor.com/download)
- [Modbus HMI Builder](https://www.modbusmonitor.com/modbus-hmi)
- [Compare Modbus Monitor XPF with Other Tools](https://www.modbusmonitor.com/compare)

## Related Device Maps

- [All Accuenergy Modbus Register Maps](./index.md)
- [All XPF Device Maps](../../../../modbus-device-maps/index.md)

<!-- public-preview-metadata -->
<script type="application/ld+json">{"@context": "https://schema.org", "@type": "Dataset", "name": "Accuenergy Acuvim II public register preview", "description": "Sample register addresses and data types; not a complete map or hardware verification.", "url": "https://docs.quantumbitsolutions.com/products/xpf/device-maps/accuenergy/acuvim-ii/", "license": "https://modbus-monitor.github.io/modbus-device-maps/data-license/", "creator": {"@type": "Organization", "name": "Quantum Bit Solutions", "url": "https://quantumbitsolutions.com/"}, "distribution": {"@type": "DataDownload", "encodingFormat": "application/json", "contentUrl": "https://modbus-monitor.github.io/modbus-device-maps/maps/accuenergy/acuvim-ii.json"}}</script>
<!-- /public-preview-metadata -->
