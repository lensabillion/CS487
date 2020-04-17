# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def insertionSortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
      
        sorted_list = ListNode(None)
        curr = head
        prev = sorted_list
        next = None
        while curr:
            next = curr.next
            while prev.next != None and prev.next.val < curr.val:
                prev = prev.next
            curr.next = prev.next
            prev.next = curr
            prev = sorted_list
            curr = next
           
        return sorted_list.next
