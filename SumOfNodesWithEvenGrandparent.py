# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sumEvenGrandparent(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        sum = 0

        if not root:
            return 0
      
        if root.val % 2 == 0:
            if root.left:
                if root.left.left :
                    sum += root.left.left.val
                if root.left.right :
                    sum += root.left.right.val
            if root.right:
                if root.right.left:
                    sum += root.right.left.val 
                if root.right.right :
                    sum += root.right.right.val
                
        left = self.sumEvenGrandparent(root.left)
        right = self.sumEvenGrandparent(root.right)
       
        return sum + left + right
