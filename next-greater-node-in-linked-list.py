# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def nextLargerNodes(self, head):
        """
        :type head: ListNode
        :rtype: List[int]
        """
        
        answer = []
        stack = []
        i = 0
        while head:
            answer.append(0)
            value = head.val
            while len(stack) > 0 and stack[-1][1] < value:
                answer[stack.pop()[0]] = value
            stack.append((i,value))
                
            head = head.next
            i += 1
        return answer
               
