class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        if not m or not n:
            return 0
        if obstacleGrid[0][0] or obstacleGrid[-1][-1]:
            return 0
        row =[0 for _ in range(n + 1)]
        row[1] = 1

        for i in range(1,m+1):
            new = [0]
            for j in range(1,n+1):
                if obstacleGrid[i-1][j-1]:
                    new.append(0)
                else:
                    new.append(new[-1] + row[j])
            row = new
              
        return row[-1]
        
