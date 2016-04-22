# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

    def to_list(self):
        ret = []
        curr = self
        while curr:
            ret.append(curr.val)
            curr = curr.next
        return ret


def build_linked_list_from_pylist(lst):
    head = curr = None
    for i in lst:
        assert type(i) == int
        node = ListNode(i)
        if curr:
            curr.next = node
            curr = curr.next
        else:
            head = curr = node
    return head
