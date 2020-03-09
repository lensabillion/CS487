# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        list = []
        stack = []
        if not root:
            return []
        stack.append((root))
        while stack:
            list.append(stack[-1].val)
            child = []
            for r in stack:
                if r.left:
                    child.append(r.left)

                if r.right:
                    child.append(r.right)
            stack = child
                
                
                

        return list
