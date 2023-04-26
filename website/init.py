from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path

db = SQLAlchemy()
DB_NAME = "database.db"


def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] ='secretlol'
    app.config['SQLALCHEMY_DATABASE_URI'] = f"sqlite:///{DB_NAME}"

    from models import User
    create_db(app)

    db.init_app(app)

    return app


def create_db(app):
    if not path.exists('website/' + DB_NAME):
        db.create_all(app=app)
        print("Database created")