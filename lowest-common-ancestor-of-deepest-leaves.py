# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lcaDeepestLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        def dfs(root):
            if not root:
                return 0,None
            h1,lca1 = dfs(root.left)
            print("1",h1,lca1)
            h2,lca2 = dfs(root.right)
            print("2",h2,lca2)
            if h1 > h2:
                return h1+1,lca1
            if h1 < h2:
                return h2+1,lca2
            return h1+1,root
        return dfs(root)[1]
