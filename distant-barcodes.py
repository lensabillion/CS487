class Solution(object):
    def rearrangeBarcodes(self, barcodes):
        """
        :type barcodes: List[int]
        :rtype: List[int]
        """
        dict = {}
        rlist = [0] * len(barcodes)
        for i in barcodes:
            if i not in dict:
                dict[i] = 1
            else:
                dict[i] += 1
        print(dict)
        index = 0
        for i in sorted(dict.items(),key=lambda x:x[1], reverse = True):
            
            for j in range(0,i[1]):
                if index >= len(barcodes):
                    index = 1
                rlist[index] = i[0]
                index += 2
        return rlist
        
        
