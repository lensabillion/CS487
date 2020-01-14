class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        min = 0
        max = len(nums)-1
        while min <= max:
            middle = (min + max)//2
        
            if target == nums[middle]:
                return middle
            if target < nums[middle]:
                max = middle-1
                
            if target > nums[middle]:
                min = middle+1
                
           
        return -1
