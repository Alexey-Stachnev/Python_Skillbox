class Stack:
    def __init__(self):
        self.stack = []
    def push(self, item):
        self.stack.append(item)
    def pop(self):
        if self.is_empty():
            return None
        removed = self.stack.pop()
        return removed
    def top(self):
        if self.is_empty():
            return None
        return self.stack[len(self.stack)-1]
    def is_empty(self):
        return len(self.stack) == 0
    def size(self):
        return len(self.stack)