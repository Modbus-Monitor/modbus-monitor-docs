---
title: Siemens SEM3 Series Modbus Register Map
description: Siemens SEM3 Series Modbus map and register map with sample Modbus registers, register addresses, and power meter overview for engineers. Includes sample addresses and data types for review before use with Modbus Monitor XPF.
---

# Siemens SEM3 Series Modbus Register Map

The Siemens SEM3 Series is a power meter used for power monitoring, energy metering, and facility automation. This page provides a sample Modbus register map with addresses, data types, and signal categories to help engineers commission, troubleshoot, and monitor the device. For Siemens SEM3 Series deployments, teams often use this map to surface current, power, and status data in industrial automation panels and building management systems.

This page shows a public register preview. Check the catalog in your installed XPF version for complete-map availability and licensing.

Confirm the exact model and firmware, address base, register function, word order, scaling and units against the manufacturer manual before polling. This preview does not establish hardware validation.

## Overview

- **Device:** Siemens SEM3 Series
- **Type:** Power Meter
- **Protocol:** Confirm the supported transport for the exact device and firmware in the manufacturer manual.
- **Use case:** power monitoring, energy metering, and facility automation
- **Works with:** Modbus Monitor XPF (import directly)

## Download Modbus Map

The sample below is a public preview. Check the catalog in your installed XPF version for current availability, access and licensing.

- [Get Modbus Monitor XPF](https://www.modbusmonitor.com/download)

[Public JSON preview](https://modbus-monitor.github.io/modbus-device-maps/maps/siemens/sem3-series.json) · [Preview data terms](https://modbus-monitor.github.io/modbus-device-maps/data-license/)

## Register Table (Sample)

Sample registers from the Siemens SEM3 Series Modbus map. Confirm the sample against the exact device and firmware before use.

| Signal | Address | Type | Units | Category |
|---|---:|---|---|---|
| Monitor 1 current phase 1 Amps | 411906 | FLOAT32 | A | Current |
| Monitor 1 power factor phase 1 1 | 411930 | FLOAT32 | PF | Power |
| Monitor 1 alarm flags | 400200 | UINT16 | - | Status |
| Monitor 1 volts phase 1 Volts | 411900 | FLOAT32 | - | General |
| Monitor 2 alarm flags | 400201 | UINT16 | - | Status |
| Monitor 3 alarm flags | 400202 | UINT16 | - | Status |
| Monitor 4 alarm flags | 400203 | UINT16 | - | Status |
| Monitor 5 alarm flags | 400204 | UINT16 | - | Status |
| Monitor 6 alarm flags | 400205 | UINT16 | - | Status |
| Monitor 7 alarm flags | 400206 | UINT16 | - | Status |
| Monitor 8 alarm flags | 400207 | UINT16 | - | Status |
| Monitor 9 alarm flags | 400208 | UINT16 | - | Status |

## How to Use This Map

1. **Download Modbus Monitor XPF** — [Get the free version](https://www.modbusmonitor.com/download).
2. **Select the Siemens SEM3 Series device map** — check availability and access in the installed application catalog.
3. **Connect to your device** — confirm transport, addressing and data types before starting a read operation.
4. **Visualise and log** — build dashboards, trend data, and export readings without manual register entry.

## Why Use Pre-Built Maps

- **Saves time** — no need to manually look up or enter register addresses
- **Reduces errors** — reusable maps reduce repeated manual entry; validate addresses and data types for your device
- **Speeds commissioning** — connect and poll within minutes instead of hours
- **Reusable across projects** — use the same map across multiple sites and installations

## Data Categories Available

- Current
- Power
- Status

## Related Tools

- [Modbus Monitor XPF — Windows Modbus Tool](https://www.modbusmonitor.com/download)
- [Modbus HMI Builder](https://www.modbusmonitor.com/modbus-hmi)
- [Compare Modbus Monitor XPF with Other Tools](https://www.modbusmonitor.com/compare)

## Related Device Maps

- [Siemens PAC3200 Modbus Register Map](./sentron-pac-3200.md)
- [Siemens PAC4200 Modbus Register Map](./sentron-pac-4200.md)
- [Siemens PAC2200 Modbus Register Map](./sentron-pac-2200.md)
- [Siemens SICAM P Modbus Register Map](./sicam-p.md)
- [All Siemens Modbus Register Maps](./index.md)
- [All XPF Device Maps](../../../../modbus-device-maps/index.md)

<!-- public-preview-metadata -->
<script type="application/ld+json">{"@context": "https://schema.org", "@type": "Dataset", "name": "Siemens SEM3 Series public register preview", "description": "Sample register addresses and data types; not a complete map or hardware verification.", "url": "https://docs.quantumbitsolutions.com/products/xpf/device-maps/siemens/sem3-series/", "license": "https://modbus-monitor.github.io/modbus-device-maps/data-license/", "creator": {"@type": "Organization", "name": "Quantum Bit Solutions", "url": "https://quantumbitsolutions.com/"}, "distribution": {"@type": "DataDownload", "encodingFormat": "application/json", "contentUrl": "https://modbus-monitor.github.io/modbus-device-maps/maps/siemens/sem3-series.json"}}</script>
<!-- /public-preview-metadata -->
