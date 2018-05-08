

class Queue(object):
    def __init__(self):
        self.queue = []

    def en_queue(self, item):
        self.queue.append(item)

    def de_queue(self):
        return self.queue.pop(0)

    def is_empty(self):
        return len(self.queue) == 0

    def size(self):
        return len(self.queue)

