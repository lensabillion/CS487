# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def searchBST(self, root, val):
        """
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode
        """
        def search(root,val):
            if  val == root.val:
                return root
            if val > root.val and root.right:
                return search(root.right,val)
            if val < root.val and root.left:
                return search(root.left,val)
            else:
                return None
        return search(root,val)
