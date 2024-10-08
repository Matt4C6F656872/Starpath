# extensions.py

from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_migrate import Migrate  # Ensure this import is here
from flask_apscheduler import APScheduler

db = SQLAlchemy()
login_manager = LoginManager()
migrate = Migrate()  # Ensure migrate is initialized here
scheduler = APScheduler()

@login_manager.user_loader
def load_user(user_id):
    from models.user import User
    return User.query.get(int(user_id))
