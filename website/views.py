from flask import Blueprint, render_template, request, flash, redirect, url_for
from .models import GroupInfo
from . import db

views = Blueprint("view", __name__)

#this file is essentially the switching for every new page on the site
#itll redirect on some functions and display pages of others
@views.route("/")
def sendhome():
    return redirect(url_for("home"))
@views.route("/home")
def hello_world():
    return '<h1>Test</h1>'


@views.route("/register_group", methods=["GET", "POST"])
def register_group():
    if request.method == 'Post':
        email = request.form.get("email")
        CWID = request.form.get("CWID")
        size = int(request.form.get("size"))

        if size < 3:
            flash("Groups must be at least 3 people")
        else:
            new_group = GroupInfo(email=email, CWID=CWID, size=size)
            db.session.add(new_group)
            db.session.commit()
            flash("Your group has been created")
            return redirect(url_for("home"))
    if request.method == 'GET':
        pass
    return render_template("register_group.html")


@views.route("/join_queue")
def join_queue(group):
    queue.join_queue(group)
    flash("You've joined the queue")
    return redirect(url_for("queue"))


@views.route("/leave_queue")
def leave_queue(group):
    queue.leave_queue(group)
    flash("You've left the queue")
    return redirect(url_for("queue"))


@views.route("/queue")
def queue():
    return render_template("queue.html", queue=queue)