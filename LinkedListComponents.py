# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def numComponents(self, head, G):
        """
        :type head: ListNode
        :type G: List[int]
        :rtype: int
        """
        list = []
        for i in G:
            list.append(i)
        s = set(list)
        print(s)
        ans = 0
        while head:
            if (head.val in s ) and (head.next == None or not head.next.val in s) :
                ans += 1
            head = head.next
        return ans
