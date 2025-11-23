# How to Build the Executable

This guide will help you create `FFlagAutomatedApp.exe` from the source code.

## Prerequisites

✅ Windows 10 or 11
✅ Python 3.8 or higher installed
✅ Git (optional, for cloning)

## Step-by-Step Build Process

### 1. Install Dependencies

Open Command Prompt or PowerShell in the project directory:

```bash
pip install -r requirements.txt
```

This installs:
- PySide6 (GUI framework)
- PyAutoGUI (automation)
- pywin32 (Windows integration)
- PyInstaller (executable builder)

### 2. Build the Executable

#### Method A: Using the Build Script (Easiest)

Double-click `build_exe.bat` or run:

```bash
build_exe.bat
```

Wait 2-5 minutes for the build to complete.

#### Method B: Manual PyInstaller Command

```bash
pyinstaller --name="FFlagAutomatedApp" --onefile --windowed --add-data "example_fflags.json;." --collect-all PySide6 main.py
```

#### Method C: Using the Spec File

```bash
pyinstaller FFlagAutomatedApp.spec
```

### 3. Locate the Executable

After successful build, find your executable at:

```
dist/FFlagAutomatedApp.exe
```

### 4. Test the Executable

1. Navigate to the `dist` folder
2. Double-click `FFlagAutomatedApp.exe`
3. The app should launch without errors
4. Test all features

## Build Options Explained

### --onefile
Creates a single `.exe` file (~150-250 MB)
- **Pros**: Easy to distribute, one file
- **Cons**: Larger file size, slightly slower startup

### --windowed
No console window appears (GUI only)
- Remove this flag if you want to see console output for debugging

### --add-data
Includes `example_fflags.json` in the executable
- Users can access the example file

### --collect-all PySide6
Ensures all PySide6 (Qt) components are included
- Required for the GUI to work properly

## Build Configurations

### Standard Build (Recommended)
Single file, no console, includes example file:
```bash
pyinstaller --name="FFlagAutomatedApp" --onefile --windowed --add-data "example_fflags.json;." --collect-all PySide6 main.py
```

### Debug Build
With console for debugging:
```bash
pyinstaller --name="FFlagAutomatedApp" --onefile --add-data "example_fflags.json;." --collect-all PySide6 main.py
```

### Folder-Based Build
Smaller main .exe with separate DLLs:
```bash
pyinstaller --name="FFlagAutomatedApp" --windowed --add-data "example_fflags.json;." --collect-all PySide6 main.py
```
Output: `dist/FFlagAutomatedApp/` folder with .exe inside

## Troubleshooting

### "PyInstaller is not recognized"
```bash
pip install pyinstaller
```

### "Failed to execute script"
- Add `--debug=all` flag to see detailed errors
- Check if all imports are included
- Try rebuilding with `--onedir` instead

### Antivirus Blocks Build
- Temporarily disable antivirus
- Add exception for the project folder
- This is a false positive

### Missing DLL Errors
- Reinstall PySide6: `pip uninstall PySide6 && pip install PySide6`
- Use `--collect-all PySide6` flag

### Large File Size (>300 MB)
This is normal. The executable includes:
- Python runtime (~30 MB)
- Qt framework (~150 MB)
- PyAutoGUI and dependencies (~20 MB)
- Your code and resources (~1 MB)

To reduce size:
- Use `--onedir` (folder distribution)
- Use UPX compression: `--upx-dir=path/to/upx`

## Advanced Options

### Add an Icon
```bash
pyinstaller --icon=icon.ico --name="FFlagAutomatedApp" --onefile --windowed --add-data "example_fflags.json;." --collect-all PySide6 main.py
```
(You'll need to create/download an `icon.ico` file first)

### Enable UPX Compression
Download UPX from https://upx.github.io/ and:
```bash
pyinstaller --upx-dir=C:\path\to\upx --name="FFlagAutomatedApp" --onefile --windowed --add-data "example_fflags.json;." --collect-all PySide6 main.py
```

### Version Info (Windows)
Create a `version.txt` file and use:
```bash
pyinstaller --version-file=version.txt --name="FFlagAutomatedApp" --onefile --windowed --add-data "example_fflags.json;." --collect-all PySide6 main.py
```

## Clean Build

If you need to rebuild from scratch:

```bash
# Remove old build files
rmdir /s /q build dist
del *.spec

# Rebuild
pyinstaller --name="FFlagAutomatedApp" --onefile --windowed --add-data "example_fflags.json;." --collect-all PySide6 main.py
```

## GitHub Release Preparation

1. **Build the executable**:
   ```bash
   build_exe.bat
   ```

2. **Test thoroughly**:
   - Run from `dist/` folder
   - Test all features
   - Check on clean Windows VM

3. **Create ZIP (optional)**:
   ```bash
   Compress-Archive -Path dist\FFlagAutomatedApp.exe -DestinationPath FFlagAutomatedApp-v1.0.0.zip
   ```

4. **Upload to GitHub**:
   - Create a new release
   - Upload the .exe (or .zip)
   - Add release notes from `.github/release_template.md`

## Build Time Comparison

| Method | Time | Output |
|--------|------|--------|
| First build | 3-5 min | dist/FFlagAutomatedApp.exe (~200 MB) |
| Rebuild (no changes) | 1-2 min | Same |
| Folder build | 2-3 min | dist/FFlagAutomatedApp/ (~250 MB folder) |

## Distribution Checklist

Before releasing:
- ✅ Build completes without errors
- ✅ .exe launches on your machine
- ✅ All features work (Browse, Launch, Validate, Automate)
- ✅ Test on clean Windows VM (no Python installed)
- ✅ Antivirus scan (VirusTotal.com)
- ✅ File size reasonable (<300 MB)
- ✅ Version number updated in code
- ✅ Release notes prepared
- ✅ README.md updated with download link

## Need Help?

- Check PyInstaller docs: https://pyinstaller.org/
- Review the spec file: `FFlagAutomatedApp.spec`
- Enable debug mode: `--debug=all`
- Check build logs in `build/` folder

---

**Happy Building! 🔨**

