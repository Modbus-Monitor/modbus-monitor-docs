# Dial180 Gauge Widget — Complete Integration Guide

## Overview

The **Dial180** gauge widget is a highly configurable semicircular/270° dial gauge for HMI dashboards. It displays analog data with full customization of dial orientation, scale resolution, and colored range zones — matching the flexibility of the MultiStateIndicator widget while providing true analog gauge rendering.

**Current Version:** 2.0 (with State Ranges foundation)  
**Status:** Production-ready (all core features tested)  
**Framework:** WPF, MVVM pattern

---

## Key Features

### ✓ Configurable Dial Orientation (StartAngle / SweepAngle)

- **StartAngle** (degrees): Where the dial's minimum value is positioned
  - `0°` = right (3 o'clock) | `90°` = up | `180°` = left | `-90°` = down
  
- **SweepAngle** (degrees): Total sweep direction and magnitude
  - `-180°` = classic semicircle | `-270°` = full 270° dial

**Examples:**
```
StartAngle=225, SweepAngle=-270 → Minimum at bottom-left, maximum at bottom-right
StartAngle=90, SweepAngle=-180   → Minimum at top, maximum at bottom
StartAngle=180, SweepAngle=-180  → Classic 180° (default)
```

### ✓ Dynamic Tick Marks (MajorTickStep / MinorTickStep)

- **MajorTickStep**: Spacing (in value units) for large tick marks
- **MinorTickStep**: Spacing for smaller tick marks between major ticks
- Set `MajorTickStep=0` to hide all ticks

### ✓ Concentric Arc Layering (Visual Depth)

Three layered arcs render concentrically for professional appearance:

| Arc Layer | Color | Stroke Width | Purpose |
|-----------|-------|-------------|---------|
| **Background** | Light Gray (#E8E8E8) | 6pt | Full dial range (0–100%) |
| **Operating Range** | Light Blue (#B3D9FF) | 5pt | Valid operating range (Min–Max) |
| **Active Value** | Bright Blue (#0078D4) | 4pt | Current value indicator |

### ✓ State Ranges Foundation (Colored Range Arcs)

- Currently: Inner class `DialStateRange` ready for Phase 2
- Properties: MinValue, MaxValue, RangeColor, RangeName
- Planned: XAML ItemsControl renders each range as colored arc

---

## Properties Reference

### Binding Properties

| Property | Type | Default | Description |
|----------|------|---------|-------------|
| `CurrentValue` | `double` | `0` | Current gauge value (displayed as needle position) |
| `Minimum` | `double` | `0` | Minimum value on scale |
| `Maximum` | `double` | `100` | Maximum value on scale |

### Orientation Properties

| Property | Type | Default | Description |
|----------|------|---------|-------------|
| `StartAngle` | `double` | `180` | Dial minimum position (degrees): 0°=right, 90°=up, 180°=left, -90°=down |
| `SweepAngle` | `double` | `-180` | Total sweep: -180°=semicircle, -270°=270° dial |

### Tick Properties

| Property | Type | Default | Description |
|----------|------|---------|-------------|
| `MajorTickStep` | `double` | `20` | Spacing between major ticks (0 to hide) |
| `MinorTickStep` | `double` | `10` | Spacing between minor ticks |

### Display Properties

| Property | Type | Default | Description |
|----------|------|---------|-------------|
| `ValueFormat` | `string` | `"F1"` | Display format for current value ("F0", "F1", "F2") |
| `RangeFormat` | `string` | `"F1"` | Display format for min/max labels |
| `ShowNeedle` | `bool` | `true` | Display needle indicator |
| `ShowScale` | `bool` | `true` | Display min/max range labels |

---

## How to Use: Step-by-Step

### Step 1: Add Dial180 to Dashboard
1. Open HMI Dashboard in designer
2. Drag **Dial180** widget from toolbox
3. Position and resize to 160×140 pixels (recommended for 270° dials)

### Step 2: Bind Data
1. Right-click widget → **Properties**
2. Find **CurrentValue** property
3. Click dropdown → Select Modbus register
4. Set **Minimum** and **Maximum** to bracket expected values

### Step 3: Configure Appearance
1. Set **StartAngle** and **SweepAngle** for desired orientation
2. Adjust **MajorTickStep** and **MinorTickStep** for tick spacing
3. Toggle **ShowNeedle** and **ShowScale** as needed
4. Set **ValueFormat** for decimal precision

### Step 4: Save
1. Click **Save Dashboard** (Ctrl+S)
2. Configuration automatically persists to `.hmi` file

---

## Configuration Examples

### Example 1: Classic 180° Horizontal Dial
```
StartAngle: 180
SweepAngle: -180
MajorTickStep: 20
MinorTickStep: 10
Minimum: 0
Maximum: 100
```
**Appearance:** Horizontal semicircle with needle pointing right at max

### Example 2: Industrial 270° Dial (Down-Pointing)
```
StartAngle: 225
SweepAngle: -270
MajorTickStep: 25
MinorTickStep: 5
Minimum: 0
Maximum: 100
```
**Appearance:** 270° dial starting at bottom-left, sweeping to bottom-right

### Example 3: Temperature Gauge (Compact)
```
StartAngle: 200
SweepAngle: -140
MajorTickStep: 10
MinorTickStep: 5
Minimum: -50
Maximum: 50
ValueFormat: "F0"
```
**Appearance:** Compact 140° gauge, ideal for tight layouts

### Example 4: Inverted Dial (Needle Up = Max)
```
StartAngle: 90
SweepAngle: -180
MajorTickStep: 10
MinorTickStep: 5
Minimum: 0
Maximum: 100
```
**Appearance:** Horizontal dial with minimum on right, maximum on left

---

## Troubleshooting

| Problem | Cause | Solution |
|---------|-------|----------|
| **Needle not moving** | No data binding | Check CurrentValue binding; select register |
| **Ticks not showing** | MajorTickStep = 0 or too large | Set MajorTickStep to reasonable value (e.g., 20) |
| **270° dial appears clipped** | Missing IsLargeArc binding | Verify SweepToIsLargeArcConverter is bound (rebuild if needed) |
| **Arcs look misaligned** | Stroke thickness incorrect | Verify: background=6pt, operating=5pt, active=4pt |
| **Min/Max labels don't update** | Value out of expected range | Set Minimum and Maximum to bracket actual data |

---

## File Locations

| Component | Location |
|-----------|----------|
| **View** | Sample 1A/Widgets/Gauges/Dial180View.xaml |
| **ViewModel** | Sample 1A/Widgets/Gauges/Dial180ViewModel.cs |
| **Converters** | Sample 1A/Converters/ValueToAngleConverter.cs, ValueToArcPointConverter.cs, etc. |
| **Configuration** | Sample 1A/Models/WidgetConfiguration.cs |

---

## AI Knowledge Base Notes

### Architecture Decisions

**Q: Why use multi-value binding with converters?**  
A: Converters enable real-time binding updates without event handlers. All geometry recalculates automatically when properties change. Matches MultiStateIndicator pattern.

**Q: Why three concentric arcs?**  
A: Layered visual feedback:
- Background = full possible range (0–100%)
- Operating = valid instrument range (Min–Max)
- Active = current value indicator

**Q: How does SweepToIsLargeArcConverter solve 270° issue?**  
A: WPF's ArcSegment requires `IsLargeArc=true` for sweeps >180°. Without it, 270° arc renders as 90° in wrong direction.

### Data Flow During Value Update

```
1. Modbus register updates (e.g., 45.5)
   ↓
2. CurrentValue property setter fires PropertyChanged
   ↓
3. XAML bindings re-evaluate:
   - ValueToAngleConverter recalculates needle angle
   - ValueToArcPointConverter recalculates arc endpoints
   ↓
4. Path geometry updates → needle position & arc update rendered
```

---

**Last Updated:** 2026-01-18
