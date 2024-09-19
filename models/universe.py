# models/universe.py

from extensions import db
from config.planets import PLANETS

class Galaxy(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), nullable=False)
    number = db.Column(db.Integer, unique=True, nullable=False)
    clusters = db.relationship('Cluster', backref='galaxy', lazy=True)

class Cluster(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), nullable=False)
    galaxy_id = db.Column(db.Integer, db.ForeignKey('galaxy.id'), nullable=False)
    solar_systems = db.relationship('SolarSystem', backref='cluster', lazy=True)

class SolarSystem(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), nullable=False)
    cluster_id = db.Column(db.Integer, db.ForeignKey('cluster.id'), nullable=False)
    planets = db.relationship('Planet', backref='solar_system', lazy=True)

class Planet(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), nullable=False)
    planet_type_id = db.Column(db.Integer, nullable=False)
    solar_system_id = db.Column(db.Integer, db.ForeignKey('solar_system.id'), nullable=False)
    owner_id = db.Column(
        db.Integer,
        db.ForeignKey('user.id', name='fk_planet_owner'),
        nullable=True
    )

    # Resources and attributes
    aluminium = db.Column(db.Float, default=0)
    biomass = db.Column(db.Float, default=0)
    crystals = db.Column(db.Float, default=0)
    deuterium = db.Column(db.Float, default=0)
    ferrite = db.Column(db.Float, default=0)
    etereon = db.Column(db.Float, default=0)
    gold = db.Column(db.Float, default=0)
    # Population
    population = db.Column(db.Integer, default=0)
    population_cap = db.Column(db.Integer, default=100)
    # Relationships
    buildings = db.relationship('Building', backref='planet', lazy=True)
    researches = db.relationship('Research', backref='planet', lazy=True)

    @property
    def planet_type(self):
        return PLANETS.get(self.planet_type_id)
