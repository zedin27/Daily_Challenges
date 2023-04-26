# Resource: Linekd Lists for Technical Interview https://youtu.be/Hj_rA0dhr2I
from operator import truediv


class Node:
	def __init__(self, data):
		self.data = data
		self.next = None

	def __repr__(self):
		return self.data

def print_linkedList(head):
	current = head
	while current is not None:
		print(current.data, end=" -> ")
		current = current.next
	print("None")

#Iterative way
def linkedListValues(head):
	values = []
	current = head
	while current is not None:
		values.append(current.data)
		current = current.next
	return values

#Recursive way
def recursive_linkedListValues(head):
	values = []
	fillValues(head, values)
	return values

def fillValues(head, values):
	if head is not None:
		values.append(head.data)
		fillValues(head.next, values)

#Sum List (iterative)
def sum_linkedList(head):
	current = head
	sum = 0
	while current is not None:
		sum += current.data
		current = current.next
	return sum

# Sum List (recursive)
def recursive_sum_linkedList(head):
	if head is None:
		return 0
	return head.data + recursive_sum_linkedList(head.next)

# Find node (iterative)
def find_node(head, target):
	current = head
	while current is not None:
		if target == current.data:
			return True
		current = current.next
	return False

# Find node (recursive)
def recursive_find_node(head, target):
	if head is None:
		return False
	if head.data is target:
		return True
	return recursive_find_node(head.next, target)

	

# a = Node("A")
# b = Node("B")
# c = Node("C")
# d = Node("D")

# a.next = b
# b.next = c
# c.next = d

num1 = Node(5)
num2 = Node(5)
num3 = Node(5)
num4 = Node(5)

num1.next = num2
num2.next = num3
num3.next = num4

# print_linkedList(a)
print(recursive_sum_linkedList(num1))
