# Button Widget Documentation

## Overview

The **Button** widget is a write-only control widget that sends values to Modbus registers when clicked. It displays a clickable button with customizable labels and optionally triggers actions on a slave device.

**Best for**: Device control, mode switching, alarm acknowledgment, manual commands.

---

## Features

✅ **Click to Write** - Send values to registers  
✅ **Customizable Labels** - Display text on button  
✅ **Value Mapping** - Configure what value to write  
✅ **State-Based Colors** - Visual feedback on current state  
✅ **Multiple Button Types** - Toggle, momentary, set-value  
✅ **Confirmation Dialogs** - Optional user confirmation  
✅ **Event Logging** - Track button interactions  

---

## Quick Start (4 Steps)

### Step 1: Add Widget
```
Right-click canvas → Add Widget → Button
```

### Step 2: Configure Target Register
Property Editor:
- **Monitoring Point**: Select Modbus register to write
- **Widget Label**: Button display text

### Step 3: Set Write Value
Property Editor:
- **Write Value**: Value to send when clicked (default: 1)
- **Reset Value**: Value to reset to (if toggle mode)

### Step 4: Save
```
File → Save or Ctrl+S
```

---

## Properties

| Property | Type | Default | Purpose |
|----------|------|---------|---------|
| Label | string | "Button" | Button display text |
| WriteValue | double | 1 | Value to write on click |
| ResetValue | double | 0 | Value to reset to |
| ConfirmOnClick | bool | false | Show confirmation dialog |
| IsToggle | bool | false | Toggle mode vs momentary |
| CurrentValue | double | 0 | Current register value |

---

## Button Modes

### Mode 1: Momentary Press
```
User clicks button
  ↓
Write WriteValue to register
  ↓
Register maintains value until changed externally
  ↓
Button color updates based on current state
```

### Mode 2: Toggle
```
User clicks button
  ↓
If current value == WriteValue:
  └─ Write ResetValue
Else:
  └─ Write WriteValue
  ↓
Button toggles between two states
```

### Mode 3: Confirmed Action
```
User clicks button
  ↓
Show confirmation dialog: "Are you sure?"
  ↓
User confirms
  └─ Write WriteValue
  ↓
Or: User cancels
  └─ No action
```

---

## Configuration Examples

### Example 1: Emergency Stop Button

```
Label: EMERGENCY STOP
Write Value: 0
Reset Value: N/A (momentary)
Confirm On Click: true
Color When 0: Red
Color When 1: Green

Action: Sends 0 to register, stopping equipment
```

### Example 2: Pump On/Off Toggle

```
Label: Pump Power
Write Value: 1 (On)
Reset Value: 0 (Off)
Is Toggle: true
Confirm On Click: false

Action: Toggles pump between on/off states
```

### Example 3: Mode Selection

```
Label: Switch to Mode B
Write Value: 2
Reset Value: N/A
Confirm On Click: true

Action: Confirms mode change, sends mode code
```

---

## State Evaluation

```
Register value changes
  ↓
Button evaluates current state
  ↓
Display updated color/state
  ↓
Button shows if pressed or released
```

---

## Real-World Examples

### Example A: Manufacturing Control Panel

```
Buttons:
├─ START → Sends 1 to start register
├─ STOP  → Sends 0 to stop register
├─ EMERGENCY STOP → Sends -1 (requires confirm)
└─ RESET → Sends 99 (clears error state)

Visual Feedback:
- Green when machine running
- Yellow when warning
- Red when stopped
```

### Example B: HVAC System Control

```
Buttons:
├─ Heat Mode → Write 1
├─ Cool Mode → Write 2
├─ Auto Mode → Write 3
└─ Fan Only → Write 4

Each mode shows different color
User can switch modes via buttons
```

### Example C: Pump Station

```
Buttons:
├─ Pump A Start
├─ Pump A Stop
├─ Pump B Start
├─ Pump B Stop
└─ Emergency Flush

Each sends specific code to SCADA
Buttons show current state (red=off, green=on)
```

---

## Usage Patterns

### Pattern 1: Momentary Action

```csharp
// Button configuration
var button = new ButtonViewModel(register);
button.Label = "START";
button.WriteValue = 1;
button.IsToggle = false;

// When clicked: Sends 1, then value depends on SCADA response
```

### Pattern 2: Toggle Switch

```csharp
// Button configuration
var button = new ButtonViewModel(register);
button.Label = "PUMP POWER";
button.WriteValue = 1;    // On value
button.ResetValue = 0;    // Off value
button.IsToggle = true;   // Toggle mode

// Click toggles between 0 and 1
```

### Pattern 3: Confirmed Critical Action

```csharp
// Button configuration
var button = new ButtonViewModel(register);
button.Label = "EMERGENCY STOP";
button.WriteValue = 0;
button.ConfirmOnClick = true;  // Show dialog

// Click shows: "Are you sure? This will stop equipment"
// Only sends if user confirms
```

---

## Best Practices

### ✅ DO

1. **Use Clear Labels**
   - "START PUMP" not "SP"
   - "EMERGENCY STOP" not "ES"

2. **Require Confirmation for Critical Actions**
   - Emergency stop
   - Mode changes
   - Data deletion

3. **Test Before Deployment**
   - Verify correct register binding
   - Test write values work
   - Check state feedback updates

4. **Visual Indicators**
   - Use color to show state
   - Green = OK, Red = Warning
   - Match register feedback to button state

5. **Organize Logically**
   - Group related buttons together
   - Order by importance
   - Document what each does

### ❌ DON'T

1. **Don't Use Cryptic Values**
   - Use meaningful numbers or document them
   - Add comments in HMI file

2. **Don't Skip Confirmation**
   - Critical actions need user confirmation
   - Emergency operations require double-check

3. **Don't Assume State Feedback**
   - Always verify register returns correct value
   - Some PLCs may not echo write value

4. **Don't Flood with Buttons**
   - Too many buttons = confusion
   - Group by function

---

## Troubleshooting

### Problem: Button Click Has No Effect

**Symptoms**: Click button but nothing happens

**Solutions**:
1. Check register binding (Monitoring Point set?)
2. Verify register is writable
3. Check WriteValue is valid for device
4. Verify Modbus connection active
5. Check device permissions

### Problem: Button Shows Wrong State

**Symptoms**: Button shows opposite state than expected

**Solutions**:
1. Verify register returns value after write
2. Check if device echoes write value
3. May need ResetValue configuration
4. Check state color mapping

### Problem: Confirmation Dialog Won't Show

**Symptoms**: No confirmation even though ConfirmOnClick=true

**Solutions**:
1. Verify ConfirmOnClick property is enabled
2. Check for modal windows blocking dialog
3. Verify focus on HMI window

---

## API Reference

```csharp
public class ButtonViewModel : WidgetBaseViewModel
{
    public string Label { get; set; }
    public double WriteValue { get; set; }
    public double ResetValue { get; set; }
    public bool ConfirmOnClick { get; set; }
    public bool IsToggle { get; set; }
    public double CurrentValue { get; set; }
    
    public void OnClick();
    public Color GetStateColor();
}
```

---

## Related Documentation

- [Gauge Widgets Index](index.md)
- [Control Widgets](../ui/control_widgets.md)
- [Modbus Register Binding](../modbus/register_binding.md)
