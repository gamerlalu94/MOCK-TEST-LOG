from flask import Blueprint, render_template, jsonify, request

main_bp = Blueprint('main', __name__)

@main_bp.route('/')
def index():
    """Home page"""
    return render_template('index.html', title='Home')

@main_bp.route('/cricket')
def cricket():
    """Cricket score tracking page"""
    return render_template('cricket.html', title='Cricket Scorer')

@main_bp.route('/api/hello')
def hello_api():
    """API endpoint that returns JSON"""
    return jsonify({
        'message': 'Hello from Python Flask!',
        'status': 'success'
    })

@main_bp.route('/api/validate-players', methods=['POST'])
def validate_players():
    """
    Validate player names and start cricket game
    
    Expected JSON:
    {
        "team1_name": "India",
        "team1_players": ["Virat", "Rohit", "Bumrah"],
        "team2_name": "Australia", 
        "team2_players": ["Smith", "Warner", "Cummins"]
    }
    """
    try:
        data = request.get_json()
        
        # Extract player lists
        team1_players = data.get('team1_players', [])
        team2_players = data.get('team2_players', [])
        team1_name = data.get('team1_name', 'Team 1')
        team2_name = data.get('team2_name', 'Team 2')
        
        # Validation 1: Check if players list is not empty
        if not team1_players or not team2_players:
            return jsonify({
                'status': 'error',
                'message': 'Both teams must have at least one player'
            }), 400
        
        # Validation 2: Check for empty names or duplicates
        for player in team1_players + team2_players:
            if not player.strip():
                return jsonify({
                    'status': 'error',
                    'message': 'Player names cannot be empty'
                }), 400
        
        # Validation 3: Check for duplicate names within a team
        if len(team1_players) != len(set(team1_players)):
            return jsonify({
                'status': 'error',
                'message': 'Team 1 has duplicate player names'
            }), 400
        
        if len(team2_players) != len(set(team2_players)):
            return jsonify({
                'status': 'error',
                'message': 'Team 2 has duplicate player names'
            }), 400
        
        # All validations passed!
        return jsonify({
            'status': 'success',
            'message': 'Players validated successfully',
            'game_data': {
                'team1': {
                    'name': team1_name,
                    'players': team1_players
                },
                'team2': {
                    'name': team2_name,
                    'players': team2_players
                }
            }
        }), 200
    
    except Exception as e:
        return jsonify({
            'status': 'error',
            'message': f'Server error: {str(e)}'
        }), 500

@main_bp.route('/toss')
def toss():
    """Coin toss simulator page"""
    return render_template('toss.html', title='Coin Toss')

@main_bp.route('/scorecard')
def scorecard():
    """Cricket scorecard page"""
    return render_template('scorecard.html', title='Scorecard')

@main_bp.route('/results')
def results():
    """Match results and player statistics page"""
    return render_template('results.html', title='Match Results')

@main_bp.route('/about')
def about():
    """About page"""
    return render_template('about.html', title='About')
