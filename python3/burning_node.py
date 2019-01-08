r"""
BURNING NODE.

A binary tree is started burning from any node.
What is the time (1 second to burn from node to node) it takes to entire tree
get burned?
The fire will spread to all the paths from a node.

PERSONAL NOTES IN APPROACHING THIS PROBLEM
This was one question for an interview session with Tesla.
Tesla ask questions related to trees and algorithms because is
an autonomous vehicle.

Say you have a tree like this, where N is the node that is on fire. This is
happening in the first second, so in the zeroth second:

           1
       /       \
      1          1
    /  \          \
   1    1          1
      /   \         \
     1     N         1
                      \
                       1
_______________________________________________________________________________
After one second has passed, the tree will be updated with more burned nodes.
An example of the next second will be like this:

           1
       /       \
      N          1
    /  \          \
   1    N          1
      /   \         \
     N     N         1
                      \
                       1

_______________________________________________________________________________

           N
       /       \
      N          1
    /  \          \
   N    N          1
      /   \         \
     N     N         1
                      \
                       1

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


This example was given thanks to m69.

"Take the example below; first, traverse from the root to the leaf on fire (F):

     N
    / \
   N   N
  / \   \
 N   N   N
    / \   \
   N   F   N
  / \       \
 N   N       N
      \
       N
________________________________________________________________________________
Then, move up to its parent node, and take the sum of the distance to the
burning leaf (1) and the height of the left sub-tree (3), which is 4:

     N
    / \
   N   N
  / \   \
 N   4   N
    / \   \
   3   1   N
  / \       \
 N   2       N
      \
       1
________________________________________________________________________________
So 4 is the current maximum. Now, move up to the parent node, and take the
sum of the distance to the burning leaf (2) and the depth of the left sub-tree
(1), which is 3:

     N
    / \
   3   N
  / \   \
 1   2   N
    / \   \
   N   1   N
  / \       \
 N   N       N
      \
       N
________________________________________________________________________________
So the current maximum remains 4. Now move up to the parent node, and take the
sum of the distance to the burning leaf (3) and the depth of the right sub-tree
(4), which is 7:

     7
    / \
   3   4
  / \   \
 N   2   3
    / \   \
   N   1   2
  / \       \
 N   N       1
      \
       N
________________________________________________________________________________
The new maximum is 7, and we've reached the root node, so 7 is the answer, as
you can check by looking at which nodes are on fire after x seconds:

     3
    / \
   2   4
  / \   \
 3   1   5
    / \   \
   2   0   6
  / \       \
 3   3       7
      \
       4
________________________________________________________________________________
Here's an example where the root isn't part of the longest path:

         N            N            3                  2
        / \          / \          / \                / \
       N   N        4   N        2   1              1   3
      / \          / \          / \                / \
     N   F        3   1        N   1              2   0
    /            /            /                  /
   N            2            N                  3
  /            /            /                  /
 N            1            N                  4

The largest value encountered was 4, in the parent of the leaf on fire.
_______________________________________________________________________________"
"""

LeafSide = []

class Node:
	"""Tree class."""

	def __init__(self, key):
		"""Declare values of a node."""
		self.left = None
		self.right = None
		self.value = key

def leafHeight(root, leaf):
	"""Height of the leaf."""
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

def timeBurn(root, leaf):
	"""How long will it take to burn the the node to furthest node."""
	hl = leafHeight(root.left, leaf)
	hr = leafHeight(root.right, leaf)
	opposite_LeafSide = 1 + hl + hr
	return max(opposite_LeafSide, LeafSide[0])

if __name__ == '__main__':
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
