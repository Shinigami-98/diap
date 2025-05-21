@echo off
echo Setting up Python virtual environment...

REM Create virtual environment if it doesn't exist
if not exist venv (
    echo Creating virtual environment...
    python -m venv venv
)

REM Activate virtual environment
echo Activating virtual environment...
call venv\Scripts\activate.bat

REM Install dependencies
echo Installing dependencies...
pip install -r requirements.txt
pip install streamlit

REM Run the Streamlit app
echo Starting Streamlit app...
streamlit run app.py

REM Deactivate virtual environment when done
call deactivate 