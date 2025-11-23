# FFlags Automated App - Usage Guide

## Step-by-Step Tutorial

### 1. First Time Setup

#### Install Dependencies
1. Open the project folder
2. Double-click `install.bat`
3. Wait for installation to complete (this may take a few minutes)
4. Close the window when it says "Installation completed successfully!"

#### Troubleshooting Installation
- **"Python is not installed"**: Download and install Python from [python.org](https://www.python.org/downloads/)
  - ✅ Check "Add Python to PATH" during installation
  - Restart your computer after installation
- **"pip install failed"**: Try running Command Prompt as Administrator

---

### 2. Running the Application

#### Method 1: Double-click (Easiest)
1. Double-click `run.bat`
2. The app window will appear

#### Method 2: Command Line
1. Open Command Prompt in the project folder
2. Type: `python main.py`
3. Press Enter

---

### 3. Setting Up RuntimeFFlagEditor

#### Step 1: Select the .exe
1. Click the **"Browse..."** button in section 1
2. Navigate to your RuntimeFFlagEditor.exe location
3. Select the file and click "Open"
4. The path will appear in the text field

#### Step 2: Launch the .exe
1. Click **"Launch .exe"** button
2. The RuntimeFFlagEditor window will open
3. **IMPORTANT**: Keep this window visible on your screen

---

### 4. Preparing Your FFlags

#### Option A: Use Example File
1. Open `example_fflags.json` in a text editor
2. Copy all the contents
3. Paste into the large text box in the app

#### Option B: Write Your Own
Format your FFlags as JSON:

```json
{
  "FlagName1": "value1",
  "FlagName2": "value2",
  "FlagName3": "value3"
}
```

**Rules:**
- Must be valid JSON format
- Keys = FFlag names (in quotes)
- Values = FFlag values (in quotes)
- Separate each pair with commas
- No comma after the last pair

#### Common JSON Mistakes
❌ Missing quotes:
```json
{
  FFlagName: value
}
```

✅ Correct:
```json
{
  "FFlagName": "value"
}
```

❌ Extra comma:
```json
{
  "Flag1": "val1",
  "Flag2": "val2",
}
```

✅ Correct:
```json
{
  "Flag1": "val1",
  "Flag2": "val2"
}
```

---

### 5. Validating Your FFlags

1. After entering your JSON, click **"Validate JSON"**
2. Check the Status Log for validation result
3. If valid: ✓ Green message appears
4. If invalid: ✗ Error message shows the problem

**Fix validation errors:**
- Read the error message carefully
- It tells you the line and column number
- Common issues: missing comma, missing quote, wrong brackets

---

### 6. Running Automation

#### Pre-flight Checklist
- ✅ RuntimeFFlagEditor.exe is running and visible
- ✅ JSON is validated successfully
- ✅ "Start Automation" button is enabled
- ✅ You won't touch the mouse/keyboard during automation

#### Starting Automation
1. Click **"▶ Start Automation"**
2. A confirmation dialog appears
3. Read the information carefully
4. Click **"Yes"** to confirm

#### During Automation
⏱ **3-Second Countdown**: After clicking Yes, you have 3 seconds to:
- Click on the RuntimeFFlagEditor window
- Make sure it's focused (title bar highlighted)
- Keep your hands off keyboard/mouse

🤖 **Automation Running**:
- Progress bar shows completion percentage
- Status log shows each FFlag being processed
- Don't touch anything until it's done!

⚠ **Emergency Stop**:
- Click **"⏹ Stop"** button if something goes wrong
- Automation will halt immediately

#### After Completion
- Success message appears: "FFlags successfully applied..."
- Progress bar shows 100%
- You can now use RuntimeFFlagEditor normally

---

### 7. Managing FFlags

#### Save FFlags for Later
1. Validate your JSON first
2. Click **"💾 Save FFlags"**
3. FFlags are saved to `fflags.json`
4. Load them anytime with **"Load Saved"**

#### Load Previously Saved FFlags
1. Click **"Load Saved"** button
2. Your saved FFlags appear in the text box
3. Validate and use them again

#### Clear All FFlags
1. Click **"🗑 Clear All"** button
2. Confirm the action
3. Text box is cleared
4. Saved file is deleted

---

### 8. Closing Roblox with ALT+F4

This is a convenience feature for closing Roblox quickly.

#### How to Use
1. Make sure Roblox window is visible and focused
2. Click **"⚡ ALT+F4 Roblox"** in the app
3. Confirm the action
4. Roblox will close (as if you pressed ALT+F4 manually)

⚠ **Warning**: This sends ALT+F4 to whatever window is currently focused!
- Double-check Roblox is focused before using
- It will close the active window, so be careful

---

### 9. Understanding the Status Log

The Status Log shows everything happening in the app:

```
[12:34:56] Application started. Select an .exe to begin.
[12:35:12] Selected .exe: C:\...\RuntimeFFlagEditor.exe
[12:35:20] Launched: RuntimeFFlagEditor.exe
[12:35:45] ✓ JSON validated successfully! Found 5 FFlags.
[12:36:00] ⚙ Starting automation...
[12:36:03] [1/5] Typing key: FFlagDebugEnableStatsWidget
[12:36:04] [1/5] Typing value: true
[12:36:05] [2/5] Typing key: FFlagDebugGraphicsPreferD3D11
...
[12:36:20] Automation completed successfully!
```

**Log Symbols:**
- ✓ Success
- ✗ Error
- ⚙ Processing
- 💾 Saved
- 📂 Loaded
- 🗑 Cleared
- ⚡ Action performed

---

### 10. Tips & Best Practices

#### For Best Results
1. **Test with few FFlags first**: Start with 2-3 FFlags to test
2. **Keep windows visible**: Don't minimize RuntimeFFlagEditor during automation
3. **Don't multitask**: Close other apps that might steal focus
4. **Save your work**: Always save FFlags after validation
5. **Check logs**: Review logs if something goes wrong

#### Timing Adjustments
If automation is too fast or too slow:
1. Open `main.py` in a text editor
2. Find line ~53: `AutomationWorker(self.current_fflags, delay=0.15)`
3. Change `delay=0.15` to:
   - Slower: `delay=0.3` or `delay=0.5`
   - Faster: `delay=0.05` or `delay=0.1`
4. Save the file and restart the app

#### Window Focus Issues
If automation types in the wrong window:
- Increase the 3-second countdown (edit line ~318 in main.py)
- Make RuntimeFFlagEditor fullscreen
- Close other apps that might steal focus

---

### 11. Common Issues & Solutions

#### Issue: "Invalid JSON syntax"
**Solution**: Use an online JSON validator like jsonlint.com
- Copy your JSON
- Paste into validator
- Fix the errors shown
- Try again

#### Issue: Automation types in wrong window
**Solution**: 
- Focus RuntimeFFlagEditor immediately after clicking "Yes"
- Increase delay between actions
- Make the window larger/fullscreen

#### Issue: Some FFlags not entered correctly
**Solution**:
- Slow down the automation (increase delay)
- Check RuntimeFFlagEditor is responding
- Try with fewer FFlags at once

#### Issue: Can't find RuntimeFFlagEditor.exe
**Solution**:
- Download it from the official source
- Make sure it's not in a restricted folder (e.g., Program Files)
- Check your antivirus isn't blocking it

#### Issue: "Python is not recognized"
**Solution**:
- Reinstall Python with "Add to PATH" checked
- Restart your computer
- Try running as Administrator

---

### 12. Example Workflow

Here's a complete example from start to finish:

1. ✅ Double-click `install.bat` (first time only)
2. ✅ Double-click `run.bat`
3. ✅ Click "Browse..." and select RuntimeFFlagEditor.exe
4. ✅ Click "Launch .exe"
5. ✅ Paste FFlags JSON into text box:
```json
{
  "FFlagExample1": "true",
  "FFlagExample2": "240"
}
```
6. ✅ Click "Validate JSON"
7. ✅ Click "▶ Start Automation"
8. ✅ Click "Yes" in confirmation dialog
9. ✅ Quickly click RuntimeFFlagEditor window
10. ✅ Wait 10-15 seconds for completion
11. ✅ See success message
12. ✅ Click "💾 Save FFlags" to save for later
13. ✅ Done!

---

### 13. Advanced: Command Line Usage

For advanced users who prefer terminal:

```bash
# Navigate to project folder
cd "C:\Users\YourName\Desktop\FFlag Bypass"

# Run the app
python main.py

# View logs in real-time
type logs\automation.log

# Edit config manually
notepad config.json
```

---

### 14. Keyboard Shortcuts

Currently, the app doesn't have keyboard shortcuts, but you can navigate using:
- **Tab**: Move between fields
- **Enter**: Activate focused button
- **Alt+F4**: Close the app

---

### 15. Getting Help

If you're still having issues:

1. Check `logs/automation.log` for detailed error messages
2. Review this guide again
3. Try with the example file first (`example_fflags.json`)
4. Make sure all software is up to date
5. Verify RuntimeFFlagEditor.exe is compatible

---

## Quick Reference Card

| Action | Steps |
|--------|-------|
| Install | Double-click `install.bat` |
| Run App | Double-click `run.bat` |
| Select EXE | Browse... → Select RuntimeFFlagEditor.exe |
| Launch EXE | Click "Launch .exe" |
| Input FFlags | Paste JSON → "Validate JSON" |
| Start | "▶ Start Automation" → Focus window |
| Save | "💾 Save FFlags" |
| Load | "Load Saved" |
| Clear | "🗑 Clear All" |
| Close Roblox | Focus Roblox → "⚡ ALT+F4 Roblox" |

---

**Happy Automating! 🚀**

