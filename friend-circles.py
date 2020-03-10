class Solution(object):
    def findCircleNum(self, M):
        """
        :type M: List[List[int]]
        :rtype: int
        """
        if not M:
            return 0
        rows = len(M)
        visited = set()
        
        def dfs(i):
            for j ,val in enumerate(M[i]):
               
                if val == 1 and j not in visited:
                    visited.add(j)
                    dfs(j)
        count = 0
        
        for i in range(rows):
     
            if i not in visited:
                dfs(i)
                count += 1
        return count
