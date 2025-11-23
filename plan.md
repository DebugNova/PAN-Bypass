# **PDR — FFlags Automated App**

## **1. Overview**

The *FFlags Automated App* is a Windows desktop application designed to automate the process of inputting and managing Roblox FFlags into an external executable tool (e.g., `RuntimeFFlagEditor.exe`). The application will take a JSON input of FFlags, validate it, and automatically simulate keyboard/CLI inputs to the target `.exe` to populate values correctly.

This app streamlines the entire workflow of:

* Selecting `.exe` path
* Running the `.exe`
* Entering each FFlag name & value
* Validating and showing progress
* Managing (add/edit/clear) FFlags
* Optionally closing Roblox using ALT+F4

---

## **2. Target Platform**

* **Windows 10/11** (Primary)
* Local execution only
* No internet required

---

## **3. Tech Stack Recommendation**

### **Best Choice (Recommended): Python + PySide6 + PyAutoGUI**

**Reason:** Easiest automation for keyboard input, best JSON handling, simple GUI creation, fast to build.

**Components:**

* **Python 3.12+** — main language
* **PySide6 (Qt6)** — modern and clean GUI
* **PyAutoGUI** — simulate type, enter, ALT+F4, etc.
* **Subprocess** — launch `.exe` safely
* **JSON library (built-in)** — validate user JSON
* **Threading** — update progress bar without freezing UI
* **Rich logging** — show status and errors

---

### **Alternate Choice (More advanced): C# (.NET 8) + WPF**

**Reason:** Native Windows feel, very strong automation control using Windows API.

**But development time is longer compared to Python.**

---

## **4. Functional Requirements**

### **4.1 App Flow**

1. **Ask user for the `.exe` path** (file picker recommended)
2. Launch the `.exe` inside a subprocess
3. Show input box for JSON FFlags
4. On pressing "Validate JSON":

   * Check syntax
   * Confirm key:value pairs
   * Detect duplicates
   * Show success/error messages
5. On pressing "Start Automation":

   * For each FFlag key

     * Type the key into the `.exe`
     * Press Enter
     * Type the value
     * Press Enter
   * Update progress bar (0% → 100%)
   * Show final success message
6. Ask user if they want to ALT+F4 Roblox

---

## **4.2 FFlag Management**

### **Add FFlags**

* User enters JSON
* App validates
* App stores internally in a local JSON file

### **Edit FFlags**

* Load previously saved FFlags
* Allow value or key editing
* Overwrite old values on saving

### **Clear FFlags**

* Button to delete stored FFlags
* Confirmation alert

---

## **5. Error Handling**

* Invalid JSON → highlight exact line & error
* Missing `.exe` path → refuse to start automation
* `.exe` crashed or closed → Show emergency stop message
* Timeout if `.exe` is not responding
* If PyAutoGUI loses focus → show warning: "Target window not active"

---

## **6. User Interface (UI Layout)**

### **Top Section**

* Select `.exe` path (browse button)
* Launch `.exe` button

### **Middle Section**

* Large textbox for JSON input
* "Validate JSON" button
* Real-time status log box

### **Bottom Section**

* "Start Automation" (disabled until JSON valid)
* Progress bar
* FFlag management (Add / Edit / Clear)
* "ALT+F4 Roblox" button

---

## **7. Automation Logic**

### **Algorithm**

1. Parse JSON → list of pairs
2. For each (key, value):

   * `pyautogui.typewrite(key)`
   * Press Enter
   * `pyautogui.typewrite(value)`
   * Press Enter
3. Calculate progress per entry:

   * `progress = (index / total) * 100`
   * Update bar

---

## **8. Files & Storage**

* `config.json` → store `.exe` path
* `fflags.json` → store last uploaded FFlags
* `logs/automation.log` → errors and events

---

## **9. Completion Message**

After automation finishes, app will show:

> **"FFlags successfully applied to RuntimeFFlagEditor. No errors detected."**

---

## **10. Security Considerations**

* No online communication
* file paths stored locally
* JSON validated before processing

---

## **11. Future Expansion**

* Support for multiple `.exe` tools
* Auto-detection of Roblox process
* Dark mode / animations
* Cloud sync for FFlags presets

---

## **12. Timeline Estimate (Development)**

| Feature                       | Time     |
| ----------------------------- | -------- |
| GUI                           | 1 day    |
| JSON validation               | 1 hr     |
| EXE launcher                  | 1 hr     |
| Automation engine (PyAutoGUI) | 3–4 hrs  |
| Error handling                | 3 hrs    |
| FFlag management              | 3 hrs    |
| Testing                       | 1–2 days |

**Total:** 3–4 days (fast), or 1 week with polish.

---

## **13. Final Recommendation**

Use **Python + PySide6 + PyAutoGUI** for the fastest and smoothest development.

The app will be fully local, automated, and simple to maintain.
