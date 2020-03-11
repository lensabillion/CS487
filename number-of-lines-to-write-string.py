class Solution(object):
    def numberOfLines(self, widths, S):
        """
        :type widths: List[int]
        :type S: str
        :rtype: List[int]
        """
        
        width = 100
        line = 0
        
        for i in S:
            length = widths[ord(i)- ord("a")]
            if width + length > 100:
                line += 1
                width = 0
            width += length
           

        
        return [line,width]
