# db model for group information
from datetime import datetime
from .Room_Class import Room
from flask import flash
from . import db

# this database model is very similar to a clas structure but store info
# more efficiently because its built using an SQL database in tables


class GroupInfo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    CWID = db.Column(db.Integer)
    size = db.Column(db.Integer)
    email = db.Column(db.String(100))
    group_assigned_room = db.Column(db.Integer)
    # start_time = db.Column(start_time())

def background():
    from . import queueobject  # import queueobject here
    with app.app_context():
        while True:
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
            for key, room in rooms.items():
                if room.occupancy is False:
                    id = queueobject.groups[0]
                    group = GroupInfo.query.filter(GroupInfo.id == id).first()
                    group.group_assigned_room = room
                    room.occupancy = True
                    room.group = queueobject.groups[0]
                    queueobject.leave_queue(queueobject.groups[0])
                    flash(f"You have been assigned to Room {key}")
