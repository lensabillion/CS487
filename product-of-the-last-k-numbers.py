class ProductOfNumbers(object):

    def __init__(self):
        self.list = [1]
        

    def add(self, num):
        """
        :type num: int
        :rtype: None
        """
        if num == 0:
            self.list =[]
            self.list.append(1)
        else:
    
            self.list.append(num * self.list[-1])
      

    def getProduct(self, k):
        """
        :type k: int
        :rtype: int
        """
        if len(self.list)> k:
            return self.list[-1]//self.list[len(self.list) - k -1]
        return 0
            
        


# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)
