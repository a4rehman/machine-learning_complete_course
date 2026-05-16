"""
Phase 08: Supervised Learning
Topic: Linear Regression
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.preprocessing import StandardScaler

# ==========================================
# 1. BEGINNER: Linear Regression (Scikit-Learn)
# ==========================================
def beginner_sklearn_pipeline():
    print("--- Beginner Pipeline: Scikit-Learn ---")
    # Synthetic Data
    X = 2 * np.random.rand(100, 1)
    y = 4 + 3 * X + np.random.randn(100, 1) # y = 4 + 3x + noise
    
    # Split
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    # Train
    model = LinearRegression()
    model.fit(X_train, y_train)
    
    # Predict
    preds = model.predict(X_test)
    
    # Evaluate
    print(f"Learned Intercept (b): {model.intercept_[0]:.4f}")
    print(f"Learned Weight (w): {model.coef_[0][0]:.4f}")
    print(f"MSE: {mean_squared_error(y_test, preds):.4f}")

# ==========================================
# 2. INTERMEDIATE: Gradient Descent from Scratch
# ==========================================
class ScratchLinearRegression:
    def __init__(self, lr=0.1, epochs=1000):
        self.lr = lr
        self.epochs = epochs
        self.weights = None
        self.bias = None
        self.loss_history = []
        
    def fit(self, X, y):
        n_samples, n_features = X.shape
        self.weights = np.zeros(n_features)
        self.bias = 0
        
        for _ in range(self.epochs):
            y_pred = np.dot(X, self.weights) + self.bias
            
            # Gradients
            dw = (1 / n_samples) * np.dot(X.T, (y_pred - y))
            db = (1 / n_samples) * np.sum(y_pred - y)
            
            # Update
            self.weights -= self.lr * dw
            self.bias -= self.lr * db
            
            # Record Loss
            mse = np.mean((y_pred - y)**2)
            self.loss_history.append(mse)
            
    def predict(self, X):
        return np.dot(X, self.weights) + self.bias

def intermediate_scratch_pipeline():
    print("\n--- Intermediate Pipeline: NumPy Gradient Descent ---")
    X = 2 * np.random.rand(100, 1)
    y = 4 + 3 * X.flatten() + np.random.randn(100)
    
    model = ScratchLinearRegression(lr=0.1, epochs=100)
    model.fit(X, y)
    
    print(f"Learned Intercept: {model.bias:.4f}")
    print(f"Learned Weight: {model.weights[0]:.4f}")

# ==========================================
# 3. ADVANCED: Real-World Dataset Pipeline
# ==========================================
def advanced_production_pipeline():
    print("\n--- Advanced Pipeline: Scaling & Feature Engineering ---")
    # Simulating Housing Data: [SquareFeet, Age, DistanceToCity]
    X_raw = np.random.rand(500, 3) * [2000, 50, 20] 
    y_raw = 50000 + X_raw[:, 0]*150 - X_raw[:, 1]*1000 - X_raw[:, 2]*5000 + np.random.randn(500)*10000
    
    # 1. Scaling (Crucial for multi-variate linear regression)
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X_raw)
    
    # 2. Train-Test Split
    X_train, X_test, y_train, y_test = train_test_split(X_scaled, y_raw, test_size=0.2)
    
    # 3. Model Training
    model = LinearRegression()
    model.fit(X_train, y_train)
    
    # 4. Evaluation
    preds = model.predict(X_test)
    r2 = r2_score(y_test, preds)
    print(f"Model R2 Score: {r2:.4f}")
    
    # 5. Feature Importance Extraction
    importances = pd.DataFrame({'Feature': ['SqFt', 'Age', 'Dist'], 'Weight': model.coef_})
    print("\nFeature Importances (Scaled):")
    print(importances.sort_values(by='Weight', ascending=False))

if __name__ == "__main__":
    beginner_sklearn_pipeline()
    intermediate_scratch_pipeline()
    advanced_production_pipeline()
