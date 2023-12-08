class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class Queue:
    def __init__(self):
        self.head = None
        self.tail = None

    def enqueue(self, item):
        if self.tail is None:
            self.head = Node(item)
            self.tail = self.head
        else:
            self.tail.next = Node(item)
            self.tail.next.prev = self.tail
            self.tail = self.tail.next

    def dequeue(self):
        if self.head is None:
            return None
        temp = self.head.data
        self.head = self.head.next
        self.head.prev = None
        return temp

    def is_empty(self):
        return self.head is None

    def first(self):
        return self.head.data

    def size(self):
        temp = self.head
        count=0
        while temp is not None:
            count += 1
            temp = temp.next
        return count

    def print_queue(self):
        temp = self.head
        while temp is not None:
            print(temp.data)
            temp = temp.next
