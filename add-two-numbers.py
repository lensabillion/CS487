# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        r1 = ""
        r2 = ""
        
        while l1 != None:
            r1 = str(l1.val) + r1
            l1 = l1.next
        while l2 != None:
            r2 = str(l2.val) + r2
            l2 = l2.next
      
        sum = str(int(r1) + int(r2))
        r=rlist = ListNode(None)
        for i in range(len(sum)-1,-1,-1):
            r.next = ListNode(sum[i])
            r=r.next
          
        return rlist.next
