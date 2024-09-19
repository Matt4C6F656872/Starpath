# config/buildings.py

BUILDINGS = {
    1: {
        'name': 'Aluminium Mine',
        'description': 'Produces Aluminium',
        'category': 'Resources',
        'base_cost': {'Aluminium': 100, 'Biomass': 50},
        'cost_multiplier': 1.5,
        'base_production': {'Aluminium': 10},
    },
    2: {
        'name': 'Biomass Farm',
        'description': 'Produces Biomass',
        'category': 'Resources',
        'base_cost': {'Aluminium': 80},
        'cost_multiplier': 1.5,
        'base_production': {'Biomass': 8},
    },
    # Add other buildings...
}
