# Modbus Monitor XPF - Quick Start

!!! success "5-Minute Setup Guide"
    Get started with Modbus Monitor XPF in just 5 minutes! Perfect for first-time users.

[TOC]

## 🎯 What You'll Accomplish

By the end of this guide, you'll have:

    ✅ **Installed** Modbus Monitor XPF
    ✅ **Connected** to your first Modbus device  
    ✅ **Monitored** real-time data
    ✅ **Configured** basic monitoring points

## ⚡ Step 1: Install XPF (2 minutes)

=== "Microsoft Store (Easiest)"

    1. **Open** Microsoft Store on Windows
    2. **Search** for "Modbus Monitor XPF"  
    3. **Click** Install
    4. **Launch** from Start Menu
    
    [:material-microsoft-windows: Open in Store](ms-windows-store://pdp/?productid=9PG862WL5HSM){ .md-button .md-button--primary }

=== "Direct Download"

    1. **Visit** [Download Page](https://quantumbitsolutions.com/purchase/)
    2. **Download** executable file
    3. **Run** the downloaded file
    4. **Start** using immediately (portable version)

## 🔌 Step 2: First Connection (2 minutes)

### For TCP/IP Devices

1. **Go to** Client tab in XPF ribbon
2. **Set Interface** to "TCP"
3. **Enter IP Address** of your Modbus device (e.g., `192.168.1.100`)
4. **Set Port** to `502` (standard Modbus port)
5. **Click** Start button

![TCP Connection Setup](../../assets/screenshots/xpf/xpf-tcp-setup.png)

### For Serial Devices

1. **Go to** Client tab in XPF ribbon  
2. **Set Interface** to "Serial"
3. **Select COM Port** (e.g., COM1, COM3)
4. **Configure** baud rate (typically 9600 or 19200)
5. **Click** Start button

## 📊 Step 3: Add Monitor Points (1 minute)

### Using the Modbus Wizard (Recommended)

1. **Click** "Modbus Wizard" in Home tab
2. **Select** "Add new monitor point"
3. **Choose** Modbus function:
   - **Holding Registers** (most common) - Function 3
   - **Input Registers** - Function 4
   - **Coils** - Function 1
   - **Discrete Inputs** - Function 2
4. **Enter** starting address (e.g., 40001)
5. **Click** OK

### Manual Entry (Alternative)

| Field | Example Value | Description |
|-------|---------------|-------------|
| **Name** | Temperature Sensor | Descriptive name |
| **Address** | 400001 | First holding register |  
| **Unit ID** | 1 | Slave device ID |
| **Data Type** | INT16 | 16-bit signed integer |

## ✅ Step 4: Monitor Live Data

1. **Click** Start button (chain link icon) in Client tab
2. **Watch** the Value column update with live data
3. **Green values** = successful reads
4. **Red borders** = communication errors

![Live Data Monitoring](../../assets/screenshots/xpf/xpf-live-monitoring.png)

## 🚀 Quick Success Checklist

- [ ] **Connection Status**: No red borders in Value column
- [ ] **Live Updates**: Values changing/updating regularly  
- [ ] **Correct Data**: Values make sense for your device
- [ ] **Stable Communication**: No timeout errors

## 🔧 Common Quick Fixes

### "Connection Refused" Error
- ✅ **Check IP Address**: Verify device IP is correct
- ✅ **Check Port**: Ensure port 502 is correct  
- ✅ **Network**: Ping the device IP address
- ✅ **Firewall**: Temporarily disable Windows firewall

### "Timeout" Errors  
- ✅ **Increase Timeout**: Go to Client tab → Timeout → set to 5000ms
- ✅ **Check Cables**: Verify physical connections
- ✅ **Device Power**: Ensure Modbus device is powered on

### Wrong Values Displayed
- ✅ **Check Data Type**: Try UINT16 instead of INT16
- ✅ **Check Swap Type**: Try different byte order options
- ✅ **Verify Address**: Confirm register addresses with device manual

### Serial Port Issues
- ✅ **COM Port**: Verify correct port in Device Manager
- ✅ **Baud Rate**: Match device configuration (9600, 19200, etc.)
- ✅ **Parity/Stop Bits**: Match device settings exactly

## 🎉 What's Next?

Now that you have basic monitoring working:

### Immediate Next Steps
1. **📊 [Add More Points](user-guide.md#monitor-points-configuration)** - Monitor additional registers
2. **📈 [Enable Charting](user-guide.md#chart-visualization)** - See data trends over time
3. **💾 [Save Configuration](user-guide.md#file-operations)** - Preserve your setup
4. **🧩 [Use HMI Widgets](hmi-widget-management.md)** - Build HMI dashboard layouts
5. **📘 [Widget Reference](widget-reference.md)** - Configure all 9 widgets

### Advanced Features to Explore  
- **🧙‍♂️ [Advanced Wizard](user-guide.md#modbus-wizard)** - Complex configurations
- **🌐 [Online Maps](user-guide.md#online-maps-feature)** - Download pre-built device maps
- **🖥️ [Server Mode](user-guide.md#modbus-server-operations)** - Simulate Modbus devices
- **📝 [Logging & Export](user-guide.md#events-and-communication-log)** - Data analysis and reporting

### Get Help
- 📖 **[Complete User Guide](user-guide.md)** - Comprehensive documentation
- 🎥 **[Video Tutorials](https://www.youtube.com/@ModbusMonitor/videos)** - Step-by-step videos
- 💬 **[Community Forum](https://quantumbitsolutions.com/forums/)** - Ask questions and get help

## 🎯 Common Use Cases

### Industrial Monitoring
```yaml
Scenario: Monitor PLC data  
Address: 400001-400010
Data: Production counters, temperatures, pressures
Update Rate: Every 1 second
```

### Energy Management  
```yaml
Scenario: Power meter monitoring
Address: 300001-300020  
Data: Voltage, current, power, energy
Update Rate: Every 5 seconds
```

### Building Automation
```yaml
Scenario: HVAC system monitoring
Address: 400100-400150
Data: Temperature setpoints, valve positions
Update Rate: Every 30 seconds  
```

!!! tip "Pro Tip"
    **Start simple!** Get one register reading successfully, then add more complexity. The Modbus Wizard makes it easy to add points without manual address calculation.

---

**🎉 Congratulations!** You've successfully set up Modbus Monitor XPF and are monitoring live data. You're now ready to explore the advanced features and customize your monitoring solution.
