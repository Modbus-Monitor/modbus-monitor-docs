---
title: SEL SEL-751A Modbus Register Map
description: SEL SEL-751A Modbus map and register map with sample Modbus registers, register addresses, and relay overview for engineers. Includes sample addresses and data types for review before use with Modbus Monitor XPF.
---

# SEL SEL-751A Modbus Register Map

The SEL SEL-751A is a relay used for commissioning, troubleshooting, and operational monitoring. This page provides a sample Modbus register map with addresses, data types, and signal categories to help engineers commission, troubleshoot, and monitor the device. For SEL SEL-751A deployments, teams often use this map to surface demand, power factor, and energy data in utility metering, substations, and power quality analysis.

This page shows a public register preview. Check the catalog in your installed XPF version for complete-map availability and licensing.

Confirm the exact model and firmware, address base, register function, word order, scaling and units against the manufacturer manual before polling. This preview does not establish hardware validation.

## Overview

- **Device:** SEL SEL-751A
- **Type:** Relay
- **Protocol:** Confirm the supported transport for the exact device and firmware in the manufacturer manual.
- **Use case:** commissioning, troubleshooting, and operational monitoring
- **Works with:** Modbus Monitor XPF (import directly)

## Download Modbus Map

The sample below is a public preview. Check the catalog in your installed XPF version for current availability, access and licensing.

- [Get Modbus Monitor XPF](https://www.modbusmonitor.com/download)

[Public JSON preview](https://modbus-monitor.github.io/modbus-device-maps/maps/sel/sel-751a.json) · [Preview data terms](https://modbus-monitor.github.io/modbus-device-maps/data-license/)

## Register Table (Sample)

Sample registers from the SEL SEL-751A Modbus map. Confirm the sample against the exact device and firmware before use.

| Signal | Address | Type | Units | Category |
|---|---:|---|---|---|
| PercentVoltageUnbalance | 300685 | FLOAT32 | V | Voltage |
| PercentCurrentUnbalance | 300664 | FLOAT32 | - | Current |
| ReverseEnergy | 300691 | FLOAT32 | kWh | Energy |
| PFapparentTotal | 300689 | FLOAT32 | - | Power Factor |
| DemandIa | 301690 | FLOAT32 | kW | Demand |
| BFActive | 300267 | UINT16 | - | General |
| ForwardEnergy | 300705 | FLOAT32 | kWh | Energy |
| PFapparentA | 301485 | FLOAT32 | - | Power Factor |
| PFapparentB | 301489 | FLOAT32 | - | Power Factor |
| PFapparentC | 301493 | FLOAT32 | - | Power Factor |
| DemandIb | 301691 | FLOAT32 | kW | Demand |
| DemandIc | 301692 | FLOAT32 | kW | Demand |

## How to Use This Map

1. **Download Modbus Monitor XPF** — [Get the free version](https://www.modbusmonitor.com/download).
2. **Select the SEL SEL-751A device map** — check availability and access in the installed application catalog.
3. **Connect to your device** — confirm transport, addressing and data types before starting a read operation.
4. **Visualise and log** — build dashboards, trend data, and export readings without manual register entry.

## Why Use Pre-Built Maps

- **Saves time** — no need to manually look up or enter register addresses
- **Reduces errors** — reusable maps reduce repeated manual entry; validate addresses and data types for your device
- **Speeds commissioning** — connect and poll within minutes instead of hours
- **Reusable across projects** — use the same map across multiple sites and installations

## Data Categories Available

- Demand
- Power Factor
- Energy
- Current
- Voltage

## Related Tools

- [Modbus Monitor XPF — Windows Modbus Tool](https://www.modbusmonitor.com/download)
- [Modbus HMI Builder](https://www.modbusmonitor.com/modbus-hmi)
- [Compare Modbus Monitor XPF with Other Tools](https://www.modbusmonitor.com/compare)

## Related Device Maps

- [SEL SEL-735 Modbus Register Map](./sel-735.md)
- [SEL SEL-351A Modbus Register Map](./sel-351a.md)
- [SEL SEL-710 Modbus Register Map](./sel-710.md)
- [All SEL Modbus Register Maps](./index.md)
- [All XPF Device Maps](../../../../modbus-device-maps/index.md)

<!-- public-preview-metadata -->
<script type="application/ld+json">{"@context": "https://schema.org", "@type": "Dataset", "name": "SEL SEL-751A public register preview", "description": "Sample register addresses and data types; not a complete map or hardware verification.", "url": "https://docs.quantumbitsolutions.com/products/xpf/device-maps/sel/sel-751a/", "license": "https://modbus-monitor.github.io/modbus-device-maps/data-license/", "creator": {"@type": "Organization", "name": "Quantum Bit Solutions", "url": "https://quantumbitsolutions.com/"}, "distribution": {"@type": "DataDownload", "encodingFormat": "application/json", "contentUrl": "https://modbus-monitor.github.io/modbus-device-maps/maps/sel/sel-751a.json"}}</script>
<!-- /public-preview-metadata -->
