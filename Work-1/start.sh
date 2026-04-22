#!/bin/bash

# Cricket Scoring App Launcher
# This script starts the Flask web application effortlessly

echo "🏏 Starting Cricket Scoring Web App..."
echo "====================================="

# Check if virtual environment exists
if [ ! -d "venv" ]; then
    echo "❌ Virtual environment not found!"
    echo "Please run: python -m venv venv && source venv/bin/activate && pip install -r requirements.txt"
    exit 1
fi

# Activate virtual environment
echo "🔧 Activating virtual environment..."
source venv/bin/activate

# Check if Flask is installed
if ! python -c "import flask" 2>/dev/null; then
    echo "❌ Flask not installed!"
    echo "Installing dependencies..."
    pip install -r requirements.txt
fi

# Start the Flask application
echo "🚀 Starting Flask server..."
echo "📱 App will be available at: http://127.0.0.1:5000"
echo "🎯 Press Ctrl+C to stop the server"
echo ""

python run.py
