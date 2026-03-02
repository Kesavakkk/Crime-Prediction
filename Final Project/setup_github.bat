@echo off
echo ========================================
echo GitHub Setup for Crime Prediction
echo ========================================
echo.

cd /d "%~dp0"

echo Step 1: Initializing Git...
git init

echo Step 2: Adding files...
git add .

echo Step 3: Creating commit...
git commit -m "Initial commit - Crime Prediction System"

echo.
echo ========================================
echo NEXT STEPS:
echo ========================================
echo 1. Go to: https://github.com/new
echo 2. Create a repository named: crime-prediction
echo 3. Copy the repository URL
echo 4. Run these commands:
echo.
echo    git remote add origin YOUR_REPO_URL
echo    git branch -M main
echo    git push -u origin main
echo.
echo ========================================
pause
