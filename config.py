# Building Configurations with Formulas
BUILDINGS = {
    1: {
        "name": "Administratum",
        "description": "Central hub for planetary administration and population management",
        "base_cost": {"Aluminium": 500, "Crystals": 200},
        "cost_formula": lambda level: {
            "Aluminium": 500 * (level ** 1.3),  # Example formula: Aluminium increases by level^1.3
            "Crystals": 200 * (level ** 1.2)  # Example formula: Crystals increase by level^1.2
        },
        "category": "Administrative"
    },
    2: {
        "name": "Habitat Dome",
        "description": "Increases the planet's population cap by providing additional habitable space",
        "base_cost": {"Aluminium": 400, "Biomass": 300},
        "cost_formula": lambda level: {
            "Aluminium": 400 * (level ** 1.4),
            "Biomass": 300 * (level ** 1.3)
        },
        "category": "Population and Growth"
    },
    3: {
        "name": "Biomass Farm",
        "description": "Produces Biomass to sustain the population and growth",
        "base_cost": {"Aluminium": 300, "Biomass": 100},
        "cost_formula": lambda level: {
            "Aluminium": 300 * (level ** 1.1),
            "Biomass": 100 * (level ** 1.05)
        },
        "category": "Resources"
    },
    4: {
        "name": "Solar Power Plant",
        "description": "Generates energy for planetary systems using solar technology",
        "base_cost": {"Aluminium": 300, "Crystals": 100},
        "cost_formula": lambda level: {
            "Aluminium": 300 * (level ** 1.2),
            "Crystals": 100 * (level ** 1.15)
        },
        "category": "Energy"
    },
    5: {
        "name": "Fusion Reactor",
        "description": "Produces massive energy by consuming Deuterium in a controlled fusion reaction",
        "base_cost": {"Aluminium": 500, "Deuterium": 200},
        "cost_formula": lambda level: {
            "Aluminium": 500 * (level ** 1.5),
            "Deuterium": 200 * (level ** 1.3)
        },
        "category": "Energy"
    },
    6: {
        "name": "Shipyard",
        "description": "Builds and maintains fleets for interstellar travel and warfare",
        "base_cost": {"Aluminium": 700, "Deuterium": 300},
        "cost_formula": lambda level: {
            "Aluminium": 700 * (level ** 1.6),
            "Deuterium": 300 * (level ** 1.4)
        },
        "category": "Military"
    },
    7: {
        "name": "Planetary Defense Grid",
        "description": "Provides advanced defense against external threats and invasions",
        "base_cost": {"Aluminium": 600, "Crystals": 300},
        "cost_formula": lambda level: {
            "Aluminium": 600 * (level ** 1.4),
            "Crystals": 300 * (level ** 1.3)
        },
        "category": "Military"
    },
    8: {
        "name": "Trade Hub",
        "description": "Facilitates trade between planets, improving resource acquisition",
        "base_cost": {"Aluminium": 300, "Crystals": 150},
        "cost_formula": lambda level: {
            "Aluminium": 300 * (level ** 1.3),
            "Crystals": 150 * (level ** 1.25)
        },
        "category": "Trading"
    },
    9: {
        "name": "Market Exchange",
        "description": "Enables the buying and selling of resources through interplanetary markets",
        "base_cost": {"Aluminium": 250, "Gold": 50},
        "cost_formula": lambda level: {
            "Aluminium": 250 * (level ** 1.25),
            "Gold": 50 * (level ** 1.1)
        },
        "category": "Trading"
    }
}

# Resource Configurations
RESOURCES = {
    1: {
        "name": "Aluminium",
        "description": "Common resource used in the construction of basic structures and ships",
        "rarity": "Common"
    },
    2: {
        "name": "Biomass",
        "description": "Organic matter used to sustain population growth and life support systems",
        "rarity": "Common"
    },
    3: {
        "name": "Crystals",
        "description": "Valuable resource used in energy systems and advanced technology",
        "rarity": "Uncommon"
    },
    4: {
        "name": "Deuterium",
        "description": "Highly energetic isotope used in advanced energy production and weapons",
        "rarity": "Rare"
    },
    5: {
        "name": "Gold",
        "description": "Extremely rare resource used in high-tech electronics and diplomacy",
        "rarity": "Very Rare"
    }
}

# Race Configurations
RACES = {
    1: {
        "name": "Terran",
        "description": "Adaptable humanoids capable of balancing multiple areas of expertise",
        "bonus": "Slight boost to research and biomass production"
    },
    2: {
        "name": "Zythian",
        "description": "Crystal-based lifeforms specializing in energy manipulation and defense",
        "bonus": "Bonus to energy production and planetary defense"
    },
    3: {
        "name": "Mycelian",
        "description": "Fungal network beings with rapid population growth and efficient resource extraction",
        "bonus": "High biomass production and efficient resource extraction"
    },
    4: {
        "name": "Volatian",
        "description": "Gas-based entities focusing on speed and ship production",
        "bonus": "Fast ship production and movement"
    },
    5: {
        "name": "Silicoid",
        "description": "Silicon-based lifeforms excelling at mining and manufacturing",
        "bonus": "Efficient aluminium and mineral production"
    },
    6: {
        "name": "Etherial",
        "description": "Energy beings with strong research and espionage capabilities",
        "bonus": "Bonus to research speed and espionage"
    }
}
