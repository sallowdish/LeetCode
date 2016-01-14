# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        carrier = 0
        rev = None
        ptr = rev
        while l1 is not None or l2 is not None:
            op1 = l1.val if l1 is not None else 0
            op2 = l2.val if l2 is not None else 0
            s = op1 + op2 + carrier
            d = s % 10
            carrier = int(s / 10)
            if rev == None:
                rev = ListNode(d)
                ptr = rev
            else:
                ptr.next = ListNode(d)
                ptr = ptr.next
            l1 = l1.next if l1 is not None else None
            l2 = l2.next if l2 is not None else None
        if carrier != 0:
            ptr.next = ListNode(carrier)
        return rev
