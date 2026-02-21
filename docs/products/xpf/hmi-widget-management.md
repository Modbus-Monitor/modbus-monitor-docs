# HMI Tab and Widget Management (v5.0.0.0+)

This page explains how to use the HMI tab and manage widgets on the dashboard canvas.

Use this page for workflow and operations. For widget-by-widget behavior and settings, see [Widget Reference](widget-reference.md).

![HMI Dashboard Demo](../../assets/screenshots/xpf/xpf-hmi-demo.webp){ .screenshot-shadow loading="lazy" }
*Example HMI dashboard layout in XPF*

## 1) Open the HMI Dashboard

1. Open the **HMI** tab in the top ribbon.
2. The app navigates to the HMI Dashboard page.
3. Toggle **Edit** to **On** in the Widgets group to enable design operations.

<!-- Screenshot placeholder: xpf-hmi-01-tab-overview.png -->
> Image coming soon...
<!-- Suggested capture: HMI tab selected, Widgets group visible, Edit toggle highlighted -->

## 2) Ribbon Groups in HMI Tab

### Widgets Group

| Control | Function | Notes |
|---|---|---|
| Edit | Toggle edit mode | Must be On to add, remove, or modify widgets |
| Add Widget | Open widget gallery | Choose from all 9 widget types |
| Add | Add default widget | Quick-add action without opening gallery |
| Remove | Delete selected widget | Only active when a widget is selected |
| Delete All | Clear entire dashboard | Removes all widgets from canvas |

### Clipboard Group

| Control | Function | Notes |
|---|---|---|
| Copy | Copy selected widget | Keyboard: Ctrl+C |
| Paste | Paste widget at offset position | Keyboard: Ctrl+V |

### Controls Group

| Control | Function | Notes |
|---|---|---|
| Refresh | Reload current values | Use after importing data or configuration changes |
| Start/Stop | Control monitoring engine | Dashboard updates when monitoring is active |

### Close

| Control | Function |
|---|---|
| Close | Exit HMI dashboard and return to main view |

<!-- Screenshot placeholder: xpf-hmi-02-ribbon-groups.png -->
> Image coming soon...
<!-- Suggested capture: Widgets + Clipboard + Controls groups with labels -->

## 3) Add, Select, Move, Resize, Remove

### Add

1. Turn **Edit** ON.
2. Click **Add Widget** and pick a type.
3. Widget is placed on canvas (default position and size).

### Select

- Click a widget to select it.
- Selected widget is the target for Remove, Copy, and property editing.

### Move and Resize

- Drag selected widget to move it.
- Use resize handle to change width/height.

### Remove

- Click **Remove** (selected widget only), or
- Press **Delete** key in Edit mode.

### Clear Dashboard

- Click **Delete All** to remove every widget.

<!-- Screenshot placeholder: xpf-hmi-03-selection-resize.png -->
> Image coming soon...
<!-- Suggested capture: selected widget showing selection outline and resize handle -->

## 4) Configure Widget Properties

When **Edit** is On, selecting a widget opens the property editor panel on the right.

Recommended configuration sequence:

1. **Monitoring Point**: Select the Modbus register to bind (required for most widgets).
2. **Display Options**: Set labels, titles, and formatting.
3. **Value Range**: Configure minimum/maximum values and units.
4. **Visual Style**: Choose colors, fonts, and layout options.
5. **State Ranges**: Define value-based color zones (for display widgets).
6. **Test**: Toggle Edit off to preview runtime behavior.

**Example**: To configure a Numeric widget for a temperature sensor:
- Set Monitoring Point to register 40001
- Set Label to "Tank Temperature"
- Set Min: 0, Max: 100
- Set Format to "0.0 °C"
- Add state ranges: Blue (0-50), Yellow (50-80), Red (80-100)

**Notes:**
- Text Label and Clock widgets work without register binding.
- Button and Slider widgets require write permissions to function.

<!-- Screenshot placeholder: xpf-hmi-04-property-editor.png -->
> Image coming soon...
<!-- Suggested capture: selected widget + property panel + Monitoring Point row -->

## 5) Copy and Paste Widgets

**To copy a widget:**
1. Ensure Edit mode is On.
2. Select the widget you want to duplicate.
3. Click **Copy** or press Ctrl+C.

**To paste:**
1. With Edit mode still On, click **Paste** or press Ctrl+V.
2. The new widget appears at an offset position with all properties copied.

**What gets copied:**
- All property settings and values
- Visual appearance and styling configuration
- Register bindings and state ranges

**What changes:**
- Widget ID (automatically assigned)
- Position (offset to avoid overlap)

<!-- Screenshot placeholder: xpf-hmi-05-copy-paste.png -->
> Image coming soon...
<!-- Suggested capture: one widget selected, Copy clicked, pasted duplicate visible offset -->

## 6) Save and Load Dashboard Files

Save your dashboard layout to reuse it across sessions or share with your team.

**File formats:**
- `.hmi` — Packaged dashboard including all widgets and image assets
- `.json` — Dashboard layout data only

**To save:**
1. Configure your dashboard with all desired widgets.
2. Use the save command (implementation varies by version).
3. Choose a location and descriptive filename.

**To load:**
- Drag and drop an `.hmi` or `.json` file onto the canvas, or
- Use the load command from the ribbon.

**Best practices:**
- Save dashboard files alongside your Modbus register maps (`.csv`).
- Use consistent naming: `project-name.hmi` + `project-name.csv`.
- Keep backup copies before making major layout changes.

<!-- Screenshot placeholder: xpf-hmi-06-save-load.png -->
> Image coming soon...
<!-- Suggested capture: Save As flow and resulting .hmi file near .csv -->

## Related Documentation

- [Widget Reference](widget-reference.md) — Detailed properties and capabilities for each widget type
- [User Guide](user-guide.md) — Complete XPF documentation including tabs, features, and workflows
