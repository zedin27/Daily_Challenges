"""
21. Merge Two Sorted Linked List

You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists in a one sorted list. The list should be made by splicing together the nodes of the first two lists.

Return the head of the merged linked list.
"""

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __repr__(self):
        return self.data

class LinkedList:
    def __init__(self):
        self.head = None

    def __repr__(self):
        node = self.head
        nodes = []
        while node is not None:
            nodes.append(node.data)
            node = node.next
        nodes.append("None")
        return " -> ".join(nodes)

# l1 = LinkedList()
# first_node = Node("1")
# l1.head = first_node
# l1

# class Node:
# 	def __init__(self, data):
# 		self.data = data
# 		self.next = None



# l1 = Node(5)
# l1.next = Node(10)

# l2 = Node(8)
# l2.next = Node(9)

# v = []
# while l1 is not None:
# 	v.append(l1.data)
# 	l1 = l1.next

# while l2 is not None:
# 	v.append(l2.data)
# 	l2 = l2.next

# v.sort()
# result = Node(-1)
# temp = result
# for i in range(len(v)):
# 	result.next = Node(v[i])
# 	result = result.next

# temp = temp.next
# print("Merged linked list is: ")
# while temp is not None:
# 	print(temp.data, end=" ")
# 	temp = temp.next