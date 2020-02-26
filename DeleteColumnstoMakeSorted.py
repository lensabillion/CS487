class Solution(object):
    def minDeletionSize(self, A):
        """
        :type A: List[str]
        :rtype: int
        """
        d = []
        if len(A) == 1:
            return 0
        if len(A) == 2:
            if len(A[0]) == 1 and A[0] <= A[1]:
                return 0
        j = 0
        while j < len(A[0]):
            for i in range(0,len(A)-1):
                min = A[i][j]
                if A[i+1][j] < min:
                    d.append(j)
                    
                else:
                    min = A[i+1][j]
            j += 1
          
        return len(set(d))
                
                
            
