class Solution(object):
    def sortArrayByParityII(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        odd = []
        even = []
        for i in A:
            if i % 2 != 0:
                odd.append(i)
            else:
                even.append(i)
       
        for i in range(0,len(A)):
            if i % 2 == 0:
                A[i] = even[0]
                even.pop(0)      
            else:
                A[i] = odd[0]
                odd.pop(0)
        return A
