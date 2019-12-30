class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.mainStack=[]
        self.min=[]

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.mainStack.append(x)
        if not self.min or x <= self.min[-1]:
            self.min.append(x)
        

    def pop(self):
        """
        :rtype: None
        """
        item=self.mainStack.pop()
        if item == self.min[-1]:
            self.min.pop()

    def top(self):
        """
        :rtype: int
        """
        return self.mainStack[-1]
            

    def getMin(self):
        """
        :rtype: int
        """
        
        return self.min[-1]
            
 


