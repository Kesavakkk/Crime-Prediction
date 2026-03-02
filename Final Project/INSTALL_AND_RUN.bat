@echo off
color 0A
echo ========================================
echo Crime Prediction System
echo Automated Setup and Launch
echo ========================================
echo.

REM Check if Python is installed
python --version >nul 2>&1
if errorlevel 1 (
    echo [ERROR] Python is not installed!
    echo.
    echo Please install Python 3.8 or higher from:
    echo https://www.python.org/downloads/
    echo.
    echo Make sure to check "Add Python to PATH" during installation
    pause
    exit /b 1
)

echo [OK] Python is installed
python --version
echo.

echo [1/4] Checking pip...
python -m pip --version >nul 2>&1
if errorlevel 1 (
    echo [ERROR] pip not found. Installing pip...
    python -m ensurepip --default-pip
)
echo [OK] pip is ready
echo.

echo [2/4] Installing dependencies...
echo This may take a few minutes...
python -m pip install -r requirements.txt --quiet
if errorlevel 1 (
    echo [ERROR] Failed to install dependencies
    echo Trying again with verbose output...
    python -m pip install -r requirements.txt
    pause
    exit /b 1
)
echo [OK] All dependencies installed
echo.

echo [3/4] Setting up environment...
if not exist .env (
    if exist .env.example (
        copy .env.example .env >nul
        echo [OK] Created .env file from template
    ) else (
        echo [INFO] No .env file needed - using defaults
    )
) else (
    echo [OK] .env file already exists
)
echo.

echo [4/4] Starting application...
echo.
echo ========================================
echo Application is starting...
echo ========================================
echo.
echo Access the website at:
echo   http://localhost:5000
echo.
echo To stop the server, press Ctrl+C
echo.
echo ========================================
echo.

python app.py

pause
