# How Other Users Can Access Your Website

## Your App Already Configured for Network Access ✓
Your app.py already has: `host='0.0.0.0'` which allows network access.

## Steps for Users to Access

### 1. Find Your Computer's IP Address

**On Windows:**
```cmd
ipconfig
```
Look for "IPv4 Address" under your active network adapter (WiFi or Ethernet)
Example: `192.168.1.100`

**Quick Command:**
```cmd
ipconfig | findstr IPv4
```

### 2. Share the URL with Users

If your IP is `192.168.1.100`, users access via:
```
http://192.168.1.100:5000
```

### 3. Firewall Configuration (Important!)

**Allow Port 5000 through Windows Firewall:**

**Option A - Quick Command (Run as Administrator):**
```cmd
netsh advfirewall firewall add rule name="Flask App Port 5000" dir=in action=allow protocol=TCP localport=5000
```

**Option B - GUI Method:**
1. Open Windows Defender Firewall
2. Click "Advanced settings"
3. Click "Inbound Rules" → "New Rule"
4. Select "Port" → Next
5. Enter "5000" → Next
6. Select "Allow the connection" → Next
7. Check all profiles → Next
8. Name it "Flask Crime Prediction" → Finish

## Network Requirements

✓ All users must be on the **same network** (same WiFi/LAN)
✓ Port 5000 must be open in firewall
✓ Your computer must be running the app

## Testing Access

1. **Start your app:**
   ```cmd
   python app.py
   ```

2. **On your computer, test:**
   ```
   http://localhost:5000
   ```

3. **On another device (same network), test:**
   ```
   http://YOUR_IP:5000
   ```
   Replace YOUR_IP with your actual IP address

## For Internet Access (Advanced)

If you want users outside your network to access:

### Option 1: Port Forwarding (Home Router)
1. Login to your router (usually 192.168.1.1)
2. Find "Port Forwarding" settings
3. Forward external port 5000 to your computer's IP:5000
4. Share your public IP: https://whatismyipaddress.com

### Option 2: Use ngrok (Easiest)
```cmd
# Download ngrok from https://ngrok.com
ngrok http 5000
```
This gives you a public URL like: `https://abc123.ngrok.io`

### Option 3: Deploy to Cloud
- Heroku (Free tier available)
- AWS EC2
- Google Cloud
- DigitalOcean

## Quick Start Script

Save this as `start_server.bat`:
```batch
@echo off
echo ========================================
echo Crime Prediction System - Server Start
echo ========================================
echo.
echo Finding your IP address...
for /f "tokens=2 delims=:" %%a in ('ipconfig ^| findstr /c:"IPv4 Address"') do (
    set IP=%%a
    set IP=!IP:~1!
    echo.
    echo Your server will be accessible at:
    echo http://!IP!:5000
    echo.
)
echo Starting server...
echo.
python app.py
pause
```

## Troubleshooting

**Users can't connect:**
- ✓ Check firewall is allowing port 5000
- ✓ Verify all on same network
- ✓ Confirm app is running
- ✓ Try pinging your IP from their device

**Connection refused:**
- ✓ Ensure app.py has `host='0.0.0.0'` (already set)
- ✓ Check antivirus isn't blocking

**Slow performance:**
- ✓ Use production server (see below)

## Production Deployment (Recommended)

For better performance with multiple users:

```cmd
pip install waitress
```

Create `production_server.py`:
```python
from waitress import serve
from app import app

if __name__ == '__main__':
    print("Starting production server on port 5000...")
    serve(app, host='0.0.0.0', port=5000, threads=4)
```

Run: `python production_server.py`
