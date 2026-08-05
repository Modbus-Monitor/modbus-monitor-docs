Title: Modbus Mapper Pro User Manual | Modbus RTU and ASCII RS-485 Monitor, Replay and Bridge
Description: Learn how to monitor Modbus RTU and Modbus ASCII traffic, build live Modbus maps, record replay exchanges, and emulate devices with Modbus Mapper Pro.

# Modbus Mapper Pro User Manual

Modbus Mapper Pro is a Windows tool for **Modbus RTU and Modbus ASCII monitoring, RS-485 traffic analysis, transparent serial bridging, and replay testing**. Use it to understand live communications, document an existing device, or reproduce recorded request/response traffic in a test environment.

![Modbus Mapper Pro](../../assets/screenshots/mapper/modbus-mapper-concept.webp){ .screenshot-center loading="lazy" }

## Modbus RTU and Modbus ASCII Support

Mapper Pro recognizes complete valid frames automatically on the selected serial port:

- **Modbus RTU** frames are validated with their CRC.
- **Modbus ASCII** frames begin with `:` and end with CR/LF; they are validated with their LRC.

For Modbus ASCII, configure the serial port to match the device exactly. **9600, 7 data bits, Even parity, 1 stop bit (7E1)** is common, but the device documentation is authoritative. Mapper Pro applies the selected baud rate, data bits, parity, and stop bits exactly as configured.

For map building and value display, a validated ASCII frame is normalized internally to the same Modbus unit-ID/function/PDU structure used by the RTU decoder. This is an internal decoding step only: Mapper Pro does **not** convert or rewrite traffic on the wire. Original ASCII bytes are retained for raw capture, bridge forwarding, and replay.

If traffic contains both valid RTU and ASCII frames, Mapper Pro detects each frame independently. Invalid or incomplete data is retained only long enough to recover the next valid frame start, rather than permanently losing synchronization.

## What Modbus Mapper Pro Does

- Passively monitor an existing RS-485 Modbus RTU or Modbus ASCII network.
- Decode frames into readable function codes, addresses, counts, values, and CRC/LRC status.
- Build a live Modbus map from observed traffic.
- Bridge Client and Server serial ports while recording traffic for diagnostics.
- Record request/response exchanges and save them as replay files.
- Emulate recorded Modbus responses for commissioning, regression tests, and HMI/SCADA development.

!!! warning "Use active modes carefully"

    **RS-485 Monitor** is designed to be passive. **Bridge / Proxy** and **Replay Emulator** can affect communications or transmit frames. Test active modes on a bench first and never run Replay Emulator beside a real slave that can answer the same unit ID.

## Editions and Licensing

### Free Edition

Free edition is intended for safe, useful field evaluation and basic diagnostics:

- Passive **RS-485 Monitor** on the Server port.
- Traffic logging and frame decoding.
- Up to **3 live Modbus map points** and **10 captured client requests**.
- Live updating of the included map points.

### Pro Edition

Pro unlocks the active and advanced workflows:

- Bridge / Proxy mode and Replay Emulator.
- Replay recording, replay file loading, and active response emulation.
- Unlimited live map points and captured requests.
- Map auto-add, bulk operations, CSV import/export, and request export/copy tools.

### Activating Pro

Select **Activate** and choose the purchase type that matches your confirmation:

- **Perpetual Pro key** — one-time license.
- **Monthly subscription key** — access remains active while the subscription is current.
- **Legacy license file** — existing MSSniff license from an older purchase.
- **Microsoft Store** — use Store activation when purchased there.

The app checks subscription status using trusted HTTPS time. A valid perpetual or Microsoft Store license takes precedence over an expired subscription record.

<!-- Screenshot suggestion: Activate Pro dialog showing Perpetual key, Monthly subscription, Legacy license file, and Microsoft Store cards. -->

## User Interface

![Modbus Mapper Pro UI](../../assets/screenshots/mapper/modbus-mapper-pro-ui.webp){ .screenshot-center loading="lazy" }

| Area | Purpose |
|---|---|
| **Server port** | The RS-485/serial port used for passive monitoring, bridge output, or RS-485 replay. |
| **Client 1 / Client 2 ports** | Optional client-side serial ports used by Bridge / Proxy or client-port replay. |
| **Operating Mode** | Select Bridge / Proxy, RS-485 Monitor, or Replay Emulator. |
| **Traffic Log** | Timestamped lifecycle, serial, decode, and diagnostic messages. Enable it before troubleshooting a start failure. |
| **Live Modbus Map** | Discovered requests and live decoded values. Configure data type, byte swap, scaling, and labels as needed. |
| **Client Request Viewer** | Unique observed client requests for review and export. |
| **Replay Setup / Capture for Replay** | Load a replay file, choose the replay target, or record exchanges for a new replay file. |
| **Start / Stop and status LED** | Starts the selected workflow and shows `STOPPED`, `STARTING`, `RUNNING`, or an error state. |

<!-- Screenshot suggestion: Main screen annotated with Server port, mode cards, replay setup, Capture for Replay, status LED, Traffic Log, and Live Modbus Map. -->

## Choose an Operating Mode

| Mode | What it does | Ports required | Transmits? | Best for |
|---|---|---|---|---|
| **RS-485 Monitor** | Passively receives and analyzes traffic observed on an RS-485 tap. | Server only | No intentional transmit | Troubleshooting, discovery, field monitoring |
| **Bridge / Proxy** | Forwards traffic between configured Client and Server ports while capturing it. | At least one Client and Server | Yes, forwards traffic | Integration and serial pass-through diagnostics |
| **Replay Emulator** | Matches incoming requests to a loaded replay file and returns the recorded response. | Client port(s) or Server port | Yes, sends replay responses | Bench tests, regression tests, HMI/SCADA simulation |

<!-- Screenshot suggestion: Operating Mode cards with RS-485 Monitor selected, then a second screenshot with Replay Emulator selected and its setup panel visible. -->

### 1. RS-485 Monitor — Passive Modbus RTU/ASCII Sniffing

Use this mode when you need to observe an existing RS-485 network without inserting the PC into the data path.

1. Connect a correctly configured receive-only RS-485 adapter/tap to the bus.
2. Enable and configure the **Server** port: COM port, baud rate, data bits, parity, and stop bits must match the network.
3. Select **RS-485 Monitor**.
4. Enable **Traffic Log** if you want lifecycle and frame diagnostics.
5. Select **Start**.
6. Watch the Traffic Log, Client Request Viewer, and Live Modbus Map as normal bus traffic occurs.

!!! important "Passive means no intentional writes"

    The application does not intentionally write in this mode. Your adapter and wiring must also be configured so the PC cannot drive the RS-485 bus. A passive tap sees a combined bus stream, so request/response direction is inferred from Modbus structure and timing rather than electrically proven.

Use RS-485 Monitor for Modbus RTU or ASCII troubleshooting, undocumented-device discovery, polling analysis, and safe production observation.

<!-- Screenshot suggestion: RS-485 tap wiring diagram — Master and Slave remain connected; Mapper Pro receives on the Server port only. -->

### 2. Bridge / Proxy — Transparent Serial Pass-Through

Use Bridge / Proxy when Mapper Pro is intentionally installed between a Modbus client (master) and server (slave).

1. Configure **Client 1** and/or **Client 2** for the client-side connection.
2. Configure **Server** for the slave-side connection.
3. Verify serial settings on both sides before wiring the bridge into a system.
4. Select **Bridge / Proxy** and select **Start**.
5. Confirm `RUNNING` and review the Traffic Log for each port opening successfully.

Traffic is forwarded while Mapper Pro captures and decodes it. This is an active mode: do not use it for a no-touch production tap, and validate it with non-critical equipment first.

<!-- Screenshot suggestion: Bridge / Proxy wiring diagram — Client 1 (Master) → Mapper Pro → Server (Slave), with arrows for request and response traffic. -->

### 3. Replay Emulator — Respond from a Recorded File

Replay Emulator lets a test system behave like a recorded Modbus device. It compares received request bytes with TX frames in a loaded replay file and writes the associated recorded RX frame only after a complete match.

It supports normal Modbus functions and recorded custom/variable-length requests because matching is based on the actual captured request bytes, not a fixed Modbus function-length assumption.

#### Replay to Client Port(s)

Use this option when a client is connected directly to Mapper Pro for a bench or software test.

1. Select **Replay Emulator**.
2. Select **Respond on: Client port(s)**.
3. Enable Client 1 and/or Client 2 and configure their serial settings.
4. Select **Load Replay** and choose a replay CSV or text file.
5. Start the emulator.

#### RS-485 Replay Emulator

Use this option only when you deliberately want the PC to answer requests on an RS-485 bus.

1. Select **Replay Emulator**.
2. Select **Respond on: RS-485 Server port**.
3. Enable and configure the Server port.
4. Load the replay file.
5. Start and accept the safety confirmation.

!!! danger "Avoid duplicate slaves"

    Disconnect or disable real devices that may answer the same unit ID. Two responders on RS-485 can collide and create invalid replies.

#### Fragmented Requests and Timing

Serial receive callbacks do not always align with Modbus RTU or ASCII frames. Mapper Pro retains partial request prefixes, supports concatenated requests, and sends a replay response only after a full replay-file request matches. The configurable fragment idle gap is a fallback cleanup value; it should be chosen for the baud rate and traffic pattern, not used as the primary definition of a replay frame.

<!-- Screenshot suggestion: Replay Setup panel with a loaded file, frame count, Client port(s) target, RS-485 Server target, and fragment idle gap setting. -->

## Record a Replay File

Record exchanges in **Bridge / Proxy** mode when you need a faithful request/response replay file.

1. Select **Capture for Replay → Record exchanges**.
2. Run the bridge while the real client and server exchange traffic.
3. Confirm that **Captured: n** increases.
4. Select **Save Capture** to create a CSV or text replay file.

For passive RS-485 capture, Mapper Pro can infer high-confidence request/response pairs without transmitting. Broadcast writes, ambiguous frames, multiple masters, and unmatched traffic cannot always become normal replay exchanges. Keep a raw traffic/frame capture as the lossless record when direction is uncertain.

Replay CSV files can include serial-port and emulator settings. When loading one, Mapper Pro may offer to apply the saved settings; always verify the selected COM ports before starting.

<!-- Screenshot suggestion: Capture for Replay card with Record exchanges enabled and a non-zero Captured counter, followed by the Save Capture dialog. -->

## Live Modbus Map and Request Viewer

The Live Modbus Map turns observed traffic into editable points. Configure each point’s name, data type, byte/word swap, gain, offset, and address interpretation to match the device documentation.

- Use **Auto Update** to keep displayed values current.
- Use the **Client Request Viewer** to see unique requests detected from traffic.
- Export a Modbus map CSV when you need documentation, handoff, or regression-test input.
- A CSV export can include port settings and selected application options for repeatable setup.

If a value looks wrong, first confirm the serial settings and address base, then review data type, byte order, word order, and scaling.

<!-- Screenshot suggestion: Live Modbus Map showing data type and byte-swap controls beside live values. -->

## Troubleshooting

### Start does not reach RUNNING

Enable **Traffic Log** and press Start. The log reports the requested mode, selected ports, availability checks, opening/closing actions, and any failure such as access denied or a missing replay file.

- Confirm the selected COM port is not open in another application.
- Confirm baud rate, parity, data bits, and stop bits match the target network.
- In Free edition, use only RS-485 Monitor with the Server port enabled.
- For Replay Emulator, load at least one valid TX/RX replay exchange before starting.

### No traffic in RS-485 Monitor

- Confirm the bus is active and the adapter appears in Windows Device Manager.
- Verify A/B polarity and, where appropriate, signal ground.
- Match the serial settings exactly; a wrong baud rate often appears as repeated `00` bytes or CRC failures.
- Confirm the adapter is receive-only/passive for production observation.

### Replay client times out

- Verify that the request exists in the replay file exactly, including unit ID, function code, address, quantity, and custom payload bytes.
- Confirm the replay target matches the connected port.
- Check the Traffic Log for a replay miss and candidate information.
- Use a replay file recorded at matching serial settings when practical.

### Stop remains in STOPPING

Mapper Pro cancels work immediately and closes serial drivers in the background so the UI remains responsive. A slow USB/serial driver can take a short time to release an active receive/write callback. The Traffic Log reports when cleanup is still waiting on the driver.

## Downloads, Support, and Safety

- [Download Modbus Mapper Pro](../../downloads-purchase.md#mapper-pro-windows)
- [Release notes](../../release/CHANGELOG-MAPPER.md)
- [Quick Start Guide](quick-start.md)
- [Contact support](mailto:support@quantumbitsolutions.com)

<small>Modbus Mapper Pro is intended for development, commissioning, troubleshooting, and system analysis. Do not rely on it as a safety control system. Obtain authorization before modifying production wiring or enabling an active bridge/replay workflow, and follow your organization’s change-management procedures.</small>
