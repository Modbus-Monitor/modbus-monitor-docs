# Modbus Monitor XPF - Release History

All releases of Modbus Monitor XPF with features, bug fixes, and improvements.

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
