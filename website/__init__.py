from os import path
from flask import Flask
import threading
from flask_sqlalchemy import SQLAlchemy
from .Queue import Queue
from flask_timeloop import Timeloop

timeloop = Timeloop()
db = SQLAlchemy()
DB_NAME = "database.db"
global popup
queueobject = Queue()
# this entire file creates a package out of the website folder
# we use create app to config everything and get it all in one place


def create_app():
    app = Flask(__name__)
    app.config["SECRET_KEY"] = "secretlol"
    app.config["SQLALCHEMY_DATABASE_URI"] = f"sqlite:///{DB_NAME}"
    app.config["DEBUG"] = True
    db.init_app(app)

    app.config['SERVER_NAME'] = '127.0.0.1:5000'
    app.config['APPLICATION_ROOT'] = '/'
    app.config['PREFERRED_URL_SCHEME'] = 'http'

    from .views import views

    app.register_blueprint(views, url_prefix="/")

    with app.app_context():
        db.drop_all()
        db.create_all()

    timeloop.init_app(app)
    timeloop.start()


    return app


def create_db(app):
    if not path.exists("website/" + DB_NAME):
        db.create_all(app=app)
        print("Database created")

