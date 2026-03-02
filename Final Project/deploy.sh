#!/bin/bash

echo "🚀 Deploying Crime Prediction System..."

# Update system
sudo apt update && sudo apt upgrade -y

# Install dependencies
sudo apt install -y python3-pip python3-venv mysql-server nginx

# Create virtual environment
python3 -m venv venv
source venv/bin/activate

# Install Python packages
pip install -r requirements.txt
pip install gunicorn eventlet

# Setup environment
cp .env.example .env
echo "⚠️  Edit .env file with production credentials"

# Setup database
python3 setup_db.py

# Create systemd service
sudo tee /etc/systemd/system/crime-prediction.service > /dev/null <<EOF
[Unit]
Description=Crime Prediction Flask App
After=network.target

[Service]
User=$USER
WorkingDirectory=$(pwd)
Environment="PATH=$(pwd)/venv/bin"
ExecStart=$(pwd)/venv/bin/gunicorn --worker-class eventlet -w 1 --bind 0.0.0.0:5000 app:app

[Install]
WantedBy=multi-user.target
EOF

# Start service
sudo systemctl daemon-reload
sudo systemctl enable crime-prediction
sudo systemctl start crime-prediction

# Configure Nginx
sudo cp nginx.conf /etc/nginx/sites-available/crime-prediction
sudo ln -s /etc/nginx/sites-available/crime-prediction /etc/nginx/sites-enabled/
sudo nginx -t
sudo systemctl restart nginx

echo "✅ Deployment complete!"
echo "Access at: http://$(curl -s ifconfig.me)"
