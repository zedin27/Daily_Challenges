"""A binary tree is started burning from a leaf node.
What is the time(1 second to burn from node to node) it takes to entire tree get burned?
The fire will spread to all the paths from a node.

PERSONAL NOTES IN APPROACHING THIS PROBLEM
This was one question for an interview session with Tesla.
Tesla ask questions related to trees and algorithms because is
an autonomous vehicle.

Say you have a tree like this, where N is the node that is on fire. This is
happening in the first second, so in the zeroth second:

         1
     /       \
    2          3
  /  \          \
 4    N          10
    /   \         \
   6     7         11
                    \
					 12
_______________________________________________________________________________
After one second has passed, the tree will be updated with more burned nodes.
An example of the next second will be like this:
         1
     /       \
    N          3
  /  \          \
 4    N          10
    /   \         \
   N     N         11
                    \
					 12

_______________________________________________________________________________

         N
     /       \
    N          3
  /  \          \
 N    N          10
    /   \         \
   N     N         11
                    \
					 12

_______________________________________________________________________________

         N
     /       \
    N          N
  /  \          \
 N    N          N
    /   \         \
   N     N         N
                    \
					 N

If you noticed, the tree took 4 seconds to burn the whole tree. Do you see why?
Take 5 to 10 minutes to guess why this is happening.


Now that you take some time, here is a case to consider. When you get a given
node that is on fire, how will the fire spread? Easy, because is a binary tree,
it will spread from left, right, and parent if there is any. Going left and right
is a simple task, but how would you go to the parent node? That is where I got
stuck in the interview.
"""

# Tree class
class Node:
	def __init__(self, key):
		self.left = None
		self.right = None
		self.value = key

# Maximum height of a tree
def maxHeight(root):
	if root is None:
		return 0
	else:
		return 1 + max(maxHeight(root.left), maxHeight(root.right))

# Diameter of the tree
def maxDiameter(root):
	how_long = 0
	if root is None:
		return 0
	else:
		root_diameter = maxHeight(root.left) + maxHeight(root.right)

		left_diameter = maxDiameter(root.left)
		right_diameter = maxDiameter(root.right)
		how_long = max(max(left_diameter, right_diameter), root_diameter)
		return how_long

# Sample code
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.left.right.left = Node(6)
root.left.right.right = Node(7)
root.right.right = Node(10)
root.right.right.right = Node(11)
root.right.right.right.right = Node(12)
print ("Starting from the given node, it will take %ds to burn the whole tree" % (maxDiameter(root.left.right)))
