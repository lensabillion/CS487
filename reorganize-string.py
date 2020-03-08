import math
class Solution(object):
    def reorganizeString(self, S):
        """
        :type S: str
        :rtype: str
        """
        dict = {}
        r  = [0] * len(S)
        for i in S:
            if i not in dict: 
                dict[i] = 1
            else:
                dict[i] = dict.get(i) + 1
        
        index = 0
        for i in sorted(dict.items(), key=lambda x: x[1], reverse=True):
           
            
            if i[1] > math.ceil(len(S)/2.0):
                return ""
            
            
             
            for j in range(0,i[1]):
                if (index >= len(S)):
                    index = 1

                r[index] = i[0]
                index += 2
            
                  
        return "".join(r)
                    
                    
                
