class Solution(object):
    def orangesRotting(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        row = len(grid)
        col = len(grid[0])
        queue = []
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 2:
                    queue.append((i,j,0))

        direction =((0,1),(1,0),(-1,0),(0,-1))
        count = 0
        while queue:
            print(queue)
            i,j,count = queue.pop(0)
           
            for d in direction:
                ni,nj = i + d[0],j+d[1]
                if 0 <= ni < len(grid) and 0 <= nj < len(grid[0]) and grid[ni][nj] == 1:
                    grid[ni][nj] = 2
                    queue.append((ni,nj,count + 1))
                    
       
        if any(1 in row for row in grid):
            return -1
        return count
                
