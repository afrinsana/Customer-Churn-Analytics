import shap
import pandas as pd
import pickle
import matplotlib.pyplot as plt

# Load the trained model and scaler
with open('models/model.pkl', 'rb') as model_file:
    model = pickle.load(model_file)

with open('models/scaler.pkl', 'rb') as scaler_file:
    scaler = pickle.load(scaler_file)

# Example: Load a sample dataset to explain (replace with your real data if needed)
sample_data = pd.DataFrame({
    'gender': ['Female'],
    'SeniorCitizen': [0],
    'Partner': ['Yes'],
    'Dependents': ['No'],
    'tenure': [5],
    'PhoneService': ['Yes'],
    'MultipleLines': ['No'],
    'InternetService': ['DSL'],
    'OnlineSecurity': ['No'],
    'OnlineBackup': ['Yes'],
    'DeviceProtection': ['No'],
    'TechSupport': ['No'],
    'StreamingTV': ['No'],
    'StreamingMovies': ['No'],
    'Contract': ['Month-to-month'],
    'PaperlessBilling': ['Yes'],
    'PaymentMethod': ['Electronic check'],
    'MonthlyCharges': [70.35],
    'TotalCharges': [350.5]
})

# Encoding categorical variables manually
categorical_cols = ['gender', 'Partner', 'Dependents', 'PhoneService', 'MultipleLines',
                    'InternetService', 'OnlineSecurity', 'OnlineBackup', 'DeviceProtection',
                    'TechSupport', 'StreamingTV', 'StreamingMovies', 'Contract',
                    'PaperlessBilling', 'PaymentMethod']

sample_data_encoded = pd.get_dummies(sample_data, columns=categorical_cols)
# Add missing columns if needed (model expects exact features)
model_features = model.feature_names_in_
for col in model_features:
    if col not in sample_data_encoded.columns:
        sample_data_encoded[col] = 0
sample_data_encoded = sample_data_encoded[model_features]

# Scale numerical values
sample_data_scaled = scaler.transform(sample_data_encoded)

# Create SHAP Explainer
explainer = shap.Explainer(model)
shap_values = explainer(sample_data_scaled)

# Plot SHAP Explanation
shap.plots.waterfall(shap_values[0], max_display=10)
plt.show()