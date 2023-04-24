#class for the group that involves members, contact info
from datetime import datetime
class Group:
    def __init__(self, size, contact, CWID):
        self.size = size
        self.contact = contact
        self.assigned_room = None
        self.CWID = CWID
        self.start_time = self.start_time()

    def start_time(self):
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        time_list = current_time.split(":")
        time_list_int = [int(i) for i in time_list]
        return time_list_int

    def assign_room(self, room):
        self.assigned_room = room

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if value < 2:
            raise ValueError("Group size must be at least 2 members")
        else:
            self.__size = value

    @property
    def contact(self):
        return self.__contact

    @contact.setter
    def contact(self, value):
        if "@" not in value:
            raise ValueError("Group contact must be a valid email address")
        else:
            self.__contact = value
