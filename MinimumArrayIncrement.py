class Solution(object):
    def minIncrementForUnique(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        A.sort() #linear Sort
        moves = 0
        for i in range(1,len(A)):
            pre = A[i-1]
            cur = A[i]
            if pre >= cur:
                moves = moves + pre - cur + 1
                A[i] = pre + 1
        return moves
