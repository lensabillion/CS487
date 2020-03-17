# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        queue = [(root)]
        rlist = []
        while queue:
            inside_list = []
            for i in range(len(queue)):
                node = queue.pop(0)
           
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                inside_list.append(node.val)
            rlist.insert(0,inside_list)
        return rlist
    
