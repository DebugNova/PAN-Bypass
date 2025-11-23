@echo off
echo Starting FFlags Automated App...
python main.py
if errorlevel 1 (
    echo.
    echo ERROR: Failed to start the application!
    echo Make sure you have installed dependencies using install.bat
    pause
)

