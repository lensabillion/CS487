class Solution(object):
    def minSteps(self, n):
        """
        :type n: int
        :rtype: int
        """
       
        if n == 1:
            return 0
        step = n
        for i in range(2,n):
            if n % i == 0:
                step = min(step, i + self.minSteps(n//i))
               
        return step                
