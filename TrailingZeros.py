class Solution(object):
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        i = 5
        zereos=0
        while n/i >= 1:
            zereos = zereos + n/i 
            i = i *5
        
       
        return zereos
