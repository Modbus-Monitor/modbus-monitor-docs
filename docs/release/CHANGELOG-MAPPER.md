# Modbus Mapper Pro Release Notes

## v2.1.0.0 — August 5, 2026

### New

- Added a permanent Free edition with passive RS-485 monitoring and traffic logging.
- Added RS-485 Replay Emulator mode and replay exchange recording.
- Added ARM64 portable download support.
- Added Modbus ASCII monitoring, decoding, map building, capture, and replay.
- Added automatic recognition of valid Modbus RTU and Modbus ASCII frames.
- Added support for 9600 7E1 and other user-selected serial framing options.

### Improved

- Improved RS-485 passive monitoring, replay matching, fragmented-frame recovery, and serial timing.
- Improved Modbus map creation for coil and holding-register write functions.
- Added safe log-only handling for unsupported and vendor-custom Modbus function codes.
- Expanded automated regression coverage for RTU, ASCII, serial framing, replay, and write-function decoding.
- Improved replay handling for fragmented, concatenated, and custom Modbus messages.
- Replay and Modbus-map CSV exports can include serial-port and application settings.
- Simplified license activation and improved subscription validation.
- Added clear Free/Pro limits for live map points and captured requests.

### Fixed

- Fixed Modbus ASCII capture when seven data bits are selected; serial settings are now applied exactly as configured.
- Fixed write-function address and quantity decoding that could create invalid map entries.
- Added clearer serial-port diagnostics showing the settings applied when a port opens.
- Improved serial-port start, stop, diagnostics, and settings persistence.
- Fixed live status LED and replay-capture counter updates after navigation.
- Fixed x86 publishing support for Panigate dependencies.


## v1.0.0

- Initial Modbus Mapper Pro portable release.
