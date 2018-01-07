class Stack:

    def __init__(self, data=None):
        self.top = None
        if data is not None:
            self.push(data)

    def push(self, data):
        new_node = Node(data)
        if self.top is None:
            self.top = new_node
        else:
            new_node.below = self.top
            self.top = new_node

    def pop(self):
        if self.top is not None:
            node = self.top
            self.top = self.top.below
            return node
        raise StackIsEmpty

    def peek(self):
        return self.top


class Node:

    def __init__(self, data):
        self.data = data
        self.below = None


class StackIsEmpty(Exception):
    """
    Stack is empty Custom Exception Class
    """

    def __init__(self):
        pass

    def __str__(self):
        return self.__repr__()

    def __repr__(self):
        return "Stack is Empty"
