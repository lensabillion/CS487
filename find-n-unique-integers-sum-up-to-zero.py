class Solution(object):
    def sumZero(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        rlist = []
        if n == 1:
            return [0]
        if n % 2 == 0:
            for i in range(1,(n/2) +1):
                rlist.append(i)
                rlist.append(-i)
        if n % 2 != 0:
            rlist = [0]
            for i in range(1,(n/2) +1):
                rlist.append(i)
                rlist.append(-i)
        return rlist
            
