"""Linked List."""

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __str__(self):
        return str(self.data)

class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, data):
        node = Node(data)
        node.next = self.head
        self.head = node

    def print_list(self):
        current = self.head
        while current:
            print (current.data, end = " ")
            current = current.next

    def reverse_list(self):
        prev = None
        current = self.head
        while current is not None:
            next = current.next
            current.next = prev
            prev = current
            current = next
        self.head = prev

    def deleteDuplicates(self):
        current = second = self.head

        while current is not None:
            while second.next is not None:
                if second.next.data == current.data:
                    second.next = second.next.next
                else:
                    second = second.next
            current = second = current.next

    # Multiple ways to do deleteDuplicates
    # def deleteDuplicates(self):
    # 	cur = self.head
    # 	while cur:
    #
    # 		if cur.next != None and cur.data == cur.next.data:
    # 			cur.next = cur.next.next
    # 		else:
    # 			cur = cur.next
    # 	return cur
    #
    # def deleteDuplicates(self):
    # 	if self.head is None:
    # 		return None
    #
    # 	node = self.head
    # 	while node.next is not None:
    # 		if node.data == node.next.data:
    # 			node.next = node.next.next
    # 		else:
    # 			node = node.next
    # 	return node

if __name__ == '__main__':
    l = LinkedList()
    l.insert(15)
    l.insert(15)
    l.insert(15)
    l.insert(15)
    l.insert(20)
    l.insert(1)
    # l.print_list()
    l.deleteDuplicates()
    # l.print_list()
    l.reverse_list()
    l.print_list()
