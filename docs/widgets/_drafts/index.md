# Gauge Widgets Documentation

## Overview

Modbus Monitor includes four versatile gauge widgets, all supporting **state-based color mapping** through configurable value ranges. This unified architecture ensures consistency while allowing unlimited customization.

- **MultiStateIndicator** - Background color/image indicator
- **NumericGauge** - Text display with colored border
- **BarGraph** - Directional fill-based gauge
- **Dial180** - Semi-circular analog gauge

All widgets implement the same interfaces for state management, JSON persistence, and range configuration.

---

## Quick Comparison

| Widget | Display | Best For | Orientation |
|--------|---------|----------|-------------|
| [MultiStateIndicator](multistate_indicator.md) | Colored background + label | Status indicators | Fixed |
| [NumericGauge](numeric_gauge.md) | Text value + colored border | Simple numeric monitoring | Fixed |
| [BarGraph](bar_graph.md) | Animated fill bar | Levels, trends | 4 directions |
| [Dial180](dial180_index.md) | Needle + colored arcs | Analog monitoring | 180° sweep |

---

## Core Features (All Widgets)

### State-Based Colors
- Define unlimited value ranges with associated colors
- Automatic state evaluation when value changes
- Named states for clear context
- Default fallback color for out-of-range values

### Range Management
- **Add/Remove** ranges dynamically
- **Copy/Paste** configurations between widgets
- **Copy All** for batch operations
- **Multi-select** for bulk copying

### Persistence
- **SaveToJson()** - stores all settings to HMI file
- **LoadFromJson()** - restores configuration on reopening
- Automatic persistence during HMI save

### Interfaces
- **IRangeConfigurable** - state color management
- **IJsonSerializable** - save/load support
- **IWidgetWithImages** - future image support (infrastructure ready)

---

## Getting Started

### 1. Choose a Widget

Select based on your monitoring needs:

- **Need background color?** → MultiStateIndicator
- **Need numeric display?** → NumericGauge
- **Need trending/level?** → BarGraph
- **Need analog gauge?** → Dial180

### 2. Add to HMI

```
1. Right-click on canvas
2. Select "Add Widget"
3. Choose widget type
4. Draw widget on canvas
```

### 3. Configure Register

In Property Editor:
1. Set **Monitoring Point** (select Modbus register)
2. Configure **Widget Label**
3. Adjust **Display Settings**

### 4. Define State Ranges

In Range Editor:
1. Click **Add [+]** to create range
2. Set **Min** and **Max** values
3. Click **Color** to choose color
4. Edit **Name** (state name)
5. Repeat for all zones

### 5. Copy to Other Widgets (Optional)

```
1. Click Copy All
2. Switch to another widget
3. Click Paste
→ Entire configuration applied
```

### 6. Save

Click **Save** or Ctrl+S to persist all settings.

---

## Standard Implementation Table

All widgets follow the same standardized pattern:

| Feature | MultiState | NumericGauge | BarGraph | Dial180 |
|---------|-----------|--------------|----------|---------|
| **Display Type** | Background | Border Color | Fill Bar | Needle + Arcs |
| **Inner Class** | StateRange | NumericStateRange | StateRange | DialStateRange |
| **StateColor** | ✅ Direct | ✅ Direct | ✅ Direct | ✅ Alias |
| **StateName** | ✅ Direct | ✅ Direct | ✅ Direct | ✅ Alias |
| **IRangeConfigurable** | ✅ | ✅ | ✅ | ✅ |
| **IJsonSerializable** | ✅ | ✅ | ✅ | ✅ |
| **EvaluateCurrentState()** | ✅ Public | ✅ Public | ✅ Public | ✅ Public |
| **AddStateRange()** | ✅ | ✅ | ✅ | ✅ |
| **RemoveStateRange()** | ✅ | ✅ | ✅ | ✅ |
| **SaveToJson()** | ✅ | ✅ | ✅ | ✅ |
| **LoadFromJson()** | ✅ | ✅ | ✅ | ✅ |
| **Copy/Paste Support** | ✅ | ✅ | ✅ | ✅ |

---

## Workflow Examples

### Example 1: Monitor Multiple Temperature Points

1. Add **BarGraph** for Coolant Temperature
   - Orientation: North (upward)
   - Ranges: Blue (Cold), Green (Ideal), Red (Hot)

2. Copy All from BarGraph

3. Add **MultiStateIndicator** for Engine Temperature
   - Paste the ranges
   - Same color scheme applied

Result: Consistent visualization across different widget types

### Example 2: Create Monitoring Dashboard

1. Add 4 widgets for different systems
2. Configure first widget completely
3. **Copy All** from first widget
4. **Paste** into remaining 3 widgets
5. Adjust individual ranges if needed

Result: Uniform dashboard with consistent color semantics

### Example 3: Share Configurations

1. Configure a widget with your organization's standard colors
2. **Copy All** from the widget
3. Save JSON to shared repository
4. Team members can paste into their widgets

Result: Standardized monitoring visualization across organization

---

## Range Editor Panel

All widgets share the same range management interface:

### DataGrid Columns
| Column | Type | Purpose |
|--------|------|---------|
| Min | numeric | Minimum value for this range |
| Max | numeric | Maximum value for this range |
| Name | text | State name (displayed in widget) |
| Color | visual | Color swatch (click to edit) |
| Image | button | Optional image path (future) |

### Action Buttons

| Button | Keyboard | Purpose |
|--------|----------|---------|
| Add [+] | - | Add new range with defaults |
| Remove [-] | Delete | Remove selected range(s) |
| Copy | Ctrl+C | Copy selected range(s) to clipboard |
| Paste | Ctrl+V | Paste range(s) from clipboard |
| Copy All | - | Export entire table as JSON array |
| Color | - | Open color picker |
| Clear Color | - | Make background transparent |

### Multi-Select Operations

- **Single selection**: Click any row
- **Multiple selection**: Ctrl+Click, Shift+Click, or Ctrl+A
- **Copy Selected**: Copies selected rows as JSON array
- **Paste**: Auto-detects single object or array

---

## Copy/Paste Format

### Single Range (JSON Object)
```json
{
  "MinValue": 0,
  "MaxValue": 20,
  "StateColor": "#FFC8C8C8",
  "StateName": "Low / Off",
  "ImagePath": ""
}
```

### Multiple Ranges (JSON Array)
```json
[
  { "MinValue": 0, "MaxValue": 20, "StateColor": "#FFC8C8C8", "StateName": "Low", "ImagePath": "" },
  { "MinValue": 21, "MaxValue": 60, "StateColor": "#FF00C800", "StateName": "Normal", "ImagePath": "" },
  { "MinValue": 61, "MaxValue": 100, "StateColor": "#FFC80000", "StateName": "High", "ImagePath": "" }
]
```

### Color Format
- **Format**: `#AARRGGBB` (hex with alpha)
- **#FFC80000** = Red (opaque)
- **#80FF0000** = Red (50% transparent)
- **#00000000** = Fully transparent

---

## Best Practices

### ✅ Configuration Best Practices

1. **Use Meaningful Names**
   - "Critical Alert" instead of "State5"
   - "Normal Operation" instead of "OK"

2. **Standard Color Scheme**
   - 🟢 Green = Normal/Safe
   - 🟨 Yellow = Warning
   - 🔴 Red = Critical/Alarm
   - 🔵 Blue/Gray = Off/Standby

3. **Complete Coverage**
   - Ensure ranges cover entire expected value domain
   - Minimal gaps or overlaps

4. **Test Thoroughly**
   - Verify all value zones display correctly
   - Test out-of-range values
   - Confirm color transitions

5. **Reuse Configurations**
   - Copy well-tested configurations
   - Maintain consistency across similar widgets
   - Document standard templates

### ❌ Avoid These Mistakes

1. Don't leave large value gaps uncovered
2. Don't use confusing color combinations
3. Don't modify ranges without testing
4. Don't forget to save after changes
5. Don't copy incomplete configurations

---

## Troubleshooting Guide

### Color Not Updating

**Problem**: Widget shows default color regardless of value

**Solutions**:
1. Verify register is bound (Monitoring Point set)
2. Check range Min/Max values match expected range
3. Confirm StateRanges collection is not empty
4. Verify value actually falls in a range

### Wrong State Displayed

**Problem**: Different color than expected for value

**Solutions**:
1. Check range definitions for gaps/overlaps
2. Verify Min ≤ Max for each range
3. If overlapping, first match wins
4. Test with known values to debug

### Copy/Paste Not Working

**Problem**: Paste button doesn't add ranges or shows error

**Solutions**:
1. Verify clipboard has valid JSON
2. Check JSON structure matches expected format
3. Look for error message in dialog
4. Ensure target widget is the same type

### Ranges Lost After Saving

**Problem**: Ranges disappear when HMI is reopened

**Solutions**:
1. Verify widget implements IJsonSerializable
2. Check SaveToJson() includes StateRanges
3. Confirm file was saved successfully to disk
4. Check HMI file has write permissions

---

## Architecture

### Class Hierarchy

```
WidgetBaseViewModel
├── IRangeConfigurable (interface)
├── IEditableWidget (interface)
├── IJsonSerializable (interface)
└── IWidgetWithImages (interface)

MultiStateIndicatorViewModel
├── StateRange (inner class)
└── Implements all interfaces

NumericGaugeViewModel
├── NumericStateRange (inner class)
└── Implements all interfaces

BarGraphViewModel
├── Reuses StateRange from MultiState
└── Implements all interfaces

Dial180ViewModel
├── DialStateRange (inner class with aliases)
└── Implements all interfaces
```

### State Evaluation Flow

```
Register Value Changes
      ↓
Register_PropertyChanged event
      ↓
EvaluateCurrentState()
      ↓
Compare value against StateRanges
      ↓
Find first matching range
      ↓
Set CurrentStateColor = range.StateColor
Set CurrentStateName = range.StateName
      ↓
UI updates via property binding
      ↓
Widget displays new color
```

---

## Widget Details

For comprehensive documentation, see individual widget pages:

### [MultiStateIndicator Widget](multistate_indicator.md)
- Background color/image indicator
- Two operating modes (Range & Boolean)
- Perfect for status displays

### [NumericGauge Widget](numeric_gauge.md)
- Text value with colored border
- Customizable format and precision
- Ideal for simple numeric monitoring

### [BarGraph Widget](bar_graph.md)
- Directional fill gauge (4 orientations)
- Animated fill level
- Perfect for levels and trends

### [Dial180 Widget](dial180_index.md)
- Semi-circular analog gauge
- Needle + colored range arcs
- Traditional analog appearance

### [State-Based Colors & Ranges](state_based_colors_and_ranges.md)
- Comprehensive guide to state management
- Range Editor Panel documentation
- Copy/Paste workflow examples

---

## Implementation Reference

### IRangeConfigurable Interface

```csharp
public interface IRangeConfigurable
{
    Color CurrentStateColor { get; set; }
    string CurrentStateName { get; set; }
    IList StateRanges { get; }
    
    void EvaluateCurrentState();
    void AddStateRange(double min, double max, Color color, string name);
    void RemoveStateRange(int index);
}
```

### IJsonSerializable Interface

```csharp
public interface IJsonSerializable
{
    string SaveToJson();
    void LoadFromJson(string json);
}
```

### Example Usage

```csharp
// Create widget
var widget = new MultiStateIndicatorViewModel(register);

// Add ranges
widget.AddStateRange(0, 25, Colors.Red, "Low");
widget.AddStateRange(26, 75, Colors.Green, "Normal");
widget.AddStateRange(76, 100, Colors.Yellow, "High");

// Access current state
var color = widget.CurrentStateColor;
var name = widget.CurrentStateName;

// Save to file
var json = widget.SaveToJson();

// Load from file
widget.LoadFromJson(json);
```

---

## Version History

### V2 (Current)
- ✅ State-based color support for all widgets
- ✅ IRangeConfigurable interface
- ✅ Copy/Paste range configurations
- ✅ Multi-select support
- ✅ JSON serialization
- ✅ Consistent behavior across all widgets

### V1 (Legacy)
- Boolean mode for simple on/off
- Limited customization
- Single color per state

---

## Related Documentation

- [Property Editor Panel](../ui/property_editor_panel.md)
- [HMI Persistence](../hmi/persistence.md)
- [Modbus Register Binding](../modbus/register_binding.md)
- [Color System](../ui/colors.md)
