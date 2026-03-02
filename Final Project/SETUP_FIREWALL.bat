@echo off
echo ========================================
echo Firewall Configuration for Port 5000
echo ========================================
echo.
echo This will allow other users to access your app
echo You need to run this as Administrator
echo.
pause

netsh advfirewall firewall add rule name="Crime Prediction App - Port 5000" dir=in action=allow protocol=TCP localport=5000

if %errorlevel% equ 0 (
    echo.
    echo [SUCCESS] Firewall rule added successfully!
    echo Port 5000 is now open for incoming connections.
) else (
    echo.
    echo [ERROR] Failed to add firewall rule.
    echo Please run this script as Administrator:
    echo Right-click on this file and select "Run as administrator"
)

echo.
pause
