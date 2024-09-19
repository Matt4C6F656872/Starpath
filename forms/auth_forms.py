# forms/auth_forms.py

from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SelectField, SubmitField
from wtforms.validators import DataRequired, EqualTo, ValidationError
from models.user import User
from config.races import RACES
from config.factions import FACTIONS

class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField(
        'Confirm Password', validators=[DataRequired(), EqualTo('password')]
    )
    race = SelectField(
        'Race', choices=[(str(id), data['name']) for id, data in RACES.items()],
        validators=[DataRequired()]
    )
    faction = SelectField(
        'Faction', choices=[(str(id), data['name']) for id, data in FACTIONS.items()],
        validators=[DataRequired()]
    )
    submit = SubmitField('Register')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError('Username already exists.')

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Login')
