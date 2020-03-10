# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findBottomLeftValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        queue = [root]
        
       
        while queue:
            current = queue.pop(0)
            if current.right and current.left:
                queue.append(current.right)
                queue.append(current.left)
            if not current.right and current.left:
                queue.append(current.left)
            if not current.left and current.right:
                queue.append(current.right)
        return current.val
            
        
        
