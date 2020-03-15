class Solution(object):
    def minSetSize(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        half = len(arr) / 2
        
        dict ={}
        count =0
        rlist = set()
        for i in arr:
            if i not in dict:
                dict[i] = 0
            dict[i] +=1
       
        dict = sorted(dict.items(), key=lambda x: x[1], reverse=True)
      
        for i in dict:
            if i[1] >= half:
                rlist.add(i[0])
                return len(rlist)
            else:
                
                if count < half:
                    rlist.add(i)
                    count += i[1]
                else:
                    
                    return len(rlist)
