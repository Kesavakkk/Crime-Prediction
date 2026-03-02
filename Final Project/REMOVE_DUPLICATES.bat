@echo off
echo ========================================
echo  Removing Duplicate Files
echo ========================================
echo.
echo This will delete duplicate/unused files from the project.
echo Press Ctrl+C to cancel, or
pause

echo.
echo Deleting duplicate template files...
del /F "templates\area_analysis.html" 2>nul
del /F "templates\dashboard.html" 2>nul
del /F "templates\future_prediction.html" 2>nul
del /F "templates\svm_predict.html" 2>nul
del /F "templates\userhome_enhanced.html" 2>nul
del /F "templates\userhome_new.html" 2>nul
del /F "templates\visualize.html" 2>nul
del /F "templates\safety_protection.html" 2>nul
del /F "templates\safety_protection_tn.html" 2>nul

echo.
echo Deleting old imported dataset files...
del /F "dataset\enhanced_crimes.csv" 2>nul
del /F "dataset\imported_data_20260212_214009.csv" 2>nul
del /F "dataset\imported_data_20260225_201153.csv" 2>nul
del /F "dataset\imported_data_20260225_201312.csv" 2>nul

echo.
echo Deleting duplicate Python files...
del /F "alert_system.py" 2>nul
del /F "safety_ml.py" 2>nul

echo.
echo ========================================
echo  Cleanup Complete!
echo ========================================
echo.
echo Deleted Files:
echo - 9 duplicate template files
echo - 4 old imported dataset files
echo - 2 duplicate Python files
echo.
echo Total: 15 duplicate files removed
echo.
pause
