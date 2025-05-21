 # Diabetes Prediction Application

A machine learning application that predicts diabetes risk using various classification models. The application is built with Python and Streamlit, providing an interactive web interface for predictions.

## Features

- Multiple machine learning models (Random Forest, Logistic Regression, XGBoost, KNN, Decision Tree, SGD)
- Interactive web interface using Streamlit
- Model training and evaluation pipeline
- Easy setup and deployment scripts

## Prerequisites

- Python 3.9 or higher
- pip (Python package installer)

## Installation

### Automatic Setup (Recommended)

We provide setup scripts for both Windows and Linux/macOS users:

#### For Windows Users:
1. Double-click `run.bat` or run it from the command prompt:
```bash
run.bat
```

#### For Linux/macOS Users:
1. Open terminal in the project directory
2. Make the script executable (if not already):
```bash
chmod +x run.sh
```
3. Run the script:
```bash
./run.sh
```

The scripts will automatically:
- Create a Python virtual environment
- Install all required dependencies
- Start the Streamlit application

### Manual Setup

If you prefer to set up manually:

1. Create a virtual environment:
```bash
# Windows
python -m venv venv

# Linux/macOS
python3 -m venv venv
```

2. Activate the virtual environment:
```bash
# Windows
venv\Scripts\activate

# Linux/macOS
source venv/bin/activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
pip install streamlit
```

4. Run the application:
```bash
streamlit run app.py
```

## Usage

1. After running the setup script or manual installation, the Streamlit interface will automatically open in your default web browser
2. If it doesn't open automatically, you can access it at `http://localhost:8501`
3. Use the interface to input patient data and get diabetes risk predictions

## Project Structure

```
.
├── app.py              # Streamlit application
├── train_backend.py    # Model training script
├── requirements.txt    # Python dependencies
├── run.sh             # Linux/macOS setup script
├── run.bat            # Windows setup script
└── models/            # Directory for saved models
```

## Dependencies

- pandas
- scikit-learn
- xgboost
- joblib
- streamlit

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request
