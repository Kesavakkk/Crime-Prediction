# 🆓 FREE DEPLOYMENT GUIDE - Crime Prediction System

## ✅ 100% FREE OPTIONS (No Credit Card Required)

---

## 🎯 OPTION 1: Render.com (RECOMMENDED)
**Permanent URL | Always Online | FREE Forever**

### Step-by-Step:

**1. Install Git** (if not installed):
   - Download: https://git-scm.com/download/win
   - Install with default settings

**2. Create GitHub Account**:
   - Go to: https://github.com/signup
   - Sign up (FREE)

**3. Upload Your Project**:
   ```bash
   # Open Command Prompt in your project folder
   cd "c:\Users\ELCOT\Desktop\Final Project"
   
   # Or double-click: setup_github.bat
   
   # Initialize Git
   git init
   git add .
   git commit -m "Initial commit"
   ```

**4. Create GitHub Repository**:
   - Go to: https://github.com/new
   - Repository name: `crime-prediction`
   - Click "Create repository"
   - Copy the URL (e.g., `https://github.com/YOUR_USERNAME/crime-prediction.git`)

**5. Push to GitHub**:
   ```bash
   git remote add origin YOUR_REPO_URL
   git branch -M main
   git push -u origin main
   ```

**6. Deploy on Render**:
   - Go to: https://render.com
   - Click "Get Started for Free"
   - Sign up with GitHub
   - Click "New +" → "Web Service"
   - Select your `crime-prediction` repository
   - Configure:
     - **Name**: crime-prediction
     - **Build Command**: `pip install -r requirements.txt`
     - **Start Command**: `gunicorn --worker-class eventlet -w 1 --bind 0.0.0.0:$PORT app:app`
   - Click "Advanced" → Add Environment Variables:
     ```
     SECRET_KEY = your-secret-key-12345
     SESSION_TIMEOUT = 3600
     ```
   - Click "Create Web Service"

**7. Done!** Your app will be live at:
   ```
   https://crime-prediction.onrender.com
   ```

---

## 🚀 OPTION 2: Ngrok (INSTANT - 2 Minutes)
**Temporary URL | Instant Setup | FREE**

### Step-by-Step:

**1. Download Ngrok**:
   - Go to: https://ngrok.com/download
   - Download Windows version
   - Extract ZIP file

**2. Sign Up** (FREE):
   - Go to: https://dashboard.ngrok.com/signup
   - Sign up (no credit card)
   - Copy your authtoken from dashboard

**3. Setup Ngrok**:
   ```bash
   cd path\to\ngrok
   ngrok config add-authtoken YOUR_AUTHTOKEN
   ```

**4. Run Your App**:
   ```bash
   cd "c:\Users\ELCOT\Desktop\Final Project"
   python run_app.py
   ```

**5. Start Ngrok** (in new terminal):
   ```bash
   cd path\to\ngrok
   ngrok http 5000
   ```

**6. Share the URL**:
   ```
   Forwarding: https://abc123.ngrok-free.app
   ```

**Note**: URL changes each time you restart (unless you upgrade)

---

## 🌐 OPTION 3: Vercel (Easy Deploy)
**Permanent URL | Auto-Deploy | FREE**

### Step-by-Step:

**1. Upload to GitHub** (follow Option 1, steps 1-5)

**2. Deploy on Vercel**:
   - Go to: https://vercel.com/signup
   - Sign up with GitHub (FREE)
   - Click "Add New" → "Project"
   - Import your `crime-prediction` repo
   - Click "Deploy"

**3. Done!** Your app will be live at:
   ```
   https://crime-prediction.vercel.app
   ```

---

## 📊 Comparison Table

| Platform | Setup Time | Permanent | Always On | Difficulty |
|----------|-----------|-----------|-----------|------------|
| **Render** | 15 min | ✅ Yes | ✅ Yes | Easy |
| **Ngrok** | 2 min | ❌ No | ⚠️ Manual | Very Easy |
| **Vercel** | 10 min | ✅ Yes | ✅ Yes | Easy |

---

## 🎯 MY RECOMMENDATION

**For permanent hosting**: Use **Render.com**
- Free forever
- Permanent URL
- Always online
- Professional

**For quick demo**: Use **Ngrok**
- Instant setup
- No configuration
- Perfect for testing

---

## 🆘 Troubleshooting

**Git not recognized?**
```bash
# Install Git from: https://git-scm.com/download/win
# Restart Command Prompt after installation
```

**Port 5000 in use?**
```bash
# Kill the process:
netstat -ano | findstr :5000
taskkill /PID <PID_NUMBER> /F
```

**Render build fails?**
- Check `requirements.txt` exists
- Verify Python version compatibility
- Check logs in Render dashboard

**Ngrok not working?**
- Make sure your app is running first
- Check if authtoken is added
- Try: `ngrok http 5000 --log=stdout`

---

## 📝 Quick Commands Reference

### GitHub Setup:
```bash
git init
git add .
git commit -m "Initial commit"
git remote add origin YOUR_REPO_URL
git branch -M main
git push -u origin main
```

### Update Deployment:
```bash
git add .
git commit -m "Update"
git push
```

### Run Locally:
```bash
python run_app.py
```

### Run with Ngrok:
```bash
# Terminal 1:
python run_app.py

# Terminal 2:
ngrok http 5000
```

---

## ✅ FREE RESOURCES

- **GitHub**: https://github.com (Code hosting)
- **Render**: https://render.com (App hosting)
- **Ngrok**: https://ngrok.com (Tunneling)
- **Vercel**: https://vercel.com (App hosting)
- **Git**: https://git-scm.com (Version control)

---

## 🎓 Need Help?

1. **Run**: `setup_github.bat` for automated Git setup
2. **Check**: Application logs in `app.log`
3. **Test locally**: `python run_app.py`
4. **Verify**: http://localhost:5000

---

**All options are 100% FREE - No credit card required!**
