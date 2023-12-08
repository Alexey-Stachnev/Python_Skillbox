class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def push(self, value):
        if self.head == None:
            self.head = Node(value)
        else:
            currentNode = self.head
            while currentNode.next:
                currentNode = currentNode.next
            currentNode.next = Node(value)

    def get(self, index):
        currentNode = self.head
        for i in range(index):
            if currentNode.next == None:
                return None
            currentNode = currentNode.next
        return currentNode.value

    def remove(self, index):
        currentId = 0
        previousNode = None
        for node in self:
            if currentId == index:
                if previousNode is not None:
                    previousNode.next = node.next
                else:
                    self.head = node.next
                    return
            previousNode = node
            currentId += 1

    def insert(self, index, value):
        currentId = 0
        previousNode = None
        newNode = Node(value)
        for node in self:
            if currentId == index:
                if previousNode is not None:
                    previousNode.next = newNode
                    newNode.next = node
                else:
                    self.head = newNode
                    newNode.next = node
                    return
            previousNode = node
            currentId += 1

    def __iter__(self):
        item = self.head
        while item is not None:
            yield item
            item = item.next