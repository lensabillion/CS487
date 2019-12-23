class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        myreturn =[]
      
        for i in range(0,len(nums)):
          
            for j in range(0,i):
                if nums[i] + nums[j]==target:
                    myreturn.append(j)
                    myreturn.append(i)
        return myreturn
