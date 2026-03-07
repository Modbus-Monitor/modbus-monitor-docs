# Modbus Monitor XPF - Release History

All releases of Modbus Monitor XPF with features, bug fixes, and improvements.

---

## v5.0.2.0 — March 7, 2026

**Status:** Latest Candidate | **Compatibility:** Windows 10/11 (x86, x64, ARM64)

### 🚀 New Features
- **Line Widget for HMI Dashboard Design** — Add connecting lines and visual separators to HMI dashboards for improved layout and organization.
- **Rounded Square Widget for HMI Dashboard Design** — Enhanced widget palette with rounded corner support for modern UI aesthetics.
- **HMI Dashboard Save/Load Service** — Dead-simple pack/unpack strategy for dashboard persistence with embedded image support.
  - Save dashboards with embedded sensor images to `.hmi` files
  - Load dashboards from file with automatic image extraction
  - Portable/USB-friendly with relative path support
  - Automatic cleanup of temporary extracted files
- **Manual Release Update Check** — New "Check for Updates" button in About page to manually verify newer versions.

### ⚡ Performance Improvements
- **Modbus TCP Throughput:** +182.78% (33.98 → 96.09 txn/sec)
- **Client Packet Rate:** +182.65% (68.01 → 192.23 frames/sec)  
- **Latency Reduction:** -22.50% (0.200 → 0.155 ms)
- Optimized connection pooling and resource management
- Improved multi-channel transaction handling

### 🔧 Bug Fixes & Improvements
- **Fixed Z5 Crash in HMI Property Editing** — Stabilized ComboBox behavior in property editor panel.
- **Improved Dashboard Widget Selection** — Added drag/selection guard to prevent unintended property editor updates.
- **XAML Parse Exception Handling** — Suppressed non-fatal exceptions to prevent crash-level interruption during UI state transitions.
- **License Admin Console Stability** — Enhanced robustness and added proper hide command implementation.
- **Release Notification Bell Icon** — Uses dynamic theme color (Fluent.Ribbon.Brushes.Text) instead of hardcoded DarkRed.

### ✅ Quality Assurance
- All 348+ existing test cases pass
- Backward compatible with v5.0.1.0 configurations
- Verified across x86, x64, and ARM64 architectures
- Wireshark-validated performance improvements

---

## Unreleased (main branch) — February 28, 2026

**Status:** Development Snapshot | **Compatibility:** Windows 10/11 (x86, x64, ARM64)

### New Features
- Added Line widget for HMI dashboard design.
- Added Rounded Square widget for HMI dashboard design.

### Bug Fixes
- Fixed Z5 crash path in HMI property editing by using stable ComboBox behavior in the property editor panel.
- Added drag/selection guard in dashboard widget selection flow to prevent property editor updates during active interaction.
- Suppressed non-fatal XAML parse exception handling path to prevent crash-level interruption during transient UI state changes.

### Notes
- Changes were merged from the `copilot/fix-z5-crash-issue` branch into `main` and validated by successful Debug build.

---

## v4.4.1.0 — December 23, 2025

**Status:** Latest Stable | **Compatibility:** Windows 10/11 (x86, x64, ARM64)

### New Features
- Enhanced performance optimizations
- Improved UI responsiveness
- Better error handling and recovery
- Standardized release naming convention

### Bug Fixes
- Fixed licensing window not closing after activation
- Fixed critical installer path issues
- Resolved signing certificate path problems for all architectures
- Improved file organization and naming consistency
- Enhanced connection stability

---

## v4.4.0.0 — December 14, 2025

**Status:** Archive | **Compatibility:** Windows 10/11 (x86, x64, ARM64)

### New Features
- ARM64 architecture support
- Improved connection pooling and management
- Enhanced logging system with comprehensive screen output capture
- Standardized release naming convention

### Bug Fixes
- Fixed installer filename generation issues
- Resolved signing path problems for all architectures
- Corrected file organization and naming consistency

---

## System Requirements

All versions require:

- Windows 10 version 1903 (19H1) or later
- Windows 11 (all versions)
- .NET 8.0 Runtime (included in installers)
- 100 MB free disk space
- Administrator privileges for installation

## Installation

1. Download the appropriate installer for your architecture
2. Run the installer as administrator
3. Follow the setup wizard
4. Activate with your license key

For portable versions, simply extract and run — no installation required.

## Download

[📥 Get Latest Release →](../downloads-purchase.md){ .md-button .md-button--primary }

---

*For support or questions, visit [docs.quantumbitsolutions.com](https://docs.quantumbitsolutions.com)*
