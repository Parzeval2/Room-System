from flask import flash
from models import GroupInfo
from Room_Class import Room
from timeloop import Timeloop

from . import queueobject


def background():
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
    tl = Timeloop()

    @tl.job(interval=15)
    def update_rooms():
        for key, room in rooms.items():
            if room.occupancy is False:
                id = queueobject.groups[0]
                group = GroupInfo.query.filter(GroupInfo.id == id).first()
                group.group_assigned_room = room
                room.occupancy = True
                room.group = queueobject.groups[0]
                queueobject.leave_queue(queueobject.groups[0])
                flash(f"You have been assigned to Room {key}")
