class Stack:
    def __init__(self):
        self.stack = []

    def add_to_stack(self, element):
        self.stack.append(element)

    def remove_from_stack(self):
        self.stack.pop()

    def print_stack(self):
        return self.stack
