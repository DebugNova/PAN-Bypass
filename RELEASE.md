# FFlags Automated App - Release Guide

## Building the Executable

### Prerequisites
- Windows 10/11
- Python 3.8 or higher installed
- All dependencies installed (`pip install -r requirements.txt`)

### Build Steps

1. **Install PyInstaller** (if not already installed):
   ```bash
   pip install pyinstaller
   ```

2. **Run the build script**:
   - Double-click `build_exe.bat`
   - OR run in terminal: `build_exe.bat`

3. **Wait for build** (takes 2-5 minutes):
   - PyInstaller will analyze dependencies
   - Bundle all required files
   - Create standalone executable

4. **Find your executable**:
   - Location: `dist\FFlagAutomatedApp.exe`
   - Size: ~150-250 MB (includes Python runtime + Qt)

### Testing the Executable

1. Navigate to `dist` folder
2. Double-click `FFlagAutomatedApp.exe`
3. App should launch without requiring Python installation
4. Test all features (Browse, Launch, Validate, Automate)

### Distribution

#### Option 1: GitHub Release (Recommended)

1. **Create a release on GitHub**:
   ```bash
   git tag v1.0.0
   git push origin v1.0.0
   ```

2. **Upload the executable**:
   - Go to GitHub → Releases → Create new release
   - Upload `dist\FFlagAutomatedApp.exe`
   - Add release notes

3. **Add these to release notes**:
   ```markdown
   ## FFlags Automated App v1.0.0
   
   ### Download
   - **Windows 10/11**: [FFlagAutomatedApp.exe](link-to-file)
   
   ### Features
   - ✅ Automated FFlag input for RuntimeFFlagEditor
   - ✅ JSON validation and management
   - ✅ Real-time progress tracking
   - ✅ No Python installation required
   
   ### How to Use
   1. Download `FFlagAutomatedApp.exe`
   2. Double-click to run
   3. Select your RuntimeFFlagEditor.exe
   4. Input FFlags as JSON
   5. Click Start Automation
   
   ### System Requirements
   - Windows 10/11 (64-bit)
   - ~250 MB disk space
   - RuntimeFFlagEditor.exe
   
   ### Note
   - Windows Defender might flag it (false positive)
   - Add exception or click "More Info" → "Run Anyway"
   ```

#### Option 2: Direct Download

1. Compress the executable:
   ```bash
   # Create a zip file
   Compress-Archive -Path dist\FFlagAutomatedApp.exe -DestinationPath FFlagAutomatedApp-v1.0.0.zip
   ```

2. Upload to GitHub repository:
   - Place in a `releases` folder
   - Link in README.md

3. Update README with download link

### File Structure for GitHub

```
FFlag-Bypass/
├── dist/
│   └── FFlagAutomatedApp.exe    # The built executable
├── main.py                      # Source code
├── requirements.txt             # Python dependencies
├── build_exe.bat                # Build script
├── FFlagAutomatedApp.spec       # PyInstaller config
├── README.md                    # Documentation
├── RELEASE.md                   # This file
├── USAGE_GUIDE.md               # User guide
├── example_fflags.json          # Example FFlags
└── .gitignore                   # Git ignore file
```

### .gitignore Additions

Make sure these are in your `.gitignore`:
```
# PyInstaller
build/
dist/
*.spec
__pycache__/
*.pyc
```

### Common Issues

#### "Windows protected your PC"
- This is Windows SmartScreen
- Click "More Info" → "Run Anyway"
- Or: Right-click → Properties → Unblock

#### "Not a valid Win32 application"
- Rebuild on the same architecture (64-bit vs 32-bit)
- Ensure PyInstaller matches Python architecture

#### Antivirus Detection
- PyInstaller executables sometimes trigger false positives
- Submit to antivirus vendors as false positive
- Users can add exception

#### Large File Size
- This is normal (150-250 MB)
- Includes Python runtime + Qt framework
- For smaller size, use `--onedir` instead of `--onefile`

### Alternative Build (Smaller Distribution)

For a folder-based distribution (smaller initial download):

```bash
pyinstaller --name="FFlagAutomatedApp" ^
    --windowed ^
    --add-data "example_fflags.json;." ^
    --collect-all PySide6 ^
    main.py
```

This creates a folder in `dist/FFlagAutomatedApp/` with:
- Main .exe (smaller, ~5-10 MB)
- Support DLLs and files
- Users run the .exe from this folder

### Version Numbering

Update version in `main.py`:
```python
__version__ = "1.0.0"
```

And in window title:
```python
self.setWindowTitle(f"FFlags Automated App - PDR v{__version__}")
```

### Continuous Releases

For automated builds, consider:
- GitHub Actions workflow
- Automatic version bumping
- Release on tag push

Example `.github/workflows/build.yml`:
```yaml
name: Build EXE
on:
  push:
    tags:
      - 'v*'
jobs:
  build:
    runs-on: windows-latest
    steps:
      - uses: actions/checkout@v3
      - uses: actions/setup-python@v4
        with:
          python-version: '3.11'
      - run: pip install -r requirements.txt
      - run: build_exe.bat
      - uses: actions/upload-artifact@v3
        with:
          name: FFlagAutomatedApp
          path: dist/FFlagAutomatedApp.exe
```

### Signing the Executable (Optional)

For production releases:
1. Get a code signing certificate
2. Sign with `signtool.exe`
3. Reduces false positive detections

### Support

If users report issues:
1. Check if they're running on Windows 10/11
2. Verify antivirus isn't blocking it
3. Test on clean Windows VM
4. Provide Python script as alternative

---

## Quick Build Command

```bash
# Install PyInstaller
pip install pyinstaller

# Build
build_exe.bat

# Test
cd dist
FFlagAutomatedApp.exe

# Distribute
# Upload dist\FFlagAutomatedApp.exe to GitHub Releases
```

---

**Ready to distribute! 🚀**

