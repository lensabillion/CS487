class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2 :
            return max(nums)
       
        
        def robHelper(nums):
            if len(nums) == 0:
                return 0
            Rob=[0] * len(nums)
            Rob[0] = nums[0]
            Rob[1] = nums[1]
            Rob[2] = nums[0] + nums[2]


            for i in range(3,len(nums)):
                Rob[i] = max(Rob[i-2],Rob[i-3]) + nums[i]

            return max(Rob)
        return max(robHelper(nums[0:len(nums)-2]),robHelper(nums[1:len(nums)-1]))
