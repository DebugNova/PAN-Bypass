@echo off
echo ========================================
echo FFlags Automated App - EXE Builder
echo ========================================
echo.

echo Checking PyInstaller...
pip show pyinstaller >nul 2>&1
if errorlevel 1 (
    echo PyInstaller not found. Installing...
    pip install pyinstaller
    if errorlevel 1 (
        echo ERROR: Failed to install PyInstaller!
        pause
        exit /b 1
    )
)

echo.
echo Building executable...
echo This may take a few minutes...
echo.

pyinstaller --name="PANByPass" ^
    --onefile ^
    --windowed ^
    --icon=app_icon.ico ^
    --add-data "example_fflags.json;." ^
    --hidden-import=PySide6 ^
    --hidden-import=PyAutoGUI ^
    --hidden-import=pyautogui ^
    --hidden-import=pyscreeze ^
    --hidden-import=pygetwindow ^
    --hidden-import=mouseinfo ^
    --hidden-import=pytweening ^
    --collect-all PySide6 ^
    main.py

if errorlevel 1 (
    echo.
    echo ERROR: Build failed!
    pause
    exit /b 1
)

echo.
echo ========================================
echo Build completed successfully!
echo ========================================
echo.
echo The executable is located at:
echo   dist\PANByPass.exe
echo.
echo You can now:
echo 1. Test the .exe by running it from dist folder
echo 2. Distribute it (no Python required on target system)
echo 3. Upload to GitHub
echo.
pause

