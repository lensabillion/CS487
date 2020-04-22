from collections import deque
class Solution(object):
    def shortestSubarray(self, A, k):
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        """
        length = len(A)
        
        sums = [0] * (length+1)
        for i in range(length):
            sums[i+1] = sums[i] + A[i]
        queue = deque()
        result = length + 1
        for i in range(length +1):
            while queue and sums[i] - sums[queue[0]] >= k:
                result = min(result, i - queue.popleft())
            while queue and sums[queue[-1]] >= sums[i]:
                queue.pop()
            queue.append(i)
        if result <= length:
            return result 
        else:
            return -1
