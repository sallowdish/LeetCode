# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next or not head.next.next:
            return head
        odd_head = curr = odd_last = head
        even_head = head.next
        isOdd = True
        while curr.next.next:
            tmp = curr.next
            curr.next = curr.next.next
            if isOdd:
                odd_last = curr.next
            isOdd = not isOdd
            curr = tmp
        if isOdd:
            curr.next = even_head
        else:
            curr.next.next = even_head
            curr.next = None
        return head
