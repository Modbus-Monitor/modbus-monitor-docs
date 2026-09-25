---
title: Socomec Countis E33, Countis E43 Modbus Register Map
description: Socomec Countis E33, Countis E43 Modbus map and register map with sample Modbus registers, register addresses, and power meter overview for engineers. Includes sample addresses and data types for review before use with Modbus Monitor XPF.
---

# Socomec Countis E33, Countis E43 Modbus Register Map

The Socomec Countis E33, Countis E43 is a power meter used for power monitoring, energy metering, and facility automation. This page provides a sample Modbus register map with addresses, data types, and signal categories to help engineers commission, troubleshoot, and monitor the device. For Socomec Countis E33, Countis E43 deployments, teams often use this map to surface energy, power, and current data in facility metering, commissioning, and operational analytics.

This page shows a public register preview. Check the catalog in your installed XPF version for complete-map availability and licensing.

Confirm the exact model and firmware, address base, register function, word order, scaling and units against the manufacturer manual before polling. This preview does not establish hardware validation.

## Overview

- **Device:** Socomec Countis E33, Countis E43
- **Type:** Power Meter
- **Protocol:** Confirm the supported transport for the exact device and firmware in the manufacturer manual.
- **Use case:** power monitoring, energy metering, and facility automation
- **Works with:** Modbus Monitor XPF (import directly)

## Download Modbus Map

The sample below is a public preview. Check the catalog in your installed XPF version for current availability, access and licensing.

- [Get Modbus Monitor XPF](https://www.modbusmonitor.com/download)

[Public JSON preview](https://modbus-monitor.github.io/modbus-device-maps/maps/socomec/countis-e33-countis-e43.json) · [Preview data terms](https://modbus-monitor.github.io/modbus-device-maps/data-license/)

## Register Table (Sample)

Sample registers from the Socomec Countis E33, Countis E43 Modbus map. Confirm the sample against the exact device and firmware before use.

| Signal | Address | Type | Units | Category |
|---|---:|---|---|---|
| Phase to Phase Voltage U12 V | 450514 | UINT32 | V | Voltage |
| Current Transformer secondary | 457345 | UINT16 | - | Current |
| Active Power P P W | 450536 | INT32 | kW | Power |
| Partial Positive Active Energy EaP Wh | 450780 | UINT32 | kWh | Energy |
| Frequency F Hz | 450526 | UINT32 | Hz | Frequency |
| MID status 0 non MID product 1 MID product | 440545 | UINT16 | - | Status |
| SOCO :4 | 450000 | STRING | - | General |
| JBUS Table Version EX 101 Version 1 01 | 450006 | UINT16 | - | Identification |
| Communication Board build date | 438916 | UINT16 | - | Communication |
| Current Transformer primary A | 457346 | UINT16 | - | Current |
| Phase to Phase Voltage U23 V | 450516 | UINT32 | V | Voltage |
| Phase to Phase Voltage U31 V | 450518 | UINT32 | V | Voltage |

## How to Use This Map

1. **Download Modbus Monitor XPF** — [Get the free version](https://www.modbusmonitor.com/download).
2. **Select the Socomec Countis E33, Countis E43 device map** — check availability and access in the installed application catalog.
3. **Connect to your device** — confirm transport, addressing and data types before starting a read operation.
4. **Visualise and log** — build dashboards, trend data, and export readings without manual register entry.

## Why Use Pre-Built Maps

- **Saves time** — no need to manually look up or enter register addresses
- **Reduces errors** — reusable maps reduce repeated manual entry; validate addresses and data types for your device
- **Speeds commissioning** — connect and poll within minutes instead of hours
- **Reusable across projects** — use the same map across multiple sites and installations

## Data Categories Available

- Energy
- Power
- Current
- Voltage
- Power Factor
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
<details><summary>Public catalog sample</summary><p>The public JSON sample differs from the guide table above. Both are previews; confirm the exact model and firmware before use.</p><table><thead><tr><th>Signal</th><th>Display address</th><th>Data type</th><th>Units</th><th>Category</th></tr></thead><tbody><tr><td>Phase to phase voltage U12</td><td>450514</td><td>UINT32</td><td>V</td><td>Voltage</td></tr><tr><td>Current transformer primary</td><td>457346</td><td>UINT16</td><td>-</td><td>Current</td></tr><tr><td>Active power - P</td><td>450536</td><td>INT32</td><td>kW</td><td>Power</td></tr><tr><td>Partial positive active energy ea</td><td>450780</td><td>UINT32</td><td>kWh</td><td>Energy</td></tr><tr><td>Frequency F</td><td>450526</td><td>UINT32</td><td>Hz</td><td>Frequency</td></tr><tr><td>Product name</td><td>450000</td><td>STRING</td><td>-</td><td>Identification</td></tr><tr><td>Product order ID Countis100 protection200 atys300 diris400</td><td>450004</td><td>UINT16</td><td>-</td><td>General</td></tr><tr><td>Communication board VLO</td><td>438919</td><td>STRING</td><td>-</td><td>Communication</td></tr><tr><td>Phase to phase voltage U23</td><td>450516</td><td>UINT32</td><td>V</td><td>Voltage</td></tr><tr><td>Phase to phase voltage U31</td><td>450518</td><td>UINT32</td><td>V</td><td>Voltage</td></tr><tr><td>Simple voltage V1</td><td>450520</td><td>UINT32</td><td>V</td><td>Voltage</td></tr><tr><td>Simple voltage V2</td><td>450522</td><td>UINT32</td><td>V</td><td>Voltage</td></tr></tbody></table></details>
<script type="application/ld+json">{"@context": "https://schema.org", "@type": "Dataset", "name": "Socomec Countis E33, Countis E43 public register preview", "description": "Sample register addresses and data types; not a complete map or hardware verification.", "url": "https://docs.quantumbitsolutions.com/products/xpf/device-maps/socomec/countis-e33-countis-e43/", "license": "https://modbus-monitor.github.io/modbus-device-maps/data-license/", "creator": {"@type": "Organization", "name": "Quantum Bit Solutions", "url": "https://quantumbitsolutions.com/"}, "distribution": {"@type": "DataDownload", "encodingFormat": "application/json", "contentUrl": "https://modbus-monitor.github.io/modbus-device-maps/maps/socomec/countis-e33-countis-e43.json"}}</script>
<!-- /public-preview-metadata -->
