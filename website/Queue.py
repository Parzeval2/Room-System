class Queue:

    def __init__(self):
        self.groups = []

    def join_queue(self, group):
        self.groups.append(group.id)

    def leave_queue(self, id):
        self.groups.remove(id)
