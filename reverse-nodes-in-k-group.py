# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        length = 0
        node =  head
        while node:
            length += 1
            node = node.next
        if k <= 1 or length < k:
            return head
        node =  None
        cur = head
        for _ in xrange(k):
            nxt = cur.next
            cur.next = node
            node = cur
            cur = nxt
            
        head.next = self.reverseKGroup(cur, k)
       
        return node
       
