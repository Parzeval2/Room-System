
#db model for group information

from init import db
from datetime import datetime

def start_time():
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    time_list = current_time.split(":")
    time_list_int = [int(i) for i in time_list]
    return time_list_int


class GroupInfo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    CWID = db.Column(db.Integer)
    size = db.Column(db.Integer)
    email = db.Column(db.String(100))
    group_assigned_rooms = db.Column(db.Integer)
    start_time = db.Column(start_time())