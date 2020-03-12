# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        
        def dfs(root,left,right):
            if not root:
                return True
            
            if not left < root.val < right:
                return False
            if not dfs(root.left,left,root.val) or not dfs(root.right,root.val,right):
                return False
           
            return True
           
        return dfs(root,float("-inf"), float("inf"))
