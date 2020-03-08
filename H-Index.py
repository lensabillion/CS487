class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        buckets=[0]*(len(citations)+1)
        for citation in citations:
            buckets[min(citation,len(citations))]+=1
        papers =0
        for bucket in range(len(buckets)-1,-1,-1):
            papers +=buckets[bucket]
            if papers>=bucket:
                return bucket
