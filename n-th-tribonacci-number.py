class Solution(object):
    
    def tribonacci(self, n):
        """
        :type n: int
        :rtype: int
        """
        
        result = [None] * 40
            
        def tri(n):
            if result[n] != None:
                return result[n]
            if n >= 3:
                result[n] = tri(n-3) + tri(n-2) + tri(n-1) 
                return result[n]
            else:
                if n==0:
                    return 0
                else:
                    return 1
        return tri(n)
