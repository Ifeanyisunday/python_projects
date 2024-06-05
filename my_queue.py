class Queue:
    def __init__(self):
        self.queue = []

    def add_to_queue(self, item):
        if item not in self.queue:
            self.queue.append(item)

    def remove_from_queue(self):
        self.queue.pop(0)

    def print_queue(self):
        return self.queue


