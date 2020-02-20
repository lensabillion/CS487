class Solution(object):
    def mostCommonWord(self, paragraph, banned):
        """
        :type paragraph: str
        :type banned: List[str]
        :rtype: str
        """
        
        dict = {}
        words = re.split("[!?',;.\\s]+", paragraph.lower())
        for word in words:
            if word.isalpha():
            
                if word not in dict:
                    dict[word] = 0
                dict[word] += 1
        dict = sorted(dict.items(), key=lambda x: x[1], reverse = True)
        for i in dict:
            if i[0] not in banned:
                return i[0]
            
         
       
          
