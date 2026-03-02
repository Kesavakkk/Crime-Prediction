import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler, MinMaxScaler
from sklearn.cluster import KMeans
from sklearn.svm import SVC
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix, mean_squared_error, r2_score
import pickle
from pathlib import Path
import logging

logger = logging.getLogger(__name__)

class CrimeMLModels:
    def __init__(self, dataset_path):
        self.dataset_path = Path(dataset_path)
        self.models_dir = Path(__file__).parent.parent / 'models'
        self.models_dir.mkdir(exist_ok=True)
        self.df = None
        self.kmeans_model = None
        self.svm_model = None
        self.lr_model = None
        self.scaler = None
        
    def load_data(self):
        """Load and clean dataset"""
        self.df = pd.read_csv(self.dataset_path)
        if 'Unnamed: 0' in self.df.columns:
            self.df.drop(columns=['Unnamed: 0'], inplace=True)
        self.df['STATE/UT'] = self.df['STATE/UT'].str.upper()
        logger.info(f"Data loaded: {len(self.df)} rows")
        return self.df
    
    def get_numeric_cols(self):
        """Get numeric columns excluding Year"""
        cols = self.df.select_dtypes(include=[np.number]).columns.tolist()
        if 'Year' in cols:
            cols.remove('Year')
        return cols
    
    def train_kmeans(self, n_clusters=2):
        """Train K-means clustering model"""
        numeric_cols = self.get_numeric_cols()
        state_crime = self.df.groupby('STATE/UT')[numeric_cols].sum()
        state_crime['Total'] = state_crime.sum(axis=1)
        
        X = state_crime[['Total']].values
        scaler = MinMaxScaler()
        X_scaled = scaler.fit_transform(X)
        
        self.kmeans_model = KMeans(n_clusters=n_clusters, random_state=0, n_init='auto')
        self.kmeans_model.fit(X_scaled)
        
        # Save model
        model_path = self.models_dir / 'kmeans_model.pkl'
        with open(model_path, 'wb') as f:
            pickle.dump({'model': self.kmeans_model, 'scaler': scaler}, f)
        
        logger.info(f"K-means model trained and saved to {model_path}")
        return self.kmeans_model
    
    def train_svm(self):
        """Train SVM classification model"""
        numeric_cols = self.get_numeric_cols()
        state_crime = self.df.groupby('STATE/UT')[numeric_cols].sum()
        
        X = state_crime[numeric_cols].values
        scaler = StandardScaler()
        X_scaled = scaler.fit_transform(X)
        
        # Create labels using K-means
        kmeans = KMeans(n_clusters=2, random_state=0, n_init='auto')
        y = kmeans.fit_predict(X_scaled)
        unsafe_label = np.argmax(kmeans.cluster_centers_.sum(axis=1))
        y = (y == unsafe_label).astype(int)
        
        # Split data
        X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=42)
        
        # Train SVM
        self.svm_model = SVC(kernel='rbf', probability=True, random_state=0)
        self.svm_model.fit(X_train, y_train)
        self.scaler = scaler
        
        # Evaluate
        y_pred = self.svm_model.predict(X_test)
        accuracy = accuracy_score(y_test, y_pred)
        conf_matrix = confusion_matrix(y_test, y_pred)
        class_report = classification_report(y_test, y_pred, output_dict=True)
        
        # Save model
        model_path = self.models_dir / 'svm_model.pkl'
        with open(model_path, 'wb') as f:
            pickle.dump({'model': self.svm_model, 'scaler': scaler}, f)
        
        metrics = {
            'accuracy': accuracy,
            'confusion_matrix': conf_matrix.tolist(),
            'classification_report': class_report
        }
        
        logger.info(f"SVM model trained with accuracy: {accuracy:.2%}")
        return self.svm_model, metrics
    
    def train_linear_regression(self):
        """Train Linear Regression for future prediction"""
        if 'Year' not in self.df.columns:
            logger.error("Year column not found in dataset")
            return None, None
        
        numeric_cols = self.get_numeric_cols()
        models = {}
        metrics = {}
        
        for state in self.df['STATE/UT'].unique():
            state_data = self.df[self.df['STATE/UT'] == state].copy()
            state_data = state_data.sort_values('Year')
            
            X = state_data[['Year']].values
            y = state_data[numeric_cols].sum(axis=1).values
            
            if len(X) >= 2:
                model = LinearRegression()
                model.fit(X, y)
                
                # Evaluate
                y_pred = model.predict(X)
                mse = mean_squared_error(y, y_pred)
                r2 = r2_score(y, y_pred)
                
                models[state] = model
                metrics[state] = {'mse': mse, 'r2': r2}
        
        # Save models
        model_path = self.models_dir / 'lr_models.pkl'
        with open(model_path, 'wb') as f:
            pickle.dump(models, f)
        
        logger.info(f"Linear Regression models trained for {len(models)} states")
        return models, metrics
    
    def load_model(self, model_name):
        """Load saved model"""
        model_path = self.models_dir / f'{model_name}.pkl'
        if model_path.exists():
            with open(model_path, 'rb') as f:
                return pickle.load(f)
        return None
    
    def get_model_info(self):
        """Get information about saved models"""
        info = {}
        for model_file in self.models_dir.glob('*.pkl'):
            info[model_file.stem] = {
                'path': str(model_file),
                'size': model_file.stat().st_size,
                'modified': model_file.stat().st_mtime
            }
        return info
