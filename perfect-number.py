import math
class Solution(object):
    def checkPerfectNumber(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if (num <= 0):
            return False
        sum = 0
        for i in range (1,int(math.sqrt(num))+1):
        
            if num % i == 0:
                sum += i
               
                if (i*i != num):
                    sum += num / i
        return sum - num == num
            
        
