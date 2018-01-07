from data_structures.stack import Stack


class MaxStack:

    def __init__(self, data=None):
        self.stack = Stack()
        self.max_stack = Stack()
        if data is not None:
            self.push(data)

    def push(self, data):
        self.stack.push(data)
        latest_max = self.max_stack.peek()
        if latest_max is not None:
            if latest_max.data[0] >= data:
                node = self.max_stack.pop()
                node_data = node.data
                node_data[1] += 1
                self.max_stack.push(node_data)
            else:
                self.max_stack.push([data, 1])
        else:
            self.max_stack.push([data, 1])

    def pop(self):
        popped_node = self.stack.pop()
        latest_max = self.max_stack.peek()
        if latest_max is not None:
            node = self.max_stack.pop()
            node_data = node.data
            node_data[1] -= 1
            if node_data[1] > 0:
                self.max_stack.push(node_data)
        return popped_node

    def max(self):
        latest_max = self.max_stack.peek()
        return latest_max.data[0]
