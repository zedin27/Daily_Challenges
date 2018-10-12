# A binary tree is started burning from a leaf node.
# What is the time(1 second to burn from node to node) it takes to entire tree get burned?
# The fire will spread to all the paths from a node.
#
# PERSONAL NOTES IN APPROACHING THIS PROBLEM
# This was one question for an interview session with Tesla.
# Tesla ask questions related to trees and algorithms because is
# an autonomous vehicle.
#
# Say you have a tree like this, where N is the node that is on fire. This is
# happening in the first second, so in the zeroth second:
#
#         18
#      /       \
#    15          N
#   /  \        /  \
# 40    50    100   40
#_______________________________________________________________________________
# After one second has passed, the tree will be updated with more burned nodes.
# An example of the next second will be like this:
#          N
#      /       \
#    15          N
#   /  \        /  \
# 40    50    N     N
#
#_______________________________________________________________________________

#          N
#      /       \
#     N          N
#   /  \       /   \
#  40   50    N     N
#
#_______________________________________________________________________________
#
#          N
#      /       \
#    N           N
#   /  \       /  \
#  N    N     N     N
#
# If you noticed, the tree took 4 seconds to burn the whole tree. Do you see why?
# Take 5 to 10 minutes to guess why this is happening.
#
#
# Now that you take some time, here is a case to consider. When you get a given
# node that is on fire, how will the fire spread? Easy, because is a binary tree,
# it will spread from left, right, and parent if there is any. Going left and right
# is a simple task, but how would you go to the parent node? That is where I got
# stuck in the interview.

# Tree class
class Node:
	def __init__(self, key):
		self.left = None
		self.right = None
		self.value = key

def maxHeight(root):
	if root is None:
		return 0
	else:
		return 1 + max(maxHeight(root.left), maxHeight(root.right))

def maxWidth(root):
	if root is None:
		return 0
	else:
		left_height = maxHeight(root.left)
		right_height = maxHeight(root.right)

		left_diameter = maxWidth(root.left)
		right_diameter = maxWidth(root.right)
		return max(left_height + right_height + 1, max(left_diameter, right_diameter))

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.left.right.left = Node(6)
root.left.right.right = Node(7)
print ("Starting from the given node, it will take %ds to burn the whole tree" % (maxWidth(root.left) - 2))
