# How to Run This Project on Another System

## Quick Setup (5 Minutes)

### Step 1: Copy Project Folder
Copy the entire "Final Project" folder to the new system

### Step 2: Install Python
- Download Python 3.8+ from https://www.python.org/downloads/
- During installation, CHECK "Add Python to PATH"

### Step 3: Install Dependencies
Open Command Prompt in project folder and run:
```cmd
pip install -r requirements.txt
```

### Step 4: Run the Application
```cmd
python app.py
```

### Step 5: Access the Website
Open browser and go to: http://localhost:5000

---

## Detailed Setup Instructions

### For Windows Systems

1. **Install Python**
   ```cmd
   # Check if Python is installed
   python --version
   
   # If not installed, download from python.org
   ```

2. **Navigate to Project**
   ```cmd
   cd "C:\path\to\Final Project"
   ```

3. **Create Virtual Environment (Optional but Recommended)**
   ```cmd
   python -m venv venv
   venv\Scripts\activate
   ```

4. **Install Requirements**
   ```cmd
   pip install -r requirements.txt
   ```

5. **Setup Environment Variables (Optional)**
   - Copy `.env.example` to `.env`
   - Edit `.env` with your settings

6. **Run Application**
   ```cmd
   python app.py
   ```

### For Linux/Mac Systems

1. **Install Python**
   ```bash
   # Check Python version
   python3 --version
   
   # Install if needed (Ubuntu/Debian)
   sudo apt-get update
   sudo apt-get install python3 python3-pip
   ```

2. **Navigate to Project**
   ```bash
   cd /path/to/Final\ Project
   ```

3. **Create Virtual Environment**
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

4. **Install Requirements**
   ```bash
   pip install -r requirements.txt
   ```

5. **Run Application**
   ```bash
   python3 app.py
   ```

---

## What Gets Transferred

### Required Files:
✓ `app.py` - Main application
✓ `requirements.txt` - Dependencies list
✓ `templates/` folder - All HTML files
✓ `dataset/` folder - Crime data CSV
✓ `.env.example` - Configuration template

### Optional Files:
- `users.json` - User accounts (will be created automatically)
- `reset_tokens.json` - Password reset tokens
- `app.log` - Application logs
- `.env` - Your specific configuration

### NOT Required:
✗ `__pycache__/` folders
✗ `venv/` folder (create new on each system)
✗ `.pyc` files

---

## Sharing Methods

### Method 1: USB Drive
1. Copy entire "Final Project" folder to USB
2. Paste on new system
3. Follow setup steps above

### Method 2: Cloud Storage (Google Drive, OneDrive)
1. Upload "Final Project" folder
2. Download on new system
3. Follow setup steps

### Method 3: GitHub (Best for Developers)
```bash
# On your system
git init
git add .
git commit -m "Initial commit"
git push origin main

# On new system
git clone <your-repo-url>
cd Final\ Project
pip install -r requirements.txt
python app.py
```

### Method 4: ZIP File
1. Right-click "Final Project" folder
2. Send to → Compressed (zipped) folder
3. Share the ZIP file
4. Extract on new system
5. Follow setup steps

---

## Troubleshooting on New System

### Issue: "pip not recognized"
**Solution:**
```cmd
python -m pip install -r requirements.txt
```

### Issue: "Module not found"
**Solution:**
```cmd
pip install --upgrade pip
pip install -r requirements.txt --force-reinstall
```

### Issue: "Port 5000 already in use"
**Solution:** Change port in app.py:
```python
socketio.run(app, debug=True, host='0.0.0.0', port=5001)
```

### Issue: "Permission denied"
**Solution:** Run as Administrator (Windows) or use sudo (Linux)

### Issue: Database connection fails
**Solution:** App automatically uses JSON fallback - no action needed!

---

## System Requirements

### Minimum:
- Python 3.8 or higher
- 2 GB RAM
- 500 MB free disk space
- Windows 7/10/11, Linux, or macOS

### Recommended:
- Python 3.10+
- 4 GB RAM
- 1 GB free disk space
- Windows 10/11 or Ubuntu 20.04+

---

## Quick Start Script for New Users

Save this as `SETUP.bat` (Windows):
```batch
@echo off
echo ========================================
echo Crime Prediction System - Setup
echo ========================================
echo.
echo Installing dependencies...
pip install -r requirements.txt
echo.
echo Setup complete!
echo.
echo Starting application...
python app.py
pause
```

Save this as `setup.sh` (Linux/Mac):
```bash
#!/bin/bash
echo "========================================"
echo "Crime Prediction System - Setup"
echo "========================================"
echo ""
echo "Installing dependencies..."
pip3 install -r requirements.txt
echo ""
echo "Setup complete!"
echo ""
echo "Starting application..."
python3 app.py
```

---

## Network Access on New System

To allow others to access from the new system:

1. **Find IP Address:**
   ```cmd
   ipconfig  # Windows
   ifconfig  # Linux/Mac
   ```

2. **Open Firewall:**
   ```cmd
   netsh advfirewall firewall add rule name="Flask Port 5000" dir=in action=allow protocol=TCP localport=5000
   ```

3. **Share URL:**
   ```
   http://YOUR_IP:5000
   ```

---

## Package the Project for Easy Distribution

Create `INSTALL_AND_RUN.bat`:
```batch
@echo off
echo ========================================
echo Crime Prediction System
echo Automated Setup and Launch
echo ========================================
echo.

REM Check Python
python --version >nul 2>&1
if errorlevel 1 (
    echo ERROR: Python not found!
    echo Please install Python from https://www.python.org/downloads/
    pause
    exit
)

echo [1/3] Installing dependencies...
pip install -r requirements.txt --quiet

echo [2/3] Setting up environment...
if not exist .env (
    copy .env.example .env
)

echo [3/3] Starting application...
echo.
echo Application will open at: http://localhost:5000
echo.
python app.py

pause
```

---

## Summary

**To run on another system:**
1. Copy project folder
2. Install Python
3. Run: `pip install -r requirements.txt`
4. Run: `python app.py`
5. Open: http://localhost:5000

**That's it!** The project is fully portable and works on any system with Python.
