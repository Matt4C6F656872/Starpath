# app.py

from flask import Flask
from config.settings import Config
from extensions import db, login_manager, migrate, scheduler
from blueprints.auth import auth_bp
from blueprints.main import main_bp
from blueprints.game import game_bp

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # Initialize extensions
    db.init_app(app)
    login_manager.init_app(app)
    migrate.init_app(app, db)
    scheduler.init_app(app)
    scheduler.start()

    # Register blueprints
    app.register_blueprint(auth_bp, url_prefix='/auth')
    app.register_blueprint(main_bp)
    app.register_blueprint(game_bp)

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)