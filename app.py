import streamlit as st
import joblib
model = joblib.load("model.pkl")
scaler = joblib.load("scaler.pkl")
st.sidebar.title("Customer Details")
st.title("Customer Churn Prediction")
st.write("Predict whether a customer is likely to churn based on customer information.")
tenure = st.sidebar.number_input(
    "Enter Customer Tenure (Months)",
    min_value=0,
    max_value=72
)
gender = st.sidebar.selectbox(
    "Gender",
    ["Female", "Male"]
)
senior = st.sidebar.selectbox(
    "Senior Citizen",
    [0, 1]
)

partner = st.sidebar.selectbox(
    "Partner",
    ["No", "Yes"]
)

dependents = st.sidebar.selectbox(
    "Dependents",
    ["No", "Yes"]
)

contract = st.sidebar.selectbox(
    "Contract",
    ["Month-to-month", "One year", "Two year"]
)

monthly = st.sidebar.number_input(
    "Monthly Charges",
    min_value=0.0
)

total = st.sidebar.number_input(
    "Total Charges",
    min_value=0.0
)
gender = 1 if gender == "Male" else 0

partner = 1 if partner == "Yes" else 0

dependents = 1 if dependents == "Yes" else 0

contract_mapping = {
    "Month-to-month": 0,
    "One year": 1,
    "Two year": 2
}

contract = contract_mapping[contract]
if st.sidebar.button("Predict Churn"):

    features = [[
        gender,
        senior,
        partner,
        dependents,
        tenure,
        contract,
        monthly,
        total
    ]]

    features = scaler.transform(features)

    prediction = model.predict(features)

    if prediction[0] == 1:
        st.error("🔴 Customer is likely to churn.")
    else:
        st.success("🟢 Customer is likely to stay.")