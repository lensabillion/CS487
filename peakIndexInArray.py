class Solution(object):
    def peakIndexInMountainArray(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        if len(A)>=3:
            for i in range(1,len(A)-1):
                if A[i-1] < A[i] and A[i] > A[i +1]:
                    return i
                    
                
