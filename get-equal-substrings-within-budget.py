class Solution(object):
    def equalSubstring(self, s, t, maxCost):
        """
        :type s: str
        :type t: str
        :type maxCost: int
        :rtype: int
        """
        left = 0
        maxlength = 0
        cost = 0
        for right in range(0,len(s)):
            cost += abs(ord(s[right])-ord(t[right]))
            print(cost)
            while cost > maxCost:
                cost -= abs(ord(s[left])-ord(t[left]))
                left += 1
            maxlength  = max(maxlength ,right - left + 1)
        return maxlength
         
            
