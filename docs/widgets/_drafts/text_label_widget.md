# Text Label Widget Documentation

## Overview

The **Text Label** widget displays static text on the HMI canvas. It's a non-interactive display element used for titles, annotations, instructions, and informational text.

**Best for**: Titles, section headers, instructions, static information, annotations.

---

## Features

✅ **Static Display** - No register binding required  
✅ **Rich Text** - Customizable font, size, color  
✅ **Multi-Line** - Text wrapping support  
✅ **Positioning** - Free placement on canvas  
✅ **Alignment** - Left, center, right alignment  
✅ **Transparency** - Background opacity control  
✅ **Rotation** - Text angle adjustment  

---

## Quick Start (3 Steps)

### Step 1: Add Widget
```
Right-click canvas → Add Widget → Text Label
```

### Step 2: Configure Text
Property Editor:
- **Widget Label**: Enter text to display
- **Font**: Choose font
- **Size**: Set text size
- **Color**: Choose text color

### Step 3: Position and Save
```
Drag to position on canvas
File → Save or Ctrl+S
```

---

## Properties

| Property | Type | Default | Purpose |
|----------|------|---------|---------|
| Label | string | "Text" | Text content |
| FontFamily | string | "Arial" | Font name |
| FontSize | double | 12 | Text size in points |
| FontColor | Color | Black | Text color |
| FontWeight | enum | Normal | Normal, Bold |
| FontStyle | enum | Normal | Normal, Italic |
| TextAlignment | enum | Left | Left, Center, Right |
| Background | Color | Transparent | Background color |
| Foreground | Color | Black | Text color |
| Rotation | double | 0 | Text angle in degrees |

---

## Usage Examples

### Example 1: Section Header

```
Text: "SYSTEM STATUS"
Font: Arial
Size: 24
Weight: Bold
Color: Dark Blue
Alignment: Center
```

### Example 2: Instruction Text

```
Text: "Drag slider to adjust setpoint
      Press START to begin
      Emergency Stop: Red button"
Font: Arial
Size: 11
Color: Black
Alignment: Left
```

### Example 3: Units Label

```
Text: "°F"
Font: Arial
Size: 14
Color: Gray
Alignment: Right
Position: Next to numeric gauge
```

### Example 4: Warning Banner

```
Text: "⚠ CAUTION: High Pressure Zone"
Font: Arial
Size: 16
Weight: Bold
Color: Red
Background: Yellow
Alignment: Center
```

---

## Layout Patterns

### Pattern 1: Dashboard Title

```
┌─────────────────────────────┐
│  PUMP STATION MONITOR  ← Title (bold, large)
├─────────────────────────────┤
│  Pump A: [████████]  ← Gauges
│  Pump B: [████░░░░]
│  Pressure: 120 PSI
└─────────────────────────────┘
```

### Pattern 2: Annotated Gauge

```
┌──────────────────┐
│  TEMPERATURE  ← Label above
│   ┌─────────┐
│   │    65°F │  ← Value inside
│   │    ◐    │
│   └─────────┘
│      °C     ← Unit label below
└──────────────────┘
```

### Pattern 3: Instructions

```
SETUP WIZARD
─────────────────
1. Select equipment type
2. Configure Modbus address
3. Test connection
4. Start monitoring
```

---

## Real-World Examples

### Example A: Process Control Dashboard

```
Title:
┌──────────────────────────┐
│ WASTEWATER TREATMENT     │ (Bold, 24pt, Blue)
└──────────────────────────┘

Sections (each with label):
├─ INCOMING FLOW           (18pt, Bold)
│  ├─ Level: [gauge]
│  └─ Pressure: [gauge]
│
├─ TREATMENT TANK          (18pt, Bold)
│  ├─ Temperature: [gauge]
│  └─ pH: [gauge]
│
└─ OUTGOING              (18pt, Bold)
   └─ Flow: [gauge]

Status Area (bottom):
└─ LAST UPDATE: 14:32:15  (10pt, Gray)
```

### Example B: Manufacturing HMI

```
┌─────────────────────────┐
│  PRODUCTION LINE 3      │
├─────────────────────────┤
│ LINE STATUS: RUNNING    │
│ ↓                       │
│ Speed: 1200 RPM         │
│ Temperature: 185°F      │
│ Pressure: 45 PSI        │
│                         │
│ Next Stop: 15:30        │
└─────────────────────────┘
```

### Example C: Vehicle Dashboard

```
┌──────────────────────────┐
│  VEHICLE DIAGNOSTICS     │
├──────────────────────────┤
│                          │
│ Speed: [gauge]           │
│                          │
│ Engine Temp: [gauge]     │
│                          │
│ Fuel Level: [gauge]      │
│                          │
│ Last Service: 5/15/2025  │
│ Next Service: 6/15/2025  │
│                          │
└──────────────────────────┘
```

---

## Best Practices

### ✅ DO

1. **Use Clear, Readable Text**
   - "PUMP STATUS" not "PS"
   - Full words for clarity
   - Consistent terminology

2. **Organize Hierarchically**
   - Titles larger than sections
   - Sections larger than content
   - Use spacing to group related items

3. **Choose Readable Colors**
   - High contrast (dark on light, light on dark)
   - Avoid color combinations that clash
   - Test on target display

4. **Use Consistent Formatting**
   - Same font across related elements
   - Consistent alignment
   - Regular spacing

5. **Position Logically**
   - Title at top
   - Content below
   - Labels near associated widgets
   - Group related information

### ❌ DON'T

1. **Don't Use Too Many Fonts**
   - Stick to 1-2 font families
   - Vary size and weight instead

2. **Don't Make Text Too Small**
   - Must be readable from operator distance
   - Test readability on target display

3. **Don't Overcrowd**
   - Leave space between elements
   - Use multiple screens if needed
   - Avoid wall-of-text appearance

4. **Don't Use Poor Color Contrast**
   - Light text on dark background (good)
   - Red on green (bad - colorblind unfriendly)
   - Always verify readable

5. **Don't Rotate Text Excessively**
   - Avoid rotations other than 90°
   - Rotated text is hard to read
   - Use for special cases only

---

## Text Formatting Tips

### Font Choices

| Font | Use For | Notes |
|------|---------|-------|
| Arial | General use | Clean, readable |
| Calibri | Professional | Modern |
| Consolas | Numbers/Values | Monospace |
| Impact | Headers | Large, attention-getting |
| Courier | Code/Technical | Monospace |

### Size Guidelines

| Size | Use For |
|------|---------|
| 10pt | Small labels, units |
| 12pt | Body text, annotations |
| 14-16pt | Section headers |
| 20-24pt | Main title |
| 32pt+ | Large warning/alert |

### Color Guidelines

| Color | Use For |
|-------|---------|
| Black | Body text |
| Dark Blue | Headers, professional |
| Dark Gray | Secondary text |
| Red | Warnings, alerts |
| Green | Success, normal status |
| White | On dark backgrounds |

---

## Advanced Layouts

### Multi-Line Text with Line Breaks

```
Configuration:
Text: "Line 1
Line 2
Line 3"

Display:
Line 1
Line 2
Line 3
```

### Text with Background Panel

```
Create rectangle shape behind text
Set background color
Text color contrasts with background
Creates "label" appearance
```

### Dynamic Text (via Register)

```
Note: Text Label itself is static
For dynamic values, use Numeric Gauge instead
To mix static + dynamic:
├─ Use Text Label for label
├─ Use Numeric Gauge for value
├─ Position side by side
```

---

## Accessibility Considerations

### ✅ DO

1. **High Contrast Ratios**
   - 4.5:1 minimum for body text
   - 3:1 minimum for large text

2. **Readable Fonts**
   - Sans-serif (Arial, Calibri)
   - Avoid decorative fonts

3. **Sufficient Size**
   - Minimum 12pt for body text
   - 14pt+ for operators at distance

4. **Clear Language**
   - Plain, simple words
   - Avoid jargon
   - Use industry standards where needed

### ❌ DON'T

1. Color alone to convey information
2. Very small text (< 10pt)
3. All uppercase for long text
4. Blinking or flashing text
5. Low contrast color combinations

---

## Troubleshooting

### Problem: Text Not Visible

**Symptoms**: Text doesn't appear on canvas

**Solutions**:
1. Check text color vs background
2. Verify font size is large enough
3. Check widget not behind other elements
4. Verify text not empty

### Problem: Text Too Small

**Symptoms**: Hard to read

**Solutions**:
1. Increase font size
2. Try bold weight
3. Zoom canvas view
4. Test on target display

### Problem: Text Overlaps Other Elements

**Symptoms**: Text covered by widgets

**Solutions**:
1. Right-click text → "Bring to Front"
2. Reposition text
3. Resize text to fit
4. Move overlapping widget

---

## API Reference

```csharp
public class TextLabelViewModel : WidgetBaseViewModel
{
    public string Label { get; set; }
    public string FontFamily { get; set; }
    public double FontSize { get; set; }
    public Color FontColor { get; set; }
    public FontWeight FontWeight { get; set; }
    public FontStyle FontStyle { get; set; }
    public TextAlignment TextAlignment { get; set; }
    public double Rotation { get; set; }
}

public enum TextAlignment
{
    Left,
    Center,
    Right
}

public enum FontWeight
{
    Normal,
    Bold
}

public enum FontStyle
{
    Normal,
    Italic
}
```

---

## Related Documentation

- [Gauge Widgets Index](index.md)
- [Canvas Layout](../ui/canvas_layout.md)
- [Fonts & Colors](../ui/fonts_colors.md)
