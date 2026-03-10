# Widget Reference (v5.0.3.0+)

Use this page for widget setup, key properties, and min/max ranges. For HMI workflow (add, edit, save, load), see [HMI Dashboard Management](hmi-widget-management.md).

## Widget List

| # | Widget | Register Binding | Write Support | Best Use |
|---|---|---|---|---|
| 1 | Numeric | Required | No | Clear process value display |
| 2 | Button | Required | Yes | One-click command/write |
| 3 | Dial180 | Required | No | Analog-style gauge view |
| 4 | Text Label | Optional | Optional | Titles, notes, text values |
| 5 | Clock | Not required | No | Time on dashboard |
| 6 | Slider | Required | Yes | Setpoint adjustment |
| 7 | MultiState Indicator | Required | No | State by value range |
| 8 | Bar Graph | Required | No | Fill-level visualization |
| 9 | Trend | Required | No | Real-time history trend |
| 10 | Line | Optional | No | Direction/flow line |
| 11 | Rounded Rectangle | Optional | No | Status tile / shape zone |
| 12 | Arrow | Optional | No | Direction indicator |
| 13 | Triangle | Optional | No | Compact directional marker |
| 14 | Polygon | Optional | No | Multi-sided status marker |
| 15 | Arc | Optional | No | Arc/sector indicator |

<!-- Screenshot placeholder: xpf-hmi-10-widget-gallery-all-15.png -->
> Image coming soon...
<!-- Suggested capture: Add Widget gallery open, all 15 items visible -->

## Quick Setup Rules (Use for Most Widgets)

1. Bind **Monitoring Point** first.
2. Set **Minimum/Maximum** second when the widget has a range.
3. Set formatting and labels.
4. Add state ranges (Low/Normal/High) where supported.
5. Turn Edit Off and verify runtime behavior.

## 1) Numeric

Simple numeric readout with optional range-based color behavior.

Quick setup:
1. Set `Monitoring Point`.
2. Set `DisplayFormat` (example: `F1`).
3. Set optional `MinValue` and `MaxValue`.

| Key Property | Default | Range / Options |
|---|---|---|
| `MinValue` | `0` | Any number |
| `MaxValue` | `double.MaxValue` | Must be greater than `MinValue` |
| `FontSize` | `14` | `8` to `72` |
| `WidgetWidth` | `150` | Positive value |
| `WidgetHeight` | `100` | Positive value |

<!-- Screenshot placeholder: xpf-hmi-11-widget-numeric.png -->
> Image coming soon...

## 2) Button

Writes a value to a register when clicked.

Quick setup:
1. Set `Monitoring Point`.
2. Set `WriteValue`.
3. Optional: set `MinValue` and `MaxValue` bounds.

| Key Property | Default | Range / Options |
|---|---|---|
| `WriteValue` | `1.0` | Clamped when min/max bounds are active |
| `MinValue` | `0` | Any number |
| `MaxValue` | `double.MaxValue` | Must be greater than or equal to `MinValue` |
| `WidgetWidth` | `150` | `80` to `400` |
| `WidgetHeight` | `80` | `40` to `200` |

Note: Button requires write permission.

<!-- Screenshot placeholder: xpf-hmi-12-widget-button.png -->
> Image coming soon...

## 3) Dial180

Analog gauge with configurable arc and ticks.

Quick setup:
1. Set `Monitoring Point`.
2. Set `Minimum` and `Maximum`.
3. Tune `StartAngle` and `SweepAngle` if needed.

| Key Property | Default | Range / Options |
|---|---|---|
| `Minimum` | `0` | Any number |
| `Maximum` | `100` | Must be greater than `Minimum` |
| `StartAngle` | `180` | `0` to `360` |
| `SweepAngle` | `-180` | `-359` to `359` |
| `MajorTickStep` | `20` | Greater than `0` |
| `MinorTickStep` | `10` | Greater than `0` |
| `WidgetWidth` | `250` | Positive value |
| `WidgetHeight` | `170` | Positive value |

<!-- Screenshot placeholder: xpf-hmi-13-widget-dial180.png -->
> Image coming soon...

## 4) Text Label

Static or bound text for headers, notes, or text status.

Quick setup:
1. Set `DisplayText` for static mode.
2. Enable register mode when you want bound text.

| Key Property | Default | Range / Options |
|---|---|---|
| `DisplayText` | `Sample Text` | Any text |
| `FontSize` | `14` | `8` to `72` |
| `WidgetWidth` | `150` | Positive value |
| `WidgetHeight` | `100` | Positive value |

<!-- Screenshot placeholder: xpf-hmi-14-widget-text-label.png -->
> Image coming soon...

## 5) Clock

Live clock widget with no register binding required.

| Key Property | Default | Range / Options |
|---|---|---|
| `TimeFormat` | `24h` | `12h`, `24h` |
| `DisplayMode` | `Digital` | `Digital`, `Analog` |
| `ShowSeconds` | `true` | `true`, `false` |
| `WidgetWidth` | N/A | `50` to `2000` |
| `WidgetHeight` | N/A | `50` to `2000` |

<!-- Screenshot placeholder: xpf-hmi-15-widget-clock.png -->
> Image coming soon...

## 6) Slider

Reads and writes with drag-based control.

Quick setup:
1. Set `Monitoring Point`.
2. Set `MinValue` and `MaxValue`.
3. Set `SliderStep` and write behavior.

| Key Property | Default | Range / Options |
|---|---|---|
| `MinValue` | `0` | Any number |
| `MaxValue` | `100` | Must be greater than `MinValue` |
| `WriteValue` | Current value | `MinValue` to `MaxValue` |
| `SliderStep` | `1` | Greater than `0` |
| `FontSize` | `14` | `8` to `72` |
| `WidgetWidth` | `200` | Positive value |
| `WidgetHeight` | `140` | Positive value |

Note: Slider requires write permission.

<!-- Screenshot placeholder: xpf-hmi-16-widget-slider.png -->
> Image coming soon...

## 7) MultiState Indicator

Status widget that changes by state range and can show state images.

Quick setup:
1. Set `Monitoring Point`.
2. Add `StateRanges` (example: Low/Normal/High).
3. Optional: set `ImagePath` per state.

| Key Property | Default | Range / Options |
|---|---|---|
| `StateRanges` | 3 default ranges | Each state: `MinValue`, `MaxValue`, `StateColor`, `StateName`, `ImagePath` |
| `FontSize` | `14` | `8` to `72` |
| `WidgetWidth` | `100` | Positive value |
| `WidgetHeight` | `100` | Positive value |

<!-- Screenshot placeholder: xpf-hmi-17-widget-multistate.png -->
> Image coming soon...

## 8) Bar Graph

Fill-level view with range colors and directional fill.

| Key Property | Default | Range / Options |
|---|---|---|
| `Minimum` | `0` | Any number |
| `Maximum` | `100` | Must be greater than or equal to `Minimum` |
| `Orientation` | `North` | `North`, `South`, `East`, `West` |
| `BipolarCenter` | `0` | Clamped to `Minimum`/`Maximum` |
| `WidgetWidth` | `200` | `80` to `800` |
| `WidgetHeight` | `140` | `60` to `600` |

<!-- Screenshot placeholder: xpf-hmi-18-widget-bargraph.png -->
> Image coming soon...

## 9) Trend

Real-time chart for value history and behavior over time.

| Key Property | Default | Range / Options |
|---|---|---|
| `Minimum` | `0` | Any number |
| `Maximum` | `100` | Must be greater than `Minimum` |
| `SampleCount` | `100` | `10` to `1000` |
| `RenderStyle` | `Line` | `Line`, `Scatter`, `Area` |
| `WidgetWidth` | `300` | Positive value |
| `WidgetHeight` | `200` | Positive value |

<!-- Screenshot placeholder: xpf-hmi-19-widget-trend.png -->
> Image coming soon...

## 10) Line

Simple line shape with optional state coloring.

| Key Property | Default | Range / Options |
|---|---|---|
| `LineThickness` | `5` | `0` to `20` |
| `Orientation` | `DiagonalDown` | `Horizontal`, `Vertical`, `DiagonalDown`, `DiagonalUp` |
| `AngleDegrees` | `45` | `0` to `360` |
| `WidgetWidth` | `180` | Positive value |
| `WidgetHeight` | `90` | Positive value |

<!-- Screenshot placeholder: xpf-hmi-20-widget-line.png -->
> Image coming soon...

## 11) Rounded Rectangle

Shape widget for zones, panels, and status blocks.

| Key Property | Default | Range / Options |
|---|---|---|
| `RadiusX` | `18` | `0` to `100` |
| `RadiusY` | `18` | `0` to `100` |
| `StrokeThickness` | `2` | `0` to `20` |
| `RotationDegrees` | `0` | `0` to `360` |
| `WidgetWidth` | `170` | Positive value |
| `WidgetHeight` | `120` | Positive value |

Ellipse quick tip:
- Set `RadiusX = Width / 2` and `RadiusY = Height / 2`.

<!-- Screenshot placeholder: xpf-hmi-21-widget-rounded-rectangle.png -->
> Image coming soon...

## 12) Arrow

Directional shape for flow, direction, or motion cues.

| Key Property | Default | Range / Options |
|---|---|---|
| `HeadLengthPercent` | `30` | `10` to `65` |
| `ShaftThicknessPercent` | `35` | `8` to `90` |
| `StrokeThickness` | `2` | `0` to `20` |
| `RotationDegrees` | `0` | `0` to `360` |
| `WidgetWidth` | `170` | Positive value |
| `WidgetHeight` | `100` | Positive value |

<!-- Screenshot placeholder: xpf-hmi-22-widget-arrow.png -->
> Image coming soon...

## 13) Triangle

Directional indicator for status and flow direction.

| Key Property | Default | Range / Options |
|---|---|---|
| `Orientation` | `Up` | `Up`, `Down`, `Left`, `Right` |
| `StrokeThickness` | `2` | `0` to `20` |
| `RotationDegrees` | `0` | `0` to `360` |
| `WidgetWidth` | `150` | Positive value |
| `WidgetHeight` | `120` | Positive value |

<!-- Screenshot placeholder: xpf-hmi-23-widget-triangle.png -->
> Image coming soon...

## 14) Polygon

Multi-sided shape for layout and zone markers.

| Key Property | Default | Range / Options |
|---|---|---|
| `SideCount` | `6` | `4` to `8` |
| `StrokeThickness` | `2` | `0` to `20` |
| `RotationDegrees` | `0` | `0` to `360` |
| `WidgetWidth` | `140` | Positive value |
| `WidgetHeight` | `140` | Positive value |

<!-- Screenshot placeholder: xpf-hmi-24-widget-polygon.png -->
> Image coming soon...

## 15) Arc

Arc or sector shape with full angle control.

| Key Property | Default | Range / Options |
|---|---|---|
| `StartAngle` | `225` | `0` to `360` |
| `SweepAngle` | `270` | `-359` to `359` |
| `StrokeThickness` | `8` | `0` to `20` |
| `RotationDegrees` | `0` | `0` to `360` |
| `WidgetWidth` | `170` | Positive value |
| `WidgetHeight` | `120` | Positive value |

<!-- Screenshot placeholder: xpf-hmi-25-widget-arc.png -->
> Image coming soon...

## License Tier Note

Widget visibility depends on your active license tier. The gallery shows only widgets available for that tier.

## Choosing the Right Widget

Use this quick guide when building a dashboard:
- Use `Numeric` for exact values (temperature, pressure, speed).
- Use `Dial180` or `Bar Graph` for fast visual status.
- Use `MultiState Indicator` when you need clear state colors or images.
- Use `Trend` to watch value history over time.
- Use `Button` and `Slider` for operator write actions.
- Use shape widgets (`Line`, `Rounded Rectangle`, `Arrow`, `Triangle`, `Polygon`, `Arc`) for layout, flow direction, and visual grouping.

For most pages, start with `Numeric + MultiState + Trend`, then add control and shape widgets as needed.

## Related Documentation

- [HMI Dashboard Management](hmi-widget-management.md) - HMI operations workflow
- [User Guide](user-guide.md) - Full XPF manual
