class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 1:
            return nums[0]
       
        
        list =[0] * len(nums)
        sum = 0
        for i in range(0,len(nums)):
            sum = max(list[i-1] + nums[i] , nums[i])
            
            list[i] = sum
    
        return max(list)
            
        
