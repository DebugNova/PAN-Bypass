# PAN ByPass v1.0.0 - Initial Release 🎉

## 📥 Download

**[⬇️ Download PANByPass.exe (247 MB)](https://github.com/DebugNova/PAN-Bypass/releases/download/v1.0.0/PANByPass.exe)**

**Platform**: Windows 10/11 (64-bit)
**No Python Required** - Standalone executable!

---

## ✨ What is PAN ByPass?

**PAN ByPass** is a powerful Windows desktop application that automates the process of inputting Roblox FFlags into RuntimeFFlagEditor (or similar tools). Say goodbye to tedious manual entry - let PAN ByPass handle it for you!

### Key Features

✅ **Automated FFlag Input** - Automatically types FFlags into your target editor
✅ **JSON Validation** - Detects syntax errors before you start
✅ **Real-time Progress Tracking** - See exactly what's happening with progress bar
✅ **FFlag Management** - Save, load, and manage your FFlag configurations
✅ **Lightning Fast** - Optimized automation (~0.12s per FFlag)
✅ **Error Handling** - Comprehensive error detection and reporting
✅ **No Dependencies** - Standalone executable, no Python installation needed
✅ **Modern GUI** - Clean, intuitive interface built with Qt

---

## 🚀 Quick Start

### 1. Download & Launch
- Download `PANByPass.exe` from the link above
- Double-click to run (no installation needed)

### 2. Setup Your Editor
- Click **"Browse..."** and select your FFlag editor executable
- Click **"Launch .exe"** to start it

### 3. Add Your FFlags
Paste your FFlags in JSON format:
```json
{
  "FFlagDebugEnableStatsWidget": "true",
  "FFlagDebugGraphicsPreferD3D11": "true",
  "DFIntTaskSchedulerTargetFps": "240"
}
```

### 4. Validate & Run
- Click **"Validate JSON"** to check for errors
- Click **"▶ Start Automation"** to begin
- Watch as PAN ByPass enters all your FFlags automatically!

---

## 📋 Features in Detail

### Automated Input System
- Types FFlags at optimal speed
- Handles special characters correctly
- Updates progress in real-time
- Emergency stop button for safety

### JSON Validation
- Syntax error detection with line numbers
- Duplicate key detection
- Empty value warnings
- Clear error messages

### FFlag Management
- **Save**: Store your FFlag configurations for reuse
- **Load**: Quickly load previously saved FFlags
- **Clear**: Remove all FFlags with confirmation
- Persistent storage between sessions

### User Interface
- **Section 1**: EXE path selection and launch
- **Section 2**: Large JSON input area with syntax highlighting
- **Section 3**: Real-time status log with timestamps
- **Section 4**: Progress bar and automation controls
- **Section 5**: FFlag management and utilities

### Additional Features
- **ALT+F4 Roblox** - Quick-close button for Roblox
- **Status Logging** - Detailed logs saved to `logs/automation.log`
- **Configuration Persistence** - Remembers your settings
- **Example FFlags** - Sample JSON file included

---

## ⚠️ Windows Defender Warning

When you first run `PANByPass.exe`, Windows Defender might show a security warning:

> **"Windows protected your PC"**

**This is a false positive.** The executable is not signed because code signing certificates are expensive.

**To run the app**:
1. Click **"More Info"**
2. Click **"Run Anyway"**

The app is 100% safe, open source, and contains no malware or telemetry.

---

## 📖 Documentation

Comprehensive guides are included in the repository:

- **[README.md](https://github.com/DebugNova/PAN-Bypass/blob/main/README.md)** - Main documentation
- **[USAGE_GUIDE.md](https://github.com/DebugNova/PAN-Bypass/blob/main/USAGE_GUIDE.md)** - Detailed step-by-step tutorial (15 sections)
- **[BUILD_INSTRUCTIONS.md](https://github.com/DebugNova/PAN-Bypass/blob/main/BUILD_INSTRUCTIONS.md)** - How to build from source
- **[example_fflags.json](https://github.com/DebugNova/PAN-Bypass/blob/main/example_fflags.json)** - Sample FFlags for testing

---

## 💻 System Requirements

| Requirement | Specification |
|------------|---------------|
| **Operating System** | Windows 10/11 (64-bit) |
| **RAM** | 2 GB minimum |
| **Disk Space** | ~250 MB |
| **Required** | RuntimeFFlagEditor.exe or similar tool |
| **Internet** | Not required (fully offline) |

---

## 🛠️ Technical Details

### Built With
- **Python 3.13.7** - Core language
- **PySide6 6.10.1** - Modern Qt6 GUI framework
- **PyAutoGUI 0.9.54** - Keyboard automation
- **PyInstaller 6.16.0** - Executable packaging

### Performance Metrics
- **Startup Time**: ~2-3 seconds
- **Memory Usage**: ~150-200 MB
- **Automation Speed**: ~0.12 seconds per FFlag
- **100 FFlags**: ~12 seconds total
- **File Size**: 247 MB (includes Python runtime + Qt framework)

### Security
✅ No internet connection required
✅ No telemetry or tracking
✅ No data collection
✅ Open source code - audit it yourself
✅ All processing happens locally

---

## 📊 Example Workflow

Here's a complete example from start to finish:

```
1. Launch PANByPass.exe
2. Browse and select RuntimeFFlagEditor.exe
3. Click "Launch .exe"
4. Paste your FFlags JSON:
   {
     "FFlagExample1": "true",
     "FFlagExample2": "240",
     "FFlagExample3": "false"
   }
5. Click "Validate JSON" ✓
6. Click "▶ Start Automation"
7. Click "Yes" in confirmation
8. Watch automation complete in ~5 seconds
9. Click "💾 Save FFlags" to save for later
10. Done! 🎉
```

---

## 🐛 Known Issues

None at this time! If you encounter any bugs, please [open an issue](https://github.com/DebugNova/PAN-Bypass/issues).

---

## 🔮 Changelog

### v1.0.0 (November 24, 2025)
- 🎉 **Initial Release**
- ✅ Full automation of FFlag input
- ✅ JSON validation with detailed error reporting
- ✅ Save/Load/Clear FFlag management
- ✅ Real-time progress tracking
- ✅ Status logging with timestamps
- ✅ ALT+F4 Roblox quick-close
- ✅ Optimized speed (5x faster than initial development version)
- ✅ Custom icon and branding
- ✅ Comprehensive documentation
- ✅ Example FFlags included

---

## 🤝 Contributing

Want to contribute? Great!

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

---

## 💬 Support & Community

Need help? Here's how to get support:

1. **Read the docs**: Check [USAGE_GUIDE.md](https://github.com/DebugNova/PAN-Bypass/blob/main/USAGE_GUIDE.md)
2. **Check logs**: Review `logs/automation.log` for errors
3. **Open an issue**: [Report bugs or request features](https://github.com/DebugNova/PAN-Bypass/issues)
4. **Discussions**: Join the [Discussions tab](https://github.com/DebugNova/PAN-Bypass/discussions) for questions

---

## 📜 License

This project is licensed under the **MIT License** - see the [LICENSE](https://github.com/DebugNova/PAN-Bypass/blob/main/LICENSE) file for details.

**TL;DR**: You can use, modify, and distribute this software freely. Just keep the copyright notice.

---

## 🙏 Acknowledgments

- Built with love using Python, PySide6, and PyAutoGUI
- Packaged with PyInstaller for easy distribution
- Inspired by the need to automate repetitive tasks
- Thanks to the open source community!

---

## ⭐ Show Your Support

If you find PAN ByPass useful:

1. ⭐ **Star this repository** on GitHub
2. 🐦 **Share it** with others who might benefit
3. 🐛 **Report bugs** to help improve it
4. 💡 **Suggest features** you'd like to see

---

## 📞 Contact

**Project Maintainer**: DebugNova
**Repository**: [https://github.com/DebugNova/PAN-Bypass](https://github.com/DebugNova/PAN-Bypass)
**Issues**: [https://github.com/DebugNova/PAN-Bypass/issues](https://github.com/DebugNova/PAN-Bypass/issues)

---

## 🎯 What's Next?

Stay tuned for future updates! Potential features:

- 🌙 Dark mode theme
- 📦 Multiple editor profile support
- ☁️ Cloud sync for FFlag presets
- 🔍 Auto-detect Roblox process
- 📝 FFlag templates and presets
- ⌨️ Keyboard shortcuts
- 🪟 Auto-focus target window
- 🌐 Multi-language support

---

**Enjoy using PAN ByPass! 🚀**

*Automate the boring stuff, focus on what matters.*

---

*Made with ❤️ by DebugNova | Built for the Roblox community*

