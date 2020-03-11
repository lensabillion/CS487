class Solution(object):
    def kWeakestRows(self, mat, k):
        """
        :type mat: List[List[int]]
        :type k: int
        :rtype: List[int]
        """
        dict = {}
        list = []
        for row in range(0,len(mat)):
            s = 0
            for i in mat[row]:
                if i == 1:
                    s += 1
            dict[row] = s
      
        for i in sorted(dict.items(),key=lambda x: x[1]):
            
                list.append(i[0])
           
        
        return list[:k]
