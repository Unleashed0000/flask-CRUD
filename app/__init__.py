from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def register_extensions(app):
    db.init_app(app)

def register_blueprints(app):
    from .main import main as main_bp
    app.register_blueprint(main_bp)

def create_app():
    app  = Flask(__name__)

    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://admin:root@localhost/postgres'
    
    register_extensions(app)

    register_blueprints(app)

    return app