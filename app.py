import streamlit as st
import numpy as np
import subprocess
from predictor import predict_all, FEATURES
import pandas as pd

st.set_page_config(page_title="Diabetes Prediction App", layout="wide")
st.title("Diabetes Prediction (All Models)")

# Sidebar for input
st.sidebar.header("Input Features")
user_input = {}
# Reasonable defaults and ranges
feature_ranges = {
    "HighBP": (0, 1, 0),
    "HighChol": (0, 1, 0),
    "BMI": (10, 60, 25),
    "Smoker": (0, 1, 0),
    "Stroke": (0, 1, 0),
    "HeartDiseaseorAttack": (0, 1, 0),
    "PhysActivity": (0, 1, 1),
    "Fruits": (0, 1, 1),
    "Veggies": (0, 1, 1),
    "HvyAlcoholConsump": (0, 1, 0),
    "Age": (18, 90, 40),
}
for name in FEATURES:
    min_val, max_val, default = feature_ranges[name]
    if max_val - min_val > 1:
        user_input[name] = st.sidebar.slider(name, min_value=min_val, max_value=max_val, value=default)
    else:
        user_input[name] = st.sidebar.number_input(name, min_value=min_val, max_value=max_val, value=default, step=1)

# Button to retrain models
if st.sidebar.button("Retrain Models (Backend)"):
    with st.spinner("Retraining models. This may take a while..."):
        result = subprocess.run(["python3", "train_backend.py"], capture_output=True, text=True)
    st.success("Retraining complete! Models and accuracies updated.")
    st.rerun()

# Main area: Predict
st.header("Prediction Results")
input_df = pd.DataFrame([user_input])  # Ensures feature names are present
results = predict_all(input_df)

st.table([
    {"Model": n, "Prediction": p, "Best Accuracy": (f"{a:.4f}" if a is not None else "N/A")} for n, p, a in results
])

st.info("Prediction: 1 = Diabetes, 0 = No Diabetes") 