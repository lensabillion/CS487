class Solution(object):
    def sortedSquares(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        
        for i in range(0,len(A)):
            A[i] = A[i] * A[i]
        return sorted(A)
    
