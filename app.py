import streamlit as st
import numpy as np
import subprocess
from predictor import predict_all, FEATURES, load_models
import pandas as pd
import os

# Initialize session state for first run
if 'initial_load' not in st.session_state:
    st.session_state.initial_load = True

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

# Create input fields
for name in FEATURES:
    min_val, max_val, default = feature_ranges[name]
    if max_val - min_val > 1:
        user_input[name] = st.sidebar.slider(name, min_value=min_val, max_value=max_val, value=default)
    else:
        user_input[name] = st.sidebar.number_input(name, min_value=min_val, max_value=max_val, value=default, step=1)

# Function to retrain models
def retrain_models():
    with st.spinner("Retraining models. This may take a while..."):
        try:
            result = subprocess.run(["python3", "train_backend.py"], capture_output=True, text=True, check=True)
            load_models()
            st.success("Models trained successfully!")
        except subprocess.CalledProcessError as e:
            st.error(f"Error during retraining: {e.stderr}")
            st.stop()

# Button to retrain models
if st.sidebar.button("Retrain Models (Backend)"):
    retrain_models()
    st.rerun()

# Main area: Predict
st.header("Prediction Results")

MODEL_FILES = [
    f"models/{name.replace(' ', '_')}_best.joblib" for name in [
        "Random Forest",
        "Logistic Regression",
        "XGBoost",
        "KNN",
        "Decision Tree",
        "SGD",
    ]
]
MODEL_FILES.append("models/best_accuracies.json")

missing_models = [f for f in MODEL_FILES if not os.path.isfile(f)]

if missing_models:
    retrain_models()

input_df = pd.DataFrame([user_input])  # Ensures feature names are present

try:
    results = predict_all(input_df)
    st.table([
        {"Model": n, "Prediction": p, "Best Accuracy": (f"{a:.4f}" if a is not None else "N/A")} for n, p, a in results
    ])
    st.info("Prediction: 1 = Diabetes, 0 = No Diabetes")
except Exception as e:
    st.error(f"Error making predictions: {str(e)}")
    st.info("If this is your first run, the app is training the models. Please wait a moment and refresh the page.") 