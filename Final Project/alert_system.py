import logging
from datetime import datetime
import json

logger = logging.getLogger(__name__)

class MockAlertSystem:
    def __init__(self):
        self.sent_alerts = []
    
    def send_sms(self, phone, message):
        alert = {
            'type': 'SMS',
            'recipient': phone,
            'message': message,
            'timestamp': datetime.now().isoformat(),
            'status': 'sent'
        }
        self.sent_alerts.append(alert)
        logger.info(f"Mock SMS sent to {phone}: {message}")
        return True
    
    def send_email(self, email, subject, message):
        alert = {
            'type': 'EMAIL',
            'recipient': email,
            'subject': subject,
            'message': message,
            'timestamp': datetime.now().isoformat(),
            'status': 'sent'
        }
        self.sent_alerts.append(alert)
        logger.info(f"Mock Email sent to {email}: {subject}")
        return True
    
    def get_alert_history(self):
        return self.sent_alerts
    
    def clear_history(self):
        self.sent_alerts.clear()

alert_system = MockAlertSystem()