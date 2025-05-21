import joblib
import os
import json
import numpy as np

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

# Load models and accuracies once
models = {}
for name in MODEL_NAMES:
    model_path = f"models/{name.replace(' ', '_')}_best.joblib"
    if os.path.exists(model_path):
        models[name] = joblib.load(model_path)
    else:
        models[name] = None

# Load best accuracies
best_accuracies = {}
acc_path = "models/best_accuracies.json"
if os.path.exists(acc_path):
    with open(acc_path, "r") as f:
        best_accuracies = json.load(f)


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