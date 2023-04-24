class Queue:
    def __init__(self):
        self.groups = []

    def join_queue(self, group):
        self.groups.append(group)

    def leave_queue(self, group):
        self.groups.remove(group)