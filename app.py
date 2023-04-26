from flask import *
from timeloop import Timeloop

import Group_Class
import Queue
from Room_Class import Room

# setup for flask app
app = Flask(__name__)

ROOMS = {
    "111": Room("111"),
    "125": Room("125"),
    "131": Room("131"),
    "211": Room("211"),
    "225": Room("225"),
    "231": Room("231"),
    "311": Room("311"),
    "325": Room("325"),
    "331": Room("331"),
}
tl = Timeloop()


@tl.job(interval=15)
def update_rooms():
    for key, value in ROOMS.items():
        if value.occupancy is False:
            queue.groups[0].assign_room(value)
            value.occupancy = True
            queue.leave_queue(queue.groups[0])
            flash(f"You have been assigned to Room {key}")


############################
# Debug
app.debug = False
############################
queue = Queue.Queue()


@app.route("/home")
def hello_world():
    return render_template("index.html", title="Hello")


@app.route("/register_group")
def register_group():
    return render_template("register_group.html")


@app.route("/join_queue")
def join_queue(group):
    queue.join_queue(group)
    flash("You've joined the queue")
    return redirect(url_for("queue"))


@app.route("/leave_queue")
def leave_queue(group):
    queue.leave_queue(group)
    flash("You've left the queue")
    return redirect(url_for("queue"))


@app.route("/queue")
def queue():
    return render_template("queue.html", queue=queue)
