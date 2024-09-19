# forms/game_forms.py

from flask_wtf import FlaskForm
from wtforms import SelectField, SubmitField
from wtforms.validators import DataRequired
from config.buildings import BUILDINGS

class BuildingUpgradeForm(FlaskForm):
    building = SelectField(
        'Building', choices=[(str(id), data['name']) for id, data in BUILDINGS.items()],
        validators=[DataRequired()]
    )
    submit = SubmitField('Upgrade')
