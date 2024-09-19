# utils/tick_processor.py

from extensions import db
from models.universe import Planet
from models.game_entities import Building
from config.buildings import BUILDINGS

def process_ticks():
    print("Processing game tick...")
    # Update resource production
    planets = Planet.query.all()
    for planet in planets:
        buildings = planet.buildings
        for building in buildings:
            building_config = BUILDINGS.get(building.building_type_id)
            if building_config and 'base_production' in building_config:
                for resource, amount in building_config['base_production'].items():
                    # Calculate production based on building level
                    production = amount * building.level
                    setattr(planet, resource, getattr(planet, resource) + production)
    db.session.commit()
    print("Game tick processed.")
