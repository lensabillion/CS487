class Solution(object):
    def shiftingLetters(self, S, shifts):
        """
        :type S: str
        :type shifts: List[int]
        :rtype: str
        """
        S = [ord(i) - ord("a") for i in S]
        shift = 0
       
        for  i in range(len(shifts)-1,-1,-1):
            shift += shifts[i]
            S[i] = (S[i] + shift) % 26
            
        return "".join(chr(j + ord("a")) for j in S)
