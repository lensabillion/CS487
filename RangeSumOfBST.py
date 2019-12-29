# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def rangeSumBST(self, root, L, R):
        """
        :type root: TreeNode
        :type L: int
        :type R: int
        :rtype: int
        """
        def sum(node):
            if not node:
                return 0
            if node.val < L:
                return sum(node.right)
            if node.val > R:
                return sum(node.left)
            return node.val + sum(node.left)+ sum(node.right)
        return sum(root)

