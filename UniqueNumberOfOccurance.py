class Solution(object):
    def uniqueOccurrences(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        
        """
        count ={}
        for  i in arr:
            if count.get(i)==None:
        
                count[i]=1
            else:
                count[i] = count[i] + 1
        return len(set(count.values()))==len(count.values())
       
