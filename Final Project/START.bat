@echo off
REM Crime Prediction System Launcher
REM This script starts the Flask app and opens it in the browser

echo Starting Crime Prediction System...
echo.

REM Change to project directory
cd /d "%~dp0"

REM Start Flask app
.\.venv\Scripts\python.exe run_app.py

pause
