# Crime Prediction System

A comprehensive Flask-based web application that analyzes crime data across Indian states using machine learning to identify safe and unsafe zones, predict crime patterns, and provide real-time safety navigation.

## 🚀 Features

### Core Features
- **User Authentication**: Secure registration/login with password hashing (pbkdf2:sha256)
- **Crime Prediction**: K-means clustering and SVM models to classify states as safe/unsafe
- **Interactive Dashboard**: Real-time analytics with Chart.js visualizations
- **GPS Safe Navigation**: Real-time location-based route finding with safety zones
- **Crime Heatmaps**: Visual representation of crime hotspots across India
- **Real-Time Alerts**: WebSocket-based live crime alerts and notifications

### Advanced Features
- **ML Risk Prediction**: State-wise risk assessment using trained SVM models
- **Model Evaluation**: Accuracy metrics, confusion matrix, cross-validation scores
- **Dataset Management**: Import, augment, and manage crime datasets
- **Safety Assessment**: Location-based safety scoring with women-specific analysis
- **Zone Classification**: Automatic classification of areas into risk zones
- **Crime Trends Analysis**: Historical crime pattern visualization
- **Area Analysis**: Detailed crime statistics by region
- **Future Predictions**: Time-series forecasting of crime rates

### Admin Features
- **Dataset Info**: View and manage dataset statistics
- **Data Augmentation**: Expand dataset for better model training
- **User Management**: Admin dashboard for user oversight
- **Model Training**: Train and evaluate ML models
- **System Monitoring**: Logs and performance metrics

## 🛠️ Technology Stack

- **Backend**: Flask, Flask-SocketIO
- **Database**: MySQL (with JSON fallback)
- **Machine Learning**: scikit-learn (K-means, SVM, Linear Regression)
- **Data Processing**: pandas, numpy
- **Visualization**: Chart.js, matplotlib, seaborn, folium
- **Real-Time**: WebSocket (Socket.IO)
- **Security**: Flask-Limiter, python-dotenv, password hashing

## 📋 Prerequisites

- Python 3.7 or higher
- MySQL Server (optional - JSON fallback available)
- Modern web browser (Chrome, Firefox, Edge)

## 🔧 Installation

### 1. Install Dependencies

```bash
pip install -r requirements.txt
```

### 2. Configure Environment Variables

Copy `.env.example` to `.env`:

```bash
copy .env.example .env
```

Edit `.env` file with your settings:
```env
DB_HOST=localhost
DB_USER=root
DB_PASSWORD=your_password
DB_NAME=crime_prediction
SECRET_KEY=your-secret-key-here
SESSION_TIMEOUT=3600
```

### 3. Setup Database (Optional)

If using MySQL:
```bash
python setup_db.py
```

If not using MySQL, the app will automatically use JSON file storage.

### 4. Run the Application

**Option 1 - Using Python:**
```bash
python run_app.py
```

**Option 2 - Using Batch File (Windows):**
```bash
START.bat
```

The application will be available at: **http://localhost:5000**

## 📁 Project Structure

```
Final Project/
├── dataset/
│   └── crimes.csv              # Crime dataset
├── ml_modules/
│   ├── report_generator.py     # PDF report generation
│   └── train_models.py         # ML model training
├── models/
│   ├── svm_model.pkl           # Trained SVM model
│   └── lr_models.pkl           # Linear regression models
├── static/
│   └── database.sql            # Database schema
├── templates/                  # HTML templates (40+ pages)
│   ├── login.html
│   ├── register.html
│   ├── userhome.html
│   ├── dashboard_new.html
│   ├── safe_navigation_gps.html
│   ├── alerts.html
│   └── ...
├── app.py                      # Main Flask application
├── run_app.py                  # Application launcher
├── setup_db.py                 # Database setup script
├── requirements.txt            # Python dependencies
├── .env.example                # Environment template
├── .gitignore                  # Git ignore rules
├── README.md                   # This file
├── DEPLOYMENT_GUIDE.md         # Deployment instructions
├── NETWORK_ACCESS_GUIDE.md     # Network setup guide
└── TRANSFER_CHECKLIST.md       # Project transfer guide
```

## 🎯 Usage Guide

### For Regular Users:

1. **Register**: Create a new account with username, email, and password
2. **Login**: Access the system with your credentials
3. **Dashboard**: View crime statistics and analytics
4. **Crime Prediction**: Select crime type and predict safe/unsafe states
5. **GPS Navigation**: Use real-time GPS to find safe routes
6. **Alerts**: Monitor live crime alerts in your area

### For Admins:

1. **Dataset Management**: Import and augment crime data
2. **Model Training**: Train and evaluate ML models
3. **User Management**: View and manage registered users
4. **System Monitoring**: Check logs and performance

## 🔒 Security Features

- **Password Hashing**: Secure password storage using pbkdf2:sha256
- **Rate Limiting**: Protection against brute force attacks
- **Session Management**: Secure session cookies with timeout
- **Input Validation**: SQL injection and XSS protection
- **Environment Variables**: Sensitive data stored securely
- **Logging**: Security event monitoring and audit trails

## 🌐 Network Access

To access from other devices on your network:

1. Find your IP address:
   ```bash
   ipconfig
   ```

2. On other devices, navigate to:
   ```
   http://YOUR_IP_ADDRESS:5000
   ```

See `NETWORK_ACCESS_GUIDE.md` for detailed instructions.

## 📊 Machine Learning Models

### K-means Clustering
- Unsupervised learning for state classification
- Groups states into safe/unsafe clusters
- Based on multiple crime type features

### Support Vector Machine (SVM)
- Supervised classification with RBF kernel
- Predicts risk levels for new data
- Achieves 75-85% accuracy

### Linear Regression
- Time-series crime prediction
- Forecasts future crime rates
- Trend analysis and pattern detection

## 🐛 Troubleshooting

**MySQL Connection Failed:**
- App automatically falls back to JSON storage
- Check database credentials in `.env`
- Ensure MySQL service is running

**Port 5000 Already in Use:**
- Close other applications using port 5000
- Or modify port in `run_app.py`

**Module Import Errors:**
- Reinstall dependencies: `pip install -r requirements.txt`
- Check Python version: `python --version`

**GPS Location Not Working:**
- Allow location access in browser
- Use manual location entry as fallback
- Check HTTPS requirements for geolocation

## 📝 Logs

Application logs are stored in:
- `app.log` - General application logs
- `flask.log` - Flask server logs

Check logs for detailed error messages and debugging.

## 🚀 Deployment

For production deployment:

1. Set `debug=False` in `run_app.py`
2. Use strong `SECRET_KEY` in `.env`
3. Configure proper database credentials
4. Set up HTTPS/SSL certificates
5. Use production WSGI server (Gunicorn, uWSGI)

See `DEPLOYMENT_GUIDE.md` for detailed instructions.

## 📦 Dependencies

Core dependencies:
- Flask - Web framework
- PyMySQL - MySQL connector
- pandas - Data manipulation
- scikit-learn - Machine learning
- flask-socketio - Real-time communication
- python-dotenv - Environment management

See `requirements.txt` for complete list.

## 🤝 Contributing

This is an academic project. For improvements:
1. Test thoroughly before making changes
2. Follow existing code style
3. Update documentation
4. Add comments for complex logic

## 📄 License

This project is created for educational purposes.

## 👥 Support

For issues or questions:
- Check `DEPLOYMENT_GUIDE.md`
- Review `NETWORK_ACCESS_GUIDE.md`
- Check application logs
- Verify environment configuration

## 🎓 Academic Information

**Project Type**: Machine Learning Web Application
**Domain**: Crime Analysis and Prediction
**Technologies**: Python, Flask, Machine Learning, Real-Time Systems
**Dataset**: Indian Crime Statistics

## ⚡ Quick Start Commands

```bash
# Install dependencies
pip install -r requirements.txt

# Setup database (optional)
python setup_db.py

# Run application
python run_app.py

# Or use batch file
START.bat
```

## 🌟 Key Highlights

- ✅ Real-time crime alerts using WebSocket
- ✅ GPS-based safe navigation
- ✅ Machine learning crime prediction
- ✅ Interactive data visualizations
- ✅ Secure authentication system
- ✅ Mobile-responsive design
- ✅ Network access support
- ✅ Admin dashboard
- ✅ Comprehensive logging
- ✅ Database fallback mechanism

---

**Version**: 1.0  
**Last Updated**: 2024  
**Status**: Production Ready ✅
