from website import create_app, threading, timeloop
from datetime import timedelta
from website.views import check_empty_rooms
from turbo_flask import Turbo


app = create_app()
turbo = Turbo(app)
app.use_reloader = False


if __name__ == "__main__":
    @timeloop.job(interval=timedelta(seconds=10))
    def background():
        check_empty_rooms(app, turbo)
    app.run()




