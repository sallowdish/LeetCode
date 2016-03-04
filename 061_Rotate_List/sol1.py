# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if not head:
            return head
        l = []
        curr = head
        while curr:
            l.append(curr.val)
            curr = curr.next
        k %= len(l)
        l = l[-k:]+l[:-k]
        newHead = None
        for i in l:
            new_node = ListNode(i)
            if not newHead:
                newHead = new_node
                curr = newHead
            else:
                curr.next = new_node
                curr = curr.next
        return newHead