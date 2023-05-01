from flask import Blueprint, flash, redirect, render_template, request, url_for

from . import db, queueobject
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


@views.route("/leave_queue")
def leave_queue(CWID=None):
    if CWID is None:
        return redirect(url_for("view.queue"))
    for group in GroupInfo.query.filter_by(CWID=CWID):
        if CWID == group.CWID:
            queueobject.leave_queue(group)
            flash("Your group has left the queue")
    return redirect(url_for("queue"))


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
