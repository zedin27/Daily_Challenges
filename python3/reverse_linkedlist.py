class Node:
	def __init__(self, data):
		self.data = data
		self.next = None

	def __repr__(self):
		return str(self.data)

# Iterative approach
def reverseList(head):
	prev_node = None
	current_node = head

	while current_node is not None:
		next_node = current_node.next
		current_node.next = prev_node
		prev_node = current_node
		current_node = next_node
	
	return prev_node

# Recursive approach
def recursive_reverseList(head, prev = None):
	if head is None:
		return prev
	next = head.next
	head.next = prev
	return recursive_reverseList(next, head)


def print_linkedList(head):
	current = head
	while current is not None:
		print(current.data, end=" -> ")
		current = current.next
	print("None")

num1 = Node(1)
num2 = Node(2)
num3 = Node(3)
num4 = Node(4)
num5 = Node(5)

num1.next = num2
num2.next = num3
num3.next = num4
num4.next = num5
print_linkedList(recursive_reverseList(num1))
