class Solution(object):
    def minimumTotal(self, tri):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        for i in range(len(tri)-1,-1,-1):
            for j  in range(len(tri[i])-1):
                tri[i-1][j] += min(tri[i][j],tri[i][j+1])
                
        return tri[0][0]
    
