class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        stack = []
        operator = {"/","*","+","-"}
       
        for i in tokens:
            if i in operator:
                right = stack.pop()
                left = stack.pop()
                if i == "/":
                    stack.append(int(left/float(right)))
                else:
                    stack.append((eval(str(left) + i + str(right))))
            else:
                stack.append(int(i))
        
            
            
        return stack[-1]
