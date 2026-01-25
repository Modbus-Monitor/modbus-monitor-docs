# Slider Widget Documentation

## Overview

The **Slider** widget provides a graphical slider control for both reading and writing Modbus register values. Users can drag to set values, with optional state-based color ranges and real-time value display.

**Best for**: Analog control, adjustable setpoints, variable speed control, level adjustment.

---

## Features

✅ **Drag to Adjust** - Interactive value control  
✅ **Bidirectional** - Read and write values  
✅ **State Colors** - Value ranges with colors  
✅ **Min/Max Bounds** - Configurable value limits  
✅ **Real-Time Display** - Shows current value  
✅ **Smooth Animation** - Animated slider movement  
✅ **Horizontal/Vertical** - Multiple orientations  

---

## Quick Start (4 Steps)

### Step 1: Add Widget
```
Right-click canvas → Add Widget → Slider
```

### Step 2: Configure Register
Property Editor:
- **Monitoring Point**: Select register
- **Widget Label**: Slider name

### Step 3: Set Value Range
Property Editor:
- **Min Value**: Minimum slider position
- **Max Value**: Maximum slider position

### Step 4: Save
```
File → Save or Ctrl+S
```

---

## Properties

| Property | Type | Default | Purpose |
|----------|------|---------|---------|
| Label | string | "Slider" | Display name |
| MinValue | double | 0 | Minimum value |
| MaxValue | double | 100 | Maximum value |
| CurrentValue | double | 0 | Current position |
| Orientation | enum | Horizontal | Horizontal or Vertical |
| ShowValue | bool | true | Display numeric value |
| Unit | string | "" | Unit label (e.g., "%") |

---

## Slider Modes

### Mode 1: Read-Only Monitoring

```
Register value changes
  ↓
Slider position updates automatically
  ↓
User sees slider move
  ↓
User cannot drag (read-only mode)
```

### Mode 2: Adjustable Control

```
User drags slider
  ↓
Value updates in real-time
  ↓
Write value to register
  ↓
Register echoes value back
  ↓
Slider position confirmed
```

### Mode 3: Setpoint Configuration

```
User drags to desired value
  ↓
Slider shows preview value
  ↓
User releases mouse
  ↓
Value written to register
  ↓
Device confirms with response value
```

---

## Configuration Examples

### Example 1: Fan Speed Control

```
Label: Fan Speed
Min Value: 0
Max Value: 100
Unit: %
Orientation: Horizontal

Usage:
- 0%: Off
- 1-33%: Low
- 34-66%: Medium
- 67-100%: High

User drags to set speed
```

### Example 2: Temperature Setpoint

```
Label: Setpoint Temperature
Min Value: 50
Max Value: 100
Unit: °F
Orientation: Vertical

Usage:
- Drag slider up to increase target
- Drag down to decrease target
- Current temperature shown separately
- Setpoint shown on slider
```

### Example 3: Pump Pressure Adjustment

```
Label: Discharge Pressure
Min Value: 0
Max Value: 200
Unit: psi
Orientation: Horizontal

Color Zones:
- 0-50: Blue (Low)
- 50-150: Green (Normal)
- 150-200: Red (High)
```

---

## State-Based Colors (Optional)

Sliders can optionally use state ranges:

```
Define ranges in Range Editor:
├─ 0 to 33   → Blue (Low)
├─ 34 to 66  → Green (Normal)
└─ 67 to 100 → Red (High)

Slider fill shows current state color
```

---

## Real-World Examples

### Example A: HVAC Thermostat

```
Slider: Room Temperature Setpoint
├─ Range: 60°F to 85°F
├─ Display: "72°F"
├─ Orientation: Vertical
├─ Tick marks: Every 5°F
└─ Color zones: Blue/Green/Red

User drags to set comfort temperature
System maintains setpoint via PLC
```

### Example B: Industrial Speed Control

```
Slider: Motor Speed Control
├─ Range: 0 to 1200 RPM
├─ Display: "850 RPM"
├─ Orientation: Horizontal
├─ Tick marks: Every 100 RPM
└─ Color zones: Green/Yellow/Red

User adjusts speed for production rate
Motor responds to setpoint
```

### Example C: Light Dimmer

```
Slider: Brightness Level
├─ Range: 0 to 100%
├─ Display: "65%"
├─ Orientation: Horizontal
├─ Visual: Gradient from dark to bright
└─ Color zones: Gray/Yellow/White

User drags to dim or brighten
Lights respond in real-time
```

---

## Usage Patterns

### Pattern 1: Read-Only Slider

```csharp
var slider = new SliderViewModel(register);
slider.Label = "CPU Usage";
slider.MinValue = 0;
slider.MaxValue = 100;
slider.IsReadOnly = true;  // Can't drag

// Slider updates as register changes
// User sees real-time value
```

### Pattern 2: Setpoint Adjustment

```csharp
var slider = new SliderViewModel(register);
slider.Label = "Temperature Setpoint";
slider.MinValue = 50;
slider.MaxValue = 100;
slider.Unit = "°F";

// User drags to new value
// Value written to register
// Display shows both current and setpoint
```

### Pattern 3: With State Colors

```csharp
var slider = new SliderViewModel(register);
slider.Label = "System Load";

// Add state ranges (optional)
slider.AddStateRange(0, 33, Colors.Blue, "Low");
slider.AddStateRange(34, 66, Colors.Green, "Normal");
slider.AddStateRange(67, 100, Colors.Red, "High");

// Slider fill shows state color
```

---

## Best Practices

### ✅ DO

1. **Provide Clear Labels**
   - "Temperature Setpoint" not "Temp"
   - Include units in label or slider

2. **Set Appropriate Ranges**
   - Match device min/max values
   - Use realistic bounds
   - Prevent invalid commands

3. **Show Current Value**
   - Display numeric value on slider
   - Show unit (°F, %, RPM, etc.)
   - Update in real-time

4. **Use Tick Marks**
   - Mark important values
   - Help user estimate
   - Every 10% or 25% typically

5. **Test Bounds**
   - Verify min/max values work
   - Test edge cases
   - Ensure device accepts values

### ❌ DON'T

1. **Don't Use Extreme Ranges**
   - Too wide = imprecision
   - Too narrow = limited control

2. **Don't Skip Real-Time Feedback**
   - User needs to see effect
   - Confirm values are working

3. **Don't Block User Interaction**
   - Allow continuous adjustment
   - Responsive to drags

4. **Don't Forget Undo**
   - Allow value adjustment mistakes
   - Document how to revert

---

## Troubleshooting

### Problem: Slider Won't Move

**Symptoms**: Can't drag slider, position stuck

**Solutions**:
1. Check if IsReadOnly is true
2. Verify register is writable
3. Check min/max bounds are correct
4. Ensure Modbus connection active

### Problem: Value Doesn't Update

**Symptoms**: Drag slider but value doesn't change

**Solutions**:
1. Verify register binding
2. Check device acknowledges writes
3. Confirm value is within min/max
4. Check for permission errors

### Problem: Jerky Slider Movement

**Symptoms**: Slider movement stutters or jumps

**Solutions**:
1. Check if updates from register are too frequent
2. Increase update interval
3. Verify smooth animation enabled
4. Check network latency

---

## API Reference

```csharp
public class SliderViewModel : WidgetBaseViewModel
{
    public string Label { get; set; }
    public double MinValue { get; set; }
    public double MaxValue { get; set; }
    public double CurrentValue { get; set; }
    public string Unit { get; set; }
    public SliderOrientation Orientation { get; set; }
    public bool ShowValue { get; set; }
    public bool IsReadOnly { get; set; }
    
    public event PropertyChangedEventHandler ValueChanged;
    public void SetValue(double value);
}

public enum SliderOrientation
{
    Horizontal,
    Vertical
}
```

---

## Related Documentation

- [Gauge Widgets Index](index.md)
- [Control Widgets](../ui/control_widgets.md)
- [State-Based Colors](state_based_colors_and_ranges.md) (optional)
