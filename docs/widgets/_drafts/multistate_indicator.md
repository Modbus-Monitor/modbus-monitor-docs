# MultiStateIndicator Widget

## Overview

The **MultiStateIndicator** widget displays background colors or images that change based on value ranges or boolean state. It's a versatile status indicator with support for unlimited state definitions, making it ideal for status displays, mode indicators, and condition visualization.

**Display**: Colored/image background with optional state label

**Best For**:
- Status indicators (OK, Warning, Alarm)
- Mode displays (Off, Standby, Running)
- Condition indicators (Low/Normal/High levels)
- Visual alerts (Green/Yellow/Red zones)

---

## Features

### Core Display
- **Colored background** that changes based on register value
- **Optional state image** (future enhancement, infrastructure ready)
- **State name label** (e.g., "Normal", "Alert", "Off")
- **Customizable appearance** (font size, text color, border)
- **Two operating modes**: Range-based or Boolean

### State Management
- **Unlimited state ranges** - define as many zones as needed
- **Automatic state evaluation** - updates instantly on value change
- **Named states** - clear, descriptive labels
- **Default state color** - used when value is out of range
- **Image support** - infrastructure for state-specific images

### Modes
- **Range Mode (V2)** - Value ranges with colors (new, default)
- **Boolean Mode (V1)** - Simple 0/1 on/off with two colors (legacy)

---

## Quick Start

### 1. Add MultiStateIndicator Widget

In HMI Editor:
```
1. Right-click on canvas
2. Select "Add Widget"
3. Choose "MultiStateIndicator"
4. Draw widget on canvas
```

Or programmatically:
```csharp
var widget = WidgetFactory.CreateWidget(register, "MultiStateIndicator");
canvas.Children.Add(widget);
```

### 2. Configure Monitoring Point

In **Property Editor**:
1. **Monitoring Point** → Select the Modbus register to monitor
2. **Mode** → Keep as "Range Mode" (V2, default)
3. **Show Label** → Toggle label visibility
4. **Show State Name** → Toggle state name visibility
5. **Widget Label** → Custom name (optional)

### 3. Define State Ranges

In **Property Editor → State Ranges**:

| Step | Action |
|------|--------|
| 1 | Click **Add [+]** to create new range |
| 2 | Set **Min**: 0, **Max**: 20 |
| 3 | Click **Color**, choose gray → "Low / Off" |
| 4 | Click **Add [+]** again |
| 5 | Set **Min**: 21, **Max**: 60 |
| 6 | Click **Color**, choose green → "Normal" |
| 7 | Click **Add [+]** once more |
| 8 | Set **Min**: 61, **Max**: 100 |
| 9 | Click **Color**, choose red → "High / Alert" |

### 4. Save Configuration

- Click **Save** or use Ctrl+S
- All ranges save to HMI JSON file
- Ranges reload when HMI reopens

---

## Properties

### Display Properties

| Property | Type | Default | Description |
|----------|------|---------|-------------|
| **WidgetLabel** | string | "" | Custom display name |
| **ShowLabel** | bool | true | Show/hide widget label |
| **ShowStateName** | bool | true | Show state name in widget |
| **ShowValue** | bool | false | Display numeric value |
| **FontSize** | int | 14 | Font size in points |
| **TextColor** | string | #FF000000 | Text color (hex) |
| **ShowBorder** | bool | true | Toggle 3D border/shadow |

### Mode Properties

| Property | Type | Default | Description |
|----------|------|---------|-------------|
| **IsBooleanMode** | bool | false | Toggle between boolean/range mode |
| **DefaultStateColor** | Color | RGB(200,200,200) | Color when out of range |

### State Properties

| Property | Type | Description |
|----------|------|-------------|
| **StateRanges** | ObservableCollection | List of color/state mappings |
| **CurrentStateColor** | Color | Current state's color |
| **CurrentStateName** | string | Current state's name |
| **CurrentStateImagePath** | string | Current state's image (if any) |

---

## Operating Modes

### Range Mode (V2 - Recommended)

Define multiple value zones with associated colors and names. Perfect for monitoring continuous values with gradual state progression.

**Example: Tank Level**
```
0-25%   → Red    "Low / Refill"
26-75%  → Green  "Normal"
76-100% → Yellow "Near Full"
```

**Configuration**:
- Unlimited ranges
- Set Min, Max for each zone
- Assign color to zone
- Name each state
- Evaluate: First matching range wins

### Boolean Mode (V1 - Legacy)

Simple on/off mode compatible with older HMI files. Value 0 = Off (default color), Value 1+ = On (green or custom).

**Example: Pump Status**
```
0 → Gray "Pump Off"
1 → Green "Pump Running"
```

**To Enable Boolean Mode**:
1. Open Property Editor
2. Find "Boolean Mode" toggle
3. Enable it
4. Set DefaultStateColor and OnStateColor

---

## State Evaluation

### How It Works

When the monitored register value changes:

```
1. Compare value against StateRanges list
   ↓
2. Find first range where: MinValue ≤ Value ≤ MaxValue
   ↓
3. Set CurrentStateColor = range.StateColor
   Set CurrentStateName = range.StateName
   ↓
4. UI updates immediately (binding)
   ↓
5. If no range matches → Use DefaultStateColor
```

### Example Execution

```csharp
// Value = 45
// StateRanges:
//   [0] Min=0,   Max=20,  Color=Red,   Name="Low"
//   [1] Min=21,  Max=60,  Color=Green, Name="Normal"  ← MATCHES
//   [2] Min=61,  Max=100, Color=Blue,  Name="High"

// Result: Background = Green, Label = "Normal"
```

---

## Appearance

### Default View

```
┌──────────────────────┐
│   Pump Status        │  ← Widget Label
├──────────────────────┤
│                      │
│      RUNNING         │  ← State Name
│                      │
└──────────────────────┘
  ▲
  └─ Background color changes based on state
     (Green when pump is running)
```

### State Display Examples

| Value | State Name | Color | Display |
|-------|-----------|-------|---------|
| 10 | Low/Off | 🔴 Red | Refill needed |
| 45 | Normal | 🟢 Green | Operating OK |
| 95 | Near Full | 🟨 Yellow | Almost full |

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

### Copy All Ranges

```
1. Click Copy All button
2. All ranges copied as JSON array
3. Switch to another widget  
4. Click Paste
→ Replaces all ranges with copied configuration
```

### Copy Multiple Selected Ranges

```
1. Ctrl+Click to select multiple ranges
2. Click Copy button
3. Ranges copied as array
4. Switch to another widget
5. Click Paste
→ Adds all selected ranges
```

**Example JSON Array**:
```json
[
  {
    "MinValue": 0,
    "MaxValue": 20,
    "StateColor": "#FFC8C8C8",
    "StateName": "Low / Off",
    "ImagePath": ""
  },
  {
    "MinValue": 21,
    "MaxValue": 60,
    "StateColor": "#FF00C800",
    "StateName": "Normal",
    "ImagePath": ""
  },
  {
    "MinValue": 61,
    "MaxValue": 100,
    "StateColor": "#FFC80000",
    "StateName": "High / Alert",
    "ImagePath": ""
  }
]
```

---

## Real-World Examples

### Example 1: Temperature Status Display

```
Configuration:
- 0°C to 15°C    → Blue   "Freezing"
- 16°C to 25°C   → Cyan   "Cold"
- 26°C to 35°C   → Green  "Comfortable"
- 36°C to 45°C   → Yellow "Warm"
- 46°C to 60°C   → Red    "Hot"

Widget Behavior:
Current Temp: 28°C → Display: "Comfortable" (Green background)
Current Temp: 52°C → Display: "Hot" (Red background)
```

### Example 2: System Status

```
Configuration:
- 0    → Gray    "System Off"
- 1    → Blue    "Initializing"
- 2    → Green   "Running"
- 3    → Yellow  "Warning"
- 4-99 → Red     "Error"
- 100  → Black   "Critical Failure"

Widget Behavior:
Status Register: 2 → Display: "Running" (Green)
Status Register: 3 → Display: "Warning" (Yellow)
```

### Example 3: Equipment Operating Mode

```
Configuration:
- 0     → Gray      "Standby"
- 1-50  → Green     "Low Speed"
- 51-80 → Yellow    "Medium Speed"
- 81-100 → Red      "High Speed"

Widget Behavior:
Speed: 0    → "Standby" (Gray)
Speed: 45   → "Low Speed" (Green)
Speed: 95   → "High Speed" (Red)
```

---

## Data Binding

### XAML View Bindings

```xaml
<!-- Background changes with state color -->
<Border Background="{Binding CurrentStateColor, 
    Converter={StaticResource ColorToBrushConverter}}" />

<!-- Display state name -->
<TextBlock Text="{Binding CurrentStateName}" />

<!-- Display register value (optional) -->
<TextBlock Text="{Binding CurrentValue}" />

<!-- Display label (register name or custom) -->
<TextBlock Text="{Binding DisplayLabel}" />
```

### ViewModel Auto-Updates

```csharp
// When register value changes, automatically:
protected override void Register_PropertyChanged(object sender, PropertyChangedEventArgs e)
{
    if (e.PropertyName == nameof(MMARegister.RegValueDouble))
    {
        EvaluateCurrentState();  // Recalculate color and state name
    }
}

// Properties notify when color/state changes
public Color CurrentStateColor
{
    get { return _currentStateColor; }
    set { Set(ref _currentStateColor, value); }  // Triggers UI update
}
```

---

## JSON Serialization

### SaveToJson()

Complete configuration persisted to HMI file:

```json
{
  "IsBooleanMode": false,
  "WidgetLabel": "Tank Level",
  "ShowLabel": true,
  "ShowStateName": true,
  "ShowValue": false,
  "ShowBorder": true,
  "FontSize": 14,
  "TextColor": "#FF000000",
  "DefaultStateColor": "#FFC8C8C8",
  "StateRanges": [
    {
      "MinValue": 0,
      "MaxValue": 25,
      "StateColor": "#FFC80000",
      "StateName": "Low / Refill",
      "ImagePath": ""
    },
    {
      "MinValue": 26,
      "MaxValue": 75,
      "StateColor": "#FF00C800",
      "StateName": "Normal",
      "ImagePath": ""
    },
    {
      "MinValue": 76,
      "MaxValue": 100,
      "StateColor": "#FFFFC800",
      "StateName": "Near Full",
      "ImagePath": ""
    }
  ]
}
```

### LoadFromJson()

- All state ranges restored
- Display settings applied
- Widget inherits correct mode
- Ready for display immediately

---

## IWidgetWithImages Interface

MultiStateIndicator implements `IWidgetWithImages` for future image support:

```csharp
public IEnumerable<string> GetImagePaths()
{
    foreach (var range in StateRanges)
    {
        if (!string.IsNullOrEmpty(range.ImagePath))
            yield return range.ImagePath;
    }
}
```

**Future Enhancement**: When image support is enabled, each state can display a custom image instead of (or with) the color background.

---

## Advanced Usage

### Programmatic Configuration

```csharp
var indicator = new MultiStateIndicatorViewModel(register);

// Add ranges via code
indicator.AddStateRange(0, 25, Colors.Red, "Low / Refill");
indicator.AddStateRange(26, 75, Colors.Green, "Normal");
indicator.AddStateRange(76, 100, Colors.Yellow, "Near Full");

// Access current state
Debug.WriteLine($"Color: {indicator.CurrentStateColor}");
Debug.WriteLine($"State: {indicator.CurrentStateName}");

// Switch to boolean mode
indicator.IsBooleanMode = true;

// Trigger re-evaluation
indicator.EvaluateCurrentState();
```

### Event Subscription

```csharp
indicator.PropertyChanged += (s, e) => 
{
    if (e.PropertyName == nameof(indicator.CurrentStateColor))
    {
        Debug.WriteLine($"State changed to: {indicator.CurrentStateName}");
    }
};
```

---

## Troubleshooting

### Color Doesn't Change on Value Change

1. **Check**: Monitoring Point is set to a valid register
2. **Check**: Range Min/Max values cover expected register values
3. **Check**: StateRanges collection is not empty
4. **Check**: Widget not in boolean mode if you expect ranges

### Wrong State Displayed

1. **Check**: Range definitions don't have gaps or overlaps
2. **Check**: Min ≤ Max for each range (not reversed)
3. **Check**: First matching range wins (check order if overlapping)
4. **Check**: Value really falls in the range you think

### Out-of-Range Values Show Wrong Color

1. **Verify**: Value is actually outside all ranges
2. **Set**: DefaultStateColor to desired fallback color
3. **Consider**: Adding ranges to cover full value domain

### Copy/Paste Not Working

1. **Check**: Clipboard has valid JSON format
2. **Check**: JSON matches expected range structure
3. **Check**: No special characters breaking JSON parsing
4. **Look**: For error message in paste dialog

---

## Best Practices

✅ **Do:**
- Use meaningful state names ("Critical Alert" not "State5")
- Choose intuitive colors (green=OK, red=error, yellow=warning)
- Cover the entire expected value range with ranges
- Test with out-of-range values
- Document your range definitions

❌ **Don't:**
- Overlap ranges with conflicting semantics
- Use colors that are hard to distinguish
- Leave large value gaps uncovered
- Forget to test state transitions
- Skip saving after configuration changes

---

## Migration from Boolean Mode

If upgrading from boolean mode to range mode:

1. **Enable Range Mode**: Set IsBooleanMode = false
2. **Clear Old Settings**: Remove old boolean color settings
3. **Add Ranges**: Define comprehensive ranges for your values
4. **Test**: Verify all value ranges display correctly
5. **Save**: Store new configuration

---

## Related Widgets

- [NumericGauge](numeric_gauge.md) - Text value with colored border
- [BarGraph](bar_graph.md) - Directional fill gauge
- [Dial180](dial180_index.md) - Semi-circular analog gauge

---

## Files

- **View**: `Sample 1A/Widgets/Gauges/MultiStateIndicatorView.xaml`
- **ViewModel**: `Sample 1A/Widgets/Gauges/MultiStateIndicatorViewModel.cs`
- **Range Editor**: `Sample 1A/Widgets/PropertyEditing/RangeEditorControl.xaml`
