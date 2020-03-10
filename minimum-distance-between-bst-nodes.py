# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def minDiffInBST(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        stack =[root.val]
        
        values = set()
        def dfs(root):
         
            if root.left:
                stack.append(root.left.val)
                dfs(root.left)
            if root.right:
                stack.append(root.right.val)
                dfs(root.right)
            return stack
            
        s = dfs(root)
      
        while s:
            curr = s.pop()
            for i in stack:
                values.add(abs(curr-i))
        return min(values)
