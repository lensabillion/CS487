import heapq
class Solution(object):
    def topKFrequent(self, words, k):
        """
        :type words: List[str]
        :type k: int
        :rtype: List[str]
        """
        dict = {}
        heap =[]
        list =[]
        for word in words:
            if word not in dict:
                dict[word] = 0
            dict[word] += 1
        for key, values in dict.items():
            heapq.heappush(heap,(-values,key))
        for i in range(k):
            list.append(heapq.heappop(heap)[1])
        return list
            
