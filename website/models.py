# db model for group information
from .Room_Class import Room
from flask import flash
from . import db
from timeloop import Timeloop
from datetime import timedelta

# this database model is very similar to a clas structure but store info
# more efficiently because its built using an SQL database in tables


class GroupInfo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    CWID = db.Column(db.Integer)
    size = db.Column(db.Integer)
    email = db.Column(db.String(100))
    group_assigned_room = db.Column(db.Integer)
    popup = db.Column(db.String(100))

rooms = {
            "111": Room(room_id="111"),
            "125": Room(room_id="125"),
            "131": Room(room_id="131"),
            "211": Room(room_id="211"),
            "225": Room(room_id="225"),
            "231": Room(room_id="231"),
            "311": Room(room_id="311"),
            "325": Room(room_id="325"),
            "331": Room(room_id="331"),
        }
#this is a very fun little background task that runs and checks for empty rooms

