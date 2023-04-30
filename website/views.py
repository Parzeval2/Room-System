from flask import Blueprint
from flask import flash
from flask import redirect
from flask import render_template
from flask import request
from flask import url_for

from . import db, queueobject
from .models import GroupInfo

views = Blueprint("views", __name__)

# this file is essentially the switching for every new page on the site
# itll redirect on some functions and display pages of others


@views.route("/")
def sendhome():
    return redirect("/home")

@views.route("/home")
def home():
    return render_template("HomePage.html")
@views.route("/queue")
def queue():
    return render_template("QueueAndMap.html", group=GroupInfo,queue=queueobject)

@views.route("/register_group", methods=["POST", "GET"])
def register_group():
    if request.method == "Post":
        email = request.form.get("email")
        CWID = request.form.get("ID")
        size = int(request.form.get("Group Size"))

        if size < 3:
            flash("Groups must be at least 3 people")
        else:
            new_group = GroupInfo(email=email, CWID=CWID, size=size)
            db.session.add(new_group)
            db.session.commit()
            queueobject.join_queue(new_group)
            flash("Your group has been created and the queue has been joined")
            return redirect(url_for("queue"))
    return redirect(url_for("views.queue"))


@views.route("/leave_queue")
def leave_queue(CWID=None):
    if CWID is None:
        return redirect(url_for("views.queue"))
    for group in GroupInfo.query.filter_by(CWID=CWID):
        if CWID == group.CWID:
            queueobject.leave_queue(group)
            flash("Your group has left the queue")
    return redirect(url_for("queue"))




