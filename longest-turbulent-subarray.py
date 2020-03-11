class Solution(object):
    def maxTurbulenceSize(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
      
        if len(A) == 1:
            return 1
        ans = 0
        greater = 0
        smaller = 0
        for i in range(1,len(A)):
            if A[i] > A[i-1]:
                greater += 1
                smaller = 0
            elif A[i] < A[i-1]:
                smaller += 1
                greater = 0
            else:
                greater = 0
                smaller = 0
            ans  = max(ans,greater,smaller)
            greater, smaller =smaller ,greater
        return (ans + 1) if ans != 0 else 1
