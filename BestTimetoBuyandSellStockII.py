class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        sum = 0 
        for i in range (1,len(prices)):
            
            sum = sum + max(prices[i]-prices[i-1],0)
        return sum
