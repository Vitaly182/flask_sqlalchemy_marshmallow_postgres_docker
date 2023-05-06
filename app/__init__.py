from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


db = SQLAlchemy()
migrate = Migrate()

def create_app():
    app = Flask(__name__)
    # app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:d6804775@localhost:5432/pet_clinic'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:postgres@db:5432/pet_clinic'

    db.init_app(app)
    migrate.init_app(app, db)

    from app.clients.models import Clients
    from app.pets.models import Pets

    return app

