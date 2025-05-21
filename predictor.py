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

def check_and_train_models():
    """Check if models exist, if not trigger training"""
    model_path = f"models/{MODEL_NAMES[0].replace(' ', '_')}_best.joblib"
    if not os.path.exists(model_path):
        print("Models not found. Starting initial training...")
        subprocess.run(["python3", "train_backend.py"], check=True)
        print("Initial training complete!")

# Load models and accuracies
models = {}
best_accuracies = {}

def load_models():
    """Load all models and accuracies"""
    global models, best_accuracies
    
    # Check if models need training
    check_and_train_models()
    
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
    """
    user_input_df: pandas DataFrame with one row and correct feature columns
    Returns: list of (model_name, prediction, accuracy)
    """
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