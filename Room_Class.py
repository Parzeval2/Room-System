class Room:

    def __init__(self, room_id, occupancy: bool = False):
        self.occupancy = occupancy
        self.room_id = room_id

    @property
    def room_id(self):
        return self.__room_id

    @room_id.setter
    def room_id(self, room_id):
        self.__room_id = room_id
