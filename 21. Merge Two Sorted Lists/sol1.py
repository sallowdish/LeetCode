# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        # import pdb
        # pdb.set_trace()
        c = p = None
        while l1 or l2:
            if l1 is None:
                if c is None:
                    c = l2
                    p = c
                else:
                    c.next = l2
                    c = c.next
                l2 = l2.next
                continue
            elif l2 is None:
                if c is None:
                    c = l1
                    p = c
                else:
                    c.next = l1
                    c = c.next
                l1  = l1.next
            else:
                v1 = l1.val
                v2 = l2.val
                nextNode = l1 if v1 < v2 else l2
                if c is None:
                    c = nextNode
                    p = c
                else:
                    c.next = nextNode
                    c = c.next
                l1 = l1.next if v1 < v2 else l1
                l2 = l2.next if v1 >= v2 else l2
        return p
