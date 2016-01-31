# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        while head and head.val == val:
            head = head.next
        if not head:
            return head
        prev_ptr = head
        curr_ptr = head.next
        while curr_ptr:
            if curr_ptr.val == val:
                prev_ptr.next = curr_ptr.next
                curr_ptr = curr_ptr.next
                if not curr_ptr:
                    return head
                else:
                    continue
            curr_ptr = curr_ptr.next
            prev_ptr = prev_ptr.next
        return head