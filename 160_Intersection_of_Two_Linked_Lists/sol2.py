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
        prevNode = None
        while 1:
            if not len(l1) or not len(l2):
                break
            nodeA = l1.pop()
            nodeB = l2.pop()
            if nodeA.val != nodeB.val:
                break
            prevNode = nodeA
        return prevNode

    def linkList_to_list(self, head):
        if not head:
            return []
        l = []
        while head:
            l.append(head)
            head = head.next
        return l
