
import streamlit as st
import pandas as pd
import joblib
import numpy as np

# Load the pre-trained model
model = joblib.load('../model/churn_model.pkl')

# Function to predict churn
def predict_churn(data):
    prediction = model.predict([data])
    return "Churn" if prediction[0] == 1 else "No Churn"

# Streamlit app interface
st.title("Customer Churn Prediction")
st.write("Enter customer details for churn prediction")

# Input fields for customer features (Example values)
tenure = st.slider("Tenure (Months)", 0, 72, 24)
monthly_charges = st.number_input("Monthly Charges", min_value=0.0, value=30.0)
total_charges = st.number_input("Total Charges", min_value=0.0, value=1000.0)
senior_citizen = st.radio("Senior Citizen", options=[0, 1])

# Prepare input data as a list
input_data = [tenure, monthly_charges, total_charges, senior_citizen]

if st.button("Predict Churn"):
    result = predict_churn(input_data)
    st.write(f"Prediction: {result}")
