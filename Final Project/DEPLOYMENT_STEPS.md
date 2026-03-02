# Deployment Guide - Crime Prediction System

## Quick Deployment Options

### 1. Local Network (Already Working)
```bash
python run_app.py
# Access: http://YOUR_IP:5000
```

### 2. Heroku (Free Cloud Hosting)

**Step 1: Install Heroku CLI**
```bash
# Download from: https://devcenter.heroku.com/articles/heroku-cli
```

**Step 2: Login and Create App**
```bash
heroku login
heroku create crime-prediction-app
```

**Step 3: Add MySQL Database**
```bash
heroku addons:create cleardb:ignite
heroku config:get CLEARDB_DATABASE_URL
# Copy the URL and update .env
```

**Step 4: Set Environment Variables**
```bash
heroku config:set SECRET_KEY=your-secret-key-here
heroku config:set SESSION_TIMEOUT=3600
```

**Step 5: Deploy**
```bash
git init
git add .
git commit -m "Initial deployment"
git push heroku main
```

**Step 6: Open App**
```bash
heroku open
```

### 3. AWS EC2 (Professional Hosting)

**Step 1: Launch EC2 Instance**
- Choose Ubuntu 22.04 LTS
- Instance type: t2.micro (free tier)
- Configure security group: Allow ports 22, 80, 5000

**Step 2: Connect to Instance**
```bash
ssh -i your-key.pem ubuntu@your-ec2-ip
```

**Step 3: Run Deployment Script**
```bash
git clone your-repo-url
cd "Final Project"
chmod +x deploy.sh
./deploy.sh
```

**Step 4: Configure Domain (Optional)**
- Point your domain to EC2 IP
- Update nginx.conf with your domain
- Install SSL: `sudo certbot --nginx`

### 4. Railway (Modern Platform)

**Step 1: Visit railway.app**
- Sign up with GitHub

**Step 2: New Project**
- Deploy from GitHub repo
- Select "Final Project" folder

**Step 3: Add Variables**
```
SECRET_KEY=your-secret-key
DB_HOST=mysql-host
DB_USER=root
DB_PASSWORD=password
DB_NAME=crime_prediction
```

**Step 4: Deploy**
- Automatic deployment on push

### 5. PythonAnywhere (Beginner-Friendly)

**Step 1: Sign up at pythonanywhere.com**

**Step 2: Upload Files**
- Use Files tab to upload project

**Step 3: Create Web App**
- Dashboard → Web → Add new web app
- Choose Flask
- Python 3.9

**Step 4: Configure WSGI**
```python
import sys
path = '/home/yourusername/Final Project'
if path not in sys.path:
    sys.path.append(path)

from app import app as application
```

**Step 5: Install Requirements**
```bash
pip3 install --user -r requirements.txt
```

**Step 6: Reload Web App**

## Production Checklist

- [ ] Set `debug=False` in app.py
- [ ] Use strong SECRET_KEY (32+ characters)
- [ ] Configure production database
- [ ] Enable HTTPS/SSL
- [ ] Set up monitoring/logging
- [ ] Configure firewall rules
- [ ] Set up automated backups
- [ ] Test all features
- [ ] Configure rate limiting
- [ ] Set up error tracking

## Environment Variables (Production)

```env
# Database
DB_HOST=production-db-host
DB_USER=production_user
DB_PASSWORD=strong-password-here
DB_NAME=crime_prediction

# Security
SECRET_KEY=generate-32-char-random-string
SESSION_TIMEOUT=3600

# App Settings
FLASK_ENV=production
DEBUG=False
```

## Monitoring

**Check Logs:**
```bash
# Heroku
heroku logs --tail

# EC2/Linux
sudo journalctl -u crime-prediction -f
tail -f app.log

# PythonAnywhere
Check error log in Web tab
```

**Health Check:**
```bash
curl http://your-domain.com/
```

## Troubleshooting

**Port Issues:**
- Heroku: Uses $PORT automatically
- EC2: Open port 5000 in security group
- Use Nginx reverse proxy for port 80

**Database Connection:**
- Verify credentials in .env
- Check firewall rules
- Test connection: `mysql -h HOST -u USER -p`

**WebSocket Issues:**
- Ensure eventlet is installed
- Check proxy configuration for WebSocket upgrade
- Verify CORS settings

## Scaling

**Horizontal Scaling:**
```bash
# Heroku
heroku ps:scale web=2

# AWS
Use Load Balancer + Auto Scaling Group
```

**Database Optimization:**
- Add indexes to frequently queried columns
- Use connection pooling
- Enable query caching

## Security Hardening

1. **Enable HTTPS:**
```bash
sudo certbot --nginx -d your-domain.com
```

2. **Configure Firewall:**
```bash
sudo ufw allow 22
sudo ufw allow 80
sudo ufw allow 443
sudo ufw enable
```

3. **Update Dependencies:**
```bash
pip install --upgrade -r requirements.txt
```

4. **Set Up Fail2Ban:**
```bash
sudo apt install fail2ban
```

## Backup Strategy

**Database Backup:**
```bash
mysqldump -u user -p crime_prediction > backup.sql
```

**Automated Backups:**
```bash
# Add to crontab
0 2 * * * mysqldump -u user -p crime_prediction > /backups/$(date +\%Y\%m\%d).sql
```

## Cost Estimates

- **Heroku Free:** $0/month (limited hours)
- **PythonAnywhere Free:** $0/month (limited)
- **AWS EC2 t2.micro:** ~$8-10/month
- **Railway:** ~$5-20/month
- **DigitalOcean Droplet:** $5-10/month

## Support

For deployment issues:
1. Check application logs
2. Verify environment variables
3. Test database connection
4. Review security group/firewall rules
5. Check service status

---

**Recommended for Beginners:** PythonAnywhere or Railway
**Recommended for Production:** AWS EC2 with Nginx
**Recommended for Quick Demo:** Heroku
