# blueprints/main/routes.py

from flask import render_template
from flask_login import login_required, current_user
from . import main_bp

@main_bp.route('/')
def index():
    return render_template('main/index.html')

@main_bp.route('/game')
@login_required
def game():
    # Get user's planets
    planets = current_user.planets
    return render_template('main/game.html', planets=planets)
