# User Guide - Crime Prediction System

## How Other Users Can Access This Application

### Option 1: Same Computer (Localhost)

**Step 1:** Start the application
```bash
python run_app.py
```
OR double-click `START.bat`

**Step 2:** Open browser and go to:
```
http://localhost:5000
```

**Step 3:** Register a new account
- Click "Register"
- Enter username, email, password
- Click "Register" button

**Step 4:** Login and use all features

---

### Option 2: Other Devices on Same WiFi Network

**On Your Computer (Server):**

**Step 1:** Find your IP address
```bash
ipconfig
```
Look for "IPv4 Address" (e.g., 192.168.1.100)

**Step 2:** Start the application
```bash
python run_app.py
```

**Step 3:** Configure firewall (Windows)
```bash
SETUP_FIREWALL.bat
```

**On Other Devices (Phone/Tablet/Laptop):**

**Step 1:** Connect to same WiFi network

**Step 2:** Open browser and go to:
```
http://YOUR_IP_ADDRESS:5000
```
Example: `http://192.168.1.100:5000`

**Step 3:** Register and login

---

### Option 3: Share Project Folder

**Step 1:** Copy entire "Final Project" folder to USB/Cloud

**Step 2:** On new computer, install Python 3.7+

**Step 3:** Install dependencies
```bash
cd "Final Project"
pip install -r requirements.txt
```

**Step 4:** Run application
```bash
python run_app.py
```

**Step 5:** Access at `http://localhost:5000`

---

## Quick Access Guide

### For Students/Classmates:

1. **Get the IP Address** from the person running the server
2. **Connect to same WiFi** (college/home network)
3. **Open browser** on your phone/laptop
4. **Type**: `http://IP_ADDRESS:5000`
5. **Register** your own account
6. **Start using** all features

### For Family/Friends:

1. Ask the host to run `START.bat`
2. Get the IP address from them
3. Connect to their WiFi
4. Open browser: `http://IP_ADDRESS:5000`
5. Create your account
6. Enjoy!

---

## Features Available to All Users

✅ **Crime Prediction** - Predict safe/unsafe states
✅ **Dashboard** - View crime analytics and charts
✅ **GPS Navigation** - Find safe routes with your location
✅ **Real-Time Alerts** - Get live crime notifications
✅ **Protection Dashboard** - Emergency contacts and safety
✅ **Area Analysis** - Analyze crime by region
✅ **Future Predictions** - Forecast crime trends
✅ **SVM Predictions** - ML-based risk assessment

---

## User Registration

**Required Information:**
- Username (unique)
- Email address
- Password (minimum 6 characters)

**After Registration:**
- Login with username and password
- Access all features immediately
- No admin approval needed

---

## Mobile Access

**Works on:**
- ✅ Android phones
- ✅ iPhones
- ✅ Tablets
- ✅ Any device with a browser

**Features on Mobile:**
- Full responsive design
- GPS location works perfectly
- Emergency contacts clickable
- All features accessible

---

## Troubleshooting

**Can't Access from Other Device?**
1. Check both devices on same WiFi
2. Verify IP address is correct
3. Run `SETUP_FIREWALL.bat` on server
4. Try `http://IP:5000` format

**Registration Not Working?**
1. Use unique username
2. Valid email format
3. Password at least 6 characters
4. Try different username if taken

**GPS Not Working?**
1. Allow location access in browser
2. Use HTTPS if required
3. Try manual location entry
4. Check browser permissions

---

## Network Setup (Detailed)

### Windows:

**Step 1:** Open Command Prompt
```bash
ipconfig
```

**Step 2:** Note IPv4 Address (e.g., 192.168.1.100)

**Step 3:** Allow through firewall
```bash
SETUP_FIREWALL.bat
```

**Step 4:** Share IP with users

### Mac/Linux:

**Step 1:** Open Terminal
```bash
ifconfig
```
OR
```bash
ip addr show
```

**Step 2:** Note IP address

**Step 3:** Start application
```bash
python run_app.py
```

---

## Multiple Users Simultaneously

✅ **Unlimited users** can access at the same time
✅ Each user has **separate account**
✅ Each user sees **their own data**
✅ **Real-time updates** for all users
✅ No performance issues with multiple users

---

## Sharing Instructions (Copy-Paste)

**Share this with your users:**

```
Crime Prediction System Access

1. Connect to WiFi: [YOUR_WIFI_NAME]
2. Open browser (Chrome/Firefox/Safari)
3. Go to: http://[YOUR_IP]:5000
4. Click "Register" to create account
5. Login and explore!

Features:
- Crime predictions
- GPS safe navigation
- Real-time alerts
- Interactive dashboard
- Emergency contacts

Need help? Contact: [YOUR_CONTACT]
```

---

## Security Notes

⚠️ **Important:**
- Each user must register separately
- Passwords are encrypted
- Don't share your password
- Logout when done on shared devices
- Admin features require admin account

---

## Demo Accounts (Optional)

If you want to create demo accounts for testing:

**Username:** demo_user
**Password:** demo123

**Username:** test_user
**Password:** test123

Users can create their own accounts anytime.

---

## Support

**For Issues:**
1. Check README.md
2. Check NETWORK_ACCESS_GUIDE.md
3. Verify all steps followed correctly
4. Restart application if needed

**Common Solutions:**
- Restart application: Close and run `START.bat` again
- Check firewall: Run `SETUP_FIREWALL.bat`
- Verify WiFi: Both devices same network
- Clear browser cache: Ctrl+Shift+Delete

---

## Quick Reference Card

```
┌─────────────────────────────────────┐
│   Crime Prediction System Access    │
├─────────────────────────────────────┤
│ Local:    http://localhost:5000     │
│ Network:  http://[IP]:5000          │
│                                     │
│ Default Port: 5000                  │
│ Registration: Open to all           │
│ Mobile: Fully supported             │
└─────────────────────────────────────┘
```

---

**Ready to Share!** 🚀

Just run the application and share your IP address with others on the same network!
