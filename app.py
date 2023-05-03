from website import create_app, threading, timeloop
from website import queueobject
from website.models import GroupInfo, rooms
from datetime import timedelta
from flask import request, redirect, url_for, render_template
from website.views import check_empty_rooms
app = create_app()
app.use_reloader = False


if __name__ == "__main__":
    @timeloop.job(interval=timedelta(seconds=5))
    def background():
        check_empty_rooms(app)
    app.run()




