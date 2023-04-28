from os import path

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
DB_NAME = "database.db"

# this entire file creates a package out of the website folder
# we use create app to config everything and get it all in one place


def create_app():
    app = Flask(__name__)
    app.config["SECRET_KEY"] = "secretlol"
    app.config["SQLALCHEMY_DATABASE_URI"] = f"sqlite:///{DB_NAME}"
    db.init_app(app)

    from .views import views

    app.register_blueprint(views, url_prefix="/")

    with app.app_context():
        db.create_all()

    return app


def create_db(app):
    if not path.exists("website/" + DB_NAME):
        db.create_all(app=app)
        print("Database created")
