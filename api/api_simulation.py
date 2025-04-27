import requests
import random
import json

API_ENDPOINT = "http://localhost:8501/predict"  # Change if your endpoint is different

def generate_random_customer():
    customer_data = {
        "gender": random.choice(["Male", "Female"]),
        "SeniorCitizen": random.choice([0, 1]),
        "Partner": random.choice(["Yes", "No"]),
        "Dependents": random.choice(["Yes", "No"]),
        "tenure": random.randint(0, 72),
        "PhoneService": random.choice(["Yes", "No"]),
        "MultipleLines": random.choice(["Yes", "No", "No phone service"]),
        "InternetService": random.choice(["DSL", "Fiber optic", "No"]),
        "OnlineSecurity": random.choice(["Yes", "No", "No internet service"]),
        "OnlineBackup": random.choice(["Yes", "No", "No internet service"]),
        "DeviceProtection": random.choice(["Yes", "No", "No internet service"]),
        "TechSupport": random.choice(["Yes", "No", "No internet service"]),
        "StreamingTV": random.choice(["Yes", "No", "No internet service"]),
        "StreamingMovies": random.choice(["Yes", "No", "No internet service"]),
        "Contract": random.choice(["Month-to-month", "One year", "Two year"]),
        "PaperlessBilling": random.choice(["Yes", "No"]),
        "PaymentMethod": random.choice(["Electronic check", "Mailed check", "Bank transfer (automatic)", "Credit card (automatic)"]),
        "MonthlyCharges": round(random.uniform(20.0, 120.0), 2),
        "TotalCharges": round(random.uniform(20.0, 9000.0), 2)
    }
    return customer_data

def send_request(customer_data):
    headers = {'Content-Type': 'application/json'}
    response = requests.post(API_ENDPOINT, data=json.dumps(customer_data), headers=headers)
    return response.json()

if __name__ == "__main__":
    new_customer = generate_random_customer()
    result = send_request(new_customer)
    print("Sent customer data:", new_customer)
    print("Prediction Result:", result)