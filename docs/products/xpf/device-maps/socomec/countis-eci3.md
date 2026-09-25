---
title: Socomec Countis ECI3 Modbus Register Map
description: Socomec Countis ECI3 Modbus map and register map with sample Modbus registers, register addresses, and power meter overview for engineers. Includes sample addresses and data types for review before use with Modbus Monitor XPF.
---

# Socomec Countis ECI3 Modbus Register Map

The Socomec Countis ECI3 is a power meter used for power monitoring, energy metering, and facility automation. This page provides a sample Modbus register map with addresses, data types, and signal categories to help engineers commission, troubleshoot, and monitor the device. For Socomec Countis ECI3 deployments, teams often use this map to surface current, frequency, and status data in facility metering, commissioning, and operational analytics.

This page shows a public register preview. Check the catalog in your installed XPF version for complete-map availability and licensing.

Confirm the exact model and firmware, address base, register function, word order, scaling and units against the manufacturer manual before polling. This preview does not establish hardware validation.

## Overview

- **Device:** Socomec Countis ECI3
- **Type:** Power Meter
- **Protocol:** Confirm the supported transport for the exact device and firmware in the manufacturer manual.
- **Use case:** power monitoring, energy metering, and facility automation
- **Works with:** Modbus Monitor XPF (import directly)

## Download Modbus Map

The sample below is a public preview. Check the catalog in your installed XPF version for current availability, access and licensing.

- [Get Modbus Monitor XPF](https://www.modbusmonitor.com/download)

[Public JSON preview](https://modbus-monitor.github.io/modbus-device-maps/maps/socomec/countis-eci3.json) · [Preview data terms](https://modbus-monitor.github.io/modbus-device-maps/data-license/)

## Register Table (Sample)

Sample registers from the Socomec Countis ECI3 Modbus map. Confirm the sample against the exact device and firmware before use.

| Signal | Address | Type | Units | Category |
|---|---:|---|---|---|
| Date Time Current s | 438016 | UINT16 | - | Current |
| Custom Meter Frequency | 439698 | UINT16 | Hz | Frequency |
| Status | 440981 | UINT16 | - | Status |
| Analogical inputs option | 438018 | UINT16 | - | General |
| Name :5 | 439936 | STRING | - | Identification |
| Address | 440448 | UINT16 | - | Communication |
| Custom Meter Frequency | 439725 | UINT16 | Hz | Frequency |
| Custom Meter Frequency | 439752 | UINT16 | Hz | Frequency |
| Custom Meter Frequency | 439779 | UINT16 | Hz | Frequency |
| Custom Meter Frequency | 439806 | UINT16 | Hz | Frequency |
| Custom Meter Frequency | 439833 | UINT16 | Hz | Frequency |
| Custom Meter Frequency | 439860 | UINT16 | Hz | Frequency |

## How to Use This Map

1. **Download Modbus Monitor XPF** — [Get the free version](https://www.modbusmonitor.com/download).
2. **Select the Socomec Countis ECI3 device map** — check availability and access in the installed application catalog.
3. **Connect to your device** — confirm transport, addressing and data types before starting a read operation.
4. **Visualise and log** — build dashboards, trend data, and export readings without manual register entry.

## Why Use Pre-Built Maps

- **Saves time** — no need to manually look up or enter register addresses
- **Reduces errors** — reusable maps reduce repeated manual entry; validate addresses and data types for your device
- **Speeds commissioning** — connect and poll within minutes instead of hours
- **Reusable across projects** — use the same map across multiple sites and installations

## Data Categories Available

- Current
- Frequency
- Status

## Related Tools

- [Modbus Monitor XPF — Windows Modbus Tool](https://www.modbusmonitor.com/download)
- [Modbus HMI Builder](https://www.modbusmonitor.com/modbus-hmi)
- [Compare Modbus Monitor XPF with Other Tools](https://www.modbusmonitor.com/compare)

## Related Device Maps

- [Socomec DIRIS A40 / A41 RS485 Modbus Register Map](./diris-a40-a41-rs485.md)
- [Socomec DIRIS I31 Modbus Register Map](./diris-i31.md)
- [Socomec DIRIS U30 Modbus Register Map](./diris-u30.md)
- [Socomec Countis ECI2 Modbus Register Map](./countis-eci2.md)
- [All Socomec Modbus Register Maps](./index.md)
- [All XPF Device Maps](../../../../modbus-device-maps/index.md)

<!-- public-preview-metadata -->
<details><summary>Public catalog sample</summary><p>The public JSON sample differs from the guide table above. Both are previews; confirm the exact model and firmware before use.</p><table><thead><tr><th>Signal</th><th>Display address</th><th>Data type</th><th>Units</th><th>Category</th></tr></thead><tbody><tr><td>Pulse meter current custom time</td><td>437139</td><td>UINT32</td><td>-</td><td>Current</td></tr><tr><td>Unit 0 A 1 V 2 W 3 kW 4 VAR 5 kVAR 6 VA 7 kVA 8 C 9 F 10 mbar 11 bar 12 custom unit</td><td>439942</td><td>UINT16</td><td>-</td><td>Power</td></tr><tr><td>Unit 0 wh 1 varh 2 VAh 3 M3 4 NM3 5 J 6 imp 7 L 8 custom unit 10 kWh 11 kvarh 12 kVAh 13 KM3 14 kNm3 15 kJ 16 k-imp</td><td>439690</td><td>UINT16</td><td>kWh</td><td>Energy</td></tr><tr><td>Custom meter frequency 0 daily 1 weekly 2 monthly 3 yearly 4 non cyclic</td><td>439698</td><td>UINT16</td><td>Hz</td><td>Frequency</td></tr><tr><td>Mode 0 disabled 1 logical state 2 analogical value 3 combination</td><td>440197</td><td>UINT16</td><td>-</td><td>Status</td></tr><tr><td>Input 1 absolute value</td><td>438020</td><td>UINT32</td><td>-</td><td>General</td></tr><tr><td>Name</td><td>439936</td><td>STRING</td><td>-</td><td>Identification</td></tr><tr><td>Unit 0 A 1 V 2 W 3 kW 4 VAR 5 kVAR 6 VA 7 kVA 8 C 9 F 10 mbar 11 bar 12 custom unit</td><td>439966</td><td>UINT16</td><td>-</td><td>Power</td></tr><tr><td>Logical mode 0 low state 1 high state 2 falling edge 3 rising edge 4 both falling and rising edge</td><td>440201</td><td>UINT16</td><td>-</td><td>Status</td></tr><tr><td>Mode 0 disabled 1 logical state 2 analogical value 3 combination</td><td>440214</td><td>UINT16</td><td>-</td><td>Status</td></tr><tr><td>Logical mode 0 low state 1 high state 2 falling edge 3 rising edge 4 both falling and rising edge</td><td>440218</td><td>UINT16</td><td>-</td><td>Status</td></tr><tr><td>Mode 0 disabled 1 logical state 2 analogical value 3 combination</td><td>440231</td><td>UINT16</td><td>-</td><td>Status</td></tr></tbody></table></details>
<script type="application/ld+json">{"@context": "https://schema.org", "@type": "Dataset", "name": "Socomec Countis ECI3 public register preview", "description": "Sample register addresses and data types; not a complete map or hardware verification.", "url": "https://docs.quantumbitsolutions.com/products/xpf/device-maps/socomec/countis-eci3/", "license": "https://modbus-monitor.github.io/modbus-device-maps/data-license/", "creator": {"@type": "Organization", "name": "Quantum Bit Solutions", "url": "https://quantumbitsolutions.com/"}, "distribution": {"@type": "DataDownload", "encodingFormat": "application/json", "contentUrl": "https://modbus-monitor.github.io/modbus-device-maps/maps/socomec/countis-eci3.json"}}</script>
<!-- /public-preview-metadata -->
