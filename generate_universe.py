# generate_universe.py

from app import create_app
from extensions import db
from utils.universe_generator import generate_universe

app = create_app()

with app.app_context():
    generate_universe()
