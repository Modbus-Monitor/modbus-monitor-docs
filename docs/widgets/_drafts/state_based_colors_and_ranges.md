# State-Based Colors and Range Configuration

## Overview

All gauge widgets in Modbus Monitor support **state-based color mapping** through the `IRangeConfigurable` interface. This allows widgets to dynamically change colors, display state names, and optionally show images based on the monitored register value.

This unified approach provides consistent behavior across all widgets while allowing full customization of color schemes and state definitions.

## Quick Start

1. Open the **Property Editor Panel** for any gauge widget
2. Look for **"State Ranges"** section
3. **Add ranges** using the [+] button to define value zones
4. Assign **colors** to each range via the Color button
5. Give each range a **state name** (e.g., "Low", "Normal", "High")
6. **Copy** configurations between widgets using Copy/Paste buttons
7. **Save** - changes persist to HMI file automatically

## How It Works

When a widget's monitored register value changes:

1. **EvaluateCurrentState()** compares the value against all configured ranges
2. First matching range (Min ≤ Value ≤ Max) sets the:
   - **CurrentStateColor** - displayed in the widget
   - **CurrentStateName** - shown in text displays
   - **CurrentStateImagePath** - optional state-specific image (if configured)
3. If no range matches, the **DefaultStateColor** is used

### Example: Temperature Zone Widget

| Range | Min | Max | Color | State Name |
|-------|-----|-----|-------|------------|
| Low   | 0   | 20  | 🔵 Blue | Cold |
| Normal | 21 | 60  | 🟢 Green | OK |
| High  | 61  | 100 | 🔴 Red | Hot |

When temperature = 45°C → Displays with **Green color** and **"OK"** label

---

## Supported Widgets

All gauge widgets support state-based color configuration:

### 1. **MultiStateIndicator**
- **Purpose:** Background color/image changes based on value ranges
- **Display:** Solid colored border with optional state name text
- **Best For:** Simple status indicators, alarm zones, mode displays

### 2. **NumericGauge**
- **Purpose:** Text value display with state-based border color
- **Display:** Register value with colored border indicating state
- **Best For:** Numeric monitoring with status context

### 3. **BarGraph**
- **Purpose:** Bar fill changes color based on value ranges
- **Display:** Directional bar (North/South/East/West) with state color
- **Best For:** Trend visualization, level indicators, rate displays

### 4. **Dial180**
- **Purpose:** 180° semi-circular gauge with colored range arcs
- **Display:** Needle with colored background arcs indicating zones
- **Best For:** Analog monitoring, pressure gauges, speed indicators

---

## Widget Standardization

All widgets implement a consistent interface for state-based colors:

| Feature | MultiState | NumericGauge | BarGraph | Dial180 |
|---------|-----------|--------------|----------|---------|
| **Inner Class** | StateRange | NumericStateRange | Reuses StateRange | DialStateRange |
| **StateColor Property** | ✅ Direct | ✅ Direct | ✅ Direct (from MultiState) | ✅ Via Alias |
| **StateName Property** | ✅ Direct | ✅ Direct | ✅ Direct (from MultiState) | ✅ Via Alias |
| **IRangeConfigurable Interface** | ✅ Yes | ✅ Yes | ✅ Yes | ✅ Yes |
| **IJsonSerializable** | ✅ Yes | ✅ Yes | ✅ Yes | ✅ Yes |
| **EvaluateCurrentState()** | ✅ Public | ✅ Public | ✅ Public | ✅ Public |
| **AddStateRange()** | ✅ Yes | ✅ Yes | ✅ Yes | ✅ Yes |
| **RemoveStateRange()** | ✅ Yes | ✅ Yes | ✅ Yes | ✅ Yes |
| **SaveToJson()** | ✅ Yes | ✅ Yes | ✅ Yes | ✅ Yes |
| **LoadFromJson()** | ✅ Yes | ✅ Yes | ✅ Yes | ✅ Yes |

---

## Range Editor Panel

The **Range Editor Control** provides a unified UI for managing state ranges across all widgets.

### Features

#### **DataGrid Display**
- **Min** - Minimum value for this range
- **Max** - Maximum value for this range
- **Name** - State name (displayed in widget)
- **Color** - Visual color swatch (click to edit)
- **Image** - Optional image file path (future feature)

#### **Action Buttons**

| Button | Action | Shortcut |
|--------|--------|----------|
| **Add [+]** | Add new range with default values | N/A |
| **Remove [-]** | Remove selected range(s) | N/A |
| **Copy** | Copy selected range(s) to clipboard | Ctrl+C |
| **Paste** | Paste range(s) from clipboard | Ctrl+V |
| **Copy All** | Export entire range table as JSON | N/A |
| **Color** | Open color picker for selected range | N/A |
| **Clear Color** | Make background transparent (border only) | N/A |

### Multi-Select Operations

- **Single Selection**: Click any row
- **Multiple Selection**: 
  - Hold **Ctrl** and click additional rows
  - Hold **Shift** and click to select range of rows
  - **Ctrl+A** to select all ranges
- **Copy Selected**: Copies selected rows as JSON array
- **Paste**: Automatically detects single object or array

### Copy/Paste Format

#### Single Range (JSON Object)
```json
{
  "MinValue": 0,
  "MaxValue": 20,
  "StateColor": "#FFC8C8C8",
  "StateName": "Low / Off",
  "ImagePath": ""
}
```

#### Multiple Ranges (JSON Array)
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

## Workflow Examples

### Scenario 1: Apply Same Color Scheme to Multiple Widgets

1. **Widget A (MultiStateIndicator)** - already configured with perfect colors
2. Click **Copy All** to copy entire color scheme
3. Switch to **Widget B (BarGraph)**
4. Click **Paste** to apply same scheme
5. Result: Both widgets use identical color zones

### Scenario 2: Create Reusable Templates

1. Create a reference widget with your standard zones:
   - 0-25: Blue (Low)
   - 26-50: Green (Normal)
   - 51-75: Yellow (Warning)
   - 76-100: Red (Critical)
2. **Copy All** to save to clipboard
3. Use **Edit → Paste Special → Format Only** if needed
4. Apply to all similar monitoring widgets

### Scenario 3: Share Configurations

1. **Copy All** from a configured widget
2. Paste into a text file or documentation
3. Share with team members
4. They can **Copy** the JSON and **Paste** directly into their widgets

### Scenario 4: Modify Individual Ranges

1. Select specific range from grid
2. Edit **Min**, **Max**, **Name** inline (live updates)
3. Click **Color** button to change color
4. Changes reflect immediately in the widget preview

---

## Property Editor Integration

Each widget exposes state range configuration through the **Property Editor Panel**:

### Basic Properties
- **Monitoring Point** - Select the register to monitor
- **Widget Label** - Custom display name
- **Show Label** - Toggle label visibility
- **Show Border** - Toggle 3D border/shadow

### Range Properties
- **State Ranges** - Table of all configured ranges
- **Edit/Add/Remove** - Manage range list
- **Default State Color** - Color when value is out of range

### Save/Load Behavior
- All range configurations automatically save to HMI JSON file
- Ranges reload when HMI is reopened
- Full undo/redo support for range modifications

---

## JSON Serialization

Each widget's `SaveToJson()` includes complete range data:

```json
{
  "WidgetLabel": "Temperature Monitor",
  "ShowLabel": true,
  "FontSize": 14,
  "TextColor": "#FF000000",
  "MinValue": 0,
  "MaxValue": 100,
  "StateRanges": [
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
}
```

### Color Format
- **Format**: `#AARRGGBB` (hex with alpha channel)
- **Example**: `#FFC80000` = Red with full opacity
- **Example**: `#80FF0000` = Red with 50% transparency
- **Example**: `#00000000` = Fully transparent

---

## Best Practices

### ✅ Do's

1. **Use Meaningful State Names**
   - "Low / Off" instead of "State1"
   - "Normal" instead of "OK"
   - "Critical Alert" instead of "High"

2. **Ensure Non-Overlapping Ranges**
   - Avoid gaps (e.g., 0-20, 30-50 leaves 21-29 uncovered)
   - Overlapping ranges are OK (first match wins)

3. **Use Standard Color Schemes**
   - Green = Normal/Safe
   - Yellow = Warning
   - Red = Critical/Alarm
   - Blue/Gray = Off/Standby

4. **Copy and Reuse**
   - Create reference configurations
   - Copy to similar widgets
   - Maintain consistency across HMI

5. **Document Edge Cases**
   - Out-of-range values use DefaultStateColor
   - Include full range coverage when possible

### ❌ Don'ts

1. **Don't** leave large value gaps without ranges
2. **Don't** use confusing color combinations
3. **Don't** copy incomplete configurations
4. **Don't** modify ranges without testing the result
5. **Don't** forget to save after major changes

---

## Troubleshooting

### Range Not Activating
- **Check**: Value actually falls in Min-Max range
- **Check**: Range is enabled in the list
- **Check**: No higher-priority range matches first

### Color Not Showing
- **Check**: StateColor is properly formatted (#AARRGGBB)
- **Check**: Alpha channel (AA) is not 00 (fully transparent)
- **Check**: Widget color binding is enabled in view

### Copy/Paste Not Working
- **Check**: Clipboard contains valid JSON
- **Check**: Range properties are properly formatted
- **Check**: No parsing errors in error dialog

### Ranges Lost After Save
- **Check**: Widget implements IJsonSerializable
- **Check**: SaveToJson() includes StateRanges
- **Check**: File saved successfully to disk

---

## Code Reference

### IRangeConfigurable Interface

```csharp
public interface IRangeConfigurable
{
    Color CurrentStateColor { get; set; }
    string CurrentStateName { get; set; }
    IList StateRanges { get; }
    
    void EvaluateCurrentState();
    void AddStateRange(double minValue, double maxValue, Color color, string name);
    void RemoveStateRange(int index);
}
```

### Example Usage

```csharp
// Access widget's state color
Color currentColor = myWidget.CurrentStateColor;
string currentState = myWidget.CurrentStateName;

// Add a new range programmatically
myWidget.AddStateRange(0, 20, Colors.Blue, "Low");
myWidget.AddStateRange(21, 60, Colors.Green, "Normal");
myWidget.AddStateRange(61, 100, Colors.Red, "High");

// Force state re-evaluation
myWidget.EvaluateCurrentState();
```

---

## Related Topics

- [MultiStateIndicator Widget](multistate_indicator.md)
- [NumericGauge Widget](numeric_gauge.md)
- [BarGraph Widget](bar_graph.md)
- [Dial180 Gauge Widget](dial180_index.md)
- [Property Editor Panel](../ui/property_editor_panel.md)
- [HMI Persistence and Save/Load](../hmi/persistence.md)
