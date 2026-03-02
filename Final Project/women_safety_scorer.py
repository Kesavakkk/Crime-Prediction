import numpy as np

class WomenSafetyScorer:
    def __init__(self):
        self.safe_zones = {
            (13.0827, 80.2707): 0.8,  # Chennai
            (12.9716, 77.5946): 0.7,  # Bangalore
            (19.0760, 72.8777): 0.5,  # Mumbai
            (28.7041, 77.1025): 0.4,  # Delhi
            (22.5726, 88.3639): 0.6   # Kolkata
        }
    
    def calculate_women_safety_score(self, lat, lng, hour=12):
        # Find nearest safe zone
        min_dist = float('inf')
        base_score = 0.5
        
        for (zone_lat, zone_lng), score in self.safe_zones.items():
            dist = ((lat - zone_lat) ** 2 + (lng - zone_lng) ** 2) ** 0.5
            if dist < min_dist:
                min_dist = dist
                base_score = score
        
        # Adjust for time
        if 6 <= hour <= 18:  # Daytime
            time_factor = 1.0
        elif 18 < hour <= 22:  # Evening
            time_factor = 0.8
        else:  # Night
            time_factor = 0.5
        
        final_score = base_score * time_factor
        
        return {
            'safety_score': round(final_score, 2),
            'safety_level': 'HIGH' if final_score > 0.7 else 'MEDIUM' if final_score > 0.4 else 'LOW',
            'recommendations': self._get_recommendations(final_score)
        }
    
    def _get_recommendations(self, score):
        if score > 0.7:
            return ['Area is generally safe', 'Stay aware of surroundings']
        elif score > 0.4:
            return ['Exercise caution', 'Avoid isolated areas', 'Travel in groups if possible']
        else:
            return ['High caution advised', 'Avoid if possible', 'Use alternative routes', 'Inform someone of your location']