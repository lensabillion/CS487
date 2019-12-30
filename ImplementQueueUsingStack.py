class MyQueue(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.stack=[]
        self.size=0
        

    def push(self, x):
        """
        Push element x to the back of queue.
        :type x: int
        :rtype: None
        """
        self.stack.append(x)
        self.size = self.size + 1

    def pop(self):
        """
        Removes the element from in front of queue and returns that element.
        :rtype: int
        """
        element = self.stack[0]
        self.stack=self.stack[1:]
        self.size = self.size - 1
        return element

    def peek(self):
        """
        Get the front element.
        :rtype: int
        """
        return self.stack[0]

    def empty(self):
        """
        Returns whether the queue is empty.
        :rtype: bool
        """
        if self.size == 0:
            return True
        else:
            return False
