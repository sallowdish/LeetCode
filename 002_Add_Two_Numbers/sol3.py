class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        return self.recAddTwoNumbers(l1,l2,0)

    def recAddTwoNumbers(self, node1, node2, carrier):
        if node1 is None and node2 is None and carrier == 0:
            return None
        else:
            if node1 is None and node2 is None:
                return ListNode(carrier)
            else:
                op1 = node1.val if node1 is not None else 0
                op2 = node2.val if node2 is not None else 0
                s = op1 + op2 + carrier
                d = s % 10
                newNode = ListNode(d)
                node1 = node1.next if node1 is not None else None
                node2 = node2.next if node2 is not None else None
                newNode.next = self.recAddTwoNumbers(node1, node2, int(s/10))
                return newNode