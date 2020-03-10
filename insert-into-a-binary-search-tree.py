# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def insertIntoBST(self, root, val):
        """
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode
        """
        
        newNode = TreeNode(val)
        if root is None:
            return newNode
        
        if root.val > val:
            if root.left is None:
                root.left = newNode
                return root

            self.insertIntoBST(root.left,val)

        if root.val < val:
            if root.right is None:
                root.right = newNode
                return root

            self.insertIntoBST(root.right,val)


        return root
