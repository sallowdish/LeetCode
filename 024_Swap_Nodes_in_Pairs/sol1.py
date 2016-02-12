# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head
        curr = prev = head
        head = head.next
        while curr and curr.next:
            tmp = curr.next.next
            curr.next.next = curr
            prev.next = curr.next
            curr.next = tmp
            prev = curr
            curr = curr.next
        return head
