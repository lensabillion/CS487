# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def constructMaximumBinaryTree(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        
        if len(nums) == 1:
            return TreeNode(nums[0])
        def findMax(nums):
            
            max = nums[0]
            index = 0
            for i in range(1,len(nums)):
                if nums[i] > max:
                    max = nums[i]
                    index = i
            return max,index
        m,i =findMax(nums)
        root = TreeNode(m)
       
        if len(nums[0:i]):
            root.left = self. constructMaximumBinaryTree(nums[0:i])
        if len(nums[i+1:]):
            root.right = self. constructMaximumBinaryTree(nums[i+1:])
        return root
                
