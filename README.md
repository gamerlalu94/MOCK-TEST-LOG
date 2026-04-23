# Cricket Scoring Web Application 🏏

A modern, professional cricket scoring application built with Flask, featuring real-time scoring, partnership tracking, player statistics, and comprehensive match results.

**Latest Version**: Enhanced with accurate stopwatch, innings summary, and run rate reference tools
**Last Updated**: April 2026

## 🚀 Quick Start (Effortless Launch)

### For Linux/macOS:
```bash
./start.sh
```

### For Windows:
```bash
start.bat
```

That's it! The app will automatically:
- ✅ Check for virtual environment
- ✅ Activate the environment  
- ✅ Install dependencies if needed
- ✅ Start the Flask server
- 📱 Available at: `http://127.0.0.1:5000`

## 📋 Manual Setup (Alternative)

If you prefer manual setup or the automated script fails:

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

### 4. Run the Application
```bash
python run.py
```

## 🎯 Features

- **Real-time Scoring** - Live cricket match scoring with timer
- **Partnership Tracking** - Detailed partnership statistics
- **Player Statistics** - Batting and bowling stats visible mid-game
- **Professional UI** - Responsive design with dark theme
- **Match Results** - Comprehensive results with winner determination
- **Keyboard Shortcuts** - Efficient scoring with keyboard controls
- **Undo Functionality** - Correct mistakes with undo feature
- **Accurate Stopwatch** - Phone-quality timer using requestAnimationFrame for precise timing
- **Innings Summary** - First innings summary modal before starting second innings
- **Run Rate Reference** - Current and required run rate display during second innings chase

## 🏗️ Project Structure

```
.
├── app/                      # Application package
│   ├── __init__.py          # Flask app factory
│   ├── routes.py            # Application routes
│   ├── templates/           # HTML templates
│   │   ├── cricket.html     # Team setup page
│   │   ├── toss.html        # Coin toss simulator
│   │   ├── scorecard.html   # Live scoring interface
│   │   ├── results.html     # Match results page
│   │   └── about.html       # About page
│   └── static/              # Static files (CSS, JS, images)
│       └── css/
│           ├── cricket.css
│           └── scorecard.css
├── config.py                # Configuration settings
├── run.py                   # Application entry point
├── start.sh                 # Linux/macOS launcher
├── start.bat                # Windows launcher
├── requirements.txt         # Python dependencies
├── .env.example             # Environment variables template
├── .gitignore              # Git ignore file
└── README.md               # This file
```

## 🎮 How to Use

1. **Setup Teams**: Start at `/cricket` to configure teams and players
2. **Coin Toss**: Go to `/toss` for the toss simulation  
3. **Live Scoring**: Use `/scorecard` for real-time match scoring
4. **View Results**: Check `/results` for comprehensive match summary

### Keyboard Shortcuts (in scorecard):
- `0-6` - Record runs
- `W` - Wide ball
- `Shift+W` - Wicket
- `Space` - Start/stop timer
- `Backspace` - Undo last ball

## ⭐ Recent Enhancements

### ⏱️ Accurate Stopwatch
- Upgraded from `setInterval` to `requestAnimationFrame` for phone-quality precision
- Sub-millisecond accuracy matching modern stopwatch apps
- Smoother animations and better performance

### 📊 First Innings Summary
- Professional summary modal appears before starting second innings
- Displays final score, wickets, overs, and run rate
- Shows target for second innings (runs + 1)
- Clean transition to player selection

### 📈 Run Rate Reference Panel
- **Current Run Rate**: Shows current scoring rate (runs per over)
- **Required Run Rate**: Displays needed rate to reach target during chase
- Only visible during second innings for relevant reference
- Smart calculations for limited overs matches
- Shows runs needed and overs remaining

## 📱 Available Routes

- `/` - Home page (redirects to cricket)
- `/cricket` - Team setup and player selection
- `/toss` - Coin toss simulator
- `/scorecard` - Live match scoring interface
- `/results` - Match results and statistics
- `/about` - About page
- `/api/validate-players` - Player validation API

## 🛠️ Technical Stack

- **Backend**: Flask 2.3.2 (Python web framework)
- **Frontend**: HTML5, CSS3, Vanilla JavaScript
- **State Management**: JavaScript gameState with localStorage
- **Architecture**: MVC pattern with Blueprint routing
- **Styling**: Responsive design with mobile-first approach
- **Timing**: requestAnimationFrame for high-precision stopwatch functionality

## 🔧 Development

To enable debug mode during development, ensure `FLASK_ENV=development` in your `.env` file.

## 📦 Dependencies

- **Flask** - Web framework
- **python-dotenv** - Environment variable management
- **Werkzeug** - WSGI utility library
