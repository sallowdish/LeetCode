# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None:
            return head
        curr = head
        appearedVal = [curr.val]
        ptr = curr.next
        while ptr is not None:
            if ptr.val in appearedVal:
                pass
            else:
                appearedVal.append(ptr.val)
                curr.next = ptr
                curr = ptr
            ptr = ptr.next
        curr.next = None
        return head