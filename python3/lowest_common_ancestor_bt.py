"""Lowest Common Ancestor"""

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """

        #O(n) linear time solution
        if not root:
            return None
        if root == p or root == q:
            return root

        right = self.lowestCommonAncestor(self, root->right, p, q)
        left = self.lowestCommonAncestor(self, root->left, p, q)

        if left is not None and right is not None:
            return root
        if not left:
            return right
        if not right:
            return left
