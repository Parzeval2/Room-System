#class for the group that involves members, contact info

class Group:
    def __init__(self, size, contact):
        self.size = size
        self.contact = contact

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
