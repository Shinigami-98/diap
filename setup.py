from setuptools import setup

setup(
    name="diabetes_prediction",
    version="1.0",
    packages=[""],
    install_requires=[
        "pandas",
        "scikit-learn",
        "xgboost",
        "joblib"
    ],
    entry_points={
        "console_scripts": [
            "train_models=train_backend:main",
        ],
    },
) 