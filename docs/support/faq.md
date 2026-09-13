# FAQ

Beginner‑friendly answers to common questions across Windows (XPF), Android (Advanced & Free), Mapper Pro, licensing, purchasing, connectivity and troubleshooting.

---
## General

### What is Modbus Monitor XPF?
Windows desktop application for professional Modbus TCP/RTU/ASCII monitoring, diagnostics, logging, charting and MQTT connectivity. See [XPF product information](https://www.modbusmonitor.com/).

### What is Modbus Monitor Advanced (Android)?
Paid Android app with additional professional features, including data logging, server modes and optional MQTT and Google Sheets add-ons. See [Modbus Monitor Advanced](https://quantumbitsolutions.com/android-monitor-advance/).

### What is Modbus Monitor Free? {#what-is-modbus-console-free}
[Modbus Monitor Free](https://quantumbitsolutions.com/android-monitor-free/) is an Android app available at no cost for basic read/write tests. Its **Modbus Console** screen is separate from the retired Windows utility, available on the [Modbus Console — Legacy Download page](../releases/modbus-console.md).

### What is Mapper Pro?
Windows tool for Modbus RTU/ASCII traffic analysis, mapping, bridging and replay. See [Mapper Pro product information](https://www.modbusmonitor.com/modbus-mapper-pro).

### Where do I download products?
Use [Downloads & Purchase](../downloads-purchase.md) for XPF and Mapper downloads and the Google Play links for Android Free and Advanced.

---
## Purchasing & Licensing

### How can I purchase XPF?
Two common flows:
    1. Microsoft Store (if available) – provides automatic updates and simplified license management.
    2. [XPF license in the QBS shop](https://quantumbitsolutions.com/shop/modbus-monitor-xpf/).

### What license type do I get via the shop?
Check the product page and your order confirmation for terms: [XPF](https://quantumbitsolutions.com/shop/modbus-monitor-xpf/), [Mapper Perpetual Pro License](https://quantumbitsolutions.com/shop/modbus-mapper-pro/), or [Mapper 30-Day License](https://quantumbitsolutions.com/shop/modbus-mapper-pro-subscription/). The Mapper 30-Day License is a one-time purchase with no automatic renewal.

### How do I activate an XPF license?

1. Install XPF.
2. Open the License/Activation dialog.
3. Paste or enter the license key from your purchase email.
4. Click Activate (internet required on first activation). For Microsoft Store purchases, use Store activation. If activation fails, contact support with your purchase details.

### Can I transfer my license to another PC?
Contact support with your order details before moving a license to another PC. Transfer eligibility and the required steps depend on the license and purchase channel.

### Microsoft Store vs Online Shop – which should I choose?
Microsoft Store manages installation and updates through your Microsoft account. The QBS shop provides direct license purchases. Follow the activation instructions for the channel you used; do not assume the two purchase methods are interchangeable.

### Where can I find invoices or download links?
Online Shop order confirmation email + account dashboard. Microsoft Store order history inside your Microsoft account.

---
## Installation & Setup

### Windows prerequisites

• .NET Desktop Runtime (if not bundled)
• Stable network or serial adapter driver installed
• Administrative rights for driver/port access where required

### Android Advanced initial setup
1. Install from Play Store.
2. Grant USB and Bluetooth permissions when prompted.
3. Configure connection (TCP host:port or serial parameters).
4. Add points or import a map (see Import/Export guide).

### USB‑OTG Serial not detected on Android – what to check?
• Use a quality OTG adapter/hub.
• Confirm chipset supported (FTDI, CH340, CP210x, Prolific, etc.).
• Grant permission dialog (tap Allow). If it never appears, replug and reopen app.
• Some phones restrict power output; try powered hub for multiple devices.

### Bluetooth Classic vs BLE?
Classic (SPP) offers virtual serial streams; BLE requires defined service/characteristics with limited throughput. Use Classic for full Modbus serial bridging when possible.

---
## Modbus Basics

### Difference between Modbus TCP and RTU?
TCP: Ethernet encapsulation, easier routing, no timing gaps. RTU: serial frame timing critical, lower overhead in closed wiring environments.

### What is 6‑digit addressing?
Normalization of function + register base into a unified 6‑digit address scheme for simpler map management. See the dedicated guide for conversion examples.

### When do I use Modbus ASCII?
Legacy environments or noisy lines where printable characters aid diagnostics. Higher overhead than RTU; use only when required.

---
## Data Logging & Export

### How do I log data?
XPF: configure logging profile (interval, format) and destination folder; enable session. Android Advanced: enable logging in session settings (CSV or integrated cloud plugin).

### Export formats available?
Export formats depend on the product. See its guide for CSV/JSON support and MQTT or Google Sheets integration.

### Large logs performance tips

• Split sessions by device group.
• Compress archives periodically.
• Use filters to reduce row volume.

---
## Cloud & Integrations

### MQTT setup basics

1. Broker host:port + TLS options.
2. Authentication (user/password or certificates).
3. Topic strategy: use per‑device prefix + measurement suffix.
4. Test with a subscriber before production.

### Google Sheets integration (Android)
Provide spreadsheet ID + sheet name; authorize account; ensure rate within Sheets API limits.

### ThingSpeak integration
The Modbus Monitor ThingSpeak add-on is retired and is not offered for new purchases. The [archived guide](../guides/thingspeak-overview.md) remains available for historical reference, not new setups.

### Can I publish Modbus RTU data to cloud from Android?
Modbus Monitor Advanced supports cloud publishing through optional [MQTT](../guides/android-mqtt-addon.md) and [Google Sheets](../guides/android-sheets-addon.md) add-ons. Modbus Monitor Free does not include these add-ons.

---
## Server & Sensor Modes

### What is Server Mode (Android)?
Device acts as a Modbus slave/server exposing registers populated from internal sensors or acquired external sources.

### What is Sensor Server?
Extends server mode adding structured sensor data mapping (e.g., environmental readings) for quick field integration.

### When to use Android as a server?
Rapid prototyping, edge aggregation, or simulation when physical PLC/RTU devices aren’t available.

---
## Hardware & Connectivity

### Common connection errors

• Incorrect COM port or baud rate (RTU)
• Firewall blocking TCP port
• Device address mismatch (unit ID)
• Cable wiring (A/B swapped) for RS‑485

### Improving unreliable RTU communication
Shorter bus length, proper termination, shielded twisted pair, stable power supply, correct biasing resistors.

### Does Mapper Pro alter traffic?
No. It passively observes packets (mirrored or sniffed) unless actively configured in injection/test mode.

---
## Troubleshooting & Error Codes

### How do I interpret error codes?
Use the Error Codes guide for mapping exceptions (ILLEGAL FUNCTION, ILLEGAL DATA ADDRESS, CRC failures). Patterns help isolate wiring vs addressing vs device faults.

### Frequent timeout causes

• Wrong slave ID
• Baud/Parity mismatch
• RF/EMI noise or unshielded cabling
• Overloaded device (poll interval too aggressive)

### Best first diagnostic step
Reduce point count to a single known good register; confirm stable reads before scaling.

---
## Performance & Optimization

### How many devices can I poll simultaneously?
Depends on channel latency and interval. Start conservative (1–2 polls/sec per device) and raise while monitoring error rate.

### Reducing Android battery drain
Lower poll frequency, disable unused transports (Bluetooth when on USB), minimize screen brightness, stop logging when not needed.

### Windows performance tips
Run on SSD, enable application logging rotation, avoid polling extremely large blocks if mostly sparse data.

---
## Security

### Is Modbus secure?
Classic Modbus lacks encryption/authentication. Use network segmentation + VPN/TLS tunnels where possible.

### Securing MQTT publishes
Enable TLS, unique credentials per deployment, least privilege topic access, periodic key rotation.

### Protecting maps and logs
Store exports in access‑controlled directories; sanitize sensitive device naming before sharing.

---
## Documentation & Support

### Where do I get help?

• Documentation Hub home page
• Community Forum (peer Q&A)
• Email / contact form for licensing issues
• YouTube channel for walkthrough videos

### What information should I include in a support request?
Product version, platform (Windows/Android), connection type, error codes/messages, log snippet, device model, steps already tried.

### Response times?
Email: 24–48h; forum: community dependent; urgent licensing: mark subject accordingly.

---
## Commerce & CTA Links

| Action | Link |
|--------|------|
| Purchase / Shop | [QBS shop](https://quantumbitsolutions.com/shop/) |
| Purchase XPF | [XPF license](https://quantumbitsolutions.com/shop/modbus-monitor-xpf/) |
| Purchase Mapper Pro | [Perpetual Pro License](https://quantumbitsolutions.com/shop/modbus-mapper-pro/) · [30-Day License](https://quantumbitsolutions.com/shop/modbus-mapper-pro-subscription/) |
| License / Activation Help | [XPF licensing](../products/xpf/user-guide.md#licensing) · [Mapper activation](../products/mapper/user-manual.md#activating-pro) |
| Download Android Advanced (paid) | [Google Play](https://play.google.com/store/apps/details?id=com.Bhavan.Galex) |
| Download Android Free (no cost) | [Google Play](https://play.google.com/store/apps/details?id=com.Bhavan.Hubble) |
| Mapper Pro Info | [Product information](https://www.modbusmonitor.com/modbus-mapper-pro) · [User manual](../products/mapper/user-manual.md) |

---
## Best Practices Summary

1. Choose your product on the [download page](../downloads-purchase.md).
2. Follow its quick start or user guide before configuring a device.
3. Confirm communication with one known register before adding more points.
4. Keep your order confirmation and use the matching activation method.
5. Include the product version and exact error message when contacting support.

---
## Still Need Help?
See the Support Center index or contact support directly: [support@quantumbitsolutions.com](mailto:support@quantumbitsolutions.com)

*Last updated: September 13, 2026*