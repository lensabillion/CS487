class Solution(object):
    def findLength(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: int
        """
        dp =[[0] * (len(B)+1) for _ in range(len(A) +1)]
        #print(dp)
        for i in range(len(A)-1,-1,-1):
            for j in range(len(B)-1,-1,-1):
                if A[i] == B[j]:
                    dp[i][j] = dp[i+1][j+1] + 1
     
        return max(max(row) for row in dp)
