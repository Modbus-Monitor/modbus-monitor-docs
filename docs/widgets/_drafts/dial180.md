# Dial180 Widget Documentation

## Overview

The **Dial180** widget is a semi-circular analog gauge with a rotating needle and colored range arcs. It displays numeric values using traditional gauge aesthetics while supporting the same state-based color system as other Modbus Monitor widgets.

**Best for**: Analog monitoring, traditional gauge aesthetics, at-a-glance value assessment.

---

## Features

✅ **Semi-Circular Gauge** - 180° rotation arc  
✅ **Rotating Needle** - Animated pointer to value  
✅ **Colored Range Arcs** - Visual state zones  
✅ **State-Based Colors** - Automatic color mapping  
✅ **Customizable Ranges** - Define unlimited zones  
✅ **Copy/Paste Support** - Share configurations  
✅ **JSON Persistence** - Save and restore settings  
✅ **Smooth Animations** - Needle movement transitions  

---

## Quick Start (5 Steps)

### Step 1: Add Widget
```
Right-click canvas → Add Widget → Dial180
```

### Step 2: Bind Register
Property Editor:
- **Monitoring Point**: Select Modbus register
- **Widget Label**: Enter descriptive name (e.g., "Pressure")

### Step 3: Set Value Range
Property Editor:
- **Min Value**: 0
- **Max Value**: 100
- (Defines needle sweep range)

### Step 4: Define Color Ranges
Range Editor Panel:
| Min | Max | Name | Color |
|-----|-----|------|-------|
| 0 | 25 | Low Pressure | 🔵 Blue |
| 26 | 60 | Normal | 🟢 Green |
| 61 | 100 | High Pressure | 🔴 Red |

### Step 5: Save
```
File → Save or Ctrl+S
```

---

## Properties

### Display Properties

| Property | Type | Default | Purpose |
|----------|------|---------|---------|
| Label | string | "Dial" | Widget title text |
| Width | double | 200 | Widget width in pixels |
| Height | double | 200 | Widget height in pixels |
| Background | Color | White | Widget background |
| Foreground | Color | Black | Text color |

### Value Properties

| Property | Type | Default | Purpose |
|----------|------|---------|---------|
| MinValue | double | 0 | Minimum value on dial |
| MaxValue | double | 100 | Maximum value on dial |
| CurrentValue | double | 0 | Current numeric value |
| Format | string | "F1" | Display format (F0, F1, F2) |
| Unit | string | "" | Unit suffix (e.g., "psi", "°C") |

### State Properties

| Property | Type | Purpose |
|----------|------|---------|
| CurrentStateColor | Color | Color of current state |
| CurrentStateName | string | Name of current state |
| StateRanges | List | All defined ranges |

### Style Properties

| Property | Type | Default | Purpose |
|----------|------|---------|---------|
| NeedleThickness | double | 2 | Needle line width |
| NeedleColor | Color | Black | Needle drawing color |
| TextSize | double | 14 | Center text size |
| ArcThickness | double | 8 | Range arc line width |

---

## Gauge Geometry

### 180° Arc Visualization

```
        Min (0)
          |
         \|/
    ┌─────●─────┐
    │  ┌─────┐  │    Arc: 180° (left to right)
    │  │  ◐  │  │    Needle: Points to value
    │  └─────┘  │    Center: Shows value text
    │           │    Bottom: Shows Min/Max labels
    └───────────┘
         Max (100)
```

### Needle Positioning

- **Arc Range**: 180° from left (0) to right (100)
- **Needle Start**: Vertical at Min value (left side)
- **Needle End**: Vertical at Max value (right side)
- **Animation**: Smooth rotation to value position
- **Formula**: `angle = (value - MinValue) / (MaxValue - MinValue) * 180°`

### Color Arcs

Range arcs overlay the dial showing state zones:
- **Arc Position**: Concentric circles around dial
- **Arc Color**: CurrentStateColor from range evaluation
- **Arc Width**: Customizable thickness
- **Arc Length**: Based on range Min/Max values

---

## Configuration Examples

### Example 1: Temperature Gauge

```
Min Value: -40
Max Value: 50
Unit: °C

Ranges:
├─ -40 to 0  → Blue (Freezing)
├─  0 to 20  → Green (Normal)
├─ 20 to 35  → Yellow (Warm)
└─ 35 to 50  → Red (Hot)
```

Gauge appearance:
```
       -40°C
         |
    ┌────●────┐
    │  ┌────┐ │
    │  │ 22 │ │ ← Shows current value
    │  │°C  │ │
    │  └────┘ │
    │    ▼    │ ← Needle at 22°C
    └────┬────┘
        50°C
```

### Example 2: Pressure Gauge

```
Min Value: 0
Max Value: 500
Unit: psi

Ranges:
├─   0 to 100 → Green (Low)
├─ 100 to 350 → Blue (Normal)
├─ 350 to 450 → Yellow (High)
└─ 450 to 500 → Red (Critical)
```

### Example 3: Speed Gauge

```
Min Value: 0
Max Value: 120
Unit: km/h

Ranges:
├─  0 to 30 → Blue (Idle)
├─ 30 to 80 → Green (Normal)
├─ 80 to 110 → Yellow (High)
└─ 110 to 120 → Red (Dangerous)
```

---

## State Evaluation

### Flow Diagram

```
Value changes from register
           ↓
Register_PropertyChanged event
           ↓
EvaluateCurrentState() called
           ↓
Loop through StateRanges
    │
    ├─ Is value >= MinValue?
    │  Is value <= MaxValue?
    │
    └─ Yes → Set CurrentStateColor
              Set CurrentStateName
              Update needle rotation
              Update arc colors
           ↓
Value displayed with new color
```

### Code Example

```csharp
public class Dial180ViewModel : WidgetBaseViewModel, IRangeConfigurable
{
    private Color _currentStateColor = Colors.Gray;
    private string _currentStateName = "Out of Range";
    
    public void EvaluateCurrentState()
    {
        foreach (var range in StateRanges)
        {
            if (CurrentValue >= range.MinValue && 
                CurrentValue <= range.MaxValue)
            {
                CurrentStateColor = range.DialStateColor;
                CurrentStateName = range.DialStateName;
                return;
            }
        }
        
        // No range matched - use default color
        CurrentStateColor = Colors.Gray;
        CurrentStateName = "Out of Range";
    }
}
```

---

## DialStateRange Structure

Dial180 uses `DialStateRange` inner class with property aliases for consistency:

```csharp
public class DialStateRange
{
    public double MinValue { get; set; }
    public double MaxValue { get; set; }
    
    // Actual storage
    private Color _color;
    private string _name;
    
    // Aliases for interface compatibility
    public Color StateColor
    {
        get => _color;
        set => _color = value;
    }
    public Color DialStateColor  // Direct property
    {
        get => StateColor;
        set => StateColor = value;
    }
    
    public string StateName
    {
        get => _name;
        set => _name = value;
    }
    public string DialStateName  // Direct property
    {
        get => StateName;
        set => StateName = value;
    }
}
```

---

## Copy/Paste Workflows

### Workflow 1: Copy Single Range

```
1. Select range row
2. Click Copy button
   └─ Copies as JSON object to clipboard

3. Switch to another Dial180 widget
4. Click Paste button
   └─ Range added to StateRanges
```

Copied JSON:
```json
{
  "MinValue": 20,
  "MaxValue": 35,
  "StateColor": "#FFFFFF00",
  "StateName": "Warm"
}
```

### Workflow 2: Copy All Ranges

```
1. Any Dial180 widget
2. Click Copy All button
   └─ Entire StateRanges array to clipboard

3. Switch to another gauge widget (Dial180, BarGraph, etc)
4. Click Paste button
   └─ All ranges applied (intelligently)
```

Copied JSON:
```json
[
  { "MinValue": -40, "MaxValue": 0, "StateColor": "#FF0000FF", "StateName": "Freezing" },
  { "MinValue": 0, "MaxValue": 20, "StateColor": "#FF00FF00", "StateName": "Normal" },
  { "MinValue": 20, "MaxValue": 35, "StateColor": "#FFFFFF00", "StateName": "Warm" },
  { "MinValue": 35, "MaxValue": 50, "StateColor": "#FFFF0000", "StateName": "Hot" }
]
```

### Workflow 3: Copy Between Different Widget Types

```
1. Dial180 with well-configured ranges
2. Click Copy All
   └─ JSON array to clipboard

3. Add BarGraph widget
4. Configure BarGraph binding
5. Click Paste in BarGraph
   └─ Same ranges applied!
   └─ BarGraph shows matching colors
   └─ Consistent state visualization
```

Result: Uniform color scheme across all gauge types.

### Workflow 4: Multi-Select Copy

```
1. Select first range (click row)
2. Hold Shift + click last range
   └─ All ranges between selected

3. Click Copy button
   └─ Multiple ranges as JSON array

4. Paste into another widget
   └─ All ranges added
```

---

## Real-World Examples

### Example A: Industrial Pressure Monitor

**Scenario**: Monitor compressor discharge pressure

```
Min/Max: 0 to 200 PSI

Configuration:
├─ Normal Idle (0-20 PSI)      → Green
├─ Building Pressure (20-80)   → Green
├─ Optimal Range (80-120 PSI)  → Green (darker)
├─ Safety Margin (120-160)     → Yellow
└─ Emergency (160-200)         → Red

Appearance:
- Green arc (largest): Normal ranges
- Yellow arc: Alert range
- Red arc: Critical range
- Needle smoothly sweeps as pressure builds
```

### Example B: HVAC System Monitor

**Scenario**: Monitor supply air temperature

```
Min/Max: 40°F to 110°F

Configuration:
├─ Too Cold (40-50°F)   → Blue
├─ Heating (50-65°F)    → Blue (lighter)
├─ Normal (65-75°F)     → Green
├─ Cooling (75-90°F)    → Blue
├─ Too Warm (90-100°F)  → Yellow
└─ Dangerous (100-110°) → Red

Appearance:
- Needle bounces between zones
- Color arcs show operational zones
- Smooth animation shows temperature trends
```

### Example C: Vehicle RPM Gauge

**Scenario**: Monitor engine RPM

```
Min/Max: 0 to 8000 RPM

Configuration:
├─ Idle (0-800 RPM)           → Green
├─ Normal Driving (800-5000)  → Green
├─ High RPM (5000-6500)       → Yellow
├─ Redline Warning (6500-7500) → Red
└─ Overspeed (7500-8000)      → Dark Red

Appearance:
- Smooth needle rotation
- Color zones clearly marked
- Traditional gauge aesthetics
- Easy to read at a glance
```

---

## JSON Serialization

### Save Format

```json
{
  "DialStateRanges": [
    {
      "MinValue": 0,
      "MaxValue": 25,
      "StateColor": "#FF0000FF",
      "StateName": "Low"
    },
    {
      "MinValue": 26,
      "MaxValue": 75,
      "StateColor": "#FF00FF00",
      "StateName": "Normal"
    },
    {
      "MinValue": 76,
      "MaxValue": 100,
      "StateColor": "#FFFF0000",
      "StateName": "High"
    }
  ],
  "MinValue": 0,
  "MaxValue": 100,
  "Label": "Temperature"
}
```

### Load Process

1. Widget loads HMI file
2. JSON deserialized to Dial180ViewModel
3. `LoadFromJson()` called
4. StateRanges collection populated
5. Display updated with loaded colors

---

## Advanced Usage

### Code Integration

```csharp
// Access current state programmatically
var dial = hmiCanvas.Widgets.OfType<Dial180ViewModel>().First();

// Check current state
if (dial.CurrentStateName == "High")
{
    // Trigger alarm
    AlertSystem.Trigger("Temperature High: " + dial.CurrentValue);
}

// Modify range programmatically
dial.AddStateRange(80, 100, Colors.Red, "Critical");

// Save current configuration
string json = dial.SaveToJson();
File.WriteAllText("dial_config.json", json);
```

### Event Handling

```csharp
// Subscribe to state changes
var dial = new Dial180ViewModel(register);

dial.PropertyChanged += (s, e) =>
{
    if (e.PropertyName == nameof(Dial180ViewModel.CurrentStateName))
    {
        Console.WriteLine($"State changed to: {dial.CurrentStateName}");
        Console.WriteLine($"Color: {dial.CurrentStateColor}");
    }
};

// Value changes trigger state evaluation
// which fires PropertyChanged events
```

### Dynamic Configuration

```csharp
// Create dial with program parameters
var dial = new Dial180ViewModel(register);

// Load standard ranges for unit type
string rangeConfig = GetStandardRanges("Temperature");
dial.LoadFromJson(rangeConfig);

// Display configuration
foreach (var range in dial.StateRanges)
{
    Console.WriteLine($"{range.MinValue}-{range.MaxValue}: {range.StateName}");
}
```

---

## Performance Considerations

### Needle Animation
- **Default Animation**: 500ms smooth rotation
- **CPU Usage**: Minimal (GPU accelerated in WPF)
- **Update Frequency**: 100-1000ms per value change (configurable)
- **Memory**: ~5KB per widget

### Range Evaluation
- **Algorithm**: Linear scan through StateRanges
- **Time Complexity**: O(n) where n = number of ranges
- **Optimization**: Typical n = 3-5 ranges
- **Impact**: Negligible (< 0.1ms per evaluation)

### Best Practices

1. **Limit Ranges**: Keep to 3-8 ranges for clarity
2. **Update Frequency**: Don't update faster than 100ms
3. **Multiple Dials**: 10+ dials in view is fine
4. **Memory**: Each widget ~5-10KB, 100 widgets = 1MB

---

## Troubleshooting

### Problem: Needle doesn't move

**Symptoms**: Gauge stuck at min value

**Solutions**:
1. Check register binding (Monitoring Point set?)
2. Verify Min < Max values
3. Confirm register is receiving values
4. Check value range matches Min/Max

**Debug**:
```csharp
// Verify state evaluation
dial.EvaluateCurrentState();
Console.WriteLine($"Value: {dial.CurrentValue}");
Console.WriteLine($"Color: {dial.CurrentStateColor}");
```

### Problem: Wrong color displayed

**Symptoms**: Color doesn't match expected range

**Solutions**:
1. Verify ranges don't overlap incorrectly
2. Check range Min/Max boundaries
3. Test with known values
4. Ensure StateRanges not empty

**Debug**:
```csharp
foreach (var range in dial.StateRanges)
{
    Console.WriteLine($"{range.MinValue}-{range.MaxValue}: {range.StateName}");
}
// Verify ranges cover expected values
```

### Problem: Ranges lost after save/load

**Symptoms**: Configuration disappears

**Solutions**:
1. Verify SaveToJson() returns valid JSON
2. Check HMI file has write permission
3. Ensure file saved successfully
4. Check LoadFromJson() implementation

**Debug**:
```csharp
string json = dial.SaveToJson();
Console.WriteLine(json); // Verify contains ranges
```

### Problem: Gauge displays out of proportion

**Symptoms**: Needle range too large/small

**Solutions**:
1. Adjust MinValue and MaxValue
2. Match to expected value range
3. Test with boundary values (min, mid, max)

**Test**:
```csharp
dial.CurrentValue = dial.MinValue; // Should be at left
dial.CurrentValue = dial.MaxValue; // Should be at right
dial.CurrentValue = (dial.MinValue + dial.MaxValue) / 2; // Should be center
```

---

## API Reference

### Dial180ViewModel

```csharp
public class Dial180ViewModel : WidgetBaseViewModel, IRangeConfigurable, IJsonSerializable
{
    // Properties
    public double CurrentValue { get; set; }
    public double MinValue { get; set; }
    public double MaxValue { get; set; }
    public Color CurrentStateColor { get; set; }
    public string CurrentStateName { get; set; }
    public IList StateRanges { get; }
    public string Label { get; set; }
    public string Unit { get; set; }
    public string Format { get; set; }
    
    // Methods
    public void EvaluateCurrentState();
    public void AddStateRange(double min, double max, Color color, string name);
    public void RemoveStateRange(int index);
    public string SaveToJson();
    public void LoadFromJson(string json);
}
```

### DialStateRange

```csharp
public class DialStateRange
{
    public double MinValue { get; set; }
    public double MaxValue { get; set; }
    
    public Color StateColor { get; set; }
    public Color DialStateColor { get; set; }  // Alias
    
    public string StateName { get; set; }
    public string DialStateName { get; set; }  // Alias
    
    public string ImagePath { get; set; }
}
```

---

## Related Documentation

- [State-Based Colors & Ranges](state_based_colors_and_ranges.md) - Master guide
- [Gauge Widgets Index](index.md) - All gauge widgets
- [Range Editor Panel](range_editor_panel.md) - UI reference
- [Widget Architecture](../architecture/widgets.md) - Technical details
- [Copy/Paste System](../features/copy_paste.md) - Configuration sharing
