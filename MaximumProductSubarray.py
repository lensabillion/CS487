class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        maxi = nums[0]
        mini = nums[0]
        r = nums[0]
        
        for i in range(1,len(nums)):
            if nums[i] < 0:
                temp = maxi
                maxi = max(nums[i],mini * nums[i])
                mini = min(nums[i],temp * nums[i])
            else:
                maxi = max(nums[i],maxi* nums[i])
                mini = min(nums[i],mini * nums[i])
            r = max(r,maxi)
        return r
