import requests

url = "http://127.0.0.1:5000/predict"

data = {
    "SeniorCitizen": 0,
    "tenure": 5,
    "PhoneService": 1,
    "MultipleLines": 0,
    "OnlineSecurity": 0,
    "OnlineBackup": 1,
    "DeviceProtection": 0,
    "TechSupport": 0,
    "StreamingTV": 0,
    "StreamingMovies": 0,
    "MonthlyCharges": 70.35,
    "TotalCharges": 350.75,
    "TotalServices": 2,
    "IsNewCustomer": 1,
    "gender_Male": 1,
    "Partner_Yes": 0,
    "Dependents_Yes": 0,
    "InternetService_Fiber optic": 1,
    "InternetService_No": 0,
    "Contract_One year": 0,
    "Contract_Two year": 0,
    "PaymentMethod_Credit card (automatic)": 0,
    "PaymentMethod_Electronic check": 1,
    "PaymentMethod_Mailed check": 0,
    "PaperlessBilling_Yes": 1
}

response = requests.post(url, json=data)
print("Status Code:", response.status_code)
print("Response:", response.json())
