class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        s = ""
        while l1 is not None:
            s += str(l1.val)
            l1 = l1.next
        op1 = int("".join(s)[::-1])
        s = ""
        while l2 is not None:
            s += str(l2.val)
            l2 = l2.next
        op2 = int("".join(s)[::-1])
        s = op1 + op2
        rev = None
        for i in list(str(s)[::-1]):
            if rev is None:
                rev = ListNode(int(i))
                ptr = rev
            else:
                ptr.next = ListNode(int(i))
                ptr = ptr.next
        return rev