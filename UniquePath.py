class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        if m == 0 or n == 0:
            return 0
        row =[1 for _ in range(n)]
        print(row)
        for i in range(m-1):
            new = [1]
            for j in range(1,n):
                new.append(new[-1] + row[j])
            row = new
                
        return row[-1]
