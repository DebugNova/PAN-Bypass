# PAN ByPass

A Windows desktop application that automates the process of inputting Roblox FFlags into RuntimeFFlagEditor.exe.

## Features

- ✅ Browse and launch RuntimeFFlagEditor.exe
- ✅ JSON-based FFlag input with validation
- ✅ Automated keyboard input simulation
- ✅ Real-time progress tracking
- ✅ FFlag management (Save/Load/Clear)
- ✅ Status logging with timestamps
- ✅ ALT+F4 Roblox quick-close
- ✅ Error handling and validation
- ✅ Persistent configuration storage

## Requirements

- Windows 10/11
- Python 3.12+ (Python 3.8+ should work)
- RuntimeFFlagEditor.exe (or similar tool)

## Installation

### Option 1: Download Executable (Easiest - No Python Required)

1. **Download the latest release**:
   - Go to [Releases](../../releases)
   - Download `PANByPass.exe`
   - Double-click to run - that's it!

> **Note**: Windows Defender might show a warning. Click "More Info" → "Run Anyway". This is a false positive because the app is not digitally signed.

### Option 2: Run from Source (For Developers)

1. **Install Python** (if not already installed)
   - Download from [python.org](https://www.python.org/downloads/)
   - Make sure to check "Add Python to PATH" during installation

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

   Or install individually:
   ```bash
   pip install PySide6 PyAutoGUI pywin32
   ```

3. **Run the app**
   ```bash
   python main.py
   ```

## Quick Start (Windows)

1. **Easy Installation** (Recommended)
   - Double-click `install.bat` to install all dependencies
   - Wait for installation to complete

2. **Run the application**
   - Double-click `run.bat` to start the app
   - Or manually: `python main.py`

## Usage

1. **Launch the application**
   - Double-click `run.bat`
   - Or run in terminal:
   ```bash
   python main.py
   ```

2. **Select RuntimeFFlagEditor.exe**
   - Click "Browse..." button
   - Navigate to your RuntimeFFlagEditor.exe
   - Click "Launch .exe" to start it

3. **Input FFlags (JSON format)**
   ```json
   {
     "FFlagDebugEnableStatsWidget": "true",
     "FFlagDebugGraphicsPreferD3D11": "true",
     "DFIntTaskSchedulerTargetFps": "240"
   }
   ```

4. **Validate JSON**
   - Click "Validate JSON" button
   - Check for any syntax errors
   - Wait for confirmation message

5. **Start Automation**
   - Click "▶ Start Automation"
   - **IMPORTANT**: You have 3 seconds to focus the RuntimeFFlagEditor window
   - Watch the progress bar as FFlags are entered
   - Wait for completion message

6. **FFlag Management**
   - **Save FFlags**: Saves current JSON to `fflags.json`
   - **Load Saved**: Loads previously saved FFlags
   - **Clear All**: Removes all FFlags and saved file

7. **Optional: Close Roblox**
   - Focus Roblox window
   - Click "⚡ ALT+F4 Roblox" button

## File Structure

```
FFlag Bypass/
├── main.py              # Main application
├── requirements.txt     # Python dependencies
├── README.md            # This file
├── plan.md              # Original project plan
├── install.bat          # Easy dependency installer (Windows)
├── run.bat              # Quick launcher (Windows)
├── example_fflags.json  # Sample FFlags for testing
├── config.json          # App configuration (auto-generated)
├── fflags.json          # Saved FFlags (auto-generated)
└── logs/
    └── automation.log   # Application logs (auto-generated)
```

## JSON Format

The application expects FFlags in JSON object format:

```json
{
  "FlagName1": "value1",
  "FlagName2": "value2",
  "FlagName3": "value3"
}
```

**Notes:**
- Keys are FFlag names (strings)
- Values can be strings, numbers, or booleans (all converted to strings)
- Duplicate keys will use the last value
- Nested objects are not supported

## Troubleshooting

### "Target window not active" or automation fails
- Make sure RuntimeFFlagEditor.exe is visible and focused
- Don't move your mouse or type during automation
- Adjust the delay in code if needed (default: 0.15s between actions)

### "Invalid JSON syntax" error
- Check for missing commas, brackets, or quotes
- Use a JSON validator online
- Make sure it's a valid JSON object `{}`

### .exe doesn't launch
- Verify the .exe path is correct
- Check if antivirus is blocking it
- Run the app as administrator

### Automation is too fast/slow
- Edit `main.py` line 53: `self.automation_worker = AutomationWorker(self.current_fflags, delay=0.15)`
- Increase delay for slower systems (e.g., `delay=0.3`)
- Decrease for faster systems (e.g., `delay=0.05`)

## Security

- ✅ No internet connection required
- ✅ All data stored locally
- ✅ No telemetry or tracking
- ✅ Open source - inspect the code yourself

## Error Handling

The app handles:
- Invalid JSON syntax with line/column errors
- Missing .exe paths
- Empty FFlag lists
- Automation interruptions
- File read/write errors
- Process launch failures

## Logs

All actions are logged to:
- `logs/automation.log` (file)
- Status log window (GUI)
- Console output (terminal)

## Future Enhancements

Potential features for future versions:
- Dark mode theme
- Multiple .exe profile support
- Cloud sync for FFlag presets
- Auto-detect Roblox process
- Batch FFlag templates
- Keyboard shortcuts
- Window auto-focus

## Building from Source

Want to build your own executable?

1. **Install PyInstaller**:
   ```bash
   pip install pyinstaller
   ```

2. **Run build script**:
   ```bash
   build_exe.bat
   ```

3. **Find executable**:
   - Located in `dist\FFlagAutomatedApp.exe`
   - See `RELEASE.md` for detailed build instructions

## Credits

Built according to the specifications in `plan.md`

**Tech Stack:**
- Python 3.12+
- PySide6 (Qt6) - GUI framework
- PyAutoGUI - Keyboard automation
- pywin32 - Windows integration
- PyInstaller - Executable bundling

## License

This project is for personal use. Use responsibly and at your own risk.

## Support

For issues or questions:
1. Check the troubleshooting section
2. Review `logs/automation.log`
3. Verify JSON format is correct
4. Ensure RuntimeFFlagEditor.exe is compatible

---

**⚠ Disclaimer:** This tool is designed to automate repetitive tasks. Always ensure you have permission to use automation tools with your target applications.

