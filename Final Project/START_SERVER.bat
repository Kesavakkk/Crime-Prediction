@echo off
setlocal enabledelayedexpansion
color 0A
echo ========================================
echo Crime Prediction System - Server Start
echo ========================================
echo.
echo Finding your IP address...
echo.

for /f "tokens=2 delims=:" %%a in ('ipconfig ^| findstr /c:"IPv4 Address"') do (
    set "IP=%%a"
    set "IP=!IP:~1!"
    if not "!IP!"=="" (
        echo [SUCCESS] Your IP Address: !IP!
        echo.
        echo Share this URL with users on your network:
        echo http://!IP!:5000
        echo.
    )
)

echo ========================================
echo Starting Flask Server...
echo ========================================
echo.
echo Press Ctrl+C to stop the server
echo.

python app.py

pause
