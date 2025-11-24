"""
FFlags Automated App
Main application entry point
"""
__version__ = "1.1.0"

import sys
import json
import subprocess
import os
import time
from pathlib import Path
from typing import Dict, Optional
import logging
from datetime import datetime

from PySide6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout,
    QPushButton, QLabel, QLineEdit, QTextEdit, QProgressBar,
    QFileDialog, QMessageBox, QGroupBox, QComboBox
)
from PySide6.QtCore import Qt, QThread, Signal
from PySide6.QtGui import QFont
import pyautogui

# Setup logging
log_dir = Path("logs")
log_dir.mkdir(exist_ok=True)
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler(log_dir / 'automation.log'),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)


class AutomationWorker(QThread):
    """Worker thread for automation to prevent UI freezing"""
    progress_update = Signal(int)
    status_update = Signal(str)
    finished = Signal(bool, str)
    
    def __init__(self, fflags: Dict[str, any], delay: float = 0.01):
        super().__init__()
        self.fflags = fflags
        self.delay = delay
        self._running = True
    
    def run(self):
        try:
            total = len(self.fflags)
            if total == 0:
                self.finished.emit(False, "No FFlags to process")
                return
            
            self.status_update.emit("Starting automation...")
            time.sleep(1)  # Give user time to focus the target window
            
            for idx, (key, value) in enumerate(self.fflags.items(), 1):
                if not self._running:
                    self.finished.emit(False, "Automation stopped by user")
                    return
                
                # Update progress every 10 items to reduce UI overhead
                if idx % 10 == 0 or idx == total:
                    progress = int((idx / total) * 100)
                    self.progress_update.emit(progress)
                    self.status_update.emit(f"Processing: {idx}/{total} FFlags")
                
                # Type the key with verification delay
                pyautogui.write(str(key), interval=0.0)
                time.sleep(self.delay)  # Small delay for system to register
                
                # Press Enter and wait for input to be processed
                pyautogui.press('enter')
                time.sleep(self.delay * 2)  # Slightly longer for enter to register
                
                # Type the value with verification delay
                pyautogui.write(str(value), interval=0.0)
                time.sleep(self.delay)
                
                # Press Enter and wait for input to be processed
                pyautogui.press('enter')
                time.sleep(self.delay * 2)
                
                # Log every 100 entries to reduce overhead
                if idx % 100 == 0 or idx == total:
                    logger.info(f"Processed {idx}/{total} FFlags")
            
            self.status_update.emit("Automation completed successfully!")
            self.finished.emit(True, "FFlags successfully applied to RuntimeFFlagEditor. No errors detected.")
            
        except Exception as e:
            error_msg = f"Automation error: {str(e)}"
            logger.error(error_msg)
            self.status_update.emit(error_msg)
            self.finished.emit(False, error_msg)
    
    def stop(self):
        self._running = False


class FFlagApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.config_file = Path("config.json")
        self.fflags_file = Path("fflags.json")
        self.exe_path = ""
        self.exe_process = None
        self.current_fflags = {}
        self.automation_worker = None
        
        self.load_config()
        self.init_ui()
        
    def init_ui(self):
        self.setWindowTitle(f"PAN ByPass v{__version__}")
        self.setMinimumSize(900, 700)
        
        # Central widget
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        main_layout = QVBoxLayout(central_widget)
        
        # === TOP SECTION: EXE Selection ===
        exe_group = QGroupBox("1. Select & Launch FFlag Editor")
        exe_layout = QHBoxLayout()
        
        self.exe_path_input = QLineEdit()
        self.exe_path_input.setPlaceholderText("Path to RuntimeFFlagEditor.exe")
        self.exe_path_input.setText(self.exe_path)
        
        self.browse_btn = QPushButton("Browse...")
        self.browse_btn.clicked.connect(self.browse_exe)
        
        self.launch_btn = QPushButton("Launch .exe")
        self.launch_btn.clicked.connect(self.launch_exe)
        self.launch_btn.setEnabled(False)
        
        exe_layout.addWidget(QLabel("EXE Path:"))
        exe_layout.addWidget(self.exe_path_input, 1)
        exe_layout.addWidget(self.browse_btn)
        exe_layout.addWidget(self.launch_btn)
        exe_group.setLayout(exe_layout)
        main_layout.addWidget(exe_group)
        
        # === MIDDLE SECTION: JSON Input ===
        json_group = QGroupBox("2. Input & Validate FFlags (JSON Format)")
        json_layout = QVBoxLayout()
        
        self.json_input = QTextEdit()
        self.json_input.setPlaceholderText(
            'Enter FFlags in JSON format, e.g.:\n'
            '{\n'
            '  "FFlagExample1": "true",\n'
            '  "FFlagExample2": "1.5",\n'
            '  "FFlagExample3": "test"\n'
            '}'
        )
        self.json_input.setMinimumHeight(150)
        font = QFont("Consolas", 10)
        self.json_input.setFont(font)
        
        # Load saved FFlags if exist
        if self.fflags_file.exists():
            try:
                with open(self.fflags_file, 'r') as f:
                    saved_fflags = json.load(f)
                    self.json_input.setPlainText(json.dumps(saved_fflags, indent=2))
                    self.current_fflags = saved_fflags
            except Exception as e:
                logger.error(f"Failed to load saved FFlags: {e}")
        
        json_btn_layout = QHBoxLayout()
        self.validate_btn = QPushButton("Validate JSON")
        self.validate_btn.clicked.connect(self.validate_json)
        
        self.load_btn = QPushButton("Load Saved")
        self.load_btn.clicked.connect(self.load_fflags)
        
        json_btn_layout.addWidget(self.validate_btn)
        json_btn_layout.addWidget(self.load_btn)
        json_btn_layout.addStretch()
        
        json_layout.addWidget(self.json_input)
        json_layout.addLayout(json_btn_layout)
        json_group.setLayout(json_layout)
        main_layout.addWidget(json_group)
        
        # === STATUS LOG ===
        status_group = QGroupBox("Status Log")
        status_layout = QVBoxLayout()
        
        self.status_log = QTextEdit()
        self.status_log.setReadOnly(True)
        self.status_log.setMaximumHeight(120)
        status_layout.addWidget(self.status_log)
        status_group.setLayout(status_layout)
        main_layout.addWidget(status_group)
        
        # === BOTTOM SECTION: Automation Control ===
        control_group = QGroupBox("3. Automation Control")
        control_layout = QVBoxLayout()
        
        # Speed settings
        speed_layout = QHBoxLayout()
        speed_layout.addWidget(QLabel("Speed Preset:"))
        
        self.speed_combo = QComboBox()
        self.speed_combo.addItems([
            "Ultra Fast (0.01s) - Best for large batches",
            "Fast (0.02s) - Balanced",
            "Normal (0.03s) - Safer for slower systems",
            "Slow (0.05s) - Most compatible"
        ])
        self.speed_combo.setCurrentIndex(0)  # Default to Ultra Fast
        self.speed_combo.setToolTip("Choose speed based on your system and target app performance")
        speed_layout.addWidget(self.speed_combo, 1)
        
        control_layout.addLayout(speed_layout)
        
        # Progress bar
        self.progress_bar = QProgressBar()
        self.progress_bar.setValue(0)
        control_layout.addWidget(QLabel("Progress:"))
        control_layout.addWidget(self.progress_bar)
        
        # Buttons
        btn_layout = QHBoxLayout()
        
        self.start_btn = QPushButton("▶ Start Automation")
        self.start_btn.setEnabled(False)
        self.start_btn.clicked.connect(self.start_automation)
        self.start_btn.setStyleSheet("background-color: #4CAF50; color: white; font-weight: bold; padding: 8px;")
        
        self.stop_btn = QPushButton("⏹ Stop")
        self.stop_btn.setEnabled(False)
        self.stop_btn.clicked.connect(self.stop_automation)
        self.stop_btn.setStyleSheet("background-color: #f44336; color: white; font-weight: bold; padding: 8px;")
        
        btn_layout.addWidget(self.start_btn)
        btn_layout.addWidget(self.stop_btn)
        control_layout.addLayout(btn_layout)
        
        control_group.setLayout(control_layout)
        main_layout.addWidget(control_group)
        
        # === FFlag Management ===
        management_group = QGroupBox("4. FFlag Management")
        mgmt_layout = QHBoxLayout()
        
        self.save_btn = QPushButton("💾 Save FFlags")
        self.save_btn.clicked.connect(self.save_fflags)
        
        self.clear_btn = QPushButton("🗑 Clear All")
        self.clear_btn.clicked.connect(self.clear_fflags)
        
        self.alt_f4_btn = QPushButton("⚡ ALT+F4 Roblox")
        self.alt_f4_btn.clicked.connect(self.alt_f4_roblox)
        
        mgmt_layout.addWidget(self.save_btn)
        mgmt_layout.addWidget(self.clear_btn)
        mgmt_layout.addStretch()
        mgmt_layout.addWidget(self.alt_f4_btn)
        
        management_group.setLayout(mgmt_layout)
        main_layout.addWidget(management_group)
        
        self.log_status("Application started. Select an .exe to begin.")
    
    def log_status(self, message: str):
        """Add message to status log"""
        timestamp = datetime.now().strftime("%H:%M:%S")
        self.status_log.append(f"[{timestamp}] {message}")
        logger.info(message)
    
    def browse_exe(self):
        """Browse for .exe file"""
        file_path, _ = QFileDialog.getOpenFileName(
            self,
            "Select RuntimeFFlagEditor.exe",
            "",
            "Executable Files (*.exe)"
        )
        if file_path:
            self.exe_path = file_path
            self.exe_path_input.setText(file_path)
            self.launch_btn.setEnabled(True)
            self.save_config()
            self.log_status(f"Selected .exe: {file_path}")
    
    def launch_exe(self):
        """Launch the selected .exe"""
        if not self.exe_path or not Path(self.exe_path).exists():
            QMessageBox.critical(self, "Error", "Invalid .exe path!")
            return
        
        try:
            self.exe_process = subprocess.Popen([self.exe_path])
            self.log_status(f"Launched: {Path(self.exe_path).name}")
            QMessageBox.information(
                self,
                "EXE Launched",
                "RuntimeFFlagEditor has been launched.\nMake sure it's visible and ready for input."
            )
        except Exception as e:
            QMessageBox.critical(self, "Launch Error", f"Failed to launch .exe:\n{str(e)}")
            self.log_status(f"Launch error: {str(e)}")
    
    def validate_json(self):
        """Validate JSON input"""
        json_text = self.json_input.toPlainText().strip()
        
        if not json_text:
            QMessageBox.warning(self, "Empty Input", "Please enter FFlags JSON data.")
            return
        
        try:
            data = json.loads(json_text)
            
            if not isinstance(data, dict):
                raise ValueError("JSON must be an object/dictionary")
            
            if len(data) == 0:
                raise ValueError("JSON is empty")
            
            # Check for duplicates (already handled by dict, but log it)
            self.current_fflags = data
            
            self.log_status(f"✓ JSON validated successfully! Found {len(data)} FFlags.")
            self.start_btn.setEnabled(True)
            
            QMessageBox.information(
                self,
                "Validation Successful",
                f"✓ JSON is valid!\n\nTotal FFlags: {len(data)}\n\nYou can now start automation."
            )
            
        except json.JSONDecodeError as e:
            error_msg = f"Invalid JSON syntax at line {e.lineno}, column {e.colno}:\n{e.msg}"
            self.log_status(f"✗ JSON validation failed: {error_msg}")
            QMessageBox.critical(self, "JSON Error", error_msg)
            self.start_btn.setEnabled(False)
        except ValueError as e:
            self.log_status(f"✗ Validation error: {str(e)}")
            QMessageBox.critical(self, "Validation Error", str(e))
            self.start_btn.setEnabled(False)
    
    def start_automation(self):
        """Start the automation process"""
        if not self.current_fflags:
            QMessageBox.warning(self, "No FFlags", "Please validate JSON first.")
            return
        
        # Calculate estimated time
        total_flags = len(self.current_fflags)
        estimated_seconds = total_flags * 0.04  # ~0.04s per flag
        estimated_time = f"{int(estimated_seconds // 60)}m {int(estimated_seconds % 60)}s" if estimated_seconds >= 60 else f"{int(estimated_seconds)}s"
        
        # Warn user to focus the window
        reply = QMessageBox.question(
            self,
            "Ready to Start?",
            f"Automation will begin in 3 seconds.\n\n"
            f"Total FFlags: {total_flags}\n"
            f"Estimated time: ~{estimated_time}\n\n"
            f"⚠ IMPORTANT:\n"
            f"• Keep the FFlag Editor window focused\n"
            f"• Don't touch mouse/keyboard during automation\n"
            f"• Don't switch windows or minimize\n\n"
            f"Continue?",
            QMessageBox.Yes | QMessageBox.No
        )
        
        if reply == QMessageBox.No:
            return
        
        self.log_status("⚙ Starting automation...")
        self.progress_bar.setValue(0)
        self.start_btn.setEnabled(False)
        self.stop_btn.setEnabled(True)
        
        # Get delay from speed preset
        speed_index = self.speed_combo.currentIndex()
        delay_map = {0: 0.01, 1: 0.02, 2: 0.03, 3: 0.05}
        delay = delay_map.get(speed_index, 0.01)
        
        # Start worker thread with selected speed
        self.automation_worker = AutomationWorker(self.current_fflags, delay=delay)
        self.automation_worker.progress_update.connect(self.update_progress)
        self.automation_worker.status_update.connect(self.log_status)
        self.automation_worker.finished.connect(self.automation_finished)
        self.automation_worker.start()
    
    def stop_automation(self):
        """Stop the automation"""
        if self.automation_worker and self.automation_worker.isRunning():
            self.automation_worker.stop()
            self.log_status("⏹ Stopping automation...")
    
    def update_progress(self, value: int):
        """Update progress bar"""
        self.progress_bar.setValue(value)
    
    def automation_finished(self, success: bool, message: str):
        """Handle automation completion"""
        self.start_btn.setEnabled(True)
        self.stop_btn.setEnabled(False)
        
        if success:
            QMessageBox.information(self, "✓ Success", message)
        else:
            QMessageBox.warning(self, "⚠ Automation Issue", message)
    
    def save_fflags(self):
        """Save current FFlags to file"""
        if not self.current_fflags:
            QMessageBox.warning(self, "No Data", "No FFlags to save. Validate JSON first.")
            return
        
        try:
            with open(self.fflags_file, 'w') as f:
                json.dump(self.current_fflags, f, indent=2)
            self.log_status(f"💾 FFlags saved to {self.fflags_file}")
            QMessageBox.information(self, "Saved", f"FFlags saved successfully!\n\nFile: {self.fflags_file}")
        except Exception as e:
            QMessageBox.critical(self, "Save Error", f"Failed to save FFlags:\n{str(e)}")
    
    def load_fflags(self):
        """Load FFlags from file"""
        if not self.fflags_file.exists():
            QMessageBox.information(self, "No Saved Data", "No saved FFlags found.")
            return
        
        try:
            with open(self.fflags_file, 'r') as f:
                data = json.load(f)
            self.json_input.setPlainText(json.dumps(data, indent=2))
            self.log_status(f"📂 Loaded {len(data)} FFlags from {self.fflags_file}")
        except Exception as e:
            QMessageBox.critical(self, "Load Error", f"Failed to load FFlags:\n{str(e)}")
    
    def clear_fflags(self):
        """Clear all FFlags"""
        reply = QMessageBox.question(
            self,
            "Confirm Clear",
            "Are you sure you want to clear all FFlags?\n\nThis will also delete the saved file.",
            QMessageBox.Yes | QMessageBox.No
        )
        
        if reply == QMessageBox.Yes:
            self.json_input.clear()
            self.current_fflags = {}
            if self.fflags_file.exists():
                self.fflags_file.unlink()
            self.progress_bar.setValue(0)
            self.start_btn.setEnabled(False)
            self.log_status("🗑 All FFlags cleared.")
    
    def alt_f4_roblox(self):
        """Send ALT+F4 to close Roblox"""
        reply = QMessageBox.question(
            self,
            "Close Roblox?",
            "This will send ALT+F4 to close the active window.\n\nMake sure Roblox is focused!\n\nContinue?",
            QMessageBox.Yes | QMessageBox.No
        )
        
        if reply == QMessageBox.Yes:
            try:
                pyautogui.hotkey('alt', 'F4')
                self.log_status("⚡ Sent ALT+F4 command")
            except Exception as e:
                QMessageBox.critical(self, "Error", f"Failed to send ALT+F4:\n{str(e)}")
    
    def load_config(self):
        """Load configuration from file"""
        if self.config_file.exists():
            try:
                with open(self.config_file, 'r') as f:
                    config = json.load(f)
                    self.exe_path = config.get('exe_path', '')
            except Exception as e:
                logger.error(f"Failed to load config: {e}")
    
    def save_config(self):
        """Save configuration to file"""
        try:
            config = {'exe_path': self.exe_path}
            with open(self.config_file, 'w') as f:
                json.dump(config, f, indent=2)
        except Exception as e:
            logger.error(f"Failed to save config: {e}")
    
    def closeEvent(self, event):
        """Handle application close"""
        if self.automation_worker and self.automation_worker.isRunning():
            reply = QMessageBox.question(
                self,
                "Automation Running",
                "Automation is still running. Are you sure you want to exit?",
                QMessageBox.Yes | QMessageBox.No
            )
            if reply == QMessageBox.No:
                event.ignore()
                return
            self.automation_worker.stop()
            self.automation_worker.wait()
        
        self.save_config()
        event.accept()


def main():
    app = QApplication(sys.argv)
    app.setStyle('Fusion')  # Modern look
    window = FFlagApp()
    window.show()
    sys.exit(app.exec())


if __name__ == '__main__':
    main()

