# Clock Widget Documentation

## Overview

The **Clock** widget displays the current system time in a customizable format. It updates automatically and does not require register binding - it's a pure display widget showing the system clock.

**Best for**: Time display, timestamps, elapsed time, session tracking.

---

## Features

✅ **Real-Time Display** - Updates automatically  
✅ **Customizable Format** - 12-hour, 24-hour, custom  
✅ **Digital/Analog** - Multiple display modes  
✅ **No Register Binding** - Standalone widget  
✅ **Auto-Update** - Refreshes continuously  
✅ **Date & Time** - Can show both or either  
✅ **Timezone Support** - Display in different timezones  

---

## Quick Start (3 Steps)

### Step 1: Add Widget
```
Right-click canvas → Add Widget → Clock
```

### Step 2: Configure Format
Property Editor:
- **Display Format**: 12-Hour, 24-Hour, or Custom
- **Show Date**: Include date display
- **Show Seconds**: Include seconds in time

### Step 3: Save
```
File → Save or Ctrl+S
```

---

## Properties

| Property | Type | Default | Purpose |
|----------|------|---------|---------|
| Format | enum | 24Hour | Display format |
| ShowDate | bool | false | Include date |
| ShowSeconds | bool | true | Include seconds |
| Use12Hour | bool | false | 12-hour vs 24-hour |
| ShowMilliseconds | bool | false | Include milliseconds |
| Timezone | TimeZone | Local | Display timezone |
| FontSize | double | 16 | Text size |
| FontColor | Color | Black | Text color |

---

## Display Formats

### Format 1: Time Only (24-Hour)

```
14:32:45

Display: HH:MM:SS
Updates: Every second
Use: Industrial systems, precise timing
```

### Format 2: Time Only (12-Hour)

```
02:32:45 PM

Display: HH:MM:SS AM/PM
Updates: Every second
Use: General displays, user-friendly
```

### Format 3: Date & Time

```
2026-01-25 14:32:45

Display: YYYY-MM-DD HH:MM:SS
Updates: Every second
Use: Logs, records, full information
```

### Format 4: Date Only

```
Saturday, January 25, 2026

Display: Day, Month Date, Year
Updates: Every midnight
Use: Calendar reference, schedules
```

### Format 5: Elapsed Time

```
00:12:34

Display: Hours:Minutes:Seconds elapsed
Updates: Every second
Use: Session tracking, operation duration
```

---

## Configuration Examples

### Example 1: Operational Clock

```
Display Format: 24-Hour
Show Date: false
Show Seconds: true
Font Size: 20pt
Font Color: Dark Blue

Display: "14:32:45"
Updates continuously
Perfect for control room
```

### Example 2: Date & Time Stamp

```
Display Format: 24-Hour with Date
Show Date: true
Show Seconds: true
Font Size: 12pt
Font Color: Gray

Display: "2026-01-25 14:32:45"
Used in event logs
Precise timestamp recording
```

### Example 3: User-Friendly Clock

```
Display Format: 12-Hour
Show Date: false
Show Seconds: false
Font Size: 18pt
Font Color: Navy

Display: "02:32 PM"
Easy to read
No seconds distraction
```

### Example 4: Session Timer

```
Display Format: Elapsed Time
Show Date: false
Show Seconds: true
Font Size: 16pt
Font Color: Green

Display: "00:45:32" (45 minutes 32 seconds)
Tracks session duration
Starts when system activates
```

---

## Real-World Examples

### Example A: Manufacturing Control Room

```
Dashboard Clock:
┌─────────────────┐
│  CURRENT TIME   │
│   14:32:45      │ (24-hour format)
│   25-JAN-2026   │ (Date below)
└─────────────────┘

Purpose:
- Reference for shift changes
- Log timestamps
- Event tracking
```

### Example B: HVAC System

```
System Status Panel:
┌──────────────────────┐
│ System Running       │
│ Since: 08:00 AM      │
│ Duration: 06:32:15   │
│ Next Service: 08:00  │
└──────────────────────┘

Clock shows elapsed operation time
```

### Example C: Process Monitoring

```
Batch Process Display:
┌─────────────────────────┐
│ BATCH #2847             │
│ Start Time: 14:00:00    │
│ Current Time: 14:32:45  │
│ Elapsed: 00:32:45       │
│ Estimated End: 15:15:00 │
└─────────────────────────┘
```

---

## Time Display Patterns

### Pattern 1: Simple Time Display

```
┌──────────────────┐
│   14:32:45       │ (Updates every second)
└──────────────────┘
```

### Pattern 2: Time with Date

```
┌────────────────────────┐
│  Saturday, Jan 25      │ (Non-updating)
│  14:32:45              │ (Updates every second)
└────────────────────────┘
```

### Pattern 3: Session Duration

```
┌────────────────────┐
│ Session Active     │
│ Duration: 01:23:45 │ (Updates every second)
└────────────────────┘
```

### Pattern 4: Analog Clock Face

```
      12
   9  ◐  3
      6

Hour hand: Rotates every 12 hours
Minute hand: Rotates every 60 minutes
Second hand: Rotates every 60 seconds
```

---

## Advanced Features

### Multiple Timezone Display

```
System Timezone: UTC
Display Timezone: Local
Conversion: Automatic

Example:
UTC Time: 19:32:45
Local Time (EST): 14:32:45
Display: 14:32:45 EST
```

### Precision Options

```
Standard: HH:MM:SS (1-second precision)
High Precision: HH:MM:SS.sss (millisecond precision)
Low Precision: HH:MM (1-minute precision)

Use case determines precision needed
```

### Display Updates

```
Standard: Updates every 1 second
High Precision: Updates every 100ms
Minimal: Updates every 60 seconds
Performance vs accuracy tradeoff
```

---

## Best Practices

### ✅ DO

1. **Choose Readable Formats**
   - 24-hour for technical systems
   - 12-hour for user displays
   - Clear timezone labeling

2. **Position Prominently**
   - Top-right corner (standard)
   - Visible without scrolling
   - Easy to reference

3. **Use Appropriate Font**
   - Large enough to read
   - Monospace for precise reading
   - High contrast colors

4. **Include Context**
   - Show timezone if non-local
   - Label elapsed time
   - Indicate purpose

5. **Test Visibility**
   - Verify readable on target display
   - Check contrast ratio
   - Test from operator distance

### ❌ DON'T

1. **Don't Use Ambiguous Formats**
   - "14:32" without AM/PM context
   - "01/02/2026" (could be Jan 2 or Feb 1)

2. **Don't Hide Time**
   - Make clock obvious
   - Don't bury in small corner
   - Operator should know current time

3. **Don't Mix Timezones Silently**
   - Always label timezone
   - Clearly show conversions
   - Prevent confusion

4. **Don't Use Problematic Colors**
   - Green on red (colorblind issues)
   - Low contrast backgrounds
   - Hard-to-read color pairs

---

## Common Use Cases

### Use Case 1: Control Room Status Board

```
Purpose: Operators reference current time
Position: Top-right of display
Format: 24-Hour HH:MM:SS
Update Rate: Every second
Display: "14:32:45"
```

### Use Case 2: Event Logger

```
Purpose: Timestamp events with precision
Position: Can be small/inconspicuous
Format: YYYY-MM-DD HH:MM:SS
Update Rate: Every second (precision)
Display: "2026-01-25 14:32:45"
```

### Use Case 3: Session Monitor

```
Purpose: Track operation duration
Position: Visible in session panel
Format: Elapsed time HH:MM:SS
Update Rate: Every second
Display: "00:45:32" (elapsed)
```

### Use Case 4: Shift Clock

```
Purpose: Reference for shift changes
Position: Prominent on HMI
Format: 12-hour with date
Update Rate: Every minute (lower precision ok)
Display: "02:32 PM" / "SAT 25-JAN"
```

---

## Troubleshooting

### Problem: Clock Stops Updating

**Symptoms**: Time frozen, not advancing

**Solutions**:
1. Check application still running
2. Verify update thread active
3. Check system clock not frozen
4. Restart HMI if necessary

### Problem: Wrong Time Displayed

**Symptoms**: Time doesn't match system clock

**Solutions**:
1. Check system time is correct
2. Verify timezone setting
3. Check for daylight saving transitions
4. Reboot if time significantly off

### Problem: Clock Format Incorrect

**Symptoms**: Time displays in wrong format

**Solutions**:
1. Check format setting in properties
2. Verify locale settings
3. Update clock configuration
4. Refresh HMI display

### Problem: Performance Issues

**Symptoms**: HMI slow with clock widget

**Solutions**:
1. Reduce update frequency
2. Use lower precision (minutes vs seconds)
3. Disable milliseconds display
4. Verify no infinite loops

---

## API Reference

```csharp
public class ClockViewModel : WidgetBaseViewModel
{
    public DateTime CurrentTime { get; }
    public string DisplayFormat { get; set; }
    public bool ShowDate { get; set; }
    public bool ShowSeconds { get; set; }
    public bool Use12Hour { get; set; }
    public TimeZoneInfo Timezone { get; set; }
    public string FormattedTime { get; }
    
    public void UpdateTime();
    public void SetTimezone(TimeZoneInfo tz);
}

public enum ClockFormat
{
    TimeOnly24Hour,        // HH:MM:SS
    TimeOnly12Hour,        // HH:MM:SS AM/PM
    DateAndTime24Hour,     // YYYY-MM-DD HH:MM:SS
    DateAndTime12Hour,     // MM/DD/YYYY HH:MM:SS AM/PM
    DateOnly,              // Saturday, January 25, 2026
    ElapsedTime            // HH:MM:SS
}
```

---

## Related Documentation

- [Gauge Widgets Index](index.md)
- [Widget Layout](../ui/widget_layout.md)
- [Display Formatting](../ui/display_formatting.md)
