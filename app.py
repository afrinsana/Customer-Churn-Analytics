import streamlit as st
import pandas as pd
from utils.utils import load_model, preprocess_input, predict

# Load the trained model
model = load_model()

# Streamlit page config
st.set_page_config(page_title="Customer Churn Prediction App", page_icon="📈")

# Title
st.title("🔮 Customer Churn Prediction")
st.subheader("Predict whether a customer is likely to churn.")

# Sidebar for user input
st.sidebar.header("Enter Customer Details")

def user_input_features():
    gender = st.sidebar.selectbox('Gender', ['Male', 'Female'])
    SeniorCitizen = st.sidebar.selectbox('Senior Citizen', [0, 1])
    Partner = st.sidebar.selectbox('Partner', ['Yes', 'No'])
    Dependents = st.sidebar.selectbox('Dependents', ['Yes', 'No'])
    tenure = st.sidebar.slider('Tenure (months)', 0, 72, 12)
    MonthlyCharges = st.sidebar.slider('Monthly Charges', 0.0, 150.0, 50.0)
    TotalCharges = st.sidebar.slider('Total Charges', 0.0, 8000.0, 1500.0)
    PhoneService = st.sidebar.selectbox('Phone Service', ['Yes', 'No'])

    data = {
        'gender': gender,
        'SeniorCitizen': SeniorCitizen,
        'Partner': Partner,
        'Dependents': Dependents,
        'tenure': tenure,
        'MonthlyCharges': MonthlyCharges,
        'TotalCharges': TotalCharges,
        'PhoneService': PhoneService
    }
    return data

user_input = user_input_features()

# When predict button is clicked
if st.button('Predict'):
    processed_input = preprocess_input(user_input)
    prediction, prediction_proba = predict(model, processed_input)

    if prediction == 1:
        st.error(f"⚠ High risk of churn! (Probability: {prediction_proba:.2f})")
    else:
        st.success(f"✅ Customer likely to stay! (Probability: {1 - prediction_proba:.2f})")

    st.subheader("Details Entered:")
    st.json(user_input)

# Footer
st.markdown("---")
st.caption("Developed with ❤ by Afrin Sana")