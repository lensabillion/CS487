# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        reversed =None
        while head:
            next=head.next
            head.next=reversed
            reversed =head
            head=next
        return reversed
