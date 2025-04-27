import pandas as pd
import pickle
import os

def load_model(model_path='models/churn_model.pkl'):
    """Load the trained machine learning model."""
    if not os.path.exists(model_path):
        raise FileNotFoundError(f"Model file not found at {model_path}")
    with open(model_path, 'rb') as file:
        model = pickle.load(file)
    return model

def preprocess_input(user_input):
    """
    Preprocess the input dictionary into the correct format for model prediction.
    """
    # Assuming input is a dictionary directly coming from Streamlit form
    df = pd.DataFrame([user_input])

    # Perform necessary feature engineering here (example only)
    if 'gender' in df.columns:
        df['gender'] = df['gender'].map({'Male': 1, 'Female': 0})
    if 'Partner' in df.columns:
        df['Partner'] = df['Partner'].map({'Yes': 1, 'No': 0})
    if 'Dependents' in df.columns:
        df['Dependents'] = df['Dependents'].map({'Yes': 1, 'No': 0})
    if 'PhoneService' in df.columns:
        df['PhoneService'] = df['PhoneService'].map({'Yes': 1, 'No': 0})

    # Handle missing expected features
    expected_cols = [
        'gender', 'SeniorCitizen', 'Partner', 'Dependents',
        'tenure', 'MonthlyCharges', 'TotalCharges', 'PhoneService'
    ]
    for col in expected_cols:
        if col not in df.columns:
            df[col] = 0

    return df[expected_cols]

def predict(model, processed_input):
    """
    Predict churn probability using the trained model.
    """
    prediction_proba = model.predict_proba(processed_input)[:, 1]
    prediction = model.predict(processed_input)
    return prediction[0], prediction_proba[0]