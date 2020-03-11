class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """

        if not s and not t:
            return True
        return sorted(s) == sorted(t)
