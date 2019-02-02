"""Queue Implementation."""

class Queue:
    def __init__(self):
        self.head = 0
        self.length = 0

    def insert(self, data):
        node = Node(data)

        if self.head is None:
            self.head = node
        else:
            last = self.head
            while last.next:
                last = last.next
            last.next = node
        self.length += 1

    def remove(self):
        node = self.head.node
        node.popleft()
