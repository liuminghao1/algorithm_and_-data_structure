

class Stack(object):
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.insert(0, item)

    def pop(self):
        self.stack.pop()

    def peek(self):
        return self.stack[0]

    def is_empty(self):
        return len(self.stack) == 0

    def size(self):
        return len(self.stack)

