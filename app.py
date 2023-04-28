from flask import *
from flask_sqlalchemy import SQLAlchemy
from timeloop import Timeloop

from website import create_app

# setup for flask app
# ROOMS = {
#     "111": Room("111"),
#     "125": Room("125"),
#     "131": Room("131"),
#     "211": Room("211"),
#     "225": Room("225"),
#     "231": Room("231"),
#     "311": Room("311"),
#     "325": Room("325"),
#     "331": Room("331"),
# }
# tl = Timeloop()


# @tl.job(interval=15)
# def update_rooms():
#     for key, value in ROOMS.items():
#         if value.occupancy is False:
#             queue.groups[0].assign_room(value)
#             value.occupancy = True
#             queue.leave_queue(queue.groups[0])
#             flash(f"You have been assigned to Room {key}")


app = create_app()

if __name__ == "__main__":
    app.run()
