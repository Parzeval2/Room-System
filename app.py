from website import create_app, threading
from website import queueobject
from website.models import GroupInfo, rooms
from datetime import timedelta
from flask import flash
from timeloop import Timeloop
app = create_app()


def background(app):

    print("Background task started")
    with app.app_context():

        tl = Timeloop()
        @tl.job(interval=timedelta(seconds=5))
        def check_empty_rooms():
            with app.app_context():
                for key, room in rooms.items():
                    #check for queue object being empt
                    if queueobject.groups:
                        if room.occupancy is False:
                                id = queueobject.groups[0]
                                group = GroupInfo.query.filter(GroupInfo.id == id).first()
                                group.group_assigned_room = room
                                room.occupancy = True
                                room.group = queueobject.groups[0]
                                queueobject.leave_queue(group)
                                global popup
                                popup = f"You have been assigned to room {key}"
        tl.start()

if __name__ == "__main__":
    background(app)
    app.run()


