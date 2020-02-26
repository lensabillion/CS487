class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        q = 0
        p = 0
        while q < len(s) and p < len(t):
            if s[q] == t[p]:
                q+=1
                p+=1
            else:
                p+=1
        return q == len(s)
