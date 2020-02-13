class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """ 
        if not grid:
            return 0
        rows =len(grid)
        cols = len(grid[0])
        
        new = [[0]*cols  for _ in range(rows)]
        new[0][0] = grid[0][0]
        for i in range(1,cols):
            new[0][i] = new[0][i-1] + grid[0][i]
        for i in range(1,rows):
            new[i][0] = new[i-1][0] + grid[i][0]
        for i in range(1 , rows):
            for j in range(1,cols):
                new[i][j] = min(new[i-1][j],new[i][j-1]) + grid[i][j]
        return new[-1][-1]
