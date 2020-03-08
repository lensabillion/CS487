class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        match = { '(':')','[':']','{':'}'}
        
        for i in s:
            if i in match:
                stack.append(i)
                
            else:
                if not stack or match[stack.pop()] != i :
                    return False
        print(stack)
        return not stack
