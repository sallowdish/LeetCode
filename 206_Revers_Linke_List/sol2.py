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
        curr_ptr = head.next
        prev = head
        while curr_ptr:
            old_next = curr_ptr.next
            curr_ptr.next = prev
            prev = curr_ptr
            curr_ptr = old_next
        head.next = None
        return prev
