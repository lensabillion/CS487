class Solution(object):
    def divisorGame(self, N):
        """
        :type N: int
        :rtype: bool
        """
        r = [False] * N
       
        if N == 1:
            return False
            
        for i in range(2,N+1):
            if r[i-2] == True:
                r[i-1] = False
            elif r[i-2] == False:
                r[i-1] = True
        #print(r)   
        return r[-1]
