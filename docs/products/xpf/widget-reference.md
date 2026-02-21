# Widget Reference (v5.0.0.0+)

This page documents the 9 widgets available from the HMI tab gallery.

Use this page for widget-specific details. For HMI tab operations (edit/add/remove/copy/start/save), see [HMI Tab and Widget Management](hmi-widget-management.md).

## Widget List

| # | Widget | Register Binding | Primary Purpose | Write Capability |
|---|---|---|---|---|
| 1 | Numeric | Required | Numeric display with status styling | No |
| 2 | Button | Required | Command/write action from dashboard | Yes |
| 3 | Dial180 | Required | Analog-style gauge with 180° sweep | No |
| 4 | Text Label | Optional | Static/dynamic text block | Optional (binding-dependent) |
| 5 | Clock | Not required | System time display | No |
| 6 | Slider | Required | Value display + interactive write slider | Yes |
| 7 | MultiState Indicator | Required | State color/image by value range | No |
| 8 | Bar Graph | Required | Directional fill level visualization | No |
| 9 | Trend | Required | Real-time trend/chart visualization | Typically advanced tier |

<!-- Screenshot placeholder: xpf-hmi-10-widget-gallery-all-9.png -->
<!-- Suggested capture: Add Widget gallery open, all 9 items visible -->

## Quick Capability Matrix

| Widget | Supports state ranges | Supports images in states | JSON save/load | Typical use |
|---|---|---|---|---|
| Numeric | Yes | No | Yes | Compact process values |
| Button | No | No | Yes | Start/stop, mode, write command |
| Dial180 | Yes | No | Yes | Operator-friendly analog display |
| Text Label | No | No | Yes | Labels, headers, notes |
| Clock | No | No | Yes | Time context on dashboard |
| Slider | No | No | Yes | Setpoint writing |
| MultiState Indicator | Yes | Yes | Yes | Discrete/zone status |
| Bar Graph | Yes | Yes | Yes | Tank/level/load bars |
| Trend | Yes | Yes | Yes | Time-series monitoring |

## Per-Widget Details

### 1) Numeric

Displays a single numeric value with customizable formatting and color-coded status indicators.

**Key features:**
- Large, readable numeric display
- Value-based color states (e.g., blue = normal, red = high)
- Optional label and unit text
- Decimal precision control
- Min/max range configuration

**Best for:**
- Process values (temperature, pressure, flow rate)
- Sensor readings requiring clear numeric display
- Status values where color context aids interpretation

**Configuration essentials:**
- **Monitoring Point**: Required - select the register to display
- **Min/Max**: Define expected value range
- **Format String**: Control decimal places (e.g., "0.00" for two decimals)
- **State Ranges**: Assign colors to value zones (optional but recommended)

<!-- Screenshot placeholder: xpf-hmi-11-widget-numeric.png -->

### 2) Button

Interactive control for sending write commands to a Modbus register.

**Key features:**
- Click to write a predefined value
- Customizable button label
- Visual feedback on click
- Supports momentary or toggle behavior

**Best for:**
- Start/stop commands
- Mode switching (Auto/Manual/Off)
- Reset signals
- Enable/disable operations

**Configuration essentials:**
- **Monitoring Point**: Required - the register to write to
- **Write Value**: The value sent when button is clicked
- **Button Label**: Descriptive text (e.g., "Start Pump", "Reset Alarm")
- **Write Mode**: Configure momentary vs sustained write

**Important:** Button widgets require write permissions. Verify your license tier and runtime configuration support write operations.

<!-- Screenshot placeholder: xpf-hmi-12-widget-button.png -->

### 3) Dial180

Semi-circular analog-style gauge providing intuitive visual indication of value position within a range.

**Key features:**
- 180-degree sweep arc
- Colored range zones on dial face
- Moving needle indicator
- Min/max labels and tick marks
- Center value display (optional)

**Best for:**
- Operator-friendly dashboards
- Values where "low-medium-high" zones matter (RPM, pressure, load)
- Mimicking traditional panel meters

**Configuration essentials:**
- **Monitoring Point**: Required - register to visualize
- **Min/Max**: Defines the dial's scale endpoints
- **State Ranges**: Color zones on the dial (e.g., green 0-70%, yellow 70-90%, red 90-100%)
- **Orientation**: Some variants support left/center/right needle starting positions

<!-- Screenshot placeholder: xpf-hmi-13-widget-dial180.png -->

### 4) Text Label

Flexible text display for adding context, instructions, or dynamic values to your dashboard.

**Key features:**
- Static or dynamic text content
- Optional register binding for live text updates
- Font, size, and color customization
- Multi-line support
- Background and border styling

**Best for:**
- Section headers ("Mixing Tank", "Zone 1 Pumps")
- Instructions ("Press Reset After Alarm")
- Units or context hints ("PSI", "Setpoint Range: 0-100")
- Dynamic status text bound to register values

**Configuration essentials:**
- **Text Content**: The label to display
- **Monitoring Point**: Optional - bind to register for dynamic updates
- **Font**: Choose size and style for readability
- **Alignment**: Left, center, or right

<!-- Screenshot placeholder: xpf-hmi-14-widget-text-label.png -->

### 5) Clock

Displays system time without requiring Modbus configuration.

**Key features:**
- Real-time clock display
- Multiple format options (12-hour, 24-hour)
- Date display options
- No register binding needed
- Automatic updates

**Best for:**
- Providing time context on dashboards
- Shift timing reference
- Timestamping dashboard snapshots

**Configuration essentials:**
- **Format**: Choose time/date format
- **Style**: Select font and size for visibility
- **Position**: Typically placed at top or corner of dashboard

<!-- Screenshot placeholder: xpf-hmi-15-widget-clock.png -->

### 6) Slider

Interactive control that both displays current value and allows operator adjustment via drag.

**Key features:**
- Live value display with draggable slider
- Write value on drag or release
- Min/max range enforcement
- Step increment control
- Horizontal or vertical orientation

**Best for:**
- Setpoint adjustment (temperature target, speed reference)
- Manual override controls
- Calibration and tuning interfaces

**Configuration essentials:**
- **Monitoring Point**: Required - register to read and write
- **Min/Max**: Slider range limits
- **Step Size**: Increment per drag position (e.g., 0.1, 1, 10)
- **Write Behavior**: Update on drag or on release

**Important:** Slider widgets require write permissions. Confirm license tier and write mode are enabled.

<!-- Screenshot placeholder: xpf-hmi-16-widget-slider.png -->

### 7) MultiState Indicator

Visual indicator that changes color or image based on which value range the current reading falls within.

**Key features:**
- Value-based state switching
- Color or image display per state
- Unlimited state definitions
- Text label per state (e.g., "Running", "Stopped", "Fault")
- Smooth or instant transitions

**Best for:**
- Discrete status indication (running/stopped, online/offline)
- Alarm annunciation (normal/warning/critical)
- Mode displays (auto/manual/maintenance)

**Configuration essentials:**
- **Monitoring Point**: Required - register determining state
- **State Ranges**: Define min/max boundaries, color, and label for each state
- **Default State**: Color/image when value doesn't match any range
- **Images** (optional): Assign custom images per state

<!-- Screenshot placeholder: xpf-hmi-17-widget-multistate.png -->

### 8) Bar Graph

Vertical or horizontal fill-level indicator with optional color zones and imagery.

**Key features:**
- Directional fill (bottom-up, top-down, left-right, right-left)
- Color ranges along fill path
- Optional background or overlay images
- Percentage or absolute value display
- Scale markings

**Best for:**
- Tank levels
- Battery charge indication
- Load percentages (motor, network, CPU)
- Progress or completion tracking

**Configuration essentials:**
- **Monitoring Point**: Required - value to visualize
- **Min/Max**: Full empty to full scale
- **Orientation**: Vertical or horizontal
- **Direction**: Fill direction within orientation
- **State Ranges**: Color zones (e.g., red=low, yellow=medium, green=full)

<!-- Screenshot placeholder: xpf-hmi-18-widget-bargraph.png -->

### 9) Trend

Real-time scrolling chart displaying historical values over time.

**Key features:**
- Time-series line chart
- Configurable time window (1 min, 5 min, 1 hour, etc.)
- Min/max Y-axis scaling
- Grid and axis labels
- Color-coded range zones (optional)

**Best for:**
- Process trend monitoring (temperature curves, pressure changes)
- Troubleshooting transient events
- Verifying control loop stability
- Historical pattern analysis

**Configuration essentials:**
- **Monitoring Point**: Required - value to chart over time
- **Time Window**: How much history to display
- **Y-Axis Min/Max**: Chart scale
- **Update Rate**: How often to sample the value
- **State Ranges**: Highlight operating zones on chart background

<!-- Screenshot placeholder: xpf-hmi-19-widget-trend.png -->

## Widget Availability by License Tier

Some widgets require higher license tiers to use.

**Available in all license tiers:**
- Numeric
- Text Label  
- Clock

**Requires Basic license or higher:**
- MultiState Indicator
- Dial180
- Bar Graph

**Requires Pro license or higher:**
- Button (write operations)
- Slider (write operations)

**Requires advanced licensing:**
- Trend (typically Enterprise tier)

The Add Widget gallery automatically shows only the widgets available for your active license tier. Widgets requiring a higher tier will not appear in the list.

## Related Documentation

- [HMI Tab and Widget Management](hmi-widget-management.md) — How to add, configure, and manage widgets
- [User Guide](user-guide.md) — Complete XPF feature documentation
- [Quick Start Guide](quick-start.md) — Get started with XPF in 5 minutes
