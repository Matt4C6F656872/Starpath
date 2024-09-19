# models/user.py

from extensions import db
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from config.races import RACES
from config.factions import FACTIONS

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)
    race_id = db.Column(db.Integer, nullable=False)
    faction_id = db.Column(db.Integer, nullable=False)
    starting_planet_id = db.Column(
        db.Integer,
        db.ForeignKey('planet.id', name='fk_user_starting_planet'),
        nullable=True
    )

    # Relationships
    owned_planets = db.relationship(
        'Planet',
        backref='owner',  # This creates the 'owner' attribute on Planet
        lazy=True,
        foreign_keys='Planet.owner_id'
    )

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    @property
    def race(self):
        return RACES.get(self.race_id)

    @property
    def faction(self):
        return FACTIONS.get(self.faction_id)
