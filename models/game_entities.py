# models/game_entities.py

from extensions import db

class Building(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    building_type_id = db.Column(db.Integer, nullable=False)
    planet_id = db.Column(db.Integer, db.ForeignKey('planet.id'), nullable=False)
    level = db.Column(db.Integer, default=1)
    population_assigned = db.Column(db.Integer, default=0)
    # Construction status
    is_under_construction = db.Column(db.Boolean, default=False)
    construction_time_remaining = db.Column(db.Integer, default=0)

class Research(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    research_type_id = db.Column(db.Integer, nullable=False)
    planet_id = db.Column(db.Integer, db.ForeignKey('planet.id'), nullable=False)
    progress = db.Column(db.Float, default=0.0)
    is_completed = db.Column(db.Boolean, default=False)
    population_assigned = db.Column(db.Integer, default=0)

class Ship(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), nullable=False)
    design = db.Column(db.Text, nullable=False)
    owner_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

class Fleet(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), nullable=False)
    ships = db.Column(db.PickleType, nullable=False)  # Stores a list of ship IDs
    owner_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    location_planet_id = db.Column(db.Integer, db.ForeignKey('planet.id'), nullable=False)
