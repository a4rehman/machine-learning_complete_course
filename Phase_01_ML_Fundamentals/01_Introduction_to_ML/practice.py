"""
Phase 01: ML Fundamentals
Topic: 01 - Introduction to ML
"""

import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

# ==============================================================================
# 1. TRADITIONAL PROGRAMMING (Rule-Based)
# ==============================================================================
def traditional_spam_filter(email_text: str) -> str:
    """
    A hard-coded, rule-based approach to solving a problem.
    This breaks down as the problem gets complex.
    """
    spam_keywords = ["free", "lottery", "urgent", "click here", "winner"]
    
    # Check if any spam keyword exists in the email
    for word in spam_keywords:
        if word in email_text.lower():
            return "Spam"
            
    return "Not Spam"

print("--- Traditional Programming ---")
print(f"Email 1: {traditional_spam_filter('Hey, are we still meeting tomorrow?')}")
print(f"Email 2: {traditional_spam_filter('URGENT! You are a winner! Click here for free money.')}")
print("\n")


# ==============================================================================
# 2. MACHINE LEARNING APPROACH
# ==============================================================================
def machine_learning_approach():
    """
    Simulating a basic Machine Learning pipeline.
    Instead of writing rules, we provide DATA and let the algorithm learn.
    """
    print("--- Machine Learning Approach ---")
    
    # 1. Dataset Generation (Mock Data)
    # Features: [word_count, contains_link(0/1), contains_urgent_word(0/1)]
    # Target: 0 (Not Spam), 1 (Spam)
    
    X = np.array([
        [10, 0, 0],  # Normal short email
        [250, 1, 1], # Long email, has link, has urgent word -> SPAM
        [45, 0, 0],  # Normal email
        [15, 1, 1],  # Short spam with link
        [100, 0, 0], # Long normal email
        [30, 1, 0]   # Email with normal link
    ])
    
    y = np.array([0, 1, 0, 1, 0, 0]) # The Labels (Supervised Learning)
    
    # 2. Train / Test Split
    # We hide some data from the model to test it later
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=42)
    
    # 3. Model Definition
    # We choose Logistic Regression (a classic ML algorithm for classification)
    model = LogisticRegression()
    
    # 4. Training (Learning the rules)
    print("Training the model...")
    model.fit(X_train, y_train)
    print("Model trained successfully!")
    
    # 5. Prediction (Testing the rules)
    predictions = model.predict(X_test)
    
    # 6. Evaluation
    acc = accuracy_score(y_test, predictions)
    print(f"Model Accuracy on unseen data: {acc * 100:.2f}%")
    
    # 7. Predicting on brand new data
    new_email = np.array([[20, 1, 1]]) # Short email, has link, is urgent
    is_spam = model.predict(new_email)
    print(f"New Email Prediction: {'Spam' if is_spam[0] == 1 else 'Not Spam'}")

if __name__ == "__main__":
    machine_learning_approach()
