@echo off
echo Setting up Python virtual environment...

REM Create virtual environment if it doesn't exist
if not exist venv (
    echo Creating virtual environment...
    python -m venv venv
    
    REM Activate virtual environment
    echo Activating virtual environment...
    call venv\Scripts\activate.bat
    
    REM Update pip to latest version
    echo Updating pip to latest version...
    python -m pip install --upgrade pip
    
    REM Install dependencies
    echo Installing dependencies...
    pip install -r requirements.txt
    pip install streamlit
) else (
    REM Activate existing virtual environment
    echo Activating existing virtual environment...
    call venv\Scripts\activate.bat
    
    REM Check if requirements are installed
    pip freeze > temp_requirements.txt
    findstr /I /G:requirements.txt temp_requirements.txt > nul
    if errorlevel 1 (
        echo Installing missing dependencies...
        pip install -r requirements.txt
    )
    del temp_requirements.txt
    
    REM Check if streamlit is installed
    pip freeze | findstr /I "streamlit" > nul
    if errorlevel 1 (
        echo Installing streamlit...
        pip install streamlit
    )
)

REM Run the Streamlit app
echo Starting Streamlit app...
streamlit run app.py

REM Deactivate virtual environment when done
call deactivate 