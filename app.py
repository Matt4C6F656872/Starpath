from flask import Flask, render_template, request, redirect, jsonify, session
from extensions import db  # Import db from extensions.py
from models import Galaxy, Cluster, SolarSystem, Planet, Race, Building, Research, Resource, User  # Import models
from config import BUILDINGS, RACES, RESOURCES  # Centralized configurations
import os
import random
from werkzeug.security import generate_password_hash, check_password_hash

# Initialize the Flask app
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///starpath.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = os.urandom(24)  # Secret key for sessions

# Initialize the db with the app
db.init_app(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/register', methods=['POST'])
def register():
    username = request.form['username']
    email = request.form['email']
    password = request.form['password']
    race_id = int(request.form['race_id'])
    race = RACES[race_id]["name"]

    # Check if username or email already exists
    if User.query.filter_by(username=username).first() or User.query.filter_by(email=email).first():
        return "Username or email already exists"

    # Hash the password before saving it
    hashed_password = generate_password_hash(password)

    new_user = User(username=username, email=email, password=hashed_password, race=race)
    db.session.add(new_user)
    db.session.commit()

    # Assign a starting planet based on race
    if race == "Terran":
        starting_planet = Planet.query.filter_by(planet_type="Paradise World").first()
    elif race == "Zythian":
        starting_planet = Planet.query.filter_by(planet_type="Crystal Planet").first()
    elif race == "Mycelian":
        starting_planet = Planet.query.filter_by(planet_type="Fungal World").first()
    elif race == "Volatian":
        starting_planet = Planet.query.filter_by(planet_type="Gas Giant").first()
    elif race == "Silicoid":
        starting_planet = Planet.query.filter_by(planet_type="Metal-Rich Planet").first()
    elif race == "Etherial":
        starting_planet = Planet.query.filter_by(planet_type="Quantum Flux World").first()
    
    # Ensure that no two players start on the same planet
    if starting_planet:
        if User.query.filter_by(starting_planet=starting_planet.name).first():
            return "This planet has already been assigned. Please try again."
        new_user.starting_planet = starting_planet.name
        db.session.commit()

    return redirect('/game')

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']
    
    user = User.query.filter_by(username=username).first()

    # Check if the user exists and verify the hashed password
    if user and check_password_hash(user.password, password):
        session['user_id'] = user.id
        return redirect('/game')
    else:
        return "Invalid credentials"

@app.route('/game')
def game():
    if 'user_id' in session:
        user = User.query.get(session['user_id'])
        planet = Planet.query.filter_by(name=user.starting_planet).first()

        # Display player's current planet and basic information
        return f"Welcome {user.username}, Race: {user.race}, Starting Planet: {planet.name}. Resources: {planet.resources}"

    return redirect('/')

@app.route('/generate_universe')
def generate_universe():
    # Example: Create 7 galaxies with clusters, solar systems, and planets
    for i in range(1, 8):
        galaxy = Galaxy(name=f"Galaxy {i}")
        db.session.add(galaxy)
        for j in range(1, 11):  # 10 clusters per galaxy
            cluster = Cluster(name=f"Cluster {j}", galaxy=galaxy)
            db.session.add(cluster)
            for k in range(1, 16):  # 15 solar systems per cluster
                system = SolarSystem(name=f"Solar System {k}", cluster=cluster)
                db.session.add(system)
                for l in range(1, 6):  # 5 planets per solar system
                    planet = Planet(
                        name=f"Planet {l}", 
                        size="Medium", 
                        planet_type="Paradise World",  # Or other types
                        solar_system=system,
                        resources={"Aluminium": 1000, "Biomass": 500}  # Example
                    )
                    db.session.add(planet)
    
    db.session.commit()
    return "Universe generated!"

@app.route('/generate_resources')
def generate_resources():
    planets = Planet.query.all()
    for planet in planets:
        for resource_name, production_rate in planet.resources.items():
            # Increase resources based on population and building level
            planet.resources[resource_name] += production_rate * random.uniform(1.0, 1.5)
        db.session.commit()
    
    return jsonify({"message": "Resources updated!"})

@app.route('/build', methods=['POST'])
def build():
    user = User.query.get(session['user_id'])
    planet = Planet.query.filter_by(name=user.starting_planet).first()

    building_id = int(request.form['building_id'])
    building_config = BUILDINGS[building_id]  # Fetch building details from config

    building = Building.query.filter_by(id=building_id, planet_id=planet.id).first()

    # Calculate costs using the formula from config
    cost = building_config["cost_formula"](building.level)

    cost_aluminium = cost["Aluminium"]
    cost_crystals = cost.get("Crystals", 0)

    # Check if enough resources are available
    if planet.resources["Aluminium"] >= cost_aluminium and planet.resources.get("Crystals", 0) >= cost_crystals:
        planet.resources["Aluminium"] -= cost_aluminium
        planet.resources["Crystals"] -= cost_crystals
        building.level += 1
        db.session.commit()
        return jsonify({"message": f"{building_config['name']} upgraded to level {building.level}"})
    
    return jsonify({"error": "Not enough resources"}), 400

@app.route('/research', methods=['POST'])
def research():
    user = User.query.get(session['user_id'])
    planet = Planet.query.filter_by(name=user.starting_planet).first()

    research_id = int(request.form['research_id'])
    research = Research.query.filter_by(id=research_id, planet_id=planet.id).first()

    # Check if resources are available
    cost_crystals = research.resource_cost["Crystals"]

    if planet.resources["Crystals"] >= cost_crystals:
        planet.resources["Crystals"] -= cost_crystals
        research.progress += 10  # Increment research progress
        db.session.commit()
        return jsonify({"message": f"Research progress: {research.progress}%"})
    
    return jsonify({"error": "Not enough resources"}), 400

@app.route('/rename/<string:entity_type>/<int:entity_id>', methods=['POST'])
def rename_entity(entity_type, entity_id):
    new_name = request.form['new_name']
    
    # Fetch and rename the entity based on type
    if entity_type == 'building':
        entity = Building.query.get(entity_id)
    elif entity_type == 'race':
        entity = Race.query.get(entity_id)
    elif entity_type == 'resource':
        entity = Resource.query.get(entity_id)
    else:
        return jsonify({"error": "Invalid entity type"}), 400

    # Update name and commit
    if entity:
        entity.name = new_name
        db.session.commit()
        return jsonify({"message": f"{entity_type.capitalize()} renamed to {new_name}"})
    
    return jsonify({"error": f"{entity_type.capitalize()} not found"}), 404

if __name__ == '__main__':
    with app.app_context():
        db.create_all()  # This will create the database and tables
    app.run(debug=True)