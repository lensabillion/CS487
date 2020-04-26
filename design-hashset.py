class MyHashSet(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.hashset = [False] * 1000001

    def add(self, key):
        """
        :type key: int
        :rtype: None
        """
        self.hashset[key] = True
        

    def remove(self, key):
        """
        :type key: int
        :rtype: None
        """
        
        self.hashset[key] =False
        

    def contains(self, key):
        """
        Returns true if this set contains the specified element
        :type key: int
        :rtype: bool
        """
       
        return self.hashset[key] 
