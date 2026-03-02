class ProtectionEngine:
    def __init__(self):
        self.general_recommendations = {
            'HIGH': [
                'Avoid the area if possible',
                'Travel in groups',
                'Use well-lit main roads',
                'Keep emergency contacts ready',
                'Share location with trusted contacts'
            ],
            'MEDIUM': [
                'Stay alert and aware',
                'Avoid isolated areas',
                'Keep valuables secure',
                'Use trusted transportation'
            ],
            'LOW': [
                'General safety precautions',
                'Stay aware of surroundings',
                'Keep emergency numbers handy'
            ]
        }
        
        self.women_specific = [
            'Use women-only transport when available',
            'Carry personal safety devices',
            'Avoid late night travel alone',
            'Use safety apps with location sharing'
        ]
    
    def get_recommendations(self, risk_level, is_female=False):
        recommendations = self.general_recommendations.get(risk_level, self.general_recommendations['LOW'])
        
        if is_female and risk_level in ['HIGH', 'MEDIUM']:
            recommendations.extend(self.women_specific[:2])
        
        return {
            'risk_level': risk_level,
            'recommendations': recommendations,
            'emergency_contacts': ['100 - Police', '108 - Emergency', '1091 - Women Helpline'],
            'safety_tips': self._get_safety_tips(risk_level)
        }
    
    def _get_safety_tips(self, risk_level):
        tips = {
            'HIGH': ['Trust your instincts', 'Have an exit plan', 'Stay in public areas'],
            'MEDIUM': ['Be cautious', 'Stay connected', 'Avoid distractions'],
            'LOW': ['Stay alert', 'Be prepared', 'Know your surroundings']
        }
        return tips.get(risk_level, tips['LOW'])