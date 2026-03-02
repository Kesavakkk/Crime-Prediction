import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier
from sklearn.svm import SVC
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
import pickle
import os

class AdvancedRiskPredictor:
    def __init__(self, dataset_path):
        self.dataset_path = dataset_path
        self.models = {}
        self.scaler = StandardScaler()
        self.feature_names = []
        
    def load_and_prepare_data(self):
        df = pd.read_csv(self.dataset_path)
        numeric_cols = df.select_dtypes(include=[np.number]).columns.tolist()
        if 'Year' in numeric_cols:
            numeric_cols.remove('Year')
        
        state_crime = df.groupby('STATE/UT')[numeric_cols].sum()
        state_crime['Total'] = state_crime.sum(axis=1)
        state_crime['CrimeRate'] = state_crime['Total'] / len(df)
        
        self.feature_names = numeric_cols + ['CrimeRate']
        X = state_crime[self.feature_names].values
        
        # Create risk labels based on crime rate
        threshold = state_crime['Total'].quantile(0.6)
        y = (state_crime['Total'] > threshold).astype(int)
        
        return X, y, state_crime
    
    def train_models(self):
        X, y, state_crime = self.load_and_prepare_data()
        X_scaled = self.scaler.fit_transform(X)
        
        X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=42)
        
        # Random Forest
        rf = RandomForestClassifier(n_estimators=100, random_state=42)
        rf.fit(X_train, y_train)
        self.models['random_forest'] = rf
        
        # Gradient Boosting
        gb = GradientBoostingClassifier(n_estimators=100, random_state=42)
        gb.fit(X_train, y_train)
        self.models['gradient_boosting'] = gb
        
        # SVM
        svm = SVC(kernel='rbf', probability=True, random_state=42)
        svm.fit(X_train, y_train)
        self.models['svm'] = svm
        
        # Calculate accuracies
        accuracies = {}
        for name, model in self.models.items():
            accuracies[name] = model.score(X_test, y_test)
        
        return accuracies, state_crime
    
    def predict_risk(self, state_data, model_name='random_forest'):
        if model_name not in self.models:
            model_name = 'random_forest'
        
        model = self.models[model_name]
        state_scaled = self.scaler.transform([state_data])
        
        risk_prob = model.predict_proba(state_scaled)[0][1]
        risk_label = 'HIGH' if risk_prob > 0.7 else 'MEDIUM' if risk_prob > 0.4 else 'LOW'
        
        return {
            'risk_score': float(risk_prob),
            'risk_level': risk_label,
            'confidence': float(max(model.predict_proba(state_scaled)[0]))
        }
    
    def get_feature_importance(self):
        if 'random_forest' in self.models:
            importances = self.models['random_forest'].feature_importances_
            return dict(zip(self.feature_names, importances))
        return {}
    
    def save_models(self, path='models'):
        os.makedirs(path, exist_ok=True)
        for name, model in self.models.items():
            with open(f'{path}/{name}.pkl', 'wb') as f:
                pickle.dump(model, f)
        with open(f'{path}/scaler.pkl', 'wb') as f:
            pickle.dump(self.scaler, f)
    
    def load_models(self, path='models'):
        for name in ['random_forest', 'gradient_boosting', 'svm']:
            try:
                with open(f'{path}/{name}.pkl', 'rb') as f:
                    self.models[name] = pickle.load(f)
            except:
                pass
        try:
            with open(f'{path}/scaler.pkl', 'rb') as f:
                self.scaler = pickle.load(f)
        except:
            pass

class TimeSeriesPredictor:
    def __init__(self, dataset_path):
        self.dataset_path = dataset_path
    
    def predict_future_crimes(self, state, years=3):
        df = pd.read_csv(self.dataset_path)
        if 'Year' not in df.columns:
            return None
        
        state_data = df[df['STATE/UT'] == state].sort_values('Year')
        if len(state_data) < 2:
            return None
        
        numeric_cols = state_data.select_dtypes(include=[np.number]).columns.tolist()
        if 'Year' in numeric_cols:
            numeric_cols.remove('Year')
        
        predictions = {}
        for col in numeric_cols:
            values = state_data[col].values
            trend = np.polyfit(range(len(values)), values, 1)
            
            future_vals = []
            for i in range(1, years + 1):
                pred = trend[0] * (len(values) + i) + trend[1]
                future_vals.append(max(0, int(pred)))
            
            predictions[col] = future_vals
        
        return predictions

class AlertSystem:
    def __init__(self):
        self.alert_threshold = 0.7
        self.alerts = []
    
    def check_risk_alert(self, risk_score, location):
        if risk_score > self.alert_threshold:
            alert = {
                'type': 'HIGH_RISK',
                'location': location,
                'risk_score': risk_score,
                'message': f'High crime risk detected in {location}',
                'severity': 'CRITICAL' if risk_score > 0.85 else 'HIGH',
                'timestamp': pd.Timestamp.now().isoformat()
            }
            self.alerts.append(alert)
            return alert
        return None
    
    def get_recent_alerts(self, limit=10):
        return self.alerts[-limit:]
    
    def clear_alerts(self):
        self.alerts = []
