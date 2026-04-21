# Python Flask Web Application

A modern Python web application built with Flask framework, ready for development and deployment.

## Project Structure

```
.
├── app/                      # Application package
│   ├── __init__.py          # Flask app factory
│   ├── routes.py            # Application routes
│   ├── templates/           # HTML templates
│   │   ├── index.html
│   │   └── about.html
│   └── static/              # Static files (CSS, JS, images)
├── config.py                # Configuration settings
├── run.py                   # Application entry point
├── requirements.txt         # Python dependencies
├── .env.example             # Environment variables template
├── .gitignore              # Git ignore file
└── README.md               # This file
```

## Prerequisites

- Python 3.8 or higher
- pip (Python package manager)

## Setup Instructions

### 1. Create Virtual Environment

```bash
python -m venv venv
```

### 2. Activate Virtual Environment

**On Linux/macOS:**
```bash
source venv/bin/activate
```

**On Windows:**
```bash
venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Create Environment File

Copy `.env.example` to `.env` and update with your settings:
```bash
cp .env.example .env
```

### 5. Run the Application

```bash
python run.py
```

The application will be available at: `http://localhost:5000`

## Available Routes

- `/` - Home page
- `/about` - About page
- `/api/hello` - JSON API endpoint

## Project Features

- **Application Factory Pattern** - Flexible app configuration
- **Configuration Management** - Environment-based settings
- **Blueprint Routing** - Modular route organization
- **Jinja2 Templates** - Dynamic HTML rendering
- **Static Files Support** - CSS, JavaScript, and images
- **Environment Variables** - Secure configuration handling

## Development

To enable debug mode during development, ensure `FLASK_ENV=development` in your `.env` file.

## Next Steps

1. Add more routes in `app/routes.py`
2. Create additional templates in `app/templates/`
3. Add static files (CSS, JS, images) to `app/static/`
4. Implement database models if needed
5. Add authentication/authorization as required
6. Create unit tests for your routes

## Dependencies

- **Flask** - Web framework
- **python-dotenv** - Environment variable management
- **Werkzeug** - WSGI utilities

For more information, visit:
- [Flask Documentation](https://flask.palletsprojects.com/)
- [Flask Best Practices](https://flask.palletsprojects.com/patterns/)

## License

This project is licensed under the MIT License.
