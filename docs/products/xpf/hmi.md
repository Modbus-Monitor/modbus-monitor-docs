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
- Typical setup: `DisplayFormat`, `MinValue`, `MaxValue`, label/text settings.
- Capabilities: Preset Write Value, Input Value Text Box Visibility, Min/Max Value

#### Button
<!-- Suggested capture: Button widget with write value and click action in runtime -->
![XPF Button Widget](../../assets/screenshots/xpf/xpf-hmi-button-widget.webp)

- Purpose: one-click write command to a bound register with preset value.
- Typical setup: `WriteValue` with optional min/max validation and label.
- Capabilities: write-controllable.

#### Dial180
<!-- Suggested capture: Dial180 with needle, ticks, and configured min/max arc -->
![Dial Guage 270 degree sweep](../../assets/screenshots/xpf/xpf-hmi-guage-270-sweep.webp) ![Dial Guage 180 degree sweep](../../assets/screenshots/xpf/xpf-hmi-guage-180-sweep.webp) 

- Purpose: analog-style needle gauge with configurable arc.
- Typical setup: `Minimum`/`Maximum`, `StartAngle`/`SweepAngle`, major/minor ticks.
- Capabilities: range-configurable, Scale Visibility, Start Angle, Sweep Angle, Gauge Min/Max, Operating Min/Max.

#### Text Label

> Image coming soon...
<!-- Suggested capture: Text Label in static mode and bound text mode -->

- Purpose: static text or optional bound text value.
- Typical setup: `DisplayText`, font/color, optional write enable in advanced use.
- Capabilities: optional write support, persistence.

#### Clock

> Image coming soon...
<!-- Suggested capture: Clock widget showing digital and analog modes -->

- Purpose: live clock widget with no register binding required.
- Typical setup: `DisplayMode` (Digital/Analog), `TimeFormat` (12h/24h), `ShowSeconds`, timezone.
- Capabilities: persistence.

#### Slider

> Image coming soon...
<!-- Suggested capture: Slider widget adjusting setpoint with current value -->

- Purpose: setpoint adjustment by dragging value to write.
- Typical setup: `MinValue`, `MaxValue`, step behavior and visual dimensions.
- Capabilities: write-controllable,  persistence.

#### MultiState Indicator

> Image coming soon...
<!-- Suggested capture: MultiState indicator with Low/Normal/High ranges and state label -->

- Purpose: state display using color/image by value range or boolean mode.
- Typical setup: `StateRanges`, `DefaultStateColor`, label/value visibility.
- Capabilities: range-configurable, image support,  persistence.

#### Bar Graph

> Image coming soon...
<!-- Suggested capture: Bar Graph with orientation and range-based state color/image -->

- Purpose: fill-level visualization for one bound register.
- Typical setup: `Minimum`, `Maximum`, `Orientation` (`North`/`South`/`East`/`West`), optional bipolar center.
- Capabilities: range-configurable, image support,  persistence.

#### Trend

> Image coming soon...
<!-- Suggested capture: Trend chart with live points and render style options -->

- Purpose: real-time value history charting.
- Typical setup: `MaxDataPoints`, `RenderStyle`, `Minimum`/`Maximum`, sample interval.
- Capabilities: range-configurable, image support,  persistence.

#### Line

> Image coming soon...
<!-- Suggested capture: Line widget with orientation/angle and state-driven appearance -->

- Purpose: directional/flow line shape with optional data-driven state styling.
- Typical setup: `LineThickness`, orientation, angle, optional state ranges.
- Capabilities: range-configurable, image support,  persistence.

#### Rounded Rectangle

> Image coming soon...
<!-- Suggested capture: Rounded Rectangle used as status panel with corner radius settings -->

- Purpose: shape/zone panel for grouping and status indication.
- Typical setup: `RadiusX`, `RadiusY`, stroke and rotation.
- Capabilities: range-configurable, image support,  persistence.

#### Arrow

> Image coming soon...
<!-- Suggested capture: Arrow widget showing direction and state-based styling -->

- Purpose: directional indicator for process flow and motion.
- Typical setup: head/shaft proportions, stroke, rotation.
- Capabilities: range-configurable, image support,  persistence.

#### Triangle

> Image coming soon...
<!-- Suggested capture: Triangle widget in multiple orientations with state color -->

- Purpose: compact directional marker.
- Typical setup: orientation (`Up`/`Down`/`Left`/`Right`), stroke, rotation.
- Capabilities: range-configurable, image support,  persistence.

#### Polygon

> Image coming soon...
<!-- Suggested capture: Polygon widget with side-count variation and status color -->

- Purpose: multi-sided marker or status zone.
- Typical setup: `SideCount`, stroke, rotation.
- Capabilities: range-configurable, image support,  persistence.

#### Arc

> Image coming soon...
<!-- Suggested capture: Arc widget with start/sweep angle and stroke thickness -->

- Purpose: arc/sector indicator for partial-scale visuals.
- Typical setup: `StartAngle`, `SweepAngle`, stroke thickness, rotation.
- Capabilities: range-configurable, image support,  persistence.

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
