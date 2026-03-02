import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler
from sklearn.cluster import KMeans
import threading
import time
from datetime import datetime

class RealtimeCrimePredictor:
    def __init__(self, dataset_path):
        self.dataset_path = dataset_path
        self.model = None
        self.scaler = MinMaxScaler()
        self._load_model()
    
    def _load_model(self):
        try:
            df = pd.read_csv(self.dataset_path)
            numeric_cols = df.select_dtypes(include=[np.number]).columns.tolist()
            if 'Year' in numeric_cols:
                numeric_cols.remove('Year')
            
            state_crime = df.groupby('STATE/UT')[numeric_cols].sum()
            X = self.scaler.fit_transform(state_crime.values)
            
            self.model = KMeans(n_clusters=2, random_state=0, n_init='auto')
            self.model.fit(X)
        except Exception as e:
            print(f"Model loading error: {e}")
    
    def predict_state(self, state):
        if not self.model:
            return {'error': 'Model not loaded'}
        
        # Simulate prediction
        risk_score = np.random.random()
        return {
            'state': state,
            'risk_level': 'HIGH' if risk_score > 0.7 else 'MEDIUM' if risk_score > 0.4 else 'LOW',
            'confidence': round(risk_score, 2)
        }

class StreamingDashboard:
    def __init__(self, predictor):
        self.predictor = predictor
        self.running = False
        self.socketio = None
    
    def start(self, socketio):
        self.socketio = socketio
        if not self.running:
            self.running = True
            thread = threading.Thread(target=self._stream_data)
            thread.daemon = True
            thread.start()
    
    def _stream_data(self):
        while self.running:
            try:
                # Simulate real-time data
                data = {
                    'timestamp': datetime.now().isoformat(),
                    'active_alerts': np.random.randint(0, 5),
                    'total_predictions': np.random.randint(100, 1000)
                }
                if self.socketio:
                    self.socketio.emit('realtime_update', data)
                time.sleep(5)
            except Exception as e:
                print(f"Streaming error: {e}")
                break