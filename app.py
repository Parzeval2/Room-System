from website import create_app, threading
from website import queueobject
from website.models import GroupInfo, rooms


app = create_app()



if __name__ == "__main__":
    app.run()


