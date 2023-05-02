from flask import Blueprint
from flask import flash
from flask import redirect
from flask import render_template
from flask import request
from flask import url_for

from . import db
from . import queueobject
from .models import GroupInfo

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
    return render_template("QueueAndMap.html", position=position)


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
