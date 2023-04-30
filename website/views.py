from flask import Blueprint
from flask import flash
from flask import redirect
from flask import render_template
from flask import request
from flask import url_for

from . import db, queueobject
from .models import GroupInfo

views = Blueprint("view", __name__)

# this file is essentially the switching for every new page on the site
# itll redirect on some functions and display pages of others



@views.route("/", methods=['GET', 'POST'])
def sendhome():
    return redirect("/home")

@views.route("/home")
def home():
    return render_template("HomePage.html")
@views.route("/queue")
def queue():
    return render_template("QueueAndMap.html", group=GroupInfo,queue=queueobject, postion=None)

@views.route("/register_group", methods=["POST", "GET"])
def register_group():
    if request.method == "Post" or request.method == "GET":
        email = request.form.get("email")
        CWID = request.form.get("ID")
        size = request.form.get("size")

        new_group = GroupInfo(email=email, CWID=CWID, size=size)
        db.session.add(new_group)
        db.session.commit()
        print(new_group.query.all())
        queueobject.join_queue(new_group)
        flash("Your group has been created and the queue has been joined")
    position = findpos(CWID)
    return redirect(url_for("view.queue", group=new_group, position=position, CWID=CWID))


@views.route("/leave_queue")
def leave_queue(CWID=None):
    if CWID is None:
        return redirect(url_for("view.queue"))
    for group in GroupInfo.query.filter_by(CWID=CWID):
        if CWID == group.CWID:
            queueobject.leave_queue(group)
            flash("Your group has left the queue")
    return redirect(url_for("queue"))

def findpos(CWID):
    #find the group in the database based on CWID
    group = GroupInfo.query.filter_by(CWID=CWID).first()

    #find the position of the group in the queue
    position = queueobject.groups.index(group)
    if position == 0:
        position = "You are next in line"
        return str(position)
    else:
        position = f"You are position {position + 1}"
        return str(position)



