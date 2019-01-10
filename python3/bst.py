"""Simple implementation of a BST.

Search, delete, insert, invert.
"""

class Node:
	def __init__(self, key):
		self.val = key
		self.left = None
		self.right = None

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
		if root.val < node.val:
			if root.right is None:
				root.right = node
			else:
				insert(root.right, node)
		else:
			if root.left is None:
				root.left = node
			else:
				insert(root.left, node)

def minVal(node):
	current = node

	while(current.left is not None):
		current = current.left
	return current

def remove(root, key):
	if root is None:
		return root
	if key < root.val:
		root.left = remove(root.left, key)
	elif key > root.val:
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

		tmp = minVal(root.right)
		root.val = tmp.val
		root.right = remove(root.right, tmp.val)

	return root

def preorder(root):
	if root:
		print(root.val)
		preorder(root.left)
		preorder(root.right)

def inorder(root):
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
				res.append(current.val)
				current = current.right
			else:
				flag = 1
	print(res)
	
	# Recursive way
	# if root:
	# 	inorder(root.left)
	# 	print(root.val)
	# 	inorder(root.right)

def postorder(root):
	if root:
		postorder(root.left)
		postorder(root.right)
		print(root.val)

def invert(root):
	if root is None:
		return root
	root.left, root.right = root.right, root.left

	invert(root.left)
	inverting(root.right)

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
