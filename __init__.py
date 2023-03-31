from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask import Blueprint

db = SQLAlchemy()

def create_app():
    app  = Flask(__name__)

    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://admin:root@localhost/postgres'
    
    db.init_app(app)

    return app