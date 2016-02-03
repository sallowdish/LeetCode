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
        if not head or not head.next:
            return head
        l = []
        curr_ptr = head
        while curr_ptr:
            l.append(curr_ptr)
            curr_ptr = curr_ptr.next
        for i in range(1, len(l)):
            l[-i].next = l[-(i+1)]
        l[0].next = None
        return l[-1]
