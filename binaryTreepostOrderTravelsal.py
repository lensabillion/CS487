# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        postOrder =[]
        def postorder(root):
         
            if not root:
                return postOrder
            if root.left is None and root.right is None:
                postOrder.append(root.val)
            if root.left is None and root.right:
                postorder(root.right)

                postOrder.append(root.val)
            if root.left and root.right is None:
                postorder(root.left)

                postOrder.append(root.val)
            if root.left and root.right:
                postorder(root.left)
                postorder(root.right)

                postOrder.append(root.val)


            return postOrder
        return postorder(root)
