---
title: Socomec DIRIS I31 Modbus Register Map
description: Socomec DIRIS I31 Modbus map and register map with sample Modbus registers, register addresses, and power meter overview for engineers. Includes sample addresses and data types for review before use with Modbus Monitor XPF.
---

# Socomec DIRIS I31 Modbus Register Map

The Socomec DIRIS I31 is a power meter used for power monitoring, energy metering, and facility automation. This page provides a sample Modbus register map with addresses, data types, and signal categories to help engineers commission, troubleshoot, and monitor the device. For Socomec DIRIS I31 deployments, teams often use this map to surface energy, power, and voltage data in facility metering, commissioning, and operational analytics.

This page shows a public register preview. Check the catalog in your installed XPF version for complete-map availability and licensing.

Confirm the exact model and firmware, address base, register function, word order, scaling and units against the manufacturer manual before polling. This preview does not establish hardware validation.

## Overview

- **Device:** Socomec DIRIS I31
- **Type:** Power Meter
- **Protocol:** Confirm the supported transport for the exact device and firmware in the manufacturer manual.
- **Use case:** power monitoring, energy metering, and facility automation
- **Works with:** Modbus Monitor XPF (import directly)

## Download Modbus Map

The sample below is a public preview. Check the catalog in your installed XPF version for current availability, access and licensing.

- [Get Modbus Monitor XPF](https://www.modbusmonitor.com/download)

[Public JSON preview](https://modbus-monitor.github.io/modbus-device-maps/maps/socomec/diris-i31.json) · [Preview data terms](https://modbus-monitor.github.io/modbus-device-maps/data-license/)

## Register Table (Sample)

Sample registers from the Socomec DIRIS I31 Modbus map. Confirm the sample against the exact device and firmware before use.

| Signal | Address | Type | Units | Category |
|---|---:|---|---|---|
| Ph N Voltage V1 V | 418444 | UINT32 | V | Voltage |
| Current I1 mA | 418458 | UINT32 | - | Current |
| Total active power W | 418476 | INT32 | kW | Power |
| Total Positive active Energy EaP kWh | 419841 | UINT32 | kWh | Energy |
| Frequency mHz | 418442 | UINT32 | Hz | Frequency |
| Load status | 418432 | UINT16 | - | Status |
| SOCO :4 | 450000 | STRING | - | General |
| MODBUS Table Version | 450006 | UINT16 | - | Identification |
| Ph N Voltage V2 V | 418446 | UINT32 | V | Voltage |
| Ph N Voltage V3 V | 418448 | UINT32 | V | Voltage |
| Ph Ph Voltage U12 V | 418452 | UINT32 | V | Voltage |
| Ph Ph Voltage U23 V | 418454 | UINT32 | V | Voltage |

## How to Use This Map

1. **Download Modbus Monitor XPF** — [Get the free version](https://www.modbusmonitor.com/download).
2. **Select the Socomec DIRIS I31 device map** — check availability and access in the installed application catalog.
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
- Voltage
- Status
- Current
- Frequency

## Related Tools

- [Modbus Monitor XPF — Windows Modbus Tool](https://www.modbusmonitor.com/download)
- [Modbus HMI Builder](https://www.modbusmonitor.com/modbus-hmi)
- [Compare Modbus Monitor XPF with Other Tools](https://www.modbusmonitor.com/compare)

## Related Device Maps

- [Socomec DIRIS A40 / A41 RS485 Modbus Register Map](./diris-a40-a41-rs485.md)
- [Socomec DIRIS U30 Modbus Register Map](./diris-u30.md)
- [Socomec Countis ECI3 Modbus Register Map](./countis-eci3.md)
- [Socomec Countis ECI2 Modbus Register Map](./countis-eci2.md)
- [All Socomec Modbus Register Maps](./index.md)
- [All XPF Device Maps](../../../../modbus-device-maps/index.md)

<!-- public-preview-metadata -->
<details><summary>Public catalog sample</summary><p>The public JSON sample differs from the guide table above. Both are previews; confirm the exact model and firmware before use.</p><table><thead><tr><th>Signal</th><th>Display address</th><th>Data type</th><th>Units</th><th>Category</th></tr></thead><tbody><tr><td>Inst Measurement Load 1 Ph N voltage V1 V</td><td>418444</td><td>UINT32</td><td>V</td><td>Voltage</td></tr><tr><td>Inst Measurement Load 1 Current I1 A</td><td>418458</td><td>UINT32</td><td>-</td><td>Current</td></tr><tr><td>Inst Measurement Load 1 Total active power W</td><td>418476</td><td>INT32</td><td>kW</td><td>Power</td></tr><tr><td>Energy measurement Load 1 Total positive active energy ea Wh</td><td>419841</td><td>UINT32</td><td>kWh</td><td>Energy</td></tr><tr><td>Inst Measurement Load 1 Frequency Hz</td><td>418442</td><td>UINT32</td><td>Hz</td><td>Frequency</td></tr><tr><td>Inst Measurement Load 1 Integration time s</td><td>418435</td><td>UINT16</td><td>-</td><td>General</td></tr><tr><td>Inst Measurement Load 1 Ph N voltage V2 V</td><td>418446</td><td>UINT32</td><td>V</td><td>Voltage</td></tr><tr><td>Inst Measurement Load 1 Ph N voltage V3 V</td><td>418448</td><td>UINT32</td><td>V</td><td>Voltage</td></tr><tr><td>Inst Measurement Load 1 Ph ph voltage U12 V</td><td>418452</td><td>UINT32</td><td>V</td><td>Voltage</td></tr><tr><td>Inst Measurement Load 1 Ph ph voltage U23 V</td><td>418454</td><td>UINT32</td><td>V</td><td>Voltage</td></tr><tr><td>Inst Measurement Load 1 Ph ph voltage U31 V</td><td>418456</td><td>UINT32</td><td>V</td><td>Voltage</td></tr><tr><td>Inst Measurement Load 1 Current I2 A</td><td>418460</td><td>UINT32</td><td>-</td><td>Current</td></tr></tbody></table></details>
<script type="application/ld+json">{"@context": "https://schema.org", "@type": "Dataset", "name": "Socomec DIRIS I31 public register preview", "description": "Sample register addresses and data types; not a complete map or hardware verification.", "url": "https://docs.quantumbitsolutions.com/products/xpf/device-maps/socomec/diris-i31/", "license": "https://modbus-monitor.github.io/modbus-device-maps/data-license/", "creator": {"@type": "Organization", "name": "Quantum Bit Solutions", "url": "https://quantumbitsolutions.com/"}, "distribution": {"@type": "DataDownload", "encodingFormat": "application/json", "contentUrl": "https://modbus-monitor.github.io/modbus-device-maps/maps/socomec/diris-i31.json"}}</script>
<!-- /public-preview-metadata -->
