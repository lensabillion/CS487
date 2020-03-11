class Solution(object):
    def maxDistToClosest(self, seats):
        """
        :type seats: List[int]
        :rtype: int
        """
   
       
        result = 0
        j = 0
        for i in range(0, len(seats)):
            if seats[i] == 1:
                if (j == 0):
                    result =max(result ,i-j)
                else:
                    result = max(result,(i-j +1)/2)
                j = i + 1
        result = max(result ,len(seats) - j)
        return result
