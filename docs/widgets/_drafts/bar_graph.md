# BarGraph Widget

## Overview

The **BarGraph** widget displays a fill-based gauge that changes color and fill level based on value ranges. The bar can be oriented in four directions (North, South, East, West), making it ideal for level indicators, trends, or directional displays.

**Display**: Animated bar fill with color that changes based on value ranges

**Best For**:
- Level indicators (tanks, batteries, capacity)
- Trend visualization (rising/falling values)
- Progress displays (work completion %)
- Directional flow indicators

---

## Features

### Core Display
- **Directional bar fill** - North (↑), South (↓), East (→), West (←)
- **State-based color** - changes based on value ranges
- **Scale display** - min/max labels on bar edges
- **Value text** - current value displayed on or near bar
- **Optional background image** - for enhanced visual appeal

### State Management
- **Unlimited state ranges** - define as many zones as needed
- **Automatic color evaluation** - updates instantly on value change
- **State-specific naming** - label each zone clearly
- **Smooth fill animation** - visual feedback on value changes

### Configuration
- **JSON save/load** - all settings persist to HMI file
- **Copy/paste ranges** - reuse configurations across widgets
- **Flexible sizing** - adapts to any canvas area

---

## Quick Start

### 1. Add BarGraph Widget

In HMI Editor:
```
1. Right-click on canvas
2. Select "Add Widget"
3. Choose "BarGraph"
4. Draw widget on canvas
```

Or programmatically:
```csharp
var widget = WidgetFactory.CreateWidget(register, "BarGraph");
canvas.Children.Add(widget);
```

### 2. Set Gauge Range

In **Property Editor**:
1. **Gauge Minimum** → 0
2. **Gauge Maximum** → 100
3. **Orientation** → North (upward bar) or other direction

### 3. Configure Monitoring Point

In **Property Editor**:
1. **Monitoring Point** → Select Modbus register
2. **Show Label** → Toggle display name
3. **Show Value** → Toggle numeric display
4. **Show Scale** → Toggle min/max labels

### 4. Define State Ranges

In **Property Editor → State Ranges**:

| Step | Action |
|------|--------|
| 1 | Click **Add [+]** |
| 2 | Set **Min**: 0, **Max**: 30 |
| 3 | Click **Color**, choose red → "Low" |
| 4 | Click **Add [+]** |
| 5 | Set **Min**: 31, **Max**: 70 |
| 6 | Click **Color**, choose green → "Normal" |
| 7 | Click **Add [+]** |
| 8 | Set **Min**: 71, **Max**: 100 |
| 9 | Click **Color**, choose yellow → "High" |

### 5. Adjust Size and Position

- Drag widget to desired canvas location
- Resize by dragging edges
- Set exact dimensions in Property Editor if needed

---

## Properties

### Display Properties

| Property | Type | Default | Description |
|----------|------|---------|-------------|
| **WidgetLabel** | string | "" | Custom display name |
| **ShowLabel** | bool | true | Show/hide widget label |
| **ShowValue** | bool | true | Show/hide numeric value |
| **ShowScale** | bool | true | Show/hide scale labels |
| **ShowBorder** | bool | true | Toggle 3D border/shadow |

### Gauge Properties

| Property | Type | Default | Description |
|----------|------|---------|-------------|
| **Minimum** | double | 0 | Gauge minimum value (display range) |
| **Maximum** | double | 100 | Gauge maximum value (display range) |
| **ValueFormat** | string | F1 | Display format (F0, F1, F2, etc.) |
| **Orientation** | string | North | Fill direction: North/South/East/West |

### Range Properties

| Property | Type | Description |
|----------|------|-------------|
| **StateRanges** | ObservableCollection | List of color/state mappings |
| **CurrentStateColor** | Color | Current state's color |
| **CurrentStateName** | string | Current state's name |
| **DefaultStateColor** | Color | Fallback color when out of range |

### Background

| Property | Type | Description |
|----------|------|-------------|
| **BackgroundImagePath** | string | Optional background image |
| **BackgroundHasImage** | bool | True if image path is set |

---

## Orientations

### North (Upward Fill)

```
    ▼ Max (100)
┌─────────────┐
│     ▓▓▓     │ ← Fill level 75%
│     ▓▓▓     │
│     ▓▓▓     │
│             │
│             │
└─────────────┘
    ▲ Min (0)
```

Use for: Tank levels, battery charge, altitude

### South (Downward Fill)

```
    ▲ Max (100)
┌─────────────┐
│             │
│             │
│     ▓▓▓     │ ← Fill level 75%
│     ▓▓▓     │
│     ▓▓▓     │
└─────────────┘
    ▼ Min (0)
```

Use for: Depth, pressure (inverted), vertical drop

### East (Rightward Fill)

```
Min    ▓▓▓▓▓▓▓▓▓    Max
(0) ◄─────────────►  (100)
    ◀─ 75% Fill ─►
```

Use for: Progress, horizontal trend, width

### West (Leftward Fill)

```
Min                 Max
(0) ◄───────────────► (100)
    ◄─ 75% Fill ─►
```

Use for: Right-to-left progress, western flow

---

## State Range Configuration

### Temperature Tank Example

```
0-30°C   → Red    "Cold"    (heating needed)
31-50°C  → Green  "Ideal"   (operating normal)
51-70°C  → Yellow "Warm"    (monitor closely)
71-100°C → Red    "Critical" (dangerous temp)
```

### Fuel Tank Example

```
0-15%   → Red    "Empty - Refuel"
16-50%  → Yellow "Low Level"
51-85%  → Green  "Normal"
86-100% → Yellow "Full"
```

### System Load Example

```
0-25%   → Green  "Idle"
26-50%  → Green  "Normal"
51-75%  → Yellow "High Load"
76-100% → Red    "Maximum Load"
```

---

## Appearance

### Default North Orientation

```
┌──────────────────┐
│  Tank Level      │  ← Widget Label
├──────────────────┤
│      75.3%       │  ← Value Display
│                  │
│      ▓▓▓▓        │
│      ▓▓▓▓        │
│      ▓▓▓▓        │ ← Bar Fill (Green = Normal)
│                  │
│ 100   ▓▓▓▓   ▓▓ │  ← Scale Labels (if enabled)
│ 0                │
└──────────────────┘
```

### Color State Examples

| Fill % | Range | Color | State Name |
|--------|-------|-------|-----------|
| 10% | 0-30 | 🔴 Red | Cold |
| 45% | 31-50 | 🟢 Green | Ideal |
| 60% | 51-70 | 🟨 Yellow | Warm |
| 95% | 71-100 | 🔴 Red | Critical |

---

## Copy/Paste Configurations

### Copy Single Range

```
1. Select a range in the grid
2. Click Copy button
3. Switch to another BarGraph widget
4. Click Paste
→ Adds that range to the other bar
```

### Copy All Ranges

```
1. Click Copy All button
2. All ranges copied as JSON array
3. Switch to another BarGraph widget
4. Click Paste
→ Replaces all ranges with copied configuration
```

### Share Between Different Orientations

```
1. Configure BarGraph (North orientation)
2. Click Copy All
3. Create new BarGraph (East orientation)
4. Click Paste
→ Same color scheme applied to different orientation
```

**Example JSON**:
```json
[
  {
    "MinValue": 0,
    "MaxValue": 30,
    "StateColor": "#FFC80000",
    "StateName": "Cold",
    "ImagePath": ""
  },
  {
    "MinValue": 31,
    "MaxValue": 50,
    "StateColor": "#FF00C800",
    "StateName": "Ideal",
    "ImagePath": ""
  },
  {
    "MinValue": 51,
    "MaxValue": 100,
    "StateColor": "#FFFFC800",
    "StateName": "Warm",
    "ImagePath": ""
  }
]
```

---

## Data Binding

### XAML View Bindings

```xaml
<!-- Bar fill color based on current state -->
<Rectangle Fill="{Binding CurrentStateColor, 
    Converter={StaticResource ColorToBrushConverter}}" />

<!-- Current value display -->
<TextBlock Text="{Binding FormattedValue}" />

<!-- State name display -->
<TextBlock Text="{Binding CurrentStateName}" />

<!-- Scale labels -->
<TextBlock Text="{Binding Minimum}" />
<TextBlock Text="{Binding Maximum}" />
```

### ViewModel Auto-Updates

```csharp
// When register value changes:
protected override void Register_PropertyChanged(object sender, PropertyChangedEventArgs e)
{
    if (e.PropertyName == nameof(MMARegister.RegValueDouble))
    {
        UpdateFormattedValue();    // Update display value
        EvaluateCurrentState();    // Update color and state
    }
}

// Fill level automatically normalized to Minimum-Maximum range
private double GetNormalizedFillLevel()
{
    var range = Maximum - Minimum;
    var position = CurrentValue - Minimum;
    return (range > 0) ? position / range : 0.0;
}
```

---

## JSON Serialization

### SaveToJson()

Complete widget configuration:

```json
{
  "WidgetLabel": "Coolant Tank",
  "ShowLabel": true,
  "ShowValue": true,
  "ShowScale": true,
  "ShowBorder": true,
  "Minimum": 0,
  "Maximum": 100,
  "ValueFormat": "F1",
  "Orientation": "North",
  "BackgroundImagePath": "",
  "StateRanges": [
    {
      "MinValue": 0,
      "MaxValue": 30,
      "StateColor": "#FFC80000",
      "StateName": "Low Level",
      "ImagePath": ""
    },
    {
      "MinValue": 31,
      "MaxValue": 100,
      "StateColor": "#FF00C800",
      "StateName": "Adequate",
      "ImagePath": ""
    }
  ]
}
```

### LoadFromJson()

- All range definitions restored
- Display settings applied
- Orientation preserved
- Background image path loaded

---

## Advanced Usage

### Programmatic Configuration

```csharp
var bar = new BarGraphViewModel(register);

// Set gauge range
bar.Minimum = 0;
bar.Maximum = 100;

// Configure orientation
bar.Orientation = "North";  // North, South, East, or West

// Add ranges
bar.AddStateRange(0, 30, Colors.Red, "Low");
bar.AddStateRange(31, 70, Colors.Green, "Normal");
bar.AddStateRange(71, 100, Colors.Yellow, "High");

// Set formatting
bar.ValueFormat = "F1";  // 1 decimal place

// Access current state
Debug.WriteLine($"Fill: {bar.FormattedValue}");
Debug.WriteLine($"State: {bar.CurrentStateName}");
Debug.WriteLine($"Color: {bar.CurrentStateColor}");
```

### Multiple Bars in Sequence

```csharp
// Create a series of bars for multi-register monitoring
var registers = new[] { tempReg, pressureReg, flowReg };
var colors = new[] { "North", "East", "South" };

for (int i = 0; i < registers.Length; i++)
{
    var bar = new BarGraphViewModel(registers[i]);
    bar.Orientation = colors[i];
    bar.WidgetLabel = registers[i].RegName;
    canvas.Children.Add(bar);
}
```

---

## Real-World Examples

### Example 1: Water Tank Level

```
Configuration:
- Gauge: 0 - 100%
- Orientation: North (upward)
- Ranges:
  0-25%   → Red    "Low - Refill"
  26-75%  → Green  "Normal"
  76-100% → Yellow "Full - Stop"

Result: Bar rises/falls with water level, color indicates status
```

### Example 2: CPU Load Monitor

```
Configuration:
- Gauge: 0 - 100%
- Orientation: East (rightward)
- Ranges:
  0-30%   → Green  "Idle"
  31-60%  → Yellow "Normal"
  61-100% → Red    "Maxed Out"

Result: Horizontal bar shows processor usage trending
```

### Example 3: Battery Capacity

```
Configuration:
- Gauge: 0 - 100%
- Orientation: North (upward)
- Ranges:
  0-10%   → Red    "Critical"
  11-30%  → Yellow "Low"
  31-100% → Green  "Charged"

Result: Vertical bar shows remaining battery capacity
```

---

## Troubleshooting

### Bar Doesn't Animate on Value Change

1. **Check**: Monitoring Point is set to a valid register
2. **Check**: Value actually changes in the register
3. **Check**: Gauge Minimum < Maximum
4. **Verify**: Widget is visible on canvas

### Color Doesn't Change

1. **Check**: StateRanges collection is not empty
2. **Check**: Range Min/Max values match expected values
3. **Check**: Value falls within one of the ranges
4. **Check**: DefaultStateColor is set if value goes out-of-range

### Bar Fills Incorrectly or Backward

1. **Check**: Orientation is set correctly
2. **Check**: Minimum < Maximum (not reversed)
3. **Adjust**: Orientation to North/South/East/West as needed
4. **Verify**: Physical orientation matches expected direction

### Scale Labels Not Showing

1. **Check**: ShowScale is enabled in Property Editor
2. **Check**: Widget is large enough to display labels
3. **Increase**: Widget size if labels are too crowded
4. **Check**: Minimum/Maximum values are set

### Copy/Paste Issues

1. **Verify**: Clipboard contains valid JSON
2. **Check**: JSON has correct range structure
3. **Look**: For error message in paste dialog
4. **Ensure**: Target widget also implements IRangeConfigurable

---

## Performance Considerations

- **Fill Animation**: Smooth updates on value change (60 FPS)
- **Color Updates**: Instant when state changes
- **Range Evaluation**: O(n) where n = number of ranges
- **Rendering**: Optimized for multiple bars on canvas

### Optimization Tips

1. **Limit Ranges**: Keep range count reasonable (< 10 per widget)
2. **Reuse Configurations**: Use Copy/Paste to avoid redundant setup
3. **Update Frequency**: Consider register poll rate vs visual updates

---

## Best Practices

✅ **Do:**
- Use consistent colors across related bars
- Label states clearly in state names
- Cover full gauge range with ranges
- Test all orientations if using multiple bars
- Save configurations frequently

❌ **Don't:**
- Overlap ranges with contradictory meanings
- Use colors that are hard to distinguish
- Leave large unmatched value zones
- Forget to test at min/max values
- Change gauge range after deploying

---

## Related Widgets

- [MultiStateIndicator](multistate_indicator.md) - Background color indicator
- [NumericGauge](numeric_gauge.md) - Text value with colored border
- [Dial180](dial180_index.md) - Semi-circular analog gauge

---

## Files

- **View**: `Sample 1A/Widgets/Gauges/BarGraphView.xaml`
- **ViewModel**: `Sample 1A/Widgets/Gauges/BarGraphViewModel.cs`
- **Range Editor**: `Sample 1A/Widgets/PropertyEditing/RangeEditorControl.xaml`
