from flask import Blueprint
from flask import flash
from flask import redirect
from flask import render_template
from flask import request
from flask import url_for
from turbo_flask import Turbo

from . import db
from . import queueobject
from .models import GroupInfo, rooms

views = Blueprint("view", __name__)


# this file is essentially the switching for every new page on the site
# itll redirect on some functions and display pages of others

@views.route("/", methods=["GET", "POST"])
def sendhome():
    return redirect("/home")


@views.route("/home")
def home():
    return render_template("HomePage.html")


@views.route("/queue/<id>", methods=["GET", "POST"])
def queue(id):
    group = GroupInfo.query.filter(GroupInfo.id == id).first()
    id = group.id
    position = findpos(id)
    return render_template("QueueAndMap.html", position=position, message=None, popup=False)


# @views.route("/assignment/<id>", methods=["GET", "POST"])
# def assignment(id):
#     group = GroupInfo.query.filter(GroupInfo.id == id).first()
#     assignedroom = group.popup
#     return render_template("Assignment.html", available_str=assignedroom)
@views.route("/register_group", methods=["POST", "GET"])
def register_group():
    if request.method in ["Post", "GET"]:
        email = request.args.get("email")
        CWID = request.args.get("ID")
        size = request.args.get("size")

        new_group = GroupInfo(email=email, CWID=CWID, size=size)
        db.session.add(new_group)
        db.session.commit()
        queueobject.join_queue(new_group)

        id = new_group.id
        flash("Your group has been created and the queue has been joined")
    return redirect(url_for("view.queue", id=id))


@views.route("/leave_queue/<CWID>", methods=["GET", "POST"])
def leave_queue(CWID):
    group = GroupInfo.query.filter(GroupInfo.CWID == CWID).first()
    group = group.id
    queueobject.leave_queue(group)
    return redirect(url_for("home"))

@views.route("room/<room_num>", methods=["GET", "POST"])
def view_room(room_num):
    current_room = rooms[f'{room_num}']
    if current_room.occupancy == True:
        text = "This room is occupied"
        return render_template("Room131.html", room_num=room_num, occupation_str=text, occupation=True)
    if current_room.occupancy == False:
        text = "This room is unoccupied"
        return render_template("Room131.html", room_num=room_num, occupation_str=text, occupation=False)

@views.route("room/<room_num>/leave", methods=["GET", "POST"])
def leave_room(room_num):
    current_room = rooms[f'{room_num}']
    text = "This room is unnoccupied"
    current_room.occupancy = False
    return redirect(url_for("view.view_room", room_num=room_num, occupation_str=text, occupation=False))


def findpos(id):
    # find the group based on CWID
    group = GroupInfo.query.filter(GroupInfo.id == id).first()
    group = group.id
    # find the position of the group in the queue
    position = queueobject.groups.index(group)
    if position == 0:
        positionstr = "You are next in line"
        return positionstr
    else:
        positionstr = f"You are position {position + 1}"
        return positionstr

def check_empty_rooms(app, turbo):
    with app.app_context():
        for key, room in rooms.items():
            # check for queue object being empt
            if queueobject.groups:
                if room.occupancy is False:
                    id = queueobject.groups[0]
                    group = GroupInfo.query.filter(GroupInfo.id == id).first()
                    group.group_assigned_room = room
                    room.occupancy = True
                    room.group = queueobject.groups[0]
                    queueobject.leave_queue(group)
                    print(key)
                    group.popup = f"You have been assigned to room {key}"
                    turbo.push(url_for("view.queue", message=group.popup, position="", id=group.id, popup=True))