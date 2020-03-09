class Solution(object):
    def isMonotonic(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """
        listin = [A[0]]
        listde = [A[0]]
        for i in range(1,len(A)):
            if A[i-1] <= A[i]:
                listin.append(A[i])
            if A[i-1] >= A[i]:
                listde.append(A[i])
        print(listin)
        print(listde)
        if len(listin ) == len(A) or len(listde) == len(A):
            return True
        return False
