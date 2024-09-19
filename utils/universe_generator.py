# utils/universe_generator.py

from extensions import db
from models.universe import Galaxy, Cluster, SolarSystem, Planet
from config.planets import PLANETS
from random import randint, choice

def generate_universe():
    # Check if universe already exists
    if Galaxy.query.first():
        print("Universe already exists.")
        return

    # Create 7 galaxies
    for galaxy_number in range(1, 8):
        galaxy = Galaxy(name=f"Galaxy {galaxy_number}", number=galaxy_number)
        db.session.add(galaxy)
        db.session.commit()

        # Create clusters in each galaxy
        for cluster_number in range(1, 6):  # Adjust number of clusters as needed
            cluster = Cluster(name=f"Cluster {cluster_number}", galaxy_id=galaxy.id)
            db.session.add(cluster)
            db.session.commit()

            # Create solar systems in each cluster
            for system_number in range(1, 6):  # Adjust number of systems as needed
                solar_system = SolarSystem(
                    name=f"System {system_number}", cluster_id=cluster.id
                )
                db.session.add(solar_system)
                db.session.commit()

                # Create planets in each solar system
                for planet_number in range(1, 6):  # Adjust number of planets as needed
                    planet_type_id = choice(list(PLANETS.keys()))
                    planet = Planet(
                        name=f"Planet {planet_number}",
                        planet_type_id=planet_type_id,
                        solar_system_id=solar_system.id
                    )
                    db.session.add(planet)
    db.session.commit()
    print("Universe generated successfully.")

def assign_starting_planet(user):
    from models.universe import Planet
    # Get homeworld planet types based on user's race
    race_planet_type_mapping = {
        1: 1,  # Terran -> Paradise World
        2: 2,  # Zythian -> Crystal Planet
        3: 3,  # Mycelian -> Fungal World
        4: 4,  # Volatian -> Gas Giant
        5: 5,  # Silicoid -> Metal-Rich Planet
        6: 6,  # Etherial -> Quantum Flux World
    }
    planet_type_id = race_planet_type_mapping.get(user.race_id)
    # Find an unowned planet of that type in the user's home galaxy
    home_galaxy_number = user.race_id + 1  # Galaxies 2-6 are home to player races
    planet = Planet.query.filter_by(
        planet_type_id=planet_type_id,
        owner_id=None
    ).join(SolarSystem).join(Cluster).join(Galaxy).filter(
        Galaxy.number == home_galaxy_number
    ).first()
    if planet:
        planet.owner_id = user.id
        user.starting_planet_id = planet.id
        db.session.commit()
        print(f"Assigned starting planet {planet.name} to user {user.username}.")
    else:
        print("No available starting planets found.")
