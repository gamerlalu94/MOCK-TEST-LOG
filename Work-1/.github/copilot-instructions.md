# Copilot Instructions for Python Web Application

- [x] Verify that the copilot-instructions.md file in the .github directory is created.

- [x] Clarify Project Requirements
  - Project type: Python web application with Flask
  - Framework: Flask
  - Language: Python 3.x

- [x] Scaffold the Project
  - Project structure created with Flask factory pattern
  - Virtual environment initialized at `venv/`
  - Directory structure includes app/, templates/, and static/ folders

- [x] Customize the Project
  - Flask app configured with application factory pattern
  - Routes setup with blueprints in `app/routes.py`
  - HTML templates created for home and about pages
  - API endpoint `/api/hello` added

- [x] Install Required Extensions
  - Python: Built-in VS Code support (no installation required)
  - Flask: Added to requirements.txt

- [x] Compile the Project
  - Dependencies installed successfully via pip
  - Virtual environment activated and verified
  - All packages from requirements.txt installed

- [x] Create and Run Task
  - Flask development server task created in `.vscode/tasks.json`
  - Default build task configured for easy launch

- [x] Launch the Project
  - Project setup complete and ready for development
  - Run with: `python -m venv venv && source venv/bin/activate && python run.py`
  - Access at: http://localhost:5000

- [x] Ensure Documentation is Complete
  - README.md created with setup instructions and project overview
  - .env.example provided as template
  - .gitignore configured for Python projects

## Project Structure
- app/ - Application package with routes and templates
- app/templates/ - HTML templates (index.html, about.html)
- app/static/ - Static files (CSS, JavaScript, images)
- config.py - Configuration settings for different environments
- requirements.txt - Python dependencies (Flask, python-dotenv, Werkzeug)
- .env - Environment variables
- .env.example - Environment variables template
- .vscode/tasks.json - VS Code development tasks
- README.md - Project documentation

## Setup Complete
Your Python Flask web application is ready to use! Next steps:
1. Review the project structure in the file explorer
2. Run the Flask server using the configured task
3. Access the app at http://localhost:5000
4. Customize routes and templates as needed
