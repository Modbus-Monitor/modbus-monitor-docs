---
title: Siemens PAC2200 Modbus Register Map
description: Siemens PAC2200 Modbus map and register map with sample Modbus registers, register addresses, and power meter overview for engineers. Includes sample addresses and data types for review before use with Modbus Monitor XPF.
---

# Siemens PAC2200 Modbus Register Map

The Siemens PAC2200 is a power meter used for power monitoring, energy metering, and facility automation. This page provides a sample Modbus register map with addresses, data types, and signal categories to help engineers commission, troubleshoot, and monitor the device. For Siemens PAC2200 deployments, teams often use this map to surface power, current, and voltage data in industrial automation panels and building management systems.

This page shows a public register preview. Check the catalog in your installed XPF version for complete-map availability and licensing.

Confirm the exact model and firmware, address base, register function, word order, scaling and units against the manufacturer manual before polling. This preview does not establish hardware validation.

## Overview

- **Device:** Siemens PAC2200
- **Type:** Power Meter
- **Protocol:** Confirm the supported transport for the exact device and firmware in the manufacturer manual.
- **Use case:** power monitoring, energy metering, and facility automation
- **Works with:** Modbus Monitor XPF (import directly)

## Download Modbus Map

The sample below is a public preview. Check the catalog in your installed XPF version for current availability, access and licensing.

- [Get Modbus Monitor XPF](https://www.modbusmonitor.com/download)

[Public JSON preview](https://modbus-monitor.github.io/modbus-device-maps/maps/siemens/sentron-pac-2200.json) · [Preview data terms](https://modbus-monitor.github.io/modbus-device-maps/data-license/)

## Register Table (Sample)

Sample registers from the Siemens PAC2200 Modbus map. Confirm the sample against the exact device and firmware before use.

| Signal | Address | Type | Units | Category |
|---|---:|---|---|---|
| Voltage UL1 N | 400002 | FLOAT32 | V | Voltage |
| Current L1 | 400014 | FLOAT32 | A | Current |
| Apparent power L1 | 400020 | FLOAT32 | kW | Power |
| Secondary total of active energy im port | 400962 | DOUBLE64 | kWh | Energy |
| Frequency | 400056 | FLOAT32 | Hz | Frequency |
| Device diagnostics and device status | 400206 | UINT32 | - | Status |
| Active tariff | 400212 | UINT32 | - | General |
| Voltage UL2 N | 400004 | FLOAT32 | V | Voltage |
| Voltage UL3 N | 400006 | FLOAT32 | V | Voltage |
| Voltage UL1 L2 | 400008 | FLOAT32 | V | Voltage |
| Voltage UL2 L3 | 400010 | FLOAT32 | V | Voltage |
| Voltage UL3 L1 | 400012 | FLOAT32 | V | Voltage |

## How to Use This Map

1. **Download Modbus Monitor XPF** — [Get the free version](https://www.modbusmonitor.com/download).
2. **Select the Siemens PAC2200 device map** — check availability and access in the installed application catalog.
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
- Frequency

## Related Tools

- [Modbus Monitor XPF — Windows Modbus Tool](https://www.modbusmonitor.com/download)
- [Modbus HMI Builder](https://www.modbusmonitor.com/modbus-hmi)
- [Compare Modbus Monitor XPF with Other Tools](https://www.modbusmonitor.com/compare)

## Related Device Maps

- [Siemens PAC3200 Modbus Register Map](./sentron-pac-3200.md)
- [Siemens PAC4200 Modbus Register Map](./sentron-pac-4200.md)
- [Siemens SICAM P Modbus Register Map](./sicam-p.md)
- [Siemens SEM3 Series Modbus Register Map](./sem3-series.md)
- [All Siemens Modbus Register Maps](./index.md)
- [All XPF Device Maps](../../../../modbus-device-maps/index.md)

<!-- public-preview-metadata -->
<script type="application/ld+json">{"@context": "https://schema.org", "@type": "Dataset", "name": "Siemens PAC2200 public register preview", "description": "Sample register addresses and data types; not a complete map or hardware verification.", "url": "https://docs.quantumbitsolutions.com/products/xpf/device-maps/siemens/sentron-pac-2200/", "license": "https://modbus-monitor.github.io/modbus-device-maps/data-license/", "creator": {"@type": "Organization", "name": "Quantum Bit Solutions", "url": "https://quantumbitsolutions.com/"}, "distribution": {"@type": "DataDownload", "encodingFormat": "application/json", "contentUrl": "https://modbus-monitor.github.io/modbus-device-maps/maps/siemens/sentron-pac-2200.json"}}</script>
<!-- /public-preview-metadata -->
