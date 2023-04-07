from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from config import config_names

db = SQLAlchemy()
migrate = Migrate()

def register_extensions(app):
    db.init_app(app)
    migrate.init_app(app, db)

def register_blueprints(app):
    from .main import main as main_bp
    app.register_blueprint(main_bp)

def create_app(config_name):
    app  = Flask(__name__)
    app.config.from_object(config_names[config_name])
    
    register_extensions(app)

    register_blueprints(app)

    return app