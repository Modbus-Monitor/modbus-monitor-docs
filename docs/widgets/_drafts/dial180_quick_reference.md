# Dial180 Widget — Quick Reference Card

**Print or bookmark this for quick lookup while using Dial180 in HMI designer**

---

## 📋 Property Quick Reference

### Data Binding
```
CurrentValue   → Current gauge value (binds to Modbus register)
Minimum        → Min value on scale (default: 0)
Maximum        → Max value on scale (default: 100)
```

### Orientation  
```
StartAngle     → Where minimum is placed (degrees, default: 180)
               0° = right  |  90° = up  |  180° = left  |  -90° = down
SweepAngle     → Total sweep magnitude (degrees, default: -180)
               -180° = semicircle  |  -270° = full 3/4 circle
```

### Tick Marks
```
MajorTickStep  → Spacing between major ticks (default: 20)
MinorTickStep  → Spacing between minor ticks (default: 10)
               Set MajorTickStep=0 to hide all ticks
```

### Display
```
ValueFormat    → Number format (default: "F1", e.g., "F2" = 2 decimals)
RangeFormat    → Format for Min/Max labels (default: "F1")
ShowNeedle     → Display needle indicator (default: true)
ShowScale      → Display Min/Max labels (default: true)
```

---

## 🎯 Configuration Recipes

### Classic 180° Horizontal Dial
```
StartAngle: 180    | SweepAngle: -180
MajorTickStep: 20  | MinorTickStep: 10
```

### Industrial 270° Dial (Needle Down)
```
StartAngle: 225    | SweepAngle: -270
MajorTickStep: 25  | MinorTickStep: 5
```

### Temperature Gauge (Compact)
```
StartAngle: 200    | SweepAngle: -140
MajorTickStep: 10  | MinorTickStep: 5
Minimum: 0         | Maximum: 100
```

### Inverted Dial (Needle Up = Max)
```
StartAngle: 90     | SweepAngle: -180
MajorTickStep: 10  | MinorTickStep: 5
```

---

## 🔧 Setup Instructions

### Step 1: Add to Dashboard
1. Open HMI Dashboard in designer
2. Drag **Dial180** widget from toolbox
3. Resize to 160×140 pixels (recommended)

### Step 2: Bind Data
1. Right-click widget → **Properties**
2. Find **CurrentValue** property
3. Click dropdown → Select Modbus register
4. Set **Minimum** and **Maximum** to bracket expected values

### Step 3: Configure Appearance
1. In Properties panel, set **StartAngle** and **SweepAngle**
2. Adjust **MajorTickStep** and **MinorTickStep**
3. Toggle **ShowNeedle** and **ShowScale**
4. Set **ValueFormat** (e.g., "F1" = 1 decimal)

### Step 4: Save
1. Click **Save Dashboard** (Ctrl+S)
2. Configuration automatically persists

---

## ⚡ Quick Troubleshooting

| Problem | Cause | Fix |
|---------|-------|-----|
| Needle not moving | No data binding | Check CurrentValue binding in properties |
| Ticks not showing | MajorTickStep = 0 | Set to reasonable value (e.g., 20) |
| Dial curves wrong way | Missing SweepAngle | Verify SweepAngle matches sweep direction |
| Arcs misaligned | Stroke thickness wrong | Verify background=6pt, operating=5pt, active=4pt |
| Labels don't update | PropertyChanged not fired | Save & reload dashboard |

---

## 📐 Angle Cheat Sheet

```
    90°
     ↑
180° ← → 0°
     ↓
   -90° (or 270°)

StartAngle Examples:
  0°   = needle at 3 o'clock (right)
  90°  = needle at 12 o'clock (top)
  180° = needle at 9 o'clock (left) ← DEFAULT
  -90° = needle at 6 o'clock (bottom)
  45°  = needle at 1:30 position
```

---

## 🎨 Color Scheme (Current)

```
Background Arc    #E8E8E8  (Light Gray)   — Full possible range
Operating Range   #B3D9FF  (Light Blue)   — Valid instrument range  
Active Value      #0078D4  (Bright Blue)  — Current value indicator
Ticks             #666666  (Dark Gray)
```

---

**Quick Reference Version:** 1.0 | **Last Updated:** 2026-01-18
