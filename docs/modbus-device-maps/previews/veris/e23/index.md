---
title: "Veris E23 Modbus register preview"
description: "Sample register addresses and data types for Veris E23. Public preview with JSON source and verification status."
---

# Veris E23 Modbus register preview

Public preview for **Veris E23** (Power Meter).
This sample is not a complete map or evidence of hardware testing.

## Preview details

- Catalog ID: `veris/e23`
- Map version: 1.0
- Verification: not-reviewed
- Protocols: RTU, TCP
- Public preview: 12 registers. Complete in-app availability is not established by this preview.

[JSON preview](https://modbus-monitor.github.io/modbus-device-maps/maps/veris/e23.json) · [Data terms](https://modbus-monitor.github.io/modbus-device-maps/data-license/)

## Register table (sample)

| Signal | Display address | Data type | Units | Category |
|---|---|---|---|---|
| Voltage line to line u average of active phases Volt | 301551 | FLOAT32 | V | Voltage |
| Current average of active phases Amp | 301555 | FLOAT32 | A | Current |
| Total instantaneous real power p kW | 301543 | FLOAT32 | kW | Power |
| Real energy ph consumption kWh | 301537 | FLOAT32 | kWh | Energy |
| Frequency derived from phase a b or C in that order Hz | 301557 | FLOAT32 | Hz | Frequency |
| Reactive energy qh consumption kVARh | 301539 | FLOAT32 | kWh | Energy |
| Apparent energy sh consumption kVAh | 301541 | FLOAT32 | kWh | Energy |
| Total instantaneous reactive power q kVAR | 301545 | FLOAT32 | kW | Power |
| Total instantaneous apparent power s kVA | 301547 | FLOAT32 | kW | Power |
| Average power factor pf total kw total kva Ratio | 301549 | FLOAT32 | PF | Power |
| Voltageline to neutral v average of active phases Volt | 301553 | FLOAT32 | V | Voltage |
| Total real power present demand kW | 301559 | FLOAT32 | kW | Power |

## Addressing and setup

Addresses and values above are copied from the public JSON preview. Confirm the exact model, firmware, register function, address base, word order, scaling and units against the manufacturer manual before polling. No manufacturer manual revision or hardware validation is established by this page.

## Use with Modbus Monitor XPF

Check the device-map catalog in your installed XPF version for current map availability and licensing. The software download link does not open this map.

[Get Modbus Monitor XPF](https://docs.quantumbitsolutions.com/downloads-purchase/) · [Request a map or correction](https://github.com/Modbus-Monitor/modbus-device-maps/issues/new/choose) · [Browse all previews](https://docs.quantumbitsolutions.com/modbus-device-maps/)

<script type="application/ld+json">{"@context": "https://schema.org", "@type": "Dataset", "name": "Veris E23 public register preview", "description": "Sample register addresses and data types; not a complete map or hardware verification.", "url": "https://docs.quantumbitsolutions.com/modbus-device-maps/previews/veris/e23/", "license": "https://modbus-monitor.github.io/modbus-device-maps/data-license/", "creator": {"@type": "Organization", "name": "Quantum Bit Solutions", "url": "https://quantumbitsolutions.com/"}, "distribution": {"@type": "DataDownload", "encodingFormat": "application/json", "contentUrl": "https://modbus-monitor.github.io/modbus-device-maps/maps/veris/e23.json"}}</script>
