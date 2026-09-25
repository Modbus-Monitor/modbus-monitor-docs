---
title: Socomec DIRIS U20 Modbus Register Map
description: Socomec DIRIS U20 Modbus map and register map with sample Modbus registers, register addresses, and power meter overview for engineers. Includes sample addresses and data types for review before use with Modbus Monitor XPF.
---

# Socomec DIRIS U20 Modbus Register Map

The Socomec DIRIS U20 is a power meter used for power monitoring, energy metering, and facility automation. This page provides a sample Modbus register map with addresses, data types, and signal categories to help engineers commission, troubleshoot, and monitor the device. For Socomec DIRIS U20 deployments, teams often use this map to surface power, current, and voltage data in facility metering, commissioning, and operational analytics.

This page shows a public register preview. Check the catalog in your installed XPF version for complete-map availability and licensing.

Confirm the exact model and firmware, address base, register function, word order, scaling and units against the manufacturer manual before polling. This preview does not establish hardware validation.

## Overview

- **Device:** Socomec DIRIS U20
- **Type:** Power Meter
- **Protocol:** Confirm the supported transport for the exact device and firmware in the manufacturer manual.
- **Use case:** power monitoring, energy metering, and facility automation
- **Works with:** Modbus Monitor XPF (import directly)

## Download Modbus Map

The sample below is a public preview. Check the catalog in your installed XPF version for current availability, access and licensing.

- [Get Modbus Monitor XPF](https://www.modbusmonitor.com/download)

[Public JSON preview](https://modbus-monitor.github.io/modbus-device-maps/maps/socomec/diris-u20.json) · [Preview data terms](https://modbus-monitor.github.io/modbus-device-maps/data-license/)

## Register Table (Sample)

Sample registers from the Socomec DIRIS U20 Modbus map. Confirm the sample against the exact device and firmware before use.

| Signal | Address | Type | Units | Category |
|---|---:|---|---|---|
| Hour meter allocation1 Auxiliary power supply 2 Currents3 phase to phase voltage 4 Input 1 5 Input2 6 Input3 | 436361 | UINT16 | V | Voltage |
| Current Transformer secondary | 457345 | UINT16 | - | Current |
| Reactive Power Calculation | 436369 | UINT16 | kW | Power |
| OUT pulse output value 0 0 1 kWh kvarh1 1 kWh kvarh2 10 kWh kvarh3 100 kWh kvarh4 1000 kWh kvarh5 10000 kWh kvarh | 436359 | UINT16 | kWh | Energy |
| Frequency F Hz | 450526 | UINT32 | Hz | Frequency |
| Alarm Type 1 I2 In3 U4 V5 PP6 QP7 SP8 PFC9 PFL10 THDU11 THDV12 THDI13 HOUR14 F | 436363 | UINT16 | - | Power Factor |
| Alarm Specified time 1 999 s | 436364 | UINT16 | - | Status |
| thd U12 | 451536 | UINT16 | - | Harmonics |
| SOCO :4 | 450000 | STRING | - | General |
| JBUS Table Version EX 101 Version 1 01 | 450006 | UINT16 | - | Identification |
| Product option code bit field bit 1 Metering Optionbit 2 Communication optionbit 3 3 inputs 1 output option | 436096 | UINT16 | - | Communication |
| Current Transformer primary A | 457346 | UINT16 | - | Current |

## How to Use This Map

1. **Download Modbus Monitor XPF** — [Get the free version](https://www.modbusmonitor.com/download).
2. **Select the Socomec DIRIS U20 device map** — check availability and access in the installed application catalog.
3. **Connect to your device** — confirm transport, addressing and data types before starting a read operation.
4. **Visualise and log** — build dashboards, trend data, and export readings without manual register entry.

## Why Use Pre-Built Maps

- **Saves time** — no need to manually look up or enter register addresses
- **Reduces errors** — reusable maps reduce repeated manual entry; validate addresses and data types for your device
- **Speeds commissioning** — connect and poll within minutes instead of hours
- **Reusable across projects** — use the same map across multiple sites and installations

## Data Categories Available

- Power
- Current
- Voltage
- Energy
- Status
- Harmonics

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
<details><summary>Public catalog sample</summary><p>The public JSON sample differs from the guide table above. Both are previews; confirm the exact model and firmware before use.</p><table><thead><tr><th>Signal</th><th>Display address</th><th>Data type</th><th>Units</th><th>Category</th></tr></thead><tbody><tr><td>Inst Measurement Network Ph N voltage V1 V</td><td>436869</td><td>UINT32</td><td>V</td><td>Voltage</td></tr><tr><td>Inst Measurement Network Frequency Hz</td><td>436867</td><td>UINT32</td><td>Hz</td><td>Frequency</td></tr><tr><td>Inst Measurement Network Date of last instance s</td><td>436864</td><td>UINT32</td><td>-</td><td>General</td></tr><tr><td>Inst Measurement Network Ph N voltage V2 V</td><td>436871</td><td>UINT32</td><td>V</td><td>Voltage</td></tr><tr><td>Inst Measurement Network Ph N voltage V3 V</td><td>436873</td><td>UINT32</td><td>V</td><td>Voltage</td></tr><tr><td>Inst Measurement Network Ph ph voltage U12 V</td><td>436875</td><td>UINT32</td><td>V</td><td>Voltage</td></tr><tr><td>Inst Measurement Network Ph ph voltage U23 V</td><td>436877</td><td>UINT32</td><td>V</td><td>Voltage</td></tr><tr><td>Inst Measurement Network Ph ph voltage U31 V</td><td>436879</td><td>UINT32</td><td>V</td><td>Voltage</td></tr><tr><td>Inst Fundamental measurement Network Ph N voltage v1h1 V</td><td>437123</td><td>UINT32</td><td>V</td><td>Voltage</td></tr><tr><td>Inst Fundamental measurement Network Ph N voltage v2h1 V</td><td>437125</td><td>UINT32</td><td>V</td><td>Voltage</td></tr><tr><td>Inst Fundamental measurement Network Ph N voltage v3h1 V</td><td>437127</td><td>UINT32</td><td>V</td><td>Voltage</td></tr><tr><td>Inst Fundamental measurement Network Ph N voltage vnh1 V</td><td>437129</td><td>UINT32</td><td>V</td><td>Voltage</td></tr></tbody></table></details>
<script type="application/ld+json">{"@context": "https://schema.org", "@type": "Dataset", "name": "Socomec DIRIS U20 public register preview", "description": "Sample register addresses and data types; not a complete map or hardware verification.", "url": "https://docs.quantumbitsolutions.com/products/xpf/device-maps/socomec/diris-u20/", "license": "https://modbus-monitor.github.io/modbus-device-maps/data-license/", "creator": {"@type": "Organization", "name": "Quantum Bit Solutions", "url": "https://quantumbitsolutions.com/"}, "distribution": {"@type": "DataDownload", "encodingFormat": "application/json", "contentUrl": "https://modbus-monitor.github.io/modbus-device-maps/maps/socomec/diris-u20.json"}}</script>
<!-- /public-preview-metadata -->
