import json
import os
from datetime import datetime
import logging

logger = logging.getLogger(__name__)

class MockAlertSystem:
    def __init__(self):
        self.alerts_file = 'alerts_log.json'
        self.contacts_file = 'emergency_contacts.json'
        self.load_contacts()
    
    def load_contacts(self):
        try:
            with open(self.contacts_file, 'r') as f:
                self.contacts = json.load(f)
        except:
            self.contacts = {
                'emergency': [
                    {'name': 'Police', 'phone': '100', 'email': 'police@emergency.gov.in'},
                    {'name': 'Ambulance', 'phone': '108', 'email': 'ambulance@emergency.gov.in'},
                    {'name': 'Women Helpline', 'phone': '1091', 'email': 'women@helpline.gov.in'}
                ],
                'personal': [
                    {'name': 'Family Contact', 'phone': '+91-9876543210', 'email': 'family@example.com'},
                    {'name': 'Friend Contact', 'phone': '+91-9876543211', 'email': 'friend@example.com'}
                ]
            }
            self.save_contacts()
    
    def save_contacts(self):
        with open(self.contacts_file, 'w') as f:
            json.dump(self.contacts, f, indent=2)
    
    def send_sms_alert(self, phone, message, alert_type='INFO'):
        alert = {
            'id': f'SMS_{datetime.now().strftime("%Y%m%d_%H%M%S")}',
            'type': 'SMS',
            'recipient': phone,
            'message': message,
            'alert_type': alert_type,
            'timestamp': datetime.now().isoformat(),
            'status': 'SENT'
        }
        self.log_alert(alert)
        logger.info(f"SMS sent to {phone}: {message}")
        return alert
    
    def send_email_alert(self, email, subject, message, alert_type='INFO'):
        alert = {
            'id': f'EMAIL_{datetime.now().strftime("%Y%m%d_%H%M%S")}',
            'type': 'EMAIL',
            'recipient': email,
            'subject': subject,
            'message': message,
            'alert_type': alert_type,
            'timestamp': datetime.now().isoformat(),
            'status': 'SENT'
        }
        self.log_alert(alert)
        logger.info(f"Email sent to {email}: {subject}")
        return alert
    
    def send_emergency_alert(self, location, risk_level, user_info=None):
        alerts_sent = []
        
        # Emergency SMS
        sms_message = f"🚨 EMERGENCY ALERT\nHigh crime risk detected at {location}\nRisk Level: {risk_level}\nTime: {datetime.now().strftime('%H:%M:%S')}"
        
        for contact in self.contacts['emergency']:
            alert = self.send_sms_alert(contact['phone'], sms_message, 'EMERGENCY')
            alerts_sent.append(alert)
        
        # Emergency Email
        email_subject = f"🚨 Crime Alert - {location}"
        email_message = f"""
        EMERGENCY CRIME ALERT
        
        Location: {location}
        Risk Level: {risk_level}
        Time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
        
        Immediate action required. Emergency services have been notified.
        
        Crime Prediction System
        """
        
        for contact in self.contacts['emergency']:
            alert = self.send_email_alert(contact['email'], email_subject, email_message, 'EMERGENCY')
            alerts_sent.append(alert)
        
        return alerts_sent
    
    def send_personal_alert(self, location, message_type='SAFETY_UPDATE'):
        alerts_sent = []
        
        if message_type == 'SAFETY_UPDATE':
            sms_message = f"📍 Safety Update\nLocation: {location}\nStatus: Monitoring active\nTime: {datetime.now().strftime('%H:%M:%S')}"
            email_subject = f"Safety Update - {location}"
            email_message = f"Your safety monitoring is active at {location}. All systems operational."
        
        elif message_type == 'DANGER_WARNING':
            sms_message = f"⚠️ Danger Warning\nAvoid {location}\nHigh crime area detected\nTime: {datetime.now().strftime('%H:%M:%S')}"
            email_subject = f"⚠️ Danger Warning - {location}"
            email_message = f"Warning: High crime activity detected at {location}. Please avoid this area and use alternative routes."
        
        for contact in self.contacts['personal']:
            alert = self.send_sms_alert(contact['phone'], sms_message, 'WARNING')
            alerts_sent.append(alert)
            
            alert = self.send_email_alert(contact['email'], email_subject, email_message, 'WARNING')
            alerts_sent.append(alert)
        
        return alerts_sent
    
    def send_sos_alert(self, location, user_info=None):
        alerts_sent = []
        
        # SOS SMS
        sms_message = f"🆘 SOS EMERGENCY\nLocation: {location}\nImmediate help needed\nTime: {datetime.now().strftime('%H:%M:%S')}\nAuto-generated alert"
        
        # SOS Email
        email_subject = "🆘 SOS EMERGENCY ALERT"
        email_message = f"""
        SOS EMERGENCY ALERT
        
        Location: {location}
        Time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
        
        This is an automated SOS alert. Immediate assistance required.
        Emergency services have been contacted.
        
        Crime Prediction System - Emergency Response
        """
        
        # Send to all contacts
        all_contacts = self.contacts['emergency'] + self.contacts['personal']
        for contact in all_contacts:
            alert = self.send_sms_alert(contact['phone'], sms_message, 'SOS')
            alerts_sent.append(alert)
            
            alert = self.send_email_alert(contact['email'], email_subject, email_message, 'SOS')
            alerts_sent.append(alert)
        
        return alerts_sent
    
    def log_alert(self, alert):
        try:
            if os.path.exists(self.alerts_file):
                with open(self.alerts_file, 'r') as f:
                    alerts = json.load(f)
            else:
                alerts = []
            
            alerts.append(alert)
            
            # Keep only last 100 alerts
            if len(alerts) > 100:
                alerts = alerts[-100:]
            
            with open(self.alerts_file, 'w') as f:
                json.dump(alerts, f, indent=2)
        except Exception as e:
            logger.error(f"Error logging alert: {e}")
    
    def get_alert_history(self, limit=20):
        try:
            with open(self.alerts_file, 'r') as f:
                alerts = json.load(f)
            return alerts[-limit:]
        except:
            return []
    
    def add_contact(self, contact_type, name, phone, email):
        if contact_type not in self.contacts:
            self.contacts[contact_type] = []
        
        self.contacts[contact_type].append({
            'name': name,
            'phone': phone,
            'email': email
        })
        self.save_contacts()
    
    def get_contacts(self):
        return self.contacts

# Initialize global alert system
alert_system = MockAlertSystem()