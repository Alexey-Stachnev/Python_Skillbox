class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, item):
        self.queue.append(item)

    def dequeue(self):
        if self.queue_is_empty():
            return None
        removed = self.queue.pop(0)
        return removed

    def queue_is_empty(self):
        return len(self.queue) == 0