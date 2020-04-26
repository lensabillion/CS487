class Solution(object):
    def powerfulIntegers(self, x, y, bound):
        """
        :type x: int
        :type y: int
        :type bound: int
        :rtype: List[int]
        """
        s = set()
       
        if x == 1:
             max_I = 1
        else:
            max_I = 1
            times = x
            while times < bound:
                times *= x
                max_I += 1
        if y == 1:
             max_J = 1
        else:
            max_J = 1
            times = y
            while times < bound:
                times *= y
                max_J += 1
        
        for i in range(max_I):
            for j in range(max_J):
                val = x**i + y**j
                if val <= bound:
                    s.add(val)
        return s
