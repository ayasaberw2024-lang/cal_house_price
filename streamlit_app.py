import streamlit as st
import numpy as np
import joblib

model = joblib.load("xgb_model.pkl")
feature_names = joblib.load("features.pkl")

st.title("🏠 House Price Prediction")

input_data = []

# Loop على الفيتشرز
for feature in feature_names:
    value = st.number_input(feature)
    input_data.append(value)

if st.button("Predict Price"):
    features_array = np.array([input_data])

    prediction = model.predict(features_array)

    st.success(f"Predicted Price: {prediction[0]:.2f}")