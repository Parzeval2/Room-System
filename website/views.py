from flask import Blueprint
from flask import flash
from flask import redirect
from flask import render_template, request
from flask import request
from flask import url_for

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
    # find the cwid from the previous route
    position = findpos(id)
    return render_template("QueueAndMap.html", position=position, id=id)


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
        print(queueobject.groups)
        id = new_group.id
        print("group made")
    return redirect(url_for("view.queue", id=id))


@views.route("/leave_queue/<id>", methods=["GET", "POST"])
def leave_queue(id):
    print("leave_queue")
    group = GroupInfo.query.filter(GroupInfo.id == id).first()
    group = group.id
    queueobject.leave_queue(group)
    print(queueobject.groups)
    return redirect(url_for("view.home"))

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

@views.route("/refresh", methods=["GET", "POST"])
def refresh():
    referrer = request.referrer
    referrer = referrer.split("/")
    id = referrer[-1]
    query = GroupInfo.query.filter(GroupInfo.id == id).first()
    print("checking")
    check = check_empty_rooms(id)
    print(check)
    if check:
        return render_template("Available.html", available_str=check)
    if check is None:
        print("viewing queue")
        return redirect(request.referrer)


def findpos(id):
    # find the group based on CWID
    group = GroupInfo.query.filter(GroupInfo.id == id).first()
    if group is None:
        print("group not found")
    id = group.id
    # find the position of the group in the queue
    position = queueobject.groups.index(id)
    if position == 0:
        positionstr = "You are next in line"
        return positionstr
    else:
        positionstr = f"You are position {position + 1}"
        return positionstr

def check_empty_rooms(id):
    for key, room in rooms.items():
        #check for queue object being empt
            if room.occupancy is False:
                group = GroupInfo.query.filter(GroupInfo.id == id).first()
                group.group_assigned_room = room
                room.occupancy = True
                room.group = queueobject.groups[0]
                queueobject.leave_queue(group)
                group.message = f"You have been assigned to room {key}"
                print(group.message)
                return group.message
    return None