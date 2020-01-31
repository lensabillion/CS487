

class Solution(object):
    def numEquivDominoPairs(self, dominoes):
        """
        :type dominoes: List[List[int]]
        :rtype: int
        """
      
        pairs = 0
        dict ={}
        for list in dominoes:
            if list[0] > list[1]:
                temp = list[1]
                list[1] = list[0]
                list[0] = temp
            d_tuple = tuple(list)
            if dict.get(d_tuple) == None:
             
                dict[d_tuple] = 0
            else:
                 
                dict[d_tuple] = dict.get(d_tuple) + 1
                pairs = dict.get(d_tuple) + pairs
                
        return pairs
