from extensions import db  # No circular import this way

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)  # Store as a hashed password in the future
    race = db.Column(db.String(50), nullable=False)  # Store race choice
    starting_planet = db.Column(db.String(100), nullable=True)  # Planet assigned to the user

class Galaxy(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    clusters = db.relationship('Cluster', backref='galaxy', lazy=True)

class Cluster(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    galaxy_id = db.Column(db.Integer, db.ForeignKey('galaxy.id'), nullable=False)
    systems = db.relationship('SolarSystem', backref='cluster', lazy=True)

class SolarSystem(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    cluster_id = db.Column(db.Integer, db.ForeignKey('cluster.id'), nullable=False)
    planets = db.relationship('Planet', backref='system', lazy=True)

class Planet(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    size = db.Column(db.String(50), nullable=False)
    planet_type = db.Column(db.String(50), nullable=False)
    solar_system_id = db.Column(db.Integer, db.ForeignKey('solar_system.id'), nullable=False)
    resources = db.Column(db.JSON, nullable=False)
    
class Race(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)  # Easily modifiable name
    description = db.Column(db.String(255), nullable=True)
    traits = db.Column(db.JSON, nullable=True)  # Traits of the race
    
class Resource(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)  # Easily modifiable name
    description = db.Column(db.String(255), nullable=True)
    rarity = db.Column(db.String(50), nullable=False)

class Building(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)  # Easily modifiable name
    level = db.Column(db.Integer, default=1)
    planet_id = db.Column(db.Integer, db.ForeignKey('planet.id'), nullable=False)
    resource_cost = db.Column(db.JSON, nullable=False)

class Research(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    progress = db.Column(db.Integer, default=0)
    planet_id = db.Column(db.Integer, db.ForeignKey('planet.id'), nullable=False)
    resource_cost = db.Column(db.JSON, nullable=False)
    time_required = db.Column(db.Integer, nullable=False)