# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def getAllElements(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: List[int]
        """
        list = []
        def inorder(root):
            if root:
                inorder(root.left)
                list.append(root.val)
                inorder(root.right)
            return list
        list1 = inorder(root1)
        list1 = inorder(root2)
   
        return sorted(list1)
