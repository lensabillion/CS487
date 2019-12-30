class MyStack(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.Queue = []
        self.size = 0

    def push(self, x):
        """
        Push element x onto stack.
        :type x: int
        :rtype: None
        """
        self.Queue.append(x)
        self.size = self.size + 1

    def pop(self):
        """
        Removes the element on top of the stack and returns that element.
        :rtype: int
        """
        element =self.Queue[self.size-1]
        self.Queue = self.Queue[0:self.size-1]
        self.size =self.size - 1
        return element
        

    def top(self):
        """
        Get the top element.
        :rtype: int
        """
        return self.Queue[self.size-1]

    def empty(self):
        """
        Returns whether the stack is empty.
        :rtype: bool
        """
        if self.size == 0:
            return True
        else:
            return False


