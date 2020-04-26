class MyHashMap(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.hash = [-1] * 1000001
        

    def put(self, key, value):
        """
        value will always be non-negative.
        :type key: int
        :type value: int
        :rtype: None
        """
        self.hash[key] = value
            
        

    def get(self, key):
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        :type key: int
        :rtype: int
        """
        # if key in self.hash:
        #     return self.hash[key]
        # return -1
        return self.hash[key]

    def remove(self, key):
        """
        Removes the mapping of the specified value key if this map contains a mapping for the key
        :type key: int
        :rtype: None
        """
        self.hash[key] = -1
        
