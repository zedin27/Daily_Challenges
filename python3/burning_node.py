"""
BURNING NODE

A binary tree is started burning from a leaf node.
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

LeafSide = []
# Tree class
class Node:
	def __init__(self, key):
		self.left = None
		self.right = None
		self.value = key

#Height of the leaf
def leafHeight(root, leaf):
	if root is None:
		return 0
	else:
		if root.left is leaf:
			aux = 1 + leafHeight(root.right, leaf)
			LeafSide.append(aux)
			return 1
		if root.right is leaf:
			aux = 1 + leafHeight(root.left, leaf)
			LeafSide.append(aux)
			return 1
		return 1 + max(leafHeight(root.left, leaf), leafHeight(root.right, leaf))

#How long will it take to burn the the node to furthest node
def timeBurn(root, leaf):
	hl = leafHeight(root.left, leaf)
	hr = leafHeight(root.right, leaf)
	opposite_LeafSide = 1 + hl + hr
	return max(opposite_LeafSide, LeafSide[0])

# Sample code
root = Node(1)
root.left = Node(1)
root.right = Node(1)
root.left.left = Node(1)
root.left.right = Node(1)
root.left.right.left = Node(1)
root.left.right.right = Node(1)
root.right.right = Node(1)
root.right.right.right = Node(1)
root.right.right.right.right = Node(1)
print ("Starting from the given node, it will take %ds to burn the whole tree" % (timeBurn(root, root.left.right)))
