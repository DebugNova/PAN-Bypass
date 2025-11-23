# PAN ByPass v1.0.0

## 📥 Download

**Windows 10/11 (64-bit)**: [PANByPass.exe](https://github.com/YOUR_USERNAME/FFlag-Bypass/releases/download/v1.0.0/PANByPass.exe)

> **File Size**: ~150-250 MB (standalone, no installation required)

## ✨ Features

- ✅ **Automated FFlag Input** - Type FFlags into RuntimeFFlagEditor automatically
- ✅ **JSON Validation** - Detect syntax errors before automation starts
- ✅ **Real-time Progress** - See exactly what's happening with progress bar
- ✅ **FFlag Management** - Save, load, and manage your FFlag configurations
- ✅ **Fast Automation** - Optimized for speed (~0.12s per FFlag)
- ✅ **Error Handling** - Comprehensive error detection and reporting
- ✅ **No Dependencies** - Standalone executable, no Python required

## 🚀 Quick Start

1. **Download** `FFlagAutomatedApp.exe`
2. **Double-click** to run the app
3. **Browse** and select your `RuntimeFFlagEditor.exe`
4. **Paste** your FFlags in JSON format
5. **Validate** and **Start Automation**
6. **Done!** FFlags are entered automatically

## 📖 Documentation

- [README.md](../blob/main/README.md) - Main documentation
- [USAGE_GUIDE.md](../blob/main/USAGE_GUIDE.md) - Detailed step-by-step tutorial
- [Example FFlags](../blob/main/example_fflags.json) - Sample JSON file

## 🖥️ System Requirements

- **OS**: Windows 10/11 (64-bit)
- **RAM**: 2 GB minimum
- **Disk Space**: ~250 MB
- **Required**: RuntimeFFlagEditor.exe

## ⚠️ Windows Defender Warning

Windows might show a security warning because the app is not digitally signed. This is a **false positive**.

**To run the app**:
1. Click "More Info"
2. Click "Run Anyway"

Or add an exception in Windows Defender.

## 📋 Example Usage

```json
{
  "FFlagDebugEnableStatsWidget": "true",
  "FFlagDebugGraphicsPreferD3D11": "true",
  "DFIntTaskSchedulerTargetFps": "240"
}
```

Paste this into the app, validate, and start automation!

## 🐛 Known Issues

None at this time. Report issues [here](../../issues).

## 📝 Changelog

### v1.0.0 (2025-11-23)
- 🎉 Initial release
- ✅ Full automation of FFlag input
- ✅ JSON validation and error reporting
- ✅ Save/Load/Clear FFlag management
- ✅ Progress tracking with status log
- ✅ ALT+F4 Roblox quick-close feature
- ✅ Optimized speed (5x faster than initial version)

## 💻 For Developers

Want to build from source or contribute?

1. Clone the repository
2. Install dependencies: `pip install -r requirements.txt`
3. Run: `python main.py`
4. Build executable: `build_exe.bat`

See [RELEASE.md](../blob/main/RELEASE.md) for build instructions.

## 🤝 Contributing

Contributions are welcome! Please:
1. Fork the repository
2. Create a feature branch
3. Submit a pull request

## 📄 License

This project is for personal use. Use responsibly and at your own risk.

## 🙏 Acknowledgments

- Built with Python, PySide6 (Qt6), and PyAutoGUI
- Packaged with PyInstaller

---

**Enjoy automating your FFlags! 🚀**

If you find this useful, please ⭐ star the repository!

