# HMI Dashboard Management (v5.0.3.0+)

Use this page to create, edit, and run HMI dashboards in XPF. For widget properties, defaults, and min/max ranges, see [Widget Reference](widget-reference.md).

![HMI Dashboard Demo](../../assets/screenshots/xpf/xpf-hmi-demo.webp){ .screenshot-shadow loading="lazy" }
*Example HMI dashboard layout in XPF*

## What You Can Do on This Page

- Create dashboards with drag-and-drop widgets.
- View live values and state colors.
- Save reusable `.hmi` dashboard files.
- Load existing dashboards for repeat jobs.

## 1) Launch the HMI Workspace

1. Open the **HMI** tab from the top ribbon.
2. XPF opens the dashboard canvas.
3. Toggle **Edit** to **On** to unlock design mode.

<!-- Screenshot placeholder: xpf-hmi-01-tab-overview.png -->
> Image coming soon...
<!-- Suggested capture: HMI tab selected, Widgets group visible, Edit toggle highlighted -->

## 2) Ribbon Controls

### Widgets Group

| Control | What It Does | Notes |
|---|---|---|
| Edit | Turns design mode on/off | Required to add, remove, or modify widgets |
| Add Widget | Opens the full gallery | Choose from all 15 widget types |
| Add | Adds a default widget | Quick way to start layout |
| Remove | Deletes selected widget | Removes only current selection |
| Delete All | Clears the canvas | Removes all widgets |

Current gallery widget types:
- Numeric, Button, Dial180, Text Label, Clock, Slider
- MultiState Indicator, Bar Graph, Trend
- Line, Rounded Rectangle, Arrow, Triangle, Polygon, Arc

### Clipboard Group

| Control | What It Does | Shortcut |
|---|---|---|
| Copy | Copies selected widget and settings | `Ctrl+C` |
| Paste | Creates duplicate at offset position | `Ctrl+V` |

### Controls Group

| Control | What It Does | Typical Use |
|---|---|---|
| Refresh | Reloads current values | After data import or map changes |
| Start/Stop | Starts or stops monitoring engine | Live update control during testing |

### Close

| Control | What It Does |
|---|---|
| Close | Exits HMI dashboard and returns to main view |

<!-- Screenshot placeholder: xpf-hmi-02-ribbon-groups.png -->
> Image coming soon...
<!-- Suggested capture: Widgets + Clipboard + Controls groups with labels -->

## 3) Add, Select, Move, Resize, Remove

### Add Widgets

1. Turn **Edit** ON.
2. Click **Add Widget**.
3. Pick a widget type from the gallery.

### Select Widgets

- Click a widget to select it.
- Selection activates **Remove**, **Copy**, and property editing.

### Move and Resize

- Drag to move.
- Use resize handles to adjust width and height.

### Remove Widgets

- Click **Remove** for selected widget, or
- Press `Delete` in Edit mode.

### Clear Entire Dashboard

- Click **Delete All**.

<!-- Screenshot placeholder: xpf-hmi-03-selection-resize.png -->
> Image coming soon...
<!-- Suggested capture: selected widget showing selection outline and resize handle -->

## 4) Configure Widgets (Simple Order)

When **Edit** is On, selecting a widget opens the property editor panel.

Recommended sequence:

1. **Monitoring Point**: choose the Modbus register binding.
2. **Range Setup**: define `Minimum` and `Maximum` where applicable.
3. **Display Format**: set labels, units, and value formatting.
4. **Visual Style**: apply colors, fonts, and layout sizing.
5. **State Ranges**: set Low/Normal/High thresholds (if supported).
6. **Runtime Validation**: turn Edit off and verify live behavior.

Example: Numeric widget for temperature
- Monitoring Point: `400001`
- Widget Label: `Tank Temperature`
- Min/Max: `0` to `100`
- Format: `0.0`
- State ranges: Blue (`0-50`, `Low`), Green (`50-80`,`Normal`), Red (`80-100`,`High`)

Notes:
- `Clock` and `Text Label` can operate without register binding.
- `Button` and `Slider` are write-capable widgets and require write permission.

<!-- Screenshot placeholder: xpf-hmi-04-property-editor.png -->
> Image coming soon...
<!-- Suggested capture: selected widget + property panel + Monitoring Point row -->

## 5) Copy and Paste Widgets

To copy:

1. Keep Edit mode On.
2. Select source widget.
3. Click **Copy** or press `Ctrl+C`.

To paste:

1. Click **Paste** or press `Ctrl+V`.
2. New widget appears with offset position.

What is copied:
- Property values and style configuration
- Register binding and state ranges

What changes automatically:
- Widget ID
- Canvas position offset

<!-- Screenshot placeholder: xpf-hmi-05-copy-paste.png -->
> Image coming soon...
<!-- Suggested capture: one widget selected, Copy clicked, pasted duplicate visible offset -->

## 6) Save and Load Dashboard Files

File formats:
- `.hmi`: packaged dashboard plus image assets
- `.json`: layout data only

Auto-pair load behavior:
- If a `.hmi` file and a `.csv` file are in the same folder and share the same base name, XPF automatically finds and loads both.
- Example: `line-a.hmi` and `line-a.csv`.

Save workflow:

1. Finalize your dashboard.
2. Trigger save command (version-specific UI path).
3. Choose descriptive filename and folder.

Load workflow:

- Drag and drop a `.hmi` file directly onto the HMI background/canvas (XPF loads the dashboard, and auto-loads matching `.csv` when present).
- Drag and drop `.json` onto the canvas, or
- Use ribbon load command.

Best practices:
- Keep `.hmi` beside corresponding register map `.csv`.
- Name pairs consistently: `line-a.hmi` and `line-a.csv`.
- Create backup checkpoints before major redesign.

<!-- Screenshot placeholder: xpf-hmi-06-save-load.png -->
> Image coming soon...
<!-- Suggested capture: Save As flow and resulting .hmi file near .csv -->

## Shape Tip: Create an Ellipse Using Rounded Rectangle

- Add **Rounded Rectangle**.
- Set `Width` and `Height` to target ellipse size.
- Set `RadiusX = Width / 2` and `RadiusY = Height / 2`.
- If corners remain visible, increase radius values slightly.

Quick examples:
- Circle: `Width=120`, `Height=120`, `RadiusX=60`, `RadiusY=60`
- Horizontal oval: `Width=180`, `Height=100`, `RadiusX=90`, `RadiusY=50`
- Vertical oval: `Width=100`, `Height=180`, `RadiusX=50`, `RadiusY=90`

## How This Helps in Daily Use

You can use the HMI page as one working area for common tasks:
- Test live device values.
- Simulate states and alarms.
- Build operator dashboards with widgets.
- Save layouts and reload them for the next shift or project.

Typical workflow:
1. Connect and start monitoring.
2. Add widgets for key registers.
3. Set ranges, labels, and colors.
4. Validate values in runtime mode.
5. Save the dashboard as `.hmi`.

This keeps testing, monitoring, and visualization in one place.

## Related Documentation

- [Widget Reference](widget-reference.md) - Widget properties, defaults, and min/max ranges
- [User Guide](user-guide.md) - Complete XPF documentation
