class Solution(object):
    def twoCitySchedCost(self, costs):
        """
        :type costs: List[List[int]]
        :rtype: int
        """

        N = len(costs)//2
        ans = 0
        diffa, diffb = [], []

        for cost in costs:  
            if cost[0] < cost[1]: 
                ans += cost[0]     
                diffb.append(cost[1]-cost[0]) 
            else:                 
                ans += cost[1]
                diffa.append(cost[0]-cost[1])

        if len(diffa) < len(diffb): 
            diffb.sort()
            for j in range(len(diffb)-N):
                ans += diffb[j]

        if len(diffa) > len(diffb): 
            diffa.sort()
            for i in range(len(diffa)-N):
                ans += diffa[i]

        return ans
