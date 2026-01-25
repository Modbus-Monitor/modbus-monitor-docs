# NumericGauge Widget

## Overview

The **NumericGauge** widget displays a single numeric value with state-based color indication. It's the simplest gauge type, ideal for straightforward numeric monitoring where you want context-aware visual feedback.

**Display**: Large numeric text with colored border indicating current state

**Best For**: 
- Simple value displays (pressure, flow rate, percentage)
- Status context through color change
- Minimal visual footprint while maintaining usability

---

## Features

### Core Display
- **Large numeric text** centered in widget
- **Colored border** that changes based on value range
- **Optional state name label** (e.g., "Normal", "Alert")
- **Custom widget label** above or below value
- **Configurable decimal places** via global settings

### State Management
- **Unlimited state ranges** - define as many zones as needed
- **Automatic color evaluation** - updates instantly on value change
- **State-specific naming** - label each zone clearly
- **Default fallback color** - used when value is out of range

### Configuration
- **JSON save/load** - all settings persist to HMI file
- **Copy/paste ranges** - reuse configurations across widgets
- **Inline editing** - modify Min, Max, Name directly in grid

---

## Quick Start

### 1. Add NumericGauge Widget

In HMI Editor:
```
1. Right-click on canvas
2. Select "Add Widget"
3. Choose "NumericGauge"
4. Draw widget on canvas
```

Or programmatically:
```csharp
var widget = WidgetFactory.CreateWidget(register, "NumericGauge");
canvas.Children.Add(widget);
```

### 2. Configure Monitoring Point

In **Property Editor**:
1. **Monitoring Point** → Select the Modbus register to display
2. **Show Label** → Toggle widget label visibility
3. **Widget Label** → Custom name (optional)

### 3. Define State Ranges

In **Property Editor → State Ranges**:

| Step | Action |
|------|--------|
| 1 | Click **Add [+]** button |
| 2 | Edit **Min** value (e.g., 0) |
| 3 | Edit **Max** value (e.g., 25) |
| 4 | Click **Color** button and choose blue |
| 5 | Edit **Name** to "Low Temperature" |
| 6 | Repeat for other zones |

### 4. Save Configuration

- Click **Save** or use Ctrl+S
- Configuration automatically saved to HMI file
- Ranges will reload when HMI is reopened

---

## Properties

### Display Properties

| Property | Type | Default | Description |
|----------|------|---------|-------------|
| **WidgetLabel** | string | "" | Custom display name |
| **ShowLabel** | bool | true | Show/hide widget label |
| **FontSize** | int | 14 | Label font size in points |
| **TextColor** | string | #FF000000 | Label text color (hex) |
| **DisplayFormat** | string | F1 | .NET format string (F0, F1, F2, etc.) |

### Range Properties

| Property | Type | Description |
|----------|------|-------------|
| **StateRanges** | ObservableCollection | List of color/state mappings |
| **CurrentStateColor** | Color | Current state's color (#AARRGGBB) |
| **CurrentStateName** | string | Current state's name |

### Bound Register

| Property | Type | Description |
|----------|------|-------------|
| **BoundRegister** | MMARegister | Modbus register to monitor |
| **CurrentValue** | double | Current register value |
| **FormattedValue** | string | Value formatted per DisplayFormat |

---

## State Range Configuration

### Adding Ranges

Each range defines a value zone with associated color and name:

```
Range 1: Min=0,   Max=20,  Color=Blue,   Name="Low"
Range 2: Min=21,  Max=60,  Color=Green,  Name="Normal"
Range 3: Min=61,  Max=100, Color=Red,    Name="High"
```

### Evaluation Logic

When register value changes:
1. Compare value against each range Min-Max
2. Use **first matching range**'s color and name
3. If no match → use **DefaultStateColor**

### Example Scenarios

**Temperature Monitoring (0-100°C)**
```
0-15°C   → Blue "Freezing"
16-25°C  → Cyan "Cold"
26-35°C  → Green "Comfortable"
36-45°C  → Yellow "Warm"
46-100°C → Red "Hot"
```

**Pressure Warning (PSI)**
```
0-50   → Green "Safe"
51-75  → Yellow "Caution"
76-100 → Red "Critical"
```

**Tank Level (%)**
```
0-25   → Red "Low"
26-75  → Green "Normal"
76-100 → Yellow "Near Full"
```

---

## Appearance

### Default View

```
┌─────────────────────┐
│  Temperature        │  ← Widget Label
├─────────────────────┤
│                     │
│      45.3°C         │  ← Numeric Value (FormattedValue)
│      Normal         │  ← State Name
│                     │
└─────────────────────┘
    ▲
    └─ Border color changes based on value
       (Green for 26-35°C)
```

### Color States Example

| Value | Range | Color | State Name |
|-------|-------|-------|-----------|
| 10 | 0-15 | 🔵 Blue | Freezing |
| 22 | 16-25 | 🟦 Cyan | Cold |
| 32 | 26-35 | 🟢 Green | Comfortable |
| 40 | 36-45 | 🟨 Yellow | Warm |
| 55 | 46-100 | 🔴 Red | Hot |

---

## Copy/Paste Configurations

### Copy Single Range

```
1. Select a range in the grid
2. Click Copy button
3. Switch to another widget
4. Click Paste
→ Adds that range to the other widget
```

**Clipboard Format** (Single Object):
```json
{
  "MinValue": 0,
  "MaxValue": 20,
  "StateColor": "#FF0000FF",
  "StateName": "Low",
  "ImagePath": ""
}
```

### Copy All Ranges

```
1. Click Copy All button (no selection needed)
2. All ranges copied as JSON array
3. Switch to another widget
4. Click Paste
→ Replaces all ranges with copied configuration
```

**Clipboard Format** (Array):
```json
[
  {
    "MinValue": 0,
    "MaxValue": 20,
    "StateColor": "#FF0000FF",
    "StateName": "Low",
    "ImagePath": ""
  },
  {
    "MinValue": 21,
    "MaxValue": 60,
    "StateColor": "#FF00FF00",
    "StateName": "Normal",
    "ImagePath": ""
  }
]
```

---

## Data Binding

### View to ViewModel

The NumericGauge View binds to ViewModel properties:

```xaml
<!-- Display current value -->
<TextBlock Text="{Binding FormattedValue}" FontSize="32" />

<!-- Display state name -->
<TextBlock Text="{Binding CurrentStateName}" FontSize="12" />

<!-- Border color based on state -->
<Border Background="{Binding CurrentStateColor, 
    Converter={StaticResource ColorToBrushConverter}}" />
```

### ViewModel Automatic Updates

```csharp
// When register value changes:
protected override void Register_PropertyChanged(object sender, PropertyChangedEventArgs e)
{
    if (e.PropertyName == nameof(MMARegister.RegValueDouble))
    {
        UpdateFormattedValue();      // Update display text
        EvaluateCurrentState();      // Update color & state name
    }
}
```

---

## JSON Serialization

### SaveToJson()

Complete widget configuration saved to HMI file:

```json
{
  "WidgetLabel": "CPU Temperature",
  "ShowLabel": true,
  "FontSize": 14,
  "TextColor": "#FF000000",
  "DisplayFormat": "F1",
  "MinValue": 0,
  "MaxValue": 100,
  "StateRanges": [
    {
      "MinValue": 0,
      "MaxValue": 40,
      "StateColor": "#FF00C800",
      "StateName": "Normal",
      "ImagePath": ""
    },
    {
      "MinValue": 41,
      "MaxValue": 70,
      "StateColor": "#FFFFC800",
      "StateName": "Warning",
      "ImagePath": ""
    },
    {
      "MinValue": 71,
      "MaxValue": 100,
      "StateColor": "#FFC80000",
      "StateName": "Critical",
      "ImagePath": ""
    }
  ]
}
```

### LoadFromJson()

Restores all settings when HMI reopens:
- Widget label and visibility
- Font size and color
- All state ranges with colors
- Display format

---

## Advanced Usage

### Programmatic State Ranges

```csharp
var gauge = new NumericGaugeViewModel(register);

// Add ranges via code
gauge.AddStateRange(0, 40, Colors.Green, "Normal");
gauge.AddStateRange(41, 70, Colors.Yellow, "Warning");
gauge.AddStateRange(71, 100, Colors.Red, "Critical");

// Access current state
Debug.WriteLine($"Color: {gauge.CurrentStateColor}");
Debug.WriteLine($"State: {gauge.CurrentStateName}");

// Force re-evaluation
gauge.EvaluateCurrentState();
```

### Custom Formatting

```csharp
// Display format strings:
gauge.DisplayFormat = "F0";    // No decimals: "45"
gauge.DisplayFormat = "F1";    // 1 decimal: "45.3"
gauge.DisplayFormat = "F2";    // 2 decimals: "45.32"
gauge.DisplayFormat = "P0";    // Percentage: "45%"
gauge.DisplayFormat = "N2";    // Thousands sep: "1,234.56"
```

### Event Subscription

```csharp
gauge.PropertyChanged += (s, e) => 
{
    if (e.PropertyName == nameof(gauge.CurrentStateColor))
    {
        Debug.WriteLine("State color changed!");
    }
};
```

---

## Troubleshooting

### Color Not Updating

**Problem**: Border color doesn't change when value changes

**Solutions**:
1. Check register is properly bound (Monitoring Point set)
2. Verify range Min/Max values cover the expected value
3. Ensure ColorToBrushConverter is available in resources
4. Check StateRanges collection is not empty

### Value Shows Wrong Format

**Problem**: Shows "45.327" instead of "45.3"

**Solutions**:
1. Set DisplayFormat to "F1" for 1 decimal place
2. Check format string syntax (.NET format codes)
3. Verify decimal settings in global app config

### Out-of-Range Values

**Problem**: Value is not within any defined range, shows default color

**Solutions**:
1. Add ranges to cover entire expected value domain
2. Use DefaultStateColor property to set fallback color
3. Consider overlapping ranges if gaps are intentional

### Copy/Paste Not Working

**Problem**: Paste button shows error or doesn't add ranges

**Solutions**:
1. Ensure clipboard contains valid JSON
2. Check JSON format matches expected structure
3. Verify range has Min < Max values
4. Look for error message in clipboard validation dialog

---

## Related Widgets

- [MultiStateIndicator](multistate_indicator.md) - Background color indicator
- [BarGraph](bar_graph.md) - Directional fill gauge
- [Dial180](dial180_index.md) - Semi-circular analog gauge

---

## Files

- **View**: `Sample 1A/Widgets/Gauges/NumericGaugeView.xaml`
- **ViewModel**: `Sample 1A/Widgets/Gauges/NumericGaugeViewModel.cs`
- **Range Editor**: `Sample 1A/Widgets/PropertyEditing/RangeEditorControl.xaml`
