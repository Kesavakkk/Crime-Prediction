import numpy as np
from datetime import datetime

class SafetyClassifier:
    def __init__(self):
        self.risk_zones = {
            'HIGH': [(28.7041, 77.1025), (19.0760, 72.8777)],  # Delhi, Mumbai
            'MEDIUM': [(12.9716, 77.5946), (22.5726, 88.3639)],  # Bangalore, Kolkata
            'LOW': [(13.0827, 80.2707)]  # Chennai
        }
    
    def predict_risk(self, lat, lng, hour=12, is_female=False, age=25):
        # Simple distance-based risk calculation
        min_dist = float('inf')
        risk_level = 'LOW'
        
        for level, coords in self.risk_zones.items():
            for coord_lat, coord_lng in coords:
                dist = ((lat - coord_lat) ** 2 + (lng - coord_lng) ** 2) ** 0.5
                if dist < min_dist:
                    min_dist = dist
                    risk_level = level
        
        # Adjust for time and demographics
        risk_score = 0.3 if risk_level == 'LOW' else 0.6 if risk_level == 'MEDIUM' else 0.9
        if hour < 6 or hour > 22:
            risk_score += 0.1
        if is_female:
            risk_score += 0.05
        if age < 18 or age > 65:
            risk_score += 0.05
            
        risk_score = min(1.0, risk_score)
        
        return {
            'risk_level': 'HIGH' if risk_score > 0.7 else 'MEDIUM' if risk_score > 0.4 else 'LOW',
            'risk_score': round(risk_score, 2),
            'factors': ['location', 'time', 'demographics']
        }