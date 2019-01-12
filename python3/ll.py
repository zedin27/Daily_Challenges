"""Linked List."""

class Node:
	def __init__(self, data):
		self.data = data
		self.next = None

	def __str__(self):
		return str(self.data)

def print_list(node):
	while node is not None:
		print(node, end=" ")
		node = node.next
	print()

def print_reverse_list(list):
	if list is None:
		return
	head = list
	tail = list.next
	print_reverse_list(tail)
	print(head, end=" ")

if __name__ == '__main__':
	node1 = Node(1)
	node2 = Node(2)
	node3 = Node(3)
	node1.next = node2
	node2.next = node3
	print_list(node1)
	print_reverse_list(node1)

# """Linked List."""
#
# class Node:
# 	def __init__(self, data):
# 		self.data = data
# 		self.next = None
#
# 	def __str__(self):
# 		return str(self.data)
#
# class LinkedList:
# 	def __init__(self):
# 		self.head = None
#
# 	def push(self, new_data):
# 		new_data = Node(new_data)
# 		new_data.next = self.head
# 		self.head = new_data
#
# 	def remove_node(self, position):
# 		if self.head is None:
# 			return
#
# 		tmp = self.head
#
# 		if position is 0:
# 			self.head = tmp.next
# 			tmp = None
# 			return
#
# 		for i in range(position - 1):
# 			tmp = tmp.next
# 			if tmp is None:
# 				break
#
# 		if tmp is None:
# 			return
# 		if tmp.next is None:
# 			return
#
# 		next = tmp.next.next
# 		tmp.next = None
# 		tmp.next = next
#
# 	def print_list(self):
# 		tmp = self.head
#
# 		while (tmp):
# 			print(tmp.data)
# 			tmp = tmp.next
#
# # def print_list(node):
# # 	while node is not None:
# # 		print(node, end=" ")
# # 		node = node.next
# # 	print()
#
# # def print_reverse_list(list):
# # 	if list is None:
# # 		return
# # 	head = list
# # 	tail = list.next
# # 	print_reverse_list(tail)
# # 	print(head, end=" ")
#
# if __name__ == '__main__':
# 	node = LinkedList()
# 	node.push(8)
# 	node.push(10)
# 	# node2 = LinkedList(2)
# 	# node3 = LinkedList(3)
# 	# node1.next = node2
# 	# node2.next = node3
# 	node.print_list()
# 	# print_reverse_list(node1)
# 	node.remove_node(2)
# 	# node.print_list()
# 	# print_list(node1)
