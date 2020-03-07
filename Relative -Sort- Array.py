class Solution(object):
    def relativeSortArray(self, arr1, arr2):
        """
        :type arr1: List[int]
        :type arr2: List[int]
        :rtype: List[int]
        """
        count=[]
        left=[]
        right=[]
        for j in range(0,max(arr1)+1):
            count.append(0)
        for k in range(0,len(arr1)):
        
            count[arr1[k]]=count[arr1[k]]+1
   
        for val in  arr2:
            if val in arr1:
                left +=[val]*count[val]
        for val in arr1:
            if val not in arr2 and val not in right:
                right +=[val]*count[val]
        right.sort()
        return left+right
        
