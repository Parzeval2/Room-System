from flask import *
from flask_sqlalchemy import SQLAlchemy
from timeloop import Timeloop

from website import create_app

app = create_app()

if __name__ == "__main__":
    app.run()
