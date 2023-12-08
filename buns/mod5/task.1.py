class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Stack:
    def __init__(self):
        self.__head = None

    def push(self, value):
        if self.__head is None:
            self.__head = Node(value)
        else:
            newNode = Node(value)
            newNode.next = self.__head
            self.__head = newNode

    def pop(self):
        if self.is_empty():
            return None
        removed = self.__head
        self.__head = self.__head.next
        removed.next = None
        return removed

    def is_empty(self):
        return self.__head is None

    def peek(self):
        if self.is_empty():
            return None
        return self.__head.value

    def print_stack(self):
        if self.is_empty():
            print("Stack Underflow")
        else:
            node = self.__head
            while(node is not None):
                print(node.value, end = "\n")
                node = node.next
