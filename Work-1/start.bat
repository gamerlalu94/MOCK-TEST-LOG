@echo off
REM Cricket Scoring App Launcher (Windows)
REM This script starts the Flask web application effortlessly

echo 🏏 Starting Cricket Scoring Web App...
echo =====================================

REM Check if virtual environment exists
if not exist "venv" (
    echo ❌ Virtual environment not found!
    echo Please run: python -m venv venv && venv\Scripts\activate && pip install -r requirements.txt
    pause
    exit /b 1
)

REM Activate virtual environment
echo 🔧 Activating virtual environment...
call venv\Scripts\activate.bat

REM Check if Flask is installed
python -c "import flask" 2>nul
if errorlevel 1 (
    echo ❌ Flask not installed!
    echo Installing dependencies...
    pip install -r requirements.txt
)

REM Start the Flask application
echo 🚀 Starting Flask server...
echo 📱 App will be available at: http://127.0.0.1:5000
echo 🎯 Press Ctrl+C to stop the server
echo.

python run.py
