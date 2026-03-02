import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import StandardScaler
from datetime import datetime, time
import json

class SafetyRiskClassifier:
    def __init__(self):
        self.model = RandomForestClassifier(n_estimators=100, random_state=42)
        self.scaler = StandardScaler()
        self.is_trained = False
        
    def get_risk_features(self, lat, lng, hour, is_female=False, age=25):
        """Extract geospatial and demographic features for risk assessment"""
        features = {
            'hour': hour,
            'is_night': 1 if hour >= 22 or hour <= 5 else 0,
            'is_evening': 1 if 18 <= hour <= 21 else 0,
            'is_female': 1 if is_female else 0,
            'age_group': 1 if age < 25 else 2 if age < 45 else 3,
            'population_density': self._estimate_population_density(lat, lng),
            'lighting_score': self._estimate_lighting(lat, lng, hour),
            'transport_availability': self._estimate_transport(lat, lng, hour),
            'police_proximity': self._estimate_police_proximity(lat, lng)
        }
        return list(features.values())
    
    def _estimate_population_density(self, lat, lng):
        """Estimate population density based on coordinates"""
        # Major cities have higher density
        major_cities = [
            (28.7041, 77.1025),  # Delhi
            (19.0760, 72.8777),  # Mumbai
            (13.0827, 80.2707),  # Chennai
            (12.9716, 77.5946),  # Bangalore
            (22.5726, 88.3639)   # Kolkata
        ]
        
        min_dist = min([((lat-city[0])**2 + (lng-city[1])**2)**0.5 for city in major_cities])
        return max(0.1, 1.0 - min_dist * 10)  # Higher score for closer to cities
    
    def _estimate_lighting(self, lat, lng, hour):
        """Estimate lighting conditions"""
        base_lighting = 0.8 if 6 <= hour <= 18 else 0.3  # Day vs night
        urban_bonus = self._estimate_population_density(lat, lng) * 0.4
        return min(1.0, base_lighting + urban_bonus)
    
    def _estimate_transport(self, lat, lng, hour):
        """Estimate public transport availability"""
        base_transport = 0.9 if 6 <= hour <= 22 else 0.2
        urban_bonus = self._estimate_population_density(lat, lng) * 0.3
        return min(1.0, base_transport + urban_bonus)
    
    def _estimate_police_proximity(self, lat, lng):
        """Estimate police station proximity"""
        return 0.5 + self._estimate_population_density(lat, lng) * 0.4
    
    def train_model(self):
        """Train the safety risk model with synthetic data"""
        # Generate synthetic training data
        np.random.seed(42)
        n_samples = 1000
        
        X = []
        y = []
        
        for _ in range(n_samples):
            lat = np.random.uniform(8, 35)  # India latitude range
            lng = np.random.uniform(68, 97)  # India longitude range
            hour = np.random.randint(0, 24)
            is_female = np.random.choice([0, 1])
            age = np.random.randint(18, 65)
            
            features = self.get_risk_features(lat, lng, hour, is_female, age)
            X.append(features)
            
            # Generate risk label based on features
            risk_score = 0
            if features[1]:  # is_night
                risk_score += 0.4
            if features[4] == 1:  # young age
                risk_score += 0.2
            if features[2]:  # is_female
                risk_score += 0.3
            if features[5] < 0.3:  # low population density
                risk_score += 0.3
            if features[6] < 0.4:  # poor lighting
                risk_score += 0.4
                
            # 0: Low, 1: Medium, 2: High
            if risk_score < 0.4:
                y.append(0)
            elif risk_score < 0.8:
                y.append(1)
            else:
                y.append(2)
        
        X = np.array(X)
        y = np.array(y)
        
        X_scaled = self.scaler.fit_transform(X)
        self.model.fit(X_scaled, y)
        self.is_trained = True
    
    def predict_risk(self, lat, lng, hour=None, is_female=False, age=25):
        """Predict safety risk level"""
        if not self.is_trained:
            self.train_model()
            
        if hour is None:
            hour = datetime.now().hour
            
        features = self.get_risk_features(lat, lng, hour, is_female, age)
        features_scaled = self.scaler.transform([features])
        
        risk_level = self.model.predict(features_scaled)[0]
        risk_prob = self.model.predict_proba(features_scaled)[0]
        
        risk_labels = ['LOW', 'MEDIUM', 'HIGH']
        return {
            'risk_level': risk_labels[risk_level],
            'risk_score': float(risk_prob[risk_level]),
            'probabilities': {
                'low': float(risk_prob[0]),
                'medium': float(risk_prob[1]),
                'high': float(risk_prob[2])
            }
        }

class WomenSafetyScorer:
    def __init__(self):
        self.safety_factors = {
            'time_of_day': {
                'morning': 0.8,    # 6-10 AM
                'day': 0.9,        # 10 AM - 6 PM
                'evening': 0.6,    # 6-9 PM
                'night': 0.3       # 9 PM - 6 AM
            },
            'location_type': {
                'residential': 0.7,
                'commercial': 0.8,
                'industrial': 0.5,
                'isolated': 0.2
            }
        }
    
    def calculate_women_safety_score(self, lat, lng, hour=None, additional_factors=None):
        """Calculate women-specific safety score"""
        if hour is None:
            hour = datetime.now().hour
            
        # Time-based scoring
        if 6 <= hour < 10:
            time_score = self.safety_factors['time_of_day']['morning']
        elif 10 <= hour < 18:
            time_score = self.safety_factors['time_of_day']['day']
        elif 18 <= hour < 21:
            time_score = self.safety_factors['time_of_day']['evening']
        else:
            time_score = self.safety_factors['time_of_day']['night']
        
        # Location-based scoring (simplified)
        location_score = 0.7  # Default
        
        # Additional women-specific factors
        crowd_density = self._estimate_crowd_density(lat, lng, hour)
        lighting_quality = self._estimate_lighting_quality(lat, lng, hour)
        emergency_access = self._estimate_emergency_access(lat, lng)
        
        # Weighted scoring
        final_score = (
            time_score * 0.3 +
            location_score * 0.2 +
            crowd_density * 0.2 +
            lighting_quality * 0.15 +
            emergency_access * 0.15
        )
        
        return {
            'overall_score': round(final_score * 100),
            'risk_level': 'HIGH' if final_score < 0.4 else 'MEDIUM' if final_score < 0.7 else 'LOW',
            'factors': {
                'time_safety': round(time_score * 100),
                'crowd_density': round(crowd_density * 100),
                'lighting': round(lighting_quality * 100),
                'emergency_access': round(emergency_access * 100)
            }
        }
    
    def _estimate_crowd_density(self, lat, lng, hour):
        """Estimate crowd density"""
        base_density = 0.8 if 9 <= hour <= 21 else 0.3
        urban_factor = min(1.0, ((lat - 20)**2 + (lng - 77)**2)**0.5 / 10)
        return max(0.1, base_density - urban_factor * 0.3)
    
    def _estimate_lighting_quality(self, lat, lng, hour):
        """Estimate lighting quality"""
        if 6 <= hour <= 18:
            return 0.9  # Daylight
        else:
            urban_lighting = min(0.8, ((lat - 20)**2 + (lng - 77)**2)**0.5 / 20)
            return max(0.2, urban_lighting)
    
    def _estimate_emergency_access(self, lat, lng):
        """Estimate emergency services access"""
        # Simplified: better in urban areas
        urban_factor = 1.0 - min(1.0, ((lat - 20)**2 + (lng - 77)**2)**0.5 / 15)
        return max(0.3, urban_factor)

class ProtectionRecommendationEngine:
    def __init__(self):
        self.recommendations = {
            'HIGH': {
                'immediate': [
                    "🚨 AVOID this area if possible",
                    "📱 Share live location with trusted contacts",
                    "🚖 Use verified taxi/ride-sharing services",
                    "👥 Travel in groups, avoid being alone"
                ],
                'precautions': [
                    "Keep emergency contacts ready",
                    "Carry personal safety devices",
                    "Stay in well-lit, populated areas",
                    "Trust your instincts - leave if uncomfortable"
                ]
            },
            'MEDIUM': {
                'immediate': [
                    "⚠️ Exercise caution in this area",
                    "📱 Keep phone charged and accessible",
                    "🚶‍♀️ Stick to main roads and paths",
                    "👀 Stay alert and aware of surroundings"
                ],
                'precautions': [
                    "Inform someone of your travel plans",
                    "Avoid displaying valuables",
                    "Use well-lit parking areas",
                    "Keep emergency numbers handy"
                ]
            },
            'LOW': {
                'immediate': [
                    "✅ Generally safe area",
                    "😊 Normal precautions sufficient",
                    "🚶‍♀️ Comfortable for solo travel",
                    "📍 Good area for regular activities"
                ],
                'precautions': [
                    "Maintain general awareness",
                    "Follow standard safety practices",
                    "Keep emergency contacts updated",
                    "Trust local advice and guidelines"
                ]
            }
        }
        
        self.women_specific = {
            'HIGH': [
                "🚺 Women's helpline: 1091",
                "👮‍♀️ Nearest police station contact",
                "🏥 Locate nearest hospital/clinic",
                "🚖 Pre-book return transport"
            ],
            'MEDIUM': [
                "👥 Consider traveling with companions",
                "📱 Use safety apps with location sharing",
                "🕐 Plan to leave before dark",
                "🚗 Park in secure, well-lit areas"
            ],
            'LOW': [
                "📱 Keep safety apps installed",
                "👥 Join local women's safety groups",
                "🗺️ Familiarize with area layout",
                "📞 Know local emergency numbers"
            ]
        }
    
    def get_recommendations(self, risk_level, is_female=False, location_context=None):
        """Get safety recommendations based on risk level"""
        base_recommendations = self.recommendations.get(risk_level, self.recommendations['MEDIUM'])
        
        recommendations = {
            'risk_level': risk_level,
            'immediate_actions': base_recommendations['immediate'],
            'general_precautions': base_recommendations['precautions']
        }
        
        if is_female:
            recommendations['women_specific'] = self.women_specific.get(risk_level, [])
        
        # Add time-specific recommendations
        current_hour = datetime.now().hour
        if current_hour >= 22 or current_hour <= 5:
            recommendations['night_safety'] = [
                "🌙 Extra caution during night hours",
                "💡 Stay in well-lit areas only",
                "🚖 Use trusted transportation",
                "📱 Keep someone informed of location"
            ]
        
        return recommendations

# Global instances
safety_classifier = SafetyRiskClassifier()
women_safety_scorer = WomenSafetyScorer()
protection_engine = ProtectionRecommendationEngine()