class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        s1 = 1
        s2 = 2
        if n == 1 or n == 0:
            return s1
        if n == 2:
            return s2
    
        for i in range(3,n+1):
            si = s1 + s2
            
            s1   = s2
            s2   = si
            
            
        return s2
            
