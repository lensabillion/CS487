class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        if not nums:
            return 0
        lis = [1] * len(nums)
        for i in range(1,len(nums)):
            for j in range(0,i):
                if  nums[i] > nums[j] and lis[i] < lis[j] + 1:
                    lis[i] = lis[j] + 1
     
        return max(lis)
       
