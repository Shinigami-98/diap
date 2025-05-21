#!/bin/bash

# Create virtual environment if it doesn't exist
if [ ! -d "venv" ]; then
    echo "Creating virtual environment..."
    python3 -m venv venv
    
    # Activate virtual environment
    echo "Activating virtual environment..."
    source venv/bin/activate
    
    # Update pip to latest version
    echo "Updating pip to latest version..."
    pip install --upgrade pip
    
    # Install dependencies
    echo "Installing dependencies..."
    pip install -r requirements.txt
    pip install streamlit
else
    # Activate existing virtual environment
    echo "Activating existing virtual environment..."
    source venv/bin/activate
    
    # Check if requirements are installed
    if ! pip freeze | grep -q -f requirements.txt; then
        echo "Installing missing dependencies..."
        pip install -r requirements.txt
    fi
    
    # Check if streamlit is installed
    if ! pip freeze | grep -q "streamlit"; then
        echo "Installing streamlit..."
        pip install streamlit
    fi
fi

# Run the Streamlit app
echo "Starting Streamlit app..."
streamlit run app.py