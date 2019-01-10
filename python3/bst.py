"""Simple implementation of a BST.

Search, delete, insert, mirror, and traversals.
"""

class Node:
	def __init__(self, key):
		self.key = key
		self.left = None
		self.right = None

	def __str__(self):
		return str(self.key)

def search(root, key):
	if root is None or root.node == key:
		return root
	if root.node < key:
		return search(root.right, key)
	return search(root.left, key)

def insert(root, node):
	if root is None:
		root = node
	else:
		if root.key < node.key:
			if root.right is None:
				root.right = node
			else:
				insert(root.right, node)
		else:
			if root.left is None:
				root.left = node
			else:
				insert(root.left, node)

def minkey(node):
	current = node

	while(current.left is not None):
		current = current.left
	return current

def remove(root, key):
	if root is None:
		return root
	if key < root.key:
		root.left = remove(root.left, key)
	elif key > root.key:
		root.right = remove(root.right, key)
	else:
		if root.left is None:
			tmp = root.right
			root = None
			return tmp

		elif root.right is None:
			tmp = root.left
			root = None
			return tmp

		tmp = minkey(root.right)
		root.key = tmp.key
		root.right = remove(root.right, tmp.key)

	return root

def preorder(root):
	"""Recursive traversal (root, left, right)."""

	if root:
		print(root.key)
		preorder(root.left)
		preorder(root.right)

def inorder(root):
	"""Non recursive traversal."""

	current = root
	stack = []
	res = []
	flag = 0

	while (not flag):
		if current is not None:
			stack.append(current)
			current = current.left
		else:
			if (len(stack) > 0):
				current = stack.pop()
				res.append(current.key)
				current = current.right
			else:
				flag = 1
	print(res)

	# """Recursive way (left, root, right)."""
	# if root:
	# 	inorder(root.left)
	# 	print(root.key)
	# 	inorder(root.right)

def postorder(root):
	"""Recursive traversal (left, right, root)."""
	if root:
		postorder(root.left)
		postorder(root.right)
		print(root.key)

def mirror(root):
	if root is None:
		return root
	root.left, root.right = root.right, root.left

	mirror(root.left)
	mirror(root.right)

	return root

if __name__ == '__main__':
	r = Node(50)
	insert(r, Node(30))
	insert(r,Node(20))
	insert(r,Node(40))
	insert(r,Node(70))
	insert(r,Node(60))
	insert(r,Node(80))

	# inorder(r)
	remove(r, 50)
	inorder(r)
	mirror(r)
