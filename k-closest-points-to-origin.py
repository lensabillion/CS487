import math
class Solution(object):
    def kClosest(self, points, K):
        """
        :type points: List[List[int]]
        :type K: int
        :rtype: List[List[int]]
        """
        dict = {}
        rlist = []
        for i in points:
            dist = math.sqrt(pow(i[0],2) + pow(i[1],2))
            dict[tuple(i)] = dist
        d = sorted(dict.items(),key=lambda x: x[1])
        for i in range(K):
            rlist.append(list(d[i][0]))
        return rlist
            
