import streamlit as st
import joblib
import numpy as np

model = joblib.load("credit_fraud_model.pkl")

st.title("Credit Card Fraud Detection")

inputs = []

for i in range(30):
    value = st.number_input(f"Feature {i+1}")
    inputs.append(value)

if st.button("Predict"):
    data = np.array([inputs])
    prediction = model.predict(data)

    if prediction[0] == 1:
        st.error("Fraud Transaction Detected")
    else:
        st.success("Normal Transaction")