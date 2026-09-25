---
title: Eaton IQ100 series,IQ130,IQ140,IQ150 Modbus Register Map
description: Eaton IQ100 series,IQ130,IQ140,IQ150 Modbus map and register map with sample Modbus registers, register addresses, and power meter overview for engineers. Includes sample addresses and data types for review before use with Modbus Monitor XPF.
---

# Eaton IQ100 series,IQ130,IQ140,IQ150 Modbus Register Map

The Eaton IQ100 series,IQ130,IQ140,IQ150 is a power meter used for power monitoring, energy metering, and facility automation. This page provides a sample Modbus register map with addresses, data types, and signal categories to help engineers commission, troubleshoot, and monitor the device. For Eaton IQ100 series,IQ130,IQ140,IQ150 deployments, teams often use this map to surface current, energy, and demand data in critical power distribution and electrical monitoring systems.

This page shows a public register preview. Check the catalog in your installed XPF version for complete-map availability and licensing.

Confirm the exact model and firmware, address base, register function, word order, scaling and units against the manufacturer manual before polling. This preview does not establish hardware validation.

## Overview

- **Device:** Eaton IQ100 series,IQ130,IQ140,IQ150
- **Type:** Power Meter
- **Protocol:** Confirm the supported transport for the exact device and firmware in the manufacturer manual.
- **Use case:** power monitoring, energy metering, and facility automation
- **Works with:** Modbus Monitor XPF (import directly)

## Download Modbus Map

The sample below is a public preview. Check the catalog in your installed XPF version for current availability, access and licensing.

- [Get Modbus Monitor XPF](https://www.modbusmonitor.com/download)

[Public JSON preview](https://modbus-monitor.github.io/modbus-device-maps/maps/eaton/iq100-series-iq130-iq140-iq150.json) · [Preview data terms](https://modbus-monitor.github.io/modbus-device-maps/data-license/)

## Register Table (Sample)

Sample registers from the Eaton IQ100 series,IQ130,IQ140,IQ150 Modbus map. Confirm the sample against the exact device and firmware before use.

| Signal | Address | Type | Units | Category |
|---|---:|---|---|---|
| Amps A amps | 401011 | FLOAT32 | A | Current |
| Positive Power Factor 3 Ph Maximum Avg Demand none | 403127 | FLOAT32 | PF | Power |
| Power Energy Format pppp nn eee ddd | 430005 | UINT16 | kWh | Energy |
| Frequency Hz | 401025 | FLOAT32 | Hz | Frequency |
| Positive pf 3 ph average -100 to 100 | 402015 | FLOAT32 | - | Power Factor |
| Positive Watts 3 Ph Maximum Avg Demand watts | 403117 | FLOAT32 | kW | Demand |
| Meter status bit-mapped | 404999 | UINT16 | - | Status |
| Meter Serial Number:8 | 400008 | STRING | - | Identification |
| Meter type bit-mapped | 400016 | UINT16 | - | General |
| Amps B amps | 401013 | FLOAT32 | A | Current |
| Amps C amps | 401015 | FLOAT32 | A | Current |
| Neutral current amps | 401027 | FLOAT32 | A | Current |

## How to Use This Map

1. **Download Modbus Monitor XPF** — [Get the free version](https://www.modbusmonitor.com/download).
2. **Select the Eaton IQ100 series,IQ130,IQ140,IQ150 device map** — check availability and access in the installed application catalog.
3. **Connect to your device** — confirm transport, addressing and data types before starting a read operation.
4. **Visualise and log** — build dashboards, trend data, and export readings without manual register entry.

## Why Use Pre-Built Maps

- **Saves time** — no need to manually look up or enter register addresses
- **Reduces errors** — reusable maps reduce repeated manual entry; validate addresses and data types for your device
- **Speeds commissioning** — connect and poll within minutes instead of hours
- **Reusable across projects** — use the same map across multiple sites and installations

## Data Categories Available

- Current
- Energy
- Demand
- Frequency
- Power
- Power Factor

## Related Tools

- [Modbus Monitor XPF — Windows Modbus Tool](https://www.modbusmonitor.com/download)
- [Modbus HMI Builder](https://www.modbusmonitor.com/modbus-hmi)
- [Compare Modbus Monitor XPF with Other Tools](https://www.modbusmonitor.com/compare)

## Related Device Maps

- [Eaton 93PM Modbus Register Map](./93pm.md)
- [Eaton BladeUPS Modbus Register Map](./bladeups.md)
- [Eaton PXM2000 Modbus Register Map](./pxm2000.md)
- [Eaton EM19 M Modbus Register Map](./em19-m.md)
- [All Eaton Modbus Register Maps](./index.md)
- [All XPF Device Maps](../../../../modbus-device-maps/index.md)

<!-- public-preview-metadata -->
<script type="application/ld+json">{"@context": "https://schema.org", "@type": "Dataset", "name": "Eaton IQ100 series,IQ130,IQ140,IQ150 public register preview", "description": "Sample register addresses and data types; not a complete map or hardware verification.", "url": "https://docs.quantumbitsolutions.com/products/xpf/device-maps/eaton/iq100-series-iq130-iq140-iq150/", "license": "https://modbus-monitor.github.io/modbus-device-maps/data-license/", "creator": {"@type": "Organization", "name": "Quantum Bit Solutions", "url": "https://quantumbitsolutions.com/"}, "distribution": {"@type": "DataDownload", "encodingFormat": "application/json", "contentUrl": "https://modbus-monitor.github.io/modbus-device-maps/maps/eaton/iq100-series-iq130-iq140-iq150.json"}}</script>
<!-- /public-preview-metadata -->
