# # Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        l = []
        while head:
            l.append(head)
            head = head.next
        c = 1
        current = None
        while 1:
            pre = l.pop() if len(l)>0 else None
            if not pre:
                return current
            else:
                if c == n:
                    c += 1
                    continue
                if c == n + 1:
                    pre.next = current
                current = pre
                c += 1

