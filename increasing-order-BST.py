# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def increasingBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        nodes = []
        def dfs(root,nodes):
            if root:
                dfs(root.left,nodes)
                nodes.append(root.val)
                dfs(root.right,nodes)

        dfs(root,nodes)
        ans = TreeNode(None)
        r = ans
       
        for i in nodes:
            r.right = TreeNode(i)
            r = r.right
        
        return ans.right
