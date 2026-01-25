# Quick Reference: State-Based Colors

One-page cheat sheet for configuring state ranges across all gauge widgets.

---

## Copy & Paste Cheat Sheet

### Copy Single Range
```
1. Click range row
2. Click [Copy]
```

### Copy Multiple Ranges
```
1. Ctrl+Click ranges OR Shift+Click range
2. Click [Copy]
```

### Copy All Ranges
```
1. Click [Copy All]
```

### Paste Ranges
```
1. Click [Paste]
```

---

## Widget Quick Start

### Add Widget
```
Right-click → Add Widget → Choose Widget Type
```

### Configure (Same for all widgets)
```
1. Set Monitoring Point (register)
2. Set Min/Max Value range
3. Add ranges in Range Editor
4. Save (Ctrl+S)
```

### Add Range
```
1. Click [+]
2. Edit Min, Max, Name
3. Click [Color] and choose color
```

---

## JSON Format

### Single Range
```json
{
  "MinValue": 0,
  "MaxValue": 100,
  "StateColor": "#FF00FF00",
  "StateName": "Normal"
}
```

### Multiple Ranges
```json
[
  { "MinValue": 0, "MaxValue": 33, "StateColor": "#FFFF0000", "StateName": "Low" },
  { "MinValue": 34, "MaxValue": 66, "StateColor": "#FFFFFF00", "StateName": "Normal" },
  { "MinValue": 67, "MaxValue": 100, "StateColor": "#FF00FF00", "StateName": "High" }
]
```

---

## Color Codes

### Standard Colors
| Color | Code | Usage |
|-------|------|-------|
| 🔴 Red | #FFFF0000 | Error, Critical, High |
| 🟢 Green | #FF00FF00 | Normal, Good, Running |
| 🟡 Yellow | #FFFFFF00 | Warning, Caution |
| 🔵 Blue | #FF0000FF | Idle, Standby, Low |
| 🔶 Orange | #FFFFA500 | Alert, Attention |
| ⚪ Gray | #FFC8C8C8 | Off, Disabled |

### Format: #AARRGGBB
- AA = Alpha (FF=opaque, 00=transparent)
- RR = Red (00-FF)
- GG = Green (00-FF)  
- BB = Blue (00-FF)

---

## Standard Range Patterns

### Temperature (°C)
```
-40 to 0   → Blue (Freezing)
0 to 20    → Green (Normal)
20 to 35   → Yellow (Warm)
35 to 50   → Red (Hot)
```

### Pressure (psi)
```
0 to 50    → Green (Low)
50 to 150  → Green (Normal)
150 to 200 → Yellow (High)
200 to 250 → Red (Critical)
```

### CPU Usage (%)
```
0 to 50    → Green (Normal)
50 to 75   → Yellow (Caution)
75 to 90   → Orange (Warning)
90 to 100  → Red (Critical)
```

---

## Multi-Select Keyboard Shortcuts

| Key | Action |
|-----|--------|
| Click | Select single row |
| Ctrl+Click | Toggle select row |
| Shift+Click | Select range |
| Ctrl+A | Select all |
| Delete | Remove selected |
| Escape | Clear selection |

---

## Common Errors & Fixes

### "Can't paste ranges"
- Copy ranges first (click Copy or Copy All)
- Verify clipboard has valid JSON

### "Ranges don't display colors"
- Check StateRanges not empty
- Verify Min ≤ Max for each range
- Click [Color] to set color

### "Changes disappear"
- Save HMI file (Ctrl+S)
- Check file has write permission

### "Invalid Min/Max values"
- Use numbers only (no text)
- Ensure Min ≤ Max
- Use decimal point (.) not comma

---

## Workflows at a Glance

### Share Config Between Widgets
```
Widget A: [Copy All] → Clipboard
Widget B: [Paste] → Configuration applied
```

### Backup Configuration
```
Widget: [Copy All] → Clipboard
Text Editor: Paste → Save as "backup.json"
```

### Restore from Backup
```
Text File: Open "backup.json" → Copy
Widget: [Paste] → Configuration restored
```

### Test Value Zone
```
Set Value: 45
Check: Widget shows correct color for range
Verify: 45 falls within expected Min/Max
```

---

## Widget Comparison

| Widget | Good For | Orientation | State Evaluation |
|--------|----------|-------------|-----------------|
| MultiState | Status | Fixed | Background color |
| NumericGauge | Numbers | Fixed | Border color |
| BarGraph | Levels | 4 directions | Fill bar |
| Dial180 | Analog | 180° | Needle + arc |

All implement: IRangeConfigurable + IJsonSerializable

---

## Essential Files

| File | Purpose |
|------|---------|
| state_based_colors_and_ranges.md | Master guide |
| index.md | Widget overview |
| range_editor_panel.md | Editor UI reference |
| multistate_indicator.md | Status widget docs |
| numeric_gauge.md | Number widget docs |
| bar_graph.md | Level widget docs |
| dial180.md | Analog widget docs |

---

## Save & Load

### Manual Save
```
File → Save (or Ctrl+S)
```

### Automatic Load
```
Open HMI file
→ All widget configurations restored
→ Colors and ranges applied
```

### Export Configuration
```
Widget: [Copy All]
Paste in: Text editor
Save as: config.json
Share: .json file with others
```

### Import Configuration
```
Open: config.json file
Copy: Content from file
Paste in: Widget Range Editor
Result: Configuration applied
```

---

## Properties Reference

### All Widgets Have

```
CurrentValue          (double) - From register
CurrentStateColor     (Color) - Evaluated color
CurrentStateName      (string) - Evaluated name
StateRanges          (List) - All ranges defined
MinValue             (double) - Min on gauge
MaxValue             (double) - Max on gauge
Label                (string) - Widget title
```

### Each Range Contains

```
MinValue             (double) - Lower boundary
MaxValue             (double) - Upper boundary
StateColor           (Color) - Color for this range
StateName            (string) - Name of state
ImagePath            (string) - Optional image
```

---

## Tips & Tricks

1. **Ctrl+Z for undo** - Revert accidental deletes
2. **Copy All first** - Save backup before major changes
3. **Test boundaries** - Try min, max, and middle values
4. **Use consistent naming** - Helps with troubleshooting
5. **Document ranges** - Add notes about what each range means

---

## Getting Help

- See [State-Based Colors & Ranges](state_based_colors_and_ranges.md) for detailed examples
- See [Range Editor Panel](range_editor_panel.md) for UI-specific help
- See individual widget docs for widget-specific features
- Check troubleshooting sections in each doc

---

## Next Steps

1. ✅ Understand state-based colors (this guide)
2. ✅ Try copy/paste between widgets
3. ✅ Create standard configurations
4. ✅ Share configurations with team
5. ✅ Backup important configs to files
