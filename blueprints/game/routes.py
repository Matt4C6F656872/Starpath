# blueprints/game/routes.py

from flask import Blueprint, render_template, redirect, url_for, request, flash
from flask_login import login_required, current_user
from . import game_bp
from models.universe import Planet
from models.game_entities import Building
from forms.game_forms import BuildingUpgradeForm
from extensions import db

game_bp = Blueprint('game', __name__)

@game_bp.route('/empire')
@login_required
def empire():
    # Your logic here, for example fetching user-related data like their planets
    return render_template('game/empire.html')

@game_bp.route('/buildings/<int:planet_id>', methods=['GET', 'POST'])
@login_required
def manage_buildings(planet_id):
    planet = Planet.query.get_or_404(planet_id)
    if planet.owner_id != current_user.id:
        flash("You do not own this planet.")
        return redirect(url_for('main.game'))

    form = BuildingUpgradeForm()
    if form.validate_on_submit():
        building_type_id = int(form.building.data)
        # Check if the building exists on the planet
        building = Building.query.filter_by(
            planet_id=planet.id,
            building_type_id=building_type_id
        ).first()
        if not building:
            # Create new building
            building = Building(
                building_type_id=building_type_id,
                planet_id=planet.id
            )
            db.session.add(building)
        else:
            # Upgrade building
            building.level += 1
        db.session.commit()
        flash("Building upgraded successfully.")
        return redirect(url_for('game.manage_buildings', planet_id=planet.id))

    # Get planet's buildings
    buildings = planet.buildings
    return render_template('game/buildings.html', planet=planet, buildings=buildings, form=form)
