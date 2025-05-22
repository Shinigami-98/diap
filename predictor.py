import joblib
import os
import json
import numpy as np
import subprocess

MODEL_NAMES = [
    "Random Forest",
    "Logistic Regression",
    "XGBoost",
    "KNN",
    "Decision Tree",
    "SGD",
]

FEATURES = [
    "HighBP",
    "HighChol",
    "BMI",
    "Smoker",
    "Stroke",
    "HeartDiseaseorAttack",
    "PhysActivity",
    "Fruits",
    "Veggies",
    "HvyAlcoholConsump",
    "Age",
]

# Load models and accuracies
models = {}
best_accuracies = {}

def load_models():
    global models, best_accuracies
    # Load models
    for name in MODEL_NAMES:
        model_path = f"models/{name.replace(' ', '_')}_best.joblib"
        try:
            models[name] = joblib.load(model_path)
        except Exception as e:
            print(f"Error loading model {name}: {e}")
            models[name] = None

    # Load best accuracies
    acc_path = "models/best_accuracies.json"
    try:
        with open(acc_path, "r") as f:
            best_accuracies = json.load(f)
    except Exception as e:
        print(f"Error loading accuracies: {e}")
        best_accuracies = {}

# Initialize models on module import
load_models()

def predict_all(user_input_df):
    results = []
    for name in MODEL_NAMES:
        model = models.get(name)
        acc = best_accuracies.get(name)
        if model is not None:
            pred = model.predict(user_input_df)[0]
            results.append((name, pred, acc))
        else:
            results.append((name, "Model not found", acc))
    return results 