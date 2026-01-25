# Range Editor Control Documentation

## Overview

The **Range Editor Control** is the unified user interface for managing state ranges across all gauge widgets (MultiStateIndicator, NumericGauge, BarGraph, Dial180). It provides a tabular DataGrid view with real-time color previews, multi-select capabilities, and clipboard-based configuration sharing.

**Purpose**: Configure which value ranges map to which colors and state names.

---

## Features

✅ **DataGrid Interface** - Table view of all ranges  
✅ **Multi-Select** - Select single or multiple rows  
✅ **Copy/Paste Ranges** - Share configurations between widgets  
✅ **Copy All** - Export entire table as JSON  
✅ **Add/Remove Ranges** - Dynamic range management  
✅ **Color Picker** - Visual color selection  
✅ **Real-Time Preview** - See colors in grid  
✅ **JSON Support** - Both single objects and arrays  

---

## User Interface

### Layout

```
┌─────────────────────────────────────────────────────┐
│ State Ranges Editor                              [X] │
├─────────────────────────────────────────────────────┤
│                                                       │
│ Min    Max    Name                      Color        │
│ ┌──────────────────────────────────────────────────┐ │
│ │ 0      25    Low                    █ Gray        │ │
│ │ 26     60    Normal                 █ Green       │ │
│ │ 61     100   High                   █ Red         │ │
│ └──────────────────────────────────────────────────┘ │
│                                                       │
│ [+] [-] [Copy] [Paste] [Copy All]  Color Clear Image│
│                                                       │
└─────────────────────────────────────────────────────┘
```

### Columns

| Column | Type | Editable | Purpose |
|--------|------|----------|---------|
| **Min** | numeric | ✅ Yes | Minimum value threshold |
| **Max** | numeric | ✅ Yes | Maximum value threshold |
| **Name** | text | ✅ Yes | State name (e.g., "Low", "Normal") |
| **Color** | visual | ❌ No | Color swatch (click to edit) |
| **Image** | button | ❌ No | Image path selector (future) |

### Buttons

| Button | Icon | Purpose | Shortcut |
|--------|------|---------|----------|
| **Add [+]** | Green plus | Create new range with defaults | - |
| **Remove [-]** | Red minus | Delete selected range(s) | Delete key |
| **Copy** | Clipboard copy | Copy selected row(s) to clipboard | Ctrl+C |
| **Paste** | Clipboard paste | Paste range(s) from clipboard | Ctrl+V |
| **Copy All** | Double arrow | Export all ranges as JSON | - |
| **Color** | Palette | Open color picker | - |
| **Clear Color** | X symbol | Make color transparent | - |
| **Image** | Picture | Select image file | - |

---

## Workflows

### Workflow 1: Add a New Range

```
Step 1: Click the [+] button
        └─ New row added with defaults
           Min: 0, Max: 100, Name: "State", Color: Gray

Step 2: Click Min cell
        └─ Edit numeric value

Step 3: Click Max cell
        └─ Edit numeric value

Step 4: Click Name cell
        └─ Edit state name

Step 5: Click Color button in row
        └─ Color picker opens

Step 6: Select color
        └─ Range now displays with chosen color
```

### Workflow 2: Edit Existing Range

```
Step 1: Click cell to edit
        ├─ Min/Max cells: Type new number
        └─ Name cell: Type new name

Step 2: Press Enter or Tab
        └─ Changes apply immediately

Step 3: Click Color to change
        └─ Color picker opens

Step 4: Result: Range updated
```

**Note**: Changes are in-memory and require **Save** to persist.

### Workflow 3: Copy Single Range

```
Step 1: Click range row (highlight it)
        └─ Row selected

Step 2: Click [Copy] button
        └─ JSON object copied to clipboard

Step 3: Paste example (Windows):
        {
          "MinValue": 26,
          "MaxValue": 60,
          "StateColor": "#FF00FF00",
          "StateName": "Normal"
        }

Step 4: Switch to another widget
        └─ Select the widget's range editor

Step 5: Click [Paste] button
        └─ Range added to new widget
```

### Workflow 4: Copy Multiple Ranges

```
Step 1: Select multiple rows
        ├─ Click first row
        ├─ Ctrl+Click other rows
        └─ Or: Shift+Click range of rows

Step 2: Click [Copy] button
        └─ JSON array copied to clipboard

Step 3: Paste example (3 rows):
        [
          { "MinValue": 0, "MaxValue": 25, "StateColor": "#FFC8C8C8", "StateName": "Low" },
          { "MinValue": 26, "MaxValue": 60, "StateColor": "#FF00FF00", "StateName": "Normal" },
          { "MinValue": 61, "MaxValue": 100, "StateColor": "#FFFF0000", "StateName": "High" }
        ]

Step 4: Go to target widget
Step 5: Click [Paste]
        └─ All ranges added
```

### Workflow 5: Copy All Ranges

```
Step 1: Click [Copy All] button
        └─ Entire StateRanges collection copied

Step 2: JSON contains all ranges:
        [
          { "MinValue": 0, "MaxValue": 25, ... },
          { "MinValue": 26, "MaxValue": 60, ... },
          { "MinValue": 61, "MaxValue": 100, ... }
        ]

Step 3: Switch to another widget

Step 4: Click [Paste]
        └─ All ranges applied to new widget
        └─ Complete configuration copied!

Result: Consistent colors across all gauges
```

### Workflow 6: Delete Range

```
Step 1: Click range row
        └─ Select range to delete

Step 2: Click [-] button OR press Delete key
        └─ Range removed from table

Step 3: Result: Gap in coverage
        ├─ Value will fall in no range
        └─ Widget shows default color
```

### Workflow 7: Reorder Ranges

Currently: No drag-and-drop reordering
Solution: Delete and recreate in desired order

```
Option 1: Delete + Recreate
Step 1: Note the range properties
Step 2: Click [-] to delete
Step 3: Click [+] to add new range
Step 4: Re-enter properties in new order

Option 2: Copy/Paste with JSON manipulation
Step 1: Copy All ranges
Step 2: Open JSON editor
Step 3: Reorder array elements
Step 4: Paste back
```

---

## Multi-Select Operations

### Single Selection

```
Click any row
└─ Row highlighted
   └─ Entire row selected
```

### Multiple Selection with Ctrl

```
Click row 1      └─ Row 1 selected
Ctrl+Click row 3 └─ Rows 1 and 3 selected
Ctrl+Click row 2 └─ Rows 1, 2, 3 selected
Ctrl+Click row 1 └─ Rows 2, 3 selected (deselected 1)
```

### Range Selection with Shift

```
Click row 1       └─ Row 1 selected
Shift+Click row 5 └─ Rows 1, 2, 3, 4, 5 selected
```

### Select All

```
Ctrl+A       └─ All rows selected
Click Copy   └─ All rows copied (same as Copy All)
```

### Clear Selection

```
Click empty area
Or: Escape key
└─ No rows selected
```

---

## Copy/Paste Format Reference

### Single Range JSON

```json
{
  "MinValue": 26,
  "MaxValue": 60,
  "StateColor": "#FF00FF00",
  "StateName": "Normal",
  "ImagePath": ""
}
```

**Fields**:
- `MinValue` (double) - Lower boundary
- `MaxValue` (double) - Upper boundary
- `StateColor` (string) - Color in #AARRGGBB format
- `StateName` (string) - Display name
- `ImagePath` (string) - Optional image file path

### Multiple Ranges JSON

```json
[
  {
    "MinValue": 0,
    "MaxValue": 25,
    "StateColor": "#FFC8C8C8",
    "StateName": "Low",
    "ImagePath": ""
  },
  {
    "MinValue": 26,
    "MaxValue": 60,
    "StateColor": "#FF00FF00",
    "StateName": "Normal",
    "ImagePath": ""
  },
  {
    "MinValue": 61,
    "MaxValue": 100,
    "StateColor": "#FFFF0000",
    "StateName": "High",
    "ImagePath": ""
  }
]
```

### Color Format

- **Format**: `#AARRGGBB` (hexadecimal)
- **AA**: Alpha/Transparency (00 = transparent, FF = opaque)
- **RR**: Red channel (00-FF)
- **GG**: Green channel (00-FF)
- **BB**: Blue channel (00-FF)

**Examples**:
- `#FFFF0000` = Red (opaque)
- `#FF00FF00` = Green (opaque)
- `#FF0000FF` = Blue (opaque)
- `#FFFFFF00` = Yellow (opaque)
- `#80FF0000` = Red (50% transparent)
- `#00000000` = Fully transparent

---

## Common Tasks

### Task 1: Create Standard Traffic Light Colors

```
Step 1: Click [+] to add ranges

Range 1:
├─ Min: 0
├─ Max: 33
├─ Name: Low
└─ Color: 🔴 Red

Range 2:
├─ Min: 34
├─ Max: 66
├─ Name: Normal
└─ Color: 🟡 Yellow

Range 3:
├─ Min: 67
├─ Max: 100
├─ Name: High
└─ Color: 🟢 Green

Result: Widget changes colors as value changes
```

### Task 2: Create Temperature Zones

```
Step 1: Add 4 ranges for temperature

Range 1: -40 to 0°C   → Blue (Freezing)
Range 2: 0 to 20°C    → Green (Normal)
Range 3: 20 to 35°C   → Yellow (Warm)
Range 4: 35 to 50°C   → Red (Hot)

Step 2: Test:
├─ Set value to -10  → Should show blue
├─ Set value to 25   → Should show yellow
└─ Set value to 40   → Should show red
```

### Task 3: Share Configuration Across All Widgets

```
Step 1: Configure first widget completely
        └─ Add all ranges, colors, names

Step 2: Click [Copy All]
        └─ All ranges to clipboard

Step 3: For each additional widget:
        ├─ Select widget's range editor
        ├─ Click [Paste]
        └─ All ranges applied

Result: Identical configuration across widgets
```

### Task 4: Import Configuration from File

```
Step 1: Have JSON file with ranges (e.g., temp_ranges.json)

Step 2: Open file in text editor
        └─ Copy the JSON content

Step 3: In Range Editor:
        ├─ Click [Paste]
        └─ Ranges added from clipboard

Result: Configuration loaded from file
```

### Task 5: Export Configuration to File

```
Step 1: Click [Copy All]
        └─ Ranges copied to clipboard

Step 2: Open text editor
        ├─ Paste clipboard content
        └─ Save as "my_config.json"

Result: Configuration saved for later use
```

---

## Editing Tips & Tricks

### Tip 1: Inline Editing

- **Click cell** → Edit mode
- **Type value** → Edit the content
- **Press Enter** → Confirm and move to next row
- **Press Tab** → Confirm and move to next cell
- **Press Escape** → Cancel edit

### Tip 2: Keyboard Navigation

```
Tab       → Next cell
Shift+Tab → Previous cell
Arrow Up  → Previous row
Arrow Down → Next row
Delete    → Remove selected range
Enter     → Confirm edit
Escape    → Cancel edit
```

### Tip 3: Quick Color Change

```
Step 1: Click row
Step 2: Click [Color] button
Step 3: Pick new color
Step 4: Color updates immediately
```

### Tip 4: Duplicate Range

```
Step 1: Copy single range
        └─ Click Copy button with row selected

Step 2: Click [+] to add new range
Step 3: Click [Paste]
        └─ New range created with copied properties

Result: Duplication complete
```

### Tip 5: Swap Colors

```
Step 1: Copy first range
Step 2: Copy second range to temp
Step 3: Paste first into second slot
Step 4: Paste second into first slot

Result: Colors swapped between ranges
```

---

## Error Handling

### Error: "Invalid JSON Format"

**Cause**: Pasted text isn't valid JSON

**Solution**:
1. Check clipboard contains proper JSON
2. Verify braces and quotes match
3. Try copying again from source

**Example of invalid**:
```json
{
  "MinValue": 0
  "MaxValue": 100  ← Missing comma
}
```

### Error: "No ranges to paste"

**Cause**: Clipboard is empty or invalid

**Solution**:
1. Copy ranges first (Copy or Copy All)
2. Verify nothing else overwrote clipboard
3. Try copying again

### Error: "Range values invalid"

**Cause**: Min > Max or invalid numbers

**Solution**:
1. Ensure Min ≤ Max
2. Use valid decimal numbers
3. Avoid text in numeric fields

### Warning: "Ranges don't cover full span"

**Cause**: Value gaps in range definitions

**Issue**: Values in gaps will show default color

**Solution**:
1. Add ranges to cover gaps
2. Overlapping ranges: first match wins
3. Test with boundary values

---

## Best Practices

### ✅ DO

1. **Use Clear Names**
   - "Low", "Normal", "High"
   - "Standby", "Running", "Error"

2. **Follow Color Standards**
   - 🟢 Green = Safe/Normal
   - 🟡 Yellow = Warning/Caution
   - 🔴 Red = Critical/Alarm
   - 🔵 Blue = Standby/Off

3. **Cover Full Range**
   - Define ranges for all expected values
   - No large uncovered gaps

4. **Test Thoroughly**
   - Test boundary values
   - Verify color transitions
   - Check out-of-range handling

5. **Document Configuration**
   - Save JSON to file as backup
   - Include documentation with ranges
   - Note which register each applies to

### ❌ DON'T

1. **Don't Leave Large Gaps**
   - Values in gaps use default color
   - Confusing to end users

2. **Don't Use Overlapping Ranges**
   - If unavoidable, document which takes precedence
   - First matching range wins

3. **Don't Use Confusing Colors**
   - Red for "good" or Green for "bad"
   - Non-standard conventions

4. **Don't Forget to Save**
   - Changes are in-memory only
   - Must save HMI file to persist

5. **Don't Over-Complicate**
   - Keep 3-8 ranges for clarity
   - Too many ranges = confusion

---

## Advanced Usage

### Scenario 1: Asymmetric Ranges

When ranges have different widths:

```
Temperature monitoring:
├─ -40 to 0°C (40 degree range)   → Blue
├─ 0 to 20°C (20 degree range)    → Green
├─ 20 to 35°C (15 degree range)   → Yellow
└─ 35 to 50°C (15 degree range)   → Red

This is valid! Different ranges can have different widths.
First match wins if overlapping.
```

### Scenario 2: Negative Values

```
Pressure differential monitoring:
├─ -100 to -20 kPa → Red (Vacuum)
├─ -20 to 0 kPa    → Yellow (Slight vacuum)
├─ 0 to 20 kPa     → Green (Normal)
└─ 20 to 100 kPa   → Yellow (Overpressure)

JSON support: Negative numbers work fine
```

### Scenario 3: High-Precision Values

```
Humidity monitoring:
├─ 0 to 30.5% → Red (Too dry)
├─ 30.5 to 65.5% → Green (Optimal)
└─ 65.5 to 100% → Red (Too humid)

Use decimal places: 30.5, 65.5 work correctly
```

### Scenario 4: Categorical Values

```
Status code mapping (0-10 range):
├─ 0 to 1 → Blue (Initializing)
├─ 2 to 3 → Green (Running)
├─ 4 to 5 → Yellow (Warning)
├─ 6 to 7 → Orange (Error)
└─ 8 to 10 → Red (Critical)

Each integer status maps to range
```

---

## Data Persistence

### Save Process

```
User clicks File → Save
        ↓
HMI serializes all widgets
        ↓
Range Editor calls SaveToJson() on widget
        ↓
All StateRanges written to JSON
        ↓
HMI file written to disk
        ↓
File saved successfully
```

### Load Process

```
User opens HMI file
        ↓
HMI deserializes from file
        ↓
Range Editor calls LoadFromJson() on widget
        ↓
StateRanges collection populated from file
        ↓
Colors and names restored
        ↓
Widget displays with loaded configuration
```

### Backup Strategy

```
Recommended:
1. Export important configurations to JSON files
2. Store in source control
3. Document which widgets use which configs
4. Keep version history

Example file structure:
/configs/
├─ temperature_gauge.json
├─ pressure_gauge.json
└─ README.md (documents what each contains)
```

---

## Troubleshooting

### Problem: Can't Edit Cell

**Symptoms**: Click cell but can't type

**Solutions**:
1. Double-click to enter edit mode
2. Check if row is readonly
3. Verify DataGrid is in focus
4. Check for dialog modal windows

### Problem: Changes Don't Persist

**Symptoms**: Changes disappear after closing

**Solutions**:
1. Save HMI file (Ctrl+S)
2. Check file has write permission
3. Verify file saved successfully
4. Check if auto-save is enabled

### Problem: Paste Doesn't Work

**Symptoms**: Click Paste but nothing happens

**Solutions**:
1. Copy ranges first (Copy or Copy All)
2. Verify clipboard has JSON
3. Check JSON format is valid
4. Try simpler JSON (single range)

### Problem: Colors Don't Show

**Symptoms**: All ranges show gray/default color

**Solutions**:
1. Verify Color column has values
2. Check color format (#AARRGGBB)
3. Try clicking [Color] button to set
4. Refresh editor (close and reopen)

### Problem: Min/Max Won't Update

**Symptoms**: Numeric fields reject input

**Solutions**:
1. Ensure valid decimal number
2. No letters or special characters
3. Use . for decimal separator (not ,)
4. Verify Min ≤ Max

---

## Related Documentation

- [Gauge Widgets Index](index.md) - All widget types
- [State-Based Colors & Ranges](state_based_colors_and_ranges.md) - Master guide
- [MultiStateIndicator](multistate_indicator.md) - Widget example
- [NumericGauge](numeric_gauge.md) - Widget example
- [BarGraph](bar_graph.md) - Widget example
- [Dial180](dial180.md) - Widget example
- [Copy/Paste System](../features/copy_paste.md) - Technical details
