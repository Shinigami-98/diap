import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression, SGDClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline
import xgboost as xgb
import os
import joblib
import json

def train_and_save_models(dataLocation="datasets/diabetes_binary_balanced.csv", n_iterations=40):
    columns = [
        "Diabetes_binary",
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

    dataFinal = pd.read_csv(dataLocation, usecols=columns)
    X = dataFinal.drop("Diabetes_binary", axis=1)
    y = dataFinal["Diabetes_binary"]

    os.makedirs("models", exist_ok=True)

    models = {
        "Random Forest": RandomForestClassifier(),
        "Logistic Regression": LogisticRegression(max_iter=1000),
        "XGBoost": xgb.XGBClassifier(),
        "KNN": KNeighborsClassifier(),
        "Decision Tree": DecisionTreeClassifier(),
        "SGD": SGDClassifier(),
    }

    best_models = {}
    best_accuracies = {}
    for name in models.keys():
        best_accuracies[name] = 0.0

    for iteration in range(1, n_iterations + 1):
        X_train, X_test, y_train, y_test = train_test_split(
            X, y, test_size=0.2, random_state=None, stratify=y
        )
        for name, model in models.items():
            if name in ["Logistic Regression", "KNN", "SGD"]:
                pipeline = Pipeline([("scaler", StandardScaler()), ("model", model)])
                pipeline.fit(X_train, y_train)
                y_pred = pipeline.predict(X_test)
                current_model = pipeline
            else:
                model.fit(X_train, y_train)
                y_pred = model.predict(X_test)
                current_model = model
            accuracy = accuracy_score(y_test, y_pred)
            if accuracy > best_accuracies[name]:
                best_accuracies[name] = accuracy
                best_models[name] = current_model
                model_filename = f"models/{name.replace(' ', '_')}_best.joblib"
                joblib.dump(current_model, model_filename)

    # Save best accuracies to JSON
    with open("models/best_accuracies.json", "w") as f:
        json.dump(best_accuracies, f)

if __name__ == "__main__":
    train_and_save_models() 