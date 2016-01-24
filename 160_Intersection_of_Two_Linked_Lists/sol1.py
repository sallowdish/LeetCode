# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        if not headA or not headB:
            return None
        l1 = self.linkList_to_list(headA)
        l2 = self.linkList_to_list(headB)
        length = len(l1) if len(l1) < len(l2) else len(l2)
        index = 0
        for i in range(1, length + 1):
            if l1[-i] == l2[-i]:
                index = i
        if not index < length + 1:
            return None
        return self.get_nth_node(headA, len(l1) - index + 1)

    def linkList_to_list(self, head):
        if not head:
            return []
        l = []
        while head:
            l.append(head.val)
            head = head.next
        return l

    def get_nth_node(self, head, n):
        try:
            c = 1
            while c < n:
                head = head.next
                c += 1
            return head
        except IndexError:
            return None
