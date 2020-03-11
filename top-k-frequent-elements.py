import heapq
class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        dict = {}
        heap = [] 
        list = []
        for i in nums:
            if i not in dict:
                dict[i] = 0
            dict[i] += 1
        for key,value in dict.items():
            heapq.heappush(heap,(-value,key))
        for _ in range(k):
            list.append(heapq.heappop(heap)[1])
            
        
        
        return list
            
