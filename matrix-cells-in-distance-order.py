class Solution(object):
    def allCellsDistOrder(self, R, C, r0, c0):
        """
        :type R: int
        :type C: int
        :type r0: int
        :type c0: int
        :rtype: List[List[int]]
        """
      
        list1 = []
        rlist = []
        dict = {}
        for i in range(R):
            for j in range(C):
                
                list1.append([i,j])
        for i in list1:
            
            dist = abs(r0 - i[0]) + abs(c0 -i[1])
            d = tuple(i)
            dict[d] = dist
        for w in sorted(dict.items(), key=lambda x: x[1]):
            rlist.append(list(w[0]))
        return rlist
