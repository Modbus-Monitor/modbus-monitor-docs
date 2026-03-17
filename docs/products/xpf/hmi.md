# Modbus Monitor XPF HMI Guide

Use this as the single HMI guide page for XPF. It covers overview, dashboard management workflow, and widget reference in one place.

![HMI Dashboard Demo](../../assets/screenshots/xpf/xpf-hmi-demo.webp){ .screenshot-shadow loading="lazy" }
*Example HMI dashboard layout in XPF*

## About HMI

The HMI feature in Modbus Monitor XPF lets you build live dashboards using widgets connected to Modbus data. You can create monitoring screens, status panels, trend views, and operator controls without building a custom interface from scratch.

Use the HMI feature when you need:

- a live dashboard for commissioning
- a simple operator screen
- a reusable monitoring layout
- a quick way to test values, states, and controls together

<!-- Screenshot placeholder: xpf-hmi-guide-01-overview.png -->
![docs/products/xpf/hmi.md](../../assets/screenshots/xpf/xpf-hmi-guide-01-overview.webp){ .screenshot-shadow loading="lazy" }
 

## What You Can Build

Common uses include:

- real-time monitoring screens
- equipment status panels
- operator control panels
- setpoint adjustment screens
- trend views for changing values
- dashboards with time and event visibility

## Available Widget Categories

### Core Gauges and Status Widgets

Use these widgets to display live values and state changes:

- `Numeric`
- `Dial180`
- `Bar Graph`
- `MultiState Indicator`

### Interactive Controls

Use these widgets when operators need to write or adjust values:

- `Button`
- `Slider`
- `Text Label` for labels, messages, or optional text write scenarios

### Advanced and Utility Widgets

Use these widgets for trends, time display, layout, and visual grouping:

- `Trend`
- `Clock`
- `Line`
- `Rounded Rectangle`
- `Arrow`
- `Triangle`
- `Polygon`
- `Arc`

Jump to [Widget Reference](#widget-reference).

<!-- Screenshot placeholder: xpf-hmi-guide-02-widget-categories.png -->
![> Image coming soon...](../../assets/screenshots/xpf/xpf-hmi-guide-02-widget-categories.webp){ .screenshot-shadow loading="lazy" }
<!-- Suggested capture: one dashboard showing numeric, state, trend, button, and shape widgets together -->

## Basic Dashboard Workflow

### 1. Open the HMI area

Open the **HMI** tab in XPF.

### 2. Add widgets

Choose the widget types needed for your dashboard.

### 3. Bind data

Connect each widget to the correct Modbus monitor point.

### 4. Configure properties

Set ranges, labels, colors, formatting, limits, and behavior.

### 5. Save the dashboard

Save the dashboard so it can be reopened, copied, or shared.

### 6. Run and monitor

Use the live dashboard for monitoring, troubleshooting, and operator interaction.

Jump to [HMI Dashboard Management](#hmi-dashboard-management).

## Save and Load Behavior

Supported file formats:

- `.hmi` for dashboard packages with image assets


When loading dashboards:
- You can drag and drop a `.hmi` file directly onto the HMI background or canvas.
- If a `.hmi` file and a `.csv` file are in the same folder and share the same base name, XPF automatically finds and loads both.
- Example: `line-a.hmi` and `line-a.csv`.

This makes it easier to reopen complete dashboard and register-map pairs.

<!-- Screenshot placeholder: xpf-hmi-guide-03-save-load.png -->
![.hmi file drag and drop to load file ](../../assets/screenshots/xpf/xpf-hmi-guide-03-save-load.webp){ .screenshot-shadow loading="lazy" }
<!-- Suggested capture: dragging a .hmi file onto the canvas and loaded dashboard result -->

## Recommended First Dashboard

A simple first dashboard usually includes:

- one `Numeric` widget
- one `Dial180` or `Bar Graph`
- one `MultiState Indicator`
- one `Trend`
- one `Button` or `Slider`
- one `Clock`

This gives a balanced screen with value display, state visibility, trend history, and operator control.

## Licensing Notes

Some widgets and dashboard capabilities depend on the active HMI license tier. Core display widgets are available in lower tiers, while controls and trending may require higher tiers.

The widget gallery shows only the widgets available for the current license tier.

## HMI Dashboard Management { #hmi-dashboard-management }

Use this section to create, edit, and run HMI dashboards in XPF.

### Ribbon Controls

| Group | Control | What It Does |
|---|---|---|
| Widgets | Edit | Turns design mode on or off |
| Widgets | Add Widget | Opens the full widget gallery |
| Widgets | Add | Adds a default widget |
| Widgets | Remove | Deletes selected widget |
| Widgets | Delete All | Clears all widgets from canvas |
| Clipboard | Copy | Copies selected widget (`Ctrl+C`) |
| Clipboard | Paste | Pastes a duplicate (`Ctrl+V`) |
| Controls | Refresh | Reloads current values |
| Controls | Start/Stop | Starts or stops monitoring engine |

### Add, Configure, and Validate Widgets

1. Turn **Edit** on.
2. Click **Add Widget** and pick a widget type.
3. Set **Monitoring Point**.
4. Configure range and display properties.
5. Add state ranges for widgets that support state logic.
6. Turn **Edit** off and validate runtime behavior.

### Copy and Paste

- Copy keeps widget properties, style, binding, and state ranges.
- Paste creates a new widget with a new ID and position offset.

### Save and Load

See [Save and Load Behavior](#save-and-load-behavior) above for file types and auto-pair behavior.

### Shape Tip: Ellipse from Rounded Rectangle

- Set `RadiusX = Width / 2`
- Set `RadiusY = Height / 2`

Example circle:

- `Width=120`, `Height=120`, `RadiusX=60`, `RadiusY=60`

## Widget Reference { #widget-reference }

Use this section for widget setup, key properties, and min/max ranges.

### Widget List

| # | Widget | Register Binding | Write Support | Free | Basic | Pro | Best Use |
|---|---|---|---|---|---|---|---|
| 1 | Numeric | Required | No | Yes | Yes | Yes | Clear process value display |
| 2 | Button | Required | Yes | No | No | Yes | One-click command/write |
| 3 | Dial180 | Required | No | No | Yes | Yes | Analog-style gauge view |
| 4 | Text Label | Optional | Optional | Yes | Yes | Yes | Titles, notes, text values |
| 5 | Clock | Not required | No | Yes | Yes | Yes | Time on dashboard |
| 6 | Slider | Required | Yes | No | No | Yes | Setpoint adjustment |
| 7 | MultiState Indicator | Required | No | No | Yes | Yes | State by value range |
| 8 | Bar Graph | Required | No | No | Yes | Yes | Fill-level visualization |
| 9 | Trend | Required | No | No | No | Yes | Real-time history trend |
| 10 | Line | Optional | No | No | Yes | Yes | Direction/flow line |
| 11 | Rounded Rectangle | Optional | No | No | Yes | Yes | Status tile / shape zone |
| 12 | Arrow | Optional | No | No | Yes | Yes | Direction indicator |
| 13 | Triangle | Optional | No | No | Yes | Yes | Compact directional marker |
| 14 | Polygon | Optional | No | No | Yes | Yes | Multi-sided status marker |
| 15 | Arc | Optional | No | No | Yes | Yes | Arc/sector indicator |

License note:

- `Free`: core view-only widgets (`Numeric`, `Text Label`, `Clock`)
- `Basic`: adds advanced display widgets and shape widgets
- `Pro`: adds control widgets (`Button`, `Slider`) and `Trend`

### Quick Setup Rules

1. Bind **Monitoring Point** first.
2. Set **Minimum/Maximum** when the widget has a range.
3. Set labels and formatting.
4. Add state ranges where supported.
5. Turn **Edit** off and validate runtime behavior.

### State Ranges (Property Window) { #state-ranges-property-window }

<!-- Suggested capture: Property panel showing State Ranges table with Add/Remove/Delete All and Color actions -->
![State Ranges](../../assets/screenshots/xpf/xpf-hmi-guide-04-state-ranges-table.webp){ .screenshot-shadow loading="lazy" }

Use **State Ranges** in the property panel for widgets that converts values into the colors, names, and images. For example the `MultiState Indicator` takes the numberical value and changes the widget background to color `red`, name `running`, image `red LED`).

State ranges define behavior by value window:

- `Min <= CurrentValue <= Max` (inclusive bounds)
- First matching range is applied
- If no range matches, widget uses its default state style

#### Table Columns

| Column | Purpose | Example |
|---|---|---|
| `MIN` | Lower inclusive bound | `0` |
| `MAX` | Upper inclusive bound | `20` |
| `NAME` | State label shown by widget | `Low / Off` |
| `COLOR` | State color preview and picker target | Gray |

#### Property Window Actions

| Action | What It Does | Notes |
|---|---|---|
| `Add` | Adds a new state row | Starts with default values you can edit |
| `Remove` | Removes selected row | Requires row selection |
| `Delete All` | Clears all ranges | Widget falls back to default state styling |
| `Copy` | Copies selected range | Useful for quick duplication |
| `Paste` | Pastes copied range(s) | Preserves values/colors/names |
| `Copy All` | Copies entire range set | Helpful between similar widgets |
| `Color` | Opens color picker for selected range | Use to set final visual state color |
| `Clear Color` | Clears selected color override | Reverts to default handling |

#### Matching and Priority Rules

- Evaluation is continuous as values update.
- Overlapping ranges are allowed, but top-first match wins.
- Gaps are allowed; gap values use default state style.
- Recommended practice: keep ranges contiguous and non-overlapping for predictable behavior.

Example ordered ranges:

- `0-20` -> `Low / Off`
- `21-60` -> `Normal`
- `61-100` -> `High / Alert`

#### Visual Highlighting Behavior

Range-capable widgets can visually emphasize the active state range at runtime.
Typical pattern:

- Active range: stronger emphasis (for example thicker stroke/full opacity)
- Inactive ranges: reduced emphasis

This gives immediate feedback when the live value moves across thresholds.

#### Save and Load Behavior for State Ranges

State ranges are persisted in widget JSON during dashboard save and restored during load.
Saved fields include:

- `MinValue`
- `MaxValue`
- `StateName`
- `StateColor`
- optional `ImagePath` where supported

If a widget supports image-backed states, image paths are included in HMI package workflows via widget image collection.

### Key Widget Property Summary

| Widget | Core Properties |
|---|---|
| Numeric | `Monitoring Point`, `DisplayFormat`, `MinValue`, `MaxValue` |
| Button | `Monitoring Point`, `WriteValue`, `MinValue`, `MaxValue` |
| Dial180 | `Monitoring Point`, `Minimum`, `Maximum`, `StartAngle`, `SweepAngle` |
| Text Label | `DisplayText`, optional binding |
| Clock | `TimeFormat`, `DisplayMode`, `ShowSeconds` |
| Slider | `Monitoring Point`, `MinValue`, `MaxValue`, `SliderStep` |
| MultiState Indicator | `Monitoring Point`, `StateRanges` |
| Bar Graph | `Minimum`, `Maximum`, `Orientation`, `BipolarCenter` |
| Trend | `Minimum`, `Maximum`, `SampleCount`, `RenderStyle` |
| Line | `LineThickness`, `Orientation`, `AngleDegrees` |
| Rounded Rectangle | `RadiusX`, `RadiusY`, `StrokeThickness`, `RotationDegrees` |
| Arrow | `HeadLengthPercent`, `ShaftThicknessPercent`, `RotationDegrees` |
| Triangle | `Orientation`, `StrokeThickness`, `RotationDegrees` |
| Polygon | `SideCount`, `StrokeThickness`, `RotationDegrees` |
| Arc | `StartAngle`, `SweepAngle`, `StrokeThickness`, `RotationDegrees` |

### Per-Widget Details

#### Numeric
<!-- Suggested capture: Numeric widget showing value, label, and state color -->
![XPF Numeric Widget](../../assets/screenshots/xpf/xpf-hmi-numeric-widget.webp) 

- Purpose: compact numeric value display bound to one monitoring point.
- Binding: required.
- Main properties: `WidgetLabel`, `DisplayFormat`, `FontSize`, `TextColor`, `ShowLabel`, `MinValue`, `MaxValue`.
- Ranges and limits: default range is `0` to unbounded max; state ranges can be used for color changes; display formatting follows the configured decimal-place settings.
- Notes: use this when operators need the exact current value, not a write control.

#### Button
<!-- Suggested capture: Button widget with write value and click action in runtime -->
![XPF Button Widget](../../assets/screenshots/xpf/xpf-hmi-button-widget.webp)

- Purpose: one-click write command to a bound register with preset value.
- Binding: required.
- Main properties: `WidgetLabel`, `ButtonLabel`, `WriteValue`, `ShowLabel`, `ShowValueTextBox`, `MinValue`, `MaxValue`.
- Ranges and limits: `WriteValue` defaults to `1.0`; optional `MinValue` and `MaxValue` clamp user input before write; status text clears automatically after the write completes.
- Notes: best for fixed commands such as start, stop, reset, or mode selection. This is a Pro-tier control widget.

#### Dial180
<!-- Suggested capture: Dial180 with needle, ticks, and configured min/max arc -->
![Dial Guage 270 degree sweep](../../assets/screenshots/xpf/xpf-hmi-guage-270-sweep.webp) ![Dial Guage 180 degree sweep](../../assets/screenshots/xpf/xpf-hmi-guage-180-sweep.webp) 

- Purpose: analog-style needle gauge with configurable arc.
- Binding: required.
- Main properties: `Monitoring Point`, `Show Label`, `Display Name`, `Show Scale`, `Show Border`, `Value Format`, `Start Angle (deg)`, `Sweep Angle (deg)`, `Gauge Minimum`, `Gauge Maximum`, `Operating Minimum`, `Operating Maximum`, `Major Tick Step`, `Minor Tick Step`, `Width`, `Height`.
- Ranges and limits: default visual range is `Gauge Minimum = 0` and `Gauge Maximum = 100`; default dial geometry is `Start Angle = 180` and `Sweep Angle = -180`; default operating range is `0-100`; tick defaults are `20` major and `10` minor; widget layout range in the property editor is `Width 100-800` and `Height 100-600`; gauge maximum is normalized so it cannot remain below minimum.
- Notes: use this when you want an analog gauge look with clear tick marks rather than a raw number. The current code exposes `Value Format` and `Show Scale`; the quick-reference mentions `RangeFormat` and `ShowNeedle`, but those are not separate user-editable properties in the current implementation.

##### Dial Drawing Rules

Use these geometry rules when drawing a dial:

- `Start Angle (deg)` places the minimum-value end of the dial.
- `Sweep Angle (deg)` controls how far the dial travels from minimum to maximum.
- Negative sweep values draw clockwise in the current implementation and are the standard choice for the built-in recipes.
- `0 = East`, `90 = North`, `180 = West`, `270` or `-90 = South`.
- `Major Tick Step = 0` hides major and minor tick generation in practice. `Minor Tick Step = 0` hides only the minor ticks.

##### Direction Cheat Sheet

| Direction | Start Angle | Meaning |
|---|---:|---|
| East | `0` | Minimum starts at the right side, around 3 o'clock |
| North | `90` | Minimum starts at the top, around 12 o'clock |
| West | `180` | Minimum starts at the left side, around 9 o'clock |
| South | `270` or `-90` | Minimum starts at the bottom, around 6 o'clock |

##### Dial Recipe Table

| Dial Style | Start Angle (deg) | Sweep Angle (deg) | Major Tick Step | Minor Tick Step | What It Draws |
|---|---:|---:|---:|---:|---|
| Classic 180 horizontal | `180` | `-180` | `20` | `10` | Standard semicircle from west to east across the top |
| Inverted 180 | `90` | `-180` | `10` | `5` | Semicircle flipped so the sweep runs across the lower half |
| Industrial 270 | `225` | `-270` | `25` | `5` | Three-quarter dial with mid-scale pointing down |
| Compact temperature arc | `200` | `-140` | `10` | `5` | Narrower partial arc for tight layouts |
| East-facing half dial | `0` | `-180` | `20` | `10` | Semicircle starting on the right side |
| North-facing half dial | `90` | `-180` | `20` | `10` | Semicircle starting at the top |
| West-facing half dial | `180` | `-180` | `20` | `10` | Semicircle starting on the left side |
| South-facing half dial | `270` | `-180` | `20` | `10` | Semicircle starting at the bottom |
| Near full circle | `225` | `-359` | `30` | `10` | Almost complete ring while avoiding a closed 360-degree overlap |
| Arbitrary custom dial | `45` | `-180` | `20` | `10` | Half dial starting around the 1:30 position |

##### Parameter Table

| Property | Purpose | Default | Validated Behavior in Code |
|---|---|---|---|
| `Start Angle (deg)` | Places the minimum end of the dial | `180` | Used directly by arc and tick converters; `0` right, `90` up, `180` left |
| `Sweep Angle (deg)` | Sets dial span and direction | `-180` | Used directly by arc and tick converters; negative values produce the standard clockwise sweep |
| `Gauge Minimum` | Visual scale minimum | `0` | If maximum is set lower than minimum, maximum is normalized up to minimum |
| `Gauge Maximum` | Visual scale maximum | `100` | Cannot remain below minimum |
| `Operating Minimum` | Lower operating band for display and state logic | `0` | Used for operating-range highlighting and display clamping |
| `Operating Maximum` | Upper operating band for display and state logic | `100` | Explicitly setting it enables display clamping behavior |
| `Major Tick Step` | Spacing between major ticks | `20` | Exposed in property editor; use `0` to suppress visible tick generation |
| `Minor Tick Step` | Spacing between minor ticks | `10` | Exposed in property editor; use `0` to hide minor ticks |
| `Value Format` | Number formatting for value and tick labels | blank | Blank falls back to the global decimal-place setting |
| `Show Scale` | Shows or hides tick marks and scale labels | `true` | Bound directly in the view |

##### Recommended Setup Order

1. Set `Monitoring Point`.
2. Set `Gauge Minimum` and `Gauge Maximum` for the full scale.
3. Set `Operating Minimum` and `Operating Maximum` if you want an operating band separate from the full gauge scale.
4. Pick `Start Angle (deg)` and `Sweep Angle (deg)` from the recipe table.
5. Adjust `Major Tick Step` and `Minor Tick Step` for coarse or dense ticks.
6. Set `Value Format` or leave it blank to use global decimal places.

#### Text Label
![Text Label](../../assets/screenshots/xpf/xpf-hmi-text-label.webp)
<!-- Suggested capture: Text Label in static mode and bound text mode -->

- Purpose: static text or optional bound text value.
- Binding: optional. Use static mode for labels and notes, or enable Modbus mode for a bound text/value display.
- Main properties: `DisplayText`, `IsModbusEnabled`, `EnableWrite`, `WidgetLabel`, `FontSize`, `TextColor`, `ShowLabel`, `WriteValue`.
- Ranges and limits: `FontSize` is clamped to `8-72`; text write support is license-gated; if Modbus is disabled the widget shows `DisplayText`, otherwise it shows the bound value.
- Notes: use this for titles, instructions, annotations, and simple text-driven status. Write mode is an advanced Pro-tier scenario.


#### Clock

![Analog Clock Widget](../../assets/screenshots/xpf/xpf-hmi-clock-analog.webp) ![Digital Clock Widget](../../assets/screenshots/xpf/xpf-hmi-clock-digitial.webp)
<!-- Suggested capture: Clock widget showing digital and analog modes -->

- Purpose: live system clock widget with dual display modes (digital and analog); no register binding required.
- Binding: not required.
- Main properties: `Show Label`, `Show Border`, `Display Mode`, `Time Format`, `Show Seconds`, `Time Zone`, `Width`, `Height`.
- Ranges and limits: `Display Mode` supports `Digital` or `Analog`; `Time Format` supports `12h` or `24h`; `Time Zone` accepts `Local`, `UTC`, `UTC±offset` (e.g., `UTC+5.5`, `UTC-8`), or Windows timezone IDs; width and height range from `50` to `2000` pixels; if an invalid timezone is specified, the widget falls back to system local time.
- Notes: the widget updates from system time every 500 milliseconds to one second. Use it for timestamp visibility on operator panels, wallboard dashboards, or any screen requiring live time display.
- Add multiple clocks to build the world-clock with different time zones.

##### Clock Time Format Examples

| Time Format | 12h Example | 24h Example | Display When `ShowSeconds = false` |
|---|---|---|---|
| `12h` with seconds | `2:45:30 PM` | N/A | `2:45 PM` |
| `24h` with seconds | N/A | `14:45:30` | `14:45` |

##### Clock Time Zone Options

**Predefined Options:**

- **System Local:** `Local` (uses operating system timezone)
- **UTC:** `UTC` (Coordinated Universal Time)
- **UTC Offsets:** `UTC-12` through `UTC+12` in 1-hour increments (e.g., `UTC+5.5` for India Standard Time)
- **Windows TimeZone IDs:** `Eastern Standard Time`, `Central Standard Time`, `Mountain Standard Time`, `Pacific Standard Time`, `GMT Standard Time`, `Central European Standard Time`, `India Standard Time`, `Singapore Standard Time`, `AUS Eastern Standard Time`, `New Zealand Standard Time`, and others

**Fallback Behavior:**

When you specify a timezone:

1. The widget attempts to find it via Windows `System Time Zone By ID`
2. If not found, it parses as a UTC offset string (e.g., `UTC+5.5`)
3. If parsing fails, it falls back to system local time

##### Clock Parameter Table

| Property | Purpose | Default | Validated Behavior in Code |
|---|---|---|---|
| `Show Label` | Display widget label above or below clock | `true` | Toggled directly in property editor |
| `Show Border` | show 3D border/shadow around widget | `true` | Toggled directly in property editor |
| `Display Mode` | Clock style: digital numbers or analog hands | `Digital` | Dropdown: `Digital` or `Analog`; property change triggers re-render |
| `Time Format` | How to display time on digital mode | `24h` | Dropdown: `12h` (with AM/PM) or `24h` (24-hour); changing format triggers `UpdateTime()` which reformats the display string and recalculates analog hand rotations |
| `Show Seconds` | Include seconds in time display | `true` | Toggled directly in property editor; toggling triggers `UpdateTime()` to switch between HH:mm:ss ↔ HH:mm format |
| `Time Zone` | Which timezone to display | `Local` | Text/dropdown; accepts `Local`, `UTC`, `UTC±offset`, or Windows timezone names; invalid zones fall back to local time via robust validation chain |
| `Width` | Clock widget width in pixels | 150 | Numeric; clamped to `50–2000` pixel range |
| `Height` | Clock widget height in pixels | 100 | Numeric; clamped to `50–2000` pixel range; aspect ratio not enforced, so you can stretch or compress |

##### Recommended Clock Setup Order

1. Optionally set `Display Name` / widget label via `Show Label`.
2. Choose `Display Mode`: `Digital` for numeric time or `Analog` for clock face.
3. Choose `Time Format`: `12h` with AM/PM or `24h` military time.
4. Optionally toggle `Show Seconds`.
5. Set `Time Zone` if you need a timezone other than system local.
6. Adjust `Width` and `Height` to fit your dashboard layout.


#### Slider

![Slider Widget](../../assets/screenshots/xpf/xpf-hmi-slider.webp)
<!-- Suggested capture: Slider widget adjusting setpoint with current value -->

- Purpose: setpoint adjustment by dragging, with optional live updates or manual write-button confirmation.
- Binding: required.
- Main properties: `Monitoring Point`, `Display Name`, `Show Label`, `Show Border`, `Font Size`, `Label Color`, `Minimum Value`, `Maximum Value`, `Tick Frequency`, `Default Write Value`, `Enable Live Updates`, `Show Write Button`, `Width`, `Height`.
- Ranges and limits: default range is `0` to `100`; `Tick Frequency` (slider step) must be `>0` and defaults to `1.0` (forced to `1` if set to `0` or negative); `Default Write Value` is automatically snapped to the nearest tick and clamped to the range; all snapping and clamping re-applies when you change the range or step; widget layout range is `Width 120-400` and `Height 100-400`.
- Notes: use `Enable Live Updates = false` (default) for safe manual writes with a button click and status feedback; use `Enable Live Updates = true` only when continuous writes during drag are acceptable. This is a Pro-tier control widget.

##### Slider Write Modes

Two modes control when values are written to the Modbus register:

1. **Manual Write Mode (Default, `Enable Live Updates = false`)**
   - Slider drag updates the display value only; no register write occurs.
   - Click the **Write** button to send the value to the register.
   - Status displays `"✓ Wrote {value} to {register}"` and clears after 2 seconds.
   - Safe for slow-responding devices or when you want operator confirmation before each write.

2. **Live Update Mode (`Enable Live Updates = true`)**
   - Every slider drag position immediately writes to the register.
   - No Write button needed (even if `Show Write Button = true`, it has no effect).
   - Status shows `"✓ Live Update"` but does not auto-clear.
   - Useful for real-time trim, PID feedback, or quick response-required scenarios.

##### Slider Step and Snap Behavior

The slider snaps all values to the nearest tick:

- `Tick Frequency = 1.0` → snaps to integers: 0, 1, 2, ... 100
- `Tick Frequency = 0.1` → snaps to tenths: 0.0, 0.1, 0.2, ... 100.0
- `Tick Frequency = 5` → snaps to fives: 0, 5, 10, ... 100

Every `WriteValue` assignment and range/step change triggers the snap pipeline:

1. Clamp to `[Minimum Value, Maximum Value]`
2. Round to nearest tick based on `Tick Frequency`
3. Re-clamp, round to 10 decimals

This ensures displayed and written values always align with the tick marks.

##### Slider Recipe Table

| Use Case | Min | Max | Tick Step | Live Update | Write Button | Notes |
|---|---|---|---|---|---|---|
| Setpoint (manual safe) | `0` | `100` | `1` | `false` | `true` | Drag, review, click Write; 2s status feedback |
| Fine-grained setpoint | `0` | `100` | `0.1` | `false` | `true` | Precise 0.1° or 0.1% adjustment with confirmation |
| Integer-only (counts) | `1` | `10` | `1` | `false` | `true` | Select whole counts: 1, 2, ... 10 without decimals |
| Continuous trim/PID | `0` | `100` | `0.5` | `true` | `false` | Real-time feedback control; every drag writes immediately |
| Pressure setpoint (psi) | `50` | `150` | `1` | `false` | `true` | 50–150 psi in 1 psi increments |
| Temperature setpoint (°C) | `15` | `30` | `0.5` | `false` | `true` | 15–30°C in 0.5° steps with manual confirmation |
| Percentage control | `0` | `100` | `5` | `true` | `false` | 0%, 5%, 10%, ... , 100% live trim |
| Ratio/multiplier | `0.5` | `2.0` | `0.1` | `true` | `false` | 0.5× to 2× scaling factor with continuous update |

##### Slider Parameter Table

| Property | Purpose | Default | Validated Behavior in Code |
|---|---|---|---|
| `Monitoring Point` | Modbus register to bind and write to | — | Required; register value initializes the slider position; changed register resets slider to that register's value |
| `Display Name` | Widget label text | `"Value"` | Falls back to bound register name if empty |
| `Show Label` | Display widget label | `true` | Toggled directly in property editor |
| `Show Border` | 3D border/shadow | `true` | Toggled directly in property editor |
| `Font Size` | Size of label and value text | `14` | Numeric input; no range limits in editor |
| `Label Color` | Color of label and value text | `#FF000000` (black) | Hex color picker |
| `Minimum Value` | Lower bound of slider range | `0.0` | Numeric; if set higher than Max, Max auto-adjusts to equal Min |
| `Maximum Value` | Upper bound of slider range | `100.0` | Numeric; normalized so it cannot be set below Min; clamps `WriteValue` and `SliderStep` when changed |
| `Tick Frequency` | Step size for slider snapping | `1.0` | Numeric; forced to minimum `1.0` if set to `0` or negative; all values snap to nearest tick |
| `Default Write Value` | Initial/button-click value | `0.0` | Snapped to nearest tick and clamped to range on assignment; tied to register sync via `_isSyncingFromRegister` guard |
| `Enable Live Updates` | Write on every drag vs. write-button only | `false` | When `true`, writes fire every time slider position changes; when `false`, writes only occur on button click |
| `Show Write Button` | Display Write/confirm button | `true` | Toggled directly in property editor; button is always available in manual mode, ignored in live mode |
| `Width` | Widget width in pixels | `200` | Numeric; clamped to `120–400` pixel range |
| `Height` | Widget height in pixels | `140` | Numeric; clamped to `100–400` pixel range |

##### Recommended Slider Setup Order

1. Set `Monitoring Point` to bind the slider to a register.
2. Set `Minimum Value` and `Maximum Value` for the operating range (e.g., `50–150` for pressure, `0–100` for percentage).
3. Set `Tick Frequency` to the desired step size (e.g., `1` for whole units, `0.1` for fine-grained control).
4. Set `Default Write Value` to a safe initial position (usually close to mid-range or the present register value).
5. Choose `Enable Live Updates`: `false` for safe manual writes with confirmation, `true` for real-time continuous feedback.
6. Adjust `Font Size`, `Label Color`, `Width`, `Height` to fit your dashboard layout and readability.

#### MultiState Indicator

> Image coming soon...
<!-- Suggested capture: MultiState indicator with Low/Normal/High ranges and state label -->

- Purpose: state display using color/image by value range or boolean mode.
- Binding: required.
- Main properties: `Monitoring Point`, `Boolean Mode`, `Custom Label`, `Show Label`, `Show State Name`, `Show Value`, `Show Border`, `Font Size`, `Text Color`, `Default State Color`.
- Ranges and limits: each range uses inclusive `MinValue` and `MaxValue`; first matching range wins; default fallback color is gray when no range matches; legacy boolean mode treats `0` as false and non-zero as true; can only display one color at a time; state ranges are user-configurable via the Range Editor.
- Notes: this is the clearest widget for alarm, run/stop, health, or traffic-light style state display. Use state ranges to define multi-state boundaries.

##### MultiState Configuration Modes

Two modes control how values are interpreted:

1. **Range-Based Mode (Default, `Boolean Mode = false`)**
   - Compares value against a list of ranges
   - Each range: `Min ≤ Value ≤ Max` → shows color and name
   - First match wins; gaps fall back to default color
   - Example: `0-20` = Gray (Low), `21-60` = Green (Normal), `61-100` = Red (High)

2. **Boolean Mode (Legacy, `Boolean Mode = true`)**
   - Treats value as `0` (false) or non-zero (true)
   - Value `0` → default color
   - Value `1+` → green (or custom)
   - Used for backward compatibility with V1 HMI files

##### MultiState Indicator Recipe Table

| State Pattern | Boolean Mode | Range Count | Default Color | Typical Use Case |
|---|---|---|---|---|
| Simple On/Off | `true` | — | Gray | Device power, switch status |
| Three-state (Low/Normal/High) | `false` | `3` | Gray | Temperature, pressure, level |
| Five-state (health) | `false` | `5` | Gray | System health: Offline/Idle/Running/Warning/Critical |
| Binary fault | `true` | — | Red | Alarm triggered (0=ok, 1=alarm) |
| Load capacity | `false` | `4` | Gray | 0-25% Empty (Blue), 26-75% Normal (Green), 76-99% Full (Yellow), 100% Overflow (Red) |
| Traffic light | `false` | `3` | Gray | Stop (Red) 0-30, Caution (Yellow) 31-60, Go (Green) 61-100 |
| Equipment mode | `false` | `6` | Gray | 1=Init (Gray), 2=Idle (Blue), 3=Run (Green), 4=Pause (Yellow), 5=Error (Red), 6=Unknown (Black) |
| Pump status | `false` | `4` | Gray | 0=Off (Gray), 1-50% Startup (Blue), 51-99% Running (Green), 100% Max (Yellow) |

##### MultiState Indicator Parameter Table

| Property | Purpose | Default | Validated Behavior in Code |
|---|---|---|---|
| `Monitoring Point` | Modbus register to monitor | — | Required; changed register clears indicator state |
| `Boolean Mode` | Toggle boolean vs. range mode | `false` | When true, treats 0=false, 1+=true |
| `Custom Label` | Optional display label | blank | Falls back to register name if empty |
| `Show Label` | Display label text | `true` | Toggled directly in property editor |
| `Show State Name` | Display current state name | `true` | Toggled directly in property editor |
| `Show Value` | Display numeric value | `false` | Toggled directly in property editor |
| `Default State Color` | Color when out of range | Gray | Used when no state range matches or in boolean mode for 0 |
| `Font Size` | Size of displayed text | `14` | Numeric input |
| `Text Color` | Color of label/value text | `#FF000000` (black) | Hex color picker |
| `Show Border` | 3D border/shadow | `true` | Toggled directly in property editor |
| State Ranges | Min/Max/Color/Name | 3 default | Add/Remove/Edit via Range Editor in property panel |

##### Recommended MultiState Setup Order

1. Set `Monitoring Point`.
2. Choose `Boolean Mode` or leave it off for range-based.
3. If range-based (default), open the Range Editor and configure Min/Max/Color/Name for each state.
4. Set `Default State Color` for out-of-range fallback.
5. Toggle `Show Label`, `Show State Name`, `Show Value` as desired.
6. Adjust `Font Size` and `Text Color` for visibility.

#### Bar Graph

![Bar Graph North](../../assets/screenshots/xpf/xpf-hmi-bar-graph-north.webp) ![Bar Graph East](../../assets/screenshots/xpf/xpf-hmi-bar-graph-east.webp)
<!-- Suggested capture: Bar Graph with orientation and range-based state color/image -->

- Purpose: fill-level visualization for one bound register.
- Binding: required.
- Main properties: `Monitoring Point`, `Show Label`, `Display Name`, `Background Image`, `Show Value`, `Show Scale`, `Show Border`, `Gauge Minimum`, `Gauge Maximum`, `Bipolar`, `Bipolar Center`, `Value Format`, `Orientation`, `Width`, `Height`.
- Ranges and limits: default range is `Gauge Minimum = 0` and `Gauge Maximum = 100`; `Orientation` supports `North`, `South`, `East`, and `West`; `BipolarCenter` is automatically clamped inside the active range; default size is `200×140` with layout limits `80-800` width and `60-600` height; state ranges can be used to change bar color based on value.
- Notes: use bipolar mode when a center reference matters, such as negative-to-positive deviation around a neutral value. Use state ranges for color-coded alerting.

##### Bar Graph Orientation Rules

- `North`: bar fills from bottom upward when value increases (default)
- `South`: bar fills from top downward
- `East`: bar fills from left to right
- `West`: bar fills from right to left
- `Bipolar`: bar extends from the center (`BipolarCenter`) toward the value; negative deviations fill in the opposite direction

##### Bar Graph Recipe Table

| Gauge Style | Orientation | Bipolar | Bipolar Center | Gauge Min | Gauge Max | State Ranges | Best Use |
|---|---|---|---|---|---|---|---|
| Classic vertical bar | `North` | No | — | `0` | `100` | Optional | Liquid level, tank fill |
| Inverted bar | `South` | No | — | `0` | `100` | Optional | Pressure drop, descent speed |
| Horizontal bar (left-right) | `East` | No | — | `0` | `100` | Optional | Filling or loading progress |
| Horizontal bar (right-left) | `West` | No | — | `0` | `100` | Optional | Consumption or drain rate |
| Bidirectional centered | `North` | Yes | `50` | `0` | `100` | Optional | Deviation from setpoint (±50) |
| Temperature deviation | `North` | Yes | `37` | `32` | `42` | 3+ states | Human temperature (±5 degrees) |
| Pressure deviation | `East` | Yes | `100` | `80` | `120` | 3+ states | Pressure vs nominal (±20 psi) |
| Speed deviation | `North` | Yes | `3000` | `0` | `6000` | 2+ states | RPM vs target (±3000) |

##### Bar Graph Parameter Table

| Property | Purpose | Default | Validated Behavior in Code |
|---|---|---|---|
| `Monitoring Point` | Modbus register to display | — | Required; widget clears data if register changes |
| `Gauge Minimum` | Visual scale minimum | `0` | If max is set lower, max is normalized up |
| `Gauge Maximum` | Visual scale maximum | `100` | Cannot remain below minimum |
| `Orientation` | Fill direction | `North` | Dropdown: North, South, East, West |
| `Bipolar` | Enable center fill mode | `false` | When true, fills from `BipolarCenter` in both directions |
| `Bipolar Center` | Center point for bipolar fill | `0` | Auto-clamped inside active range [min, max] |
| `Value Format` | Number formatting | `F1` | .NET format string; blank uses global decimal places |
| `Show Value` | Display current value | `true` | Toggled directly in property editor |
| `Show Scale` | Show min/max labels | `true` | Toggled directly in property editor |
| `Show Label` | Show widget label | `true` | Toggled directly in property editor |
| `Background Image` | Fallback image when no state matches | blank | Optional; overridden by state image if range matches |
| `Width` | Widget width | `200` | Clamped 80–800 |
| `Height` | Widget height | `140` | Clamped 60–600 |

#### MultiState Indicator

![Mutli-State Widget with Image as State showing Off state](../../assets/screenshots/xpf/xpf-hmi-multi-state-off-LED.webp){height=107}![Mutli-State Widget showing Off state with color](../../assets/screenshots/xpf/xpf-hmi-multi-state-off-plain.webp){height=107}![Mutli-State Widget with LED Image as State showing  Normal state](../../assets/screenshots/xpf/xpf-hmi-multi-state-normal-LED.webp){height=107} ![Mutli-State Widget with Image as State showing Normal state with color](../../assets/screenshots/xpf/xpf-hmi-multi-state-normal-plain.webp){height=107} ![Mutli-State Widget with Image as State showing High state](../../assets/screenshots/xpf/xpf-hmi-multi-state-high-LED.webp){height=107}![Mutli-State Widget as State showing High state with color](../../assets/screenshots/xpf/xpf-hmi-multi-state-high-plain.webp){height=107}
<!-- Suggested capture: MultiState indicator with Low/Normal/High ranges and state label -->

- Purpose: state display using color/image by value range or boolean mode.
- Binding: required.
- Main properties: `Monitoring Point`, `Boolean Mode`, `Custom Label`, `Show Label`, `Show State Name`, `Show Value`, `Show Border`, `Font Size`, `Text Color`, `Default State Color`.
- Ranges and limits: each range uses inclusive `MinValue` and `MaxValue`; first matching range wins; default fallback color is gray when no range matches; legacy boolean mode treats `0` as false and non-zero as true; can only display one color at a time; state ranges are user-configurable via the Range Editor.
- Notes: this is the clearest widget for alarm, run/stop, health, or traffic-light style state display. Use state ranges to define multi-state boundaries.

##### MultiState Configuration Modes

Two modes control how values are interpreted:

1. **Range-Based Mode (Default, `Boolean Mode = false`)**
   - Compares value against a list of ranges
   - Each range: `Min ≤ Value ≤ Max` → shows color and name
   - First match wins; gaps fall back to default color
   - Example: `0-20` = Gray (Low), `21-60` = Green (Normal), `61-100` = Red (High)

2. **Boolean Mode (Legacy, `Boolean Mode = true`)**
   - Treats value as `0` (false) or non-zero (true)
   - Value `0` → default color
   - Value `1+` → green (or custom)
   - Used for backward compatibility with V1 HMI files

##### MultiState Indicator Recipe Table

| State Pattern | Boolean Mode | Range Count | Default Color | Typical Use Case |
|---|---|---|---|---|
| Simple On/Off | `true` | — | Gray | Device power, switch status |
| Three-state (Low/Normal/High) | `false` | `3` | Gray | Temperature, pressure, level |
| Five-state (health) | `false` | `5` | Gray | System health: Offline/Idle/Running/Warning/Critical |
| Binary fault | `true` | — | Red | Alarm triggered (0=ok, 1=alarm) |
| Load capacity | `false` | `4` | Gray | 0-25% Empty (Blue), 26-75% Normal (Green), 76-99% Full (Yellow), 100% Overflow (Red) |
| Traffic light | `false` | `3` | Gray | Stop (Red) 0-30, Caution (Yellow) 31-60, Go (Green) 61-100 |
| Equipment mode | `false` | `6` | Gray | 1=Init (Gray), 2=Idle (Blue), 3=Run (Green), 4=Pause (Yellow), 5=Error (Red), 6=Unknown (Black) |
| Pump status | `false` | `4` | Gray | 0=Off (Gray), 1-50% Startup (Blue), 51-99% Running (Green), 100% Max (Yellow) |

##### MultiState Indicator Parameter Table

| Property | Purpose | Default | Validated Behavior in Code |
|---|---|---|---|
| `Monitoring Point` | Modbus register to monitor | — | Required; changed register clears indicator state |
| `Boolean Mode` | Toggle boolean vs. range mode | `false` | When true, treats 0=false, 1+=true |
| `Custom Label` | Optional display label | blank | Falls back to register name if empty |
| `Show Label` | Display label text | `true` | Toggled directly in property editor |
| `Show State Name` | Display current state name | `true` | Toggled directly in property editor |
| `Show Value` | Display numeric value | `false` | Toggled directly in property editor |
| `Default State Color` | Color when out of range | Gray | Used when no state range matches or in boolean mode for 0 |
| `Font Size` | Size of displayed text | `14` | Numeric input |
| `Text Color` | Color of label/value text | `#FF000000` (black) | Hex color picker |
| `Show Border` | 3D border/shadow | `true` | Toggled directly in property editor |
| State Ranges | Min/Max/Color/Name | 3 default | Add/Remove/Edit via Range Editor in property panel |

##### Recommended MultiState Setup Order

1. Set `Monitoring Point`.
2. Choose `Boolean Mode` or leave it off for range-based.
3. If range-based (default), open the Range Editor and configure Min/Max/Color/Name for each state.
4. Set `Default State Color` for out-of-range fallback.
5. Toggle `Show Label`, `Show State Name`, `Show Value` as desired.
6. Adjust `Font Size` and `Text Color` for visibility.

#### Trend

> Image coming soon...
<!-- Suggested capture: Trend chart with live points and render style options -->

- Purpose: real-time value history charting.
- Binding: required.
- Main properties: `Monitoring Point`, `Show Label`, `Label`, `Show Value`, `Show Grid Lines`, `Show Chart Title`, `Show Control Buttons`, `Gauge Minimum`, `Gauge Maximum`, `Max Data Points`, `Value Format`, `Render Style`, `Width`, `Height`.
- Ranges and limits: default Y-axis range is `0-100`; `Max Data Points` defaults to `100` and is clamped to minimum `10` if non-zero; `Render Style` supports `Line`, `Scatter`, and `Area`; data sampling runs on an internal timer with roughly `1` second data collection interval and batched redraw updates; default size is `400×250`; state ranges can colorize points based on value.
- Notes: this is a Pro-tier analytics widget and the largest default widget on the canvas. Use it when users need recent history, not just current state. Start/Stop/Clear buttons allow runtime control of data collection.

##### Trend Render Styles

| Render Style | Visual | Best For |
|---|---|---|
| `Line` | Continuous curve connecting points | Smooth trend visualization, default choice |
| `Scatter` | Discrete point markers | Precise moment-in-time readings, sparse data |
| `Area` | Filled area under the line | Cumulative effect, visual emphasis |

##### Trend Recipe Table

| Trend Scenario | Render Style | Max Data Points | Sample Interval | Show Grid | Min | Max | Purpose |
|---|---|---|---|---|---|---|---|
| Real-time line | `Line` | `100` | `1.0` sec | `true` | `0` | `100` | Default smooth trend |
| Precision readout | `Scatter` | `50` | `1.0` sec | `true` | `0` | `100` | Point-in-time values |
| Filled area (load) | `Area` | `100` | `1.0` sec | `true` | `0` | `100` | Visual fill under curve |
| Long history | `Line` | `500` | `1.0` sec | `false` | `0` | `100` | Extended time window |
| Dense data | `Scatter` | `200` | `0.5` sec | `false` | `0` | `100` | High-frequency sampling |
| Sparse data | `Line` | `30` | `5.0` sec | `true` | `0` | `100` | Low-frequency updates |
| Temperature trend | `Area` | `100` | `1.0` sec | `true` | `-50` | `50` | Temperature deviation |
| Pressure trend | `Line` | `120` | `1.0` sec | `true` | `80` | `120` | Pressure stability |

##### Trend Parameter Table

| Property | Purpose | Default | Validated Behavior in Code |
|---|---|---|---|
| `Monitoring Point` | Modbus register to trend | — | Required; clearing register clears all trend data |
| `Gauge Minimum` | Y-axis lower bound | `0` | Auto-normalized if set above max |
| `Gauge Maximum` | Y-axis upper bound | `100` | Cannot be below minimum |
| `Max Data Points` | Buffer size (how many points to keep) | `100` | Clamped min 10; `0` = unlimited |
| `Value Format` | Display format for current value | `F1` | .NET format string |
| `Render Style` | Chart type | `Line` | Dropdown: Line, Scatter, Area |
| `Show Grid Lines` | Display grid in background | `true` | Toggled directly in property editor |
| `Show Chart Title` | Display chart name above plot | `false` | Toggled directly in property editor |
| `Show Control Buttons` | Show Start/Stop/Clear buttons | `true` | Toggled directly in property editor |
| `Show Label` | Show widget label above chart | `true` | Toggled directly in property editor |
| `Show Value` | Display current value | `true` | Toggled directly in property editor |
| `Is Collecting Data` | Runtime data collection toggle | `false` | Start/Stop button controls this |
| `Width` | Widget width | `400` | Typical minimum `200`, maximum `800` |
| `Height` | Widget height | `250` | Typical minimum `150`, maximum `600` |

##### Recommended Trend Setup Order

1. Set `Monitoring Point`.
2. Set `Gauge Minimum` and `Gauge Maximum` to bracket expected value range.
3. Choose `Render Style` (Line is default; try Scatter for precise readings, Area for cumulative effect).
4. Adjust `Max Data Points` if you need longer history (higher = more memory, wider window).
5. Toggle `Show Grid Lines`, `Show Chart Title`, `Show Control Buttons` for presentation.
6. Start the trend and observe; adjust `Value Format` for readability if needed.

#### Trend

> Image coming soon...
<!-- Suggested capture: Trend chart with live points and render style options -->

- Purpose: real-time value history charting.
- Binding: required.
- Main properties: `Monitoring Point`, `Show Label`, `Label`, `Show Value`, `Show Grid Lines`, `Show Chart Title`, `Show Control Buttons`, `Gauge Minimum`, `Gauge Maximum`, `Max Data Points`, `Value Format`, `Render Style`, `Width`, `Height`.
- Ranges and limits: default Y-axis range is `0-100`; `Max Data Points` defaults to `100` and is clamped to minimum `10` if non-zero; `Render Style` supports `Line`, `Scatter`, and `Area`; data sampling runs on an internal timer with roughly `1` second data collection interval and batched redraw updates; default size is `400×250`; state ranges can colorize points based on value.
- Notes: this is a Pro-tier analytics widget and the largest default widget on the canvas. Use it when users need recent history, not just current state. Start/Stop/Clear buttons allow runtime control of data collection.

##### Trend Render Styles

| Render Style | Visual | Best For |
|---|---|---|
| `Line` | Continuous curve connecting points | Smooth trend visualization, default choice |
| `Scatter` | Discrete point markers | Precise moment-in-time readings, sparse data |
| `Area` | Filled area under the line | Cumulative effect, visual emphasis |

##### Trend Recipe Table

| Trend Scenario | Render Style | Max Data Points | Sample Interval | Show Grid | Min | Max | Purpose |
|---|---|---|---|---|---|---|---|
| Real-time line | `Line` | `100` | `1.0` sec | `true` | `0` | `100` | Default smooth trend |
| Precision readout | `Scatter` | `50` | `1.0` sec | `true` | `0` | `100` | Point-in-time values |
| Filled area (load) | `Area` | `100` | `1.0` sec | `true` | `0` | `100` | Visual fill under curve |
| Long history | `Line` | `500` | `1.0` sec | `false` | `0` | `100` | Extended time window |
| Dense data | `Scatter` | `200` | `0.5` sec | `false` | `0` | `100` | High-frequency sampling |
| Sparse data | `Line` | `30` | `5.0` sec | `true` | `0` | `100` | Low-frequency updates |
| Temperature trend | `Area` | `100` | `1.0` sec | `true` | `-50` | `50` | Temperature deviation |
| Pressure trend | `Line` | `120` | `1.0` sec | `true` | `80` | `120` | Pressure stability |

##### Trend Parameter Table

| Property | Purpose | Default | Validated Behavior in Code |
|---|---|---|---|
| `Monitoring Point` | Modbus register to trend | — | Required; clearing register clears all trend data |
| `Gauge Minimum` | Y-axis lower bound | `0` | Auto-normalized if set above max |
| `Gauge Maximum` | Y-axis upper bound | `100` | Cannot be below minimum |
| `Max Data Points` | Buffer size (how many points to keep) | `100` | Clamped min 10; `0` = unlimited |
| `Value Format` | Display format for current value | `F1` | .NET format string |
| `Render Style` | Chart type | `Line` | Dropdown: Line, Scatter, Area |
| `Show Grid Lines` | Display grid in background | `true` | Toggled directly in property editor |
| `Show Chart Title` | Display chart name above plot | `false` | Toggled directly in property editor |
| `Show Control Buttons` | Show Start/Stop/Clear buttons | `true` | Toggled directly in property editor |
| `Show Label` | Show widget label above chart | `true` | Toggled directly in property editor |
| `Show Value` | Display current value | `true` | Toggled directly in property editor |
| `Is Collecting Data` | Runtime data collection toggle | `false` | Start/Stop button controls this |
| `Width` | Widget width | `400` | Typical minimum `200`, maximum `800` |
| `Height` | Widget height | `250` | Typical minimum `150`, maximum `600` |

##### Recommended Trend Setup Order

1. Set `Monitoring Point`.
2. Set `Gauge Minimum` and `Gauge Maximum` to bracket expected value range.
3. Choose `Render Style` (Line is default; try Scatter for precise readings, Area for cumulative effect).
4. Adjust `Max Data Points` if you need longer history (higher = more memory, wider window).
5. Toggle `Show Grid Lines`, `Show Chart Title`, `Show Control Buttons` for presentation.
6. Start the trend and observe; adjust `Value Format` for readability if needed.

#### Line

> Image coming soon...
<!-- Suggested capture: Line widget with orientation/angle and state-driven appearance -->

- Purpose: directional/flow line shape with optional data-driven state styling.
- Binding: optional for static decoration, but needed for live state coloring.
- Main properties: `WidgetLabel`, `ShowLabel`, `ShowValue`, `LineColor`, `DefaultStateColor`, `LineThickness`, `Orientation`, `AngleDegrees`, `BackgroundImagePath`.
- Ranges and limits: `LineThickness` has a practical minimum of `1`; `Orientation` presets are `Horizontal`, `Vertical`, `DiagonalDown`, and `DiagonalUp`; preset orientations synchronize the displayed angle.
- Notes: use this for process flow paths, conveyor direction, piping runs, or connector styling between other widgets.

#### Rounded Rectangle

> Image coming soon...
<!-- Suggested capture: Rounded Rectangle used as status panel with corner radius settings -->

- Purpose: shape/zone panel for grouping and status indication.
- Binding: optional for static decoration, but needed for live state coloring.
- Main properties: `WidgetLabel`, `ShowLabel`, `ShowValue`, `RadiusX`, `RadiusY`, `StrokeThickness`, `StrokeColor`, `FillColor`, `DefaultStateColor`, `UseFill`, `StateApplyMode`, `BackgroundImagePath`.
- Ranges and limits: `RadiusX` and `RadiusY` default to `18` and cannot go below `0`; `StrokeThickness` defaults to `2` and cannot go below `0`; `StateApplyMode` supports `Fill` or `Stroke`.
- Notes: this is useful as a status tile, equipment group frame, or a quick ellipse/circle when `RadiusX` and `RadiusY` are set to half the widget size.

#### Arrow

> Image coming soon...
<!-- Suggested capture: Arrow widget showing direction and state-based styling -->

- Purpose: directional indicator for process flow and motion.
- Binding: optional for static decoration, but needed for live state coloring.
- Main properties: `HeadLengthPercent`, `ShaftThicknessPercent`, plus shared shape properties such as `StrokeColor`, `FillColor`, `DefaultStateColor`, `UseFill`, `StateApplyMode`, `StrokeThickness`, and `RotationDegrees`.
- Ranges and limits: `HeadLengthPercent` is clamped to `10-65`; `ShaftThicknessPercent` is clamped to `8-90`.
- Notes: use this when direction matters more than numeric precision, such as flow direction, transfer path, or motion indication.

#### Triangle

> Image coming soon...
<!-- Suggested capture: Triangle widget in multiple orientations with state color -->

- Purpose: compact directional marker.
- Binding: optional for static decoration, but needed for live state coloring.
- Main properties: `Orientation`, plus shared shape properties such as `StrokeColor`, `FillColor`, `DefaultStateColor`, `UseFill`, `StateApplyMode`, `StrokeThickness`, and `RotationDegrees`.
- Ranges and limits: `Orientation` supports `Up`, `Down`, `Left`, and `Right`.
- Notes: this is the simplest directional shape and works well for compact status pointers or lane markers.

#### Polygon

> Image coming soon...
<!-- Suggested capture: Polygon widget with side-count variation and status color -->

- Purpose: multi-sided marker or status zone.
- Binding: optional for static decoration, but needed for live state coloring.
- Main properties: `SideCount`, plus shared shape properties such as `StrokeColor`, `FillColor`, `DefaultStateColor`, `UseFill`, `StateApplyMode`, `StrokeThickness`, and `RotationDegrees`.
- Ranges and limits: `SideCount` is clamped to `4-8` and defaults to `6`.
- Notes: use this when a regular geometric marker is more useful than a rectangle or triangle, such as zone markers or symbolic equipment badges.

#### Arc

> Image coming soon...
<!-- Suggested capture: Arc widget with start/sweep angle and stroke thickness -->

- Purpose: arc/sector indicator for partial-scale visuals.
- Binding: optional for static decoration, but needed for live state coloring.
- Main properties: `StartAngle`, `SweepAngle`, `RenderAsSector`, plus shared shape properties such as `StrokeColor`, `FillColor`, `DefaultStateColor`, `UseFill`, `StateApplyMode`, `StrokeThickness`, and `RotationDegrees`.
- Ranges and limits: `StartAngle` is normalized into `0-360`; `SweepAngle` is clamped to `-359` through `359` and kept away from `0`; `RenderAsSector` switches between an open arc and a filled wedge.
- Notes: use this for partial rings, sector indicators, or radial emphasis around another widget.

### Choosing the Right Widget

- Use `Numeric` for exact values.
- Use `Dial180` or `Bar Graph` for quick visual status.
- Use `MultiState Indicator` for clear state color changes.
- Use `Trend` for value history.
- Use `Button` and `Slider` for write actions.
- Use shape widgets for grouping, flow direction, and layout.

## See Also

- [User Guide](user-guide.md)
- [Quick Start Guide](quick-start.md)
