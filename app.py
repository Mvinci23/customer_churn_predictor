import streamlit as st
import pandas as pd
import joblib

st.title("Customer Churn Prediction")

# Load model
model = joblib.load("final_churn_model.pkl")

st.header("Enter Customer Information")

gender = st.selectbox("Gender", ["Male","Female"])
SeniorCitizen = st.selectbox("Senior Citizen", [0,1])
Partner = st.selectbox("Partner", ["Yes","No"])
Dependents = st.selectbox("Dependents", ["Yes","No"])
tenure = st.slider("Tenure (Months)",0,72,12)

PhoneService = st.selectbox("Phone Service", ["Yes","No"])
MultipleLines = st.selectbox("Multiple Lines", ["No","Yes","No phone service"])

InternetService = st.selectbox("Internet Service", ["DSL","Fiber optic","No"])

OnlineSecurity = st.selectbox("Online Security", ["No","Yes","No internet service"])
OnlineBackup = st.selectbox("Online Backup", ["No","Yes","No internet service"])
DeviceProtection = st.selectbox("Device Protection", ["No","Yes","No internet service"])
TechSupport = st.selectbox("Tech Support", ["No","Yes","No internet service"])

StreamingTV = st.selectbox("Streaming TV", ["No","Yes","No internet service"])
StreamingMovies = st.selectbox("Streaming Movies", ["No","Yes","No internet service"])

Contract = st.selectbox("Contract", ["Month-to-month","One year","Two year"])

PaperlessBilling = st.selectbox("Paperless Billing", ["Yes","No"])

PaymentMethod = st.selectbox(
    "Payment Method",
    [
        "Electronic check",
        "Mailed check",
        "Bank transfer (automatic)",
        "Credit card (automatic)"
    ]
)

MonthlyCharges = st.number_input("Monthly Charges",0.0,200.0,70.0)
TotalCharges = st.number_input("Total Charges",0.0,10000.0,1000.0)

# Create dataframe
input_df = pd.DataFrame({
    "gender":[gender],
    "SeniorCitizen":[SeniorCitizen],
    "Partner":[Partner],
    "Dependents":[Dependents],
    "tenure":[tenure],
    "PhoneService":[PhoneService],
    "MultipleLines":[MultipleLines],
    "InternetService":[InternetService],
    "OnlineSecurity":[OnlineSecurity],
    "OnlineBackup":[OnlineBackup],
    "DeviceProtection":[DeviceProtection],
    "TechSupport":[TechSupport],
    "StreamingTV":[StreamingTV],
    "StreamingMovies":[StreamingMovies],
    "Contract":[Contract],
    "PaperlessBilling":[PaperlessBilling],
    "PaymentMethod":[PaymentMethod],
    "MonthlyCharges":[MonthlyCharges],
    "TotalCharges":[TotalCharges]
})

# Prediction
if st.button("Predict Churn"):
    
    prediction = model.predict(input_df)[0]
    probability = model.predict_proba(input_df)[0][1]

    if prediction == 1:
        st.error(f"Customer likely to CHURN ❌ (Probability: {probability:.2f})")
    else:
        st.success(f"Customer likely to STAY ✅ (Probability: {probability:.2f})")