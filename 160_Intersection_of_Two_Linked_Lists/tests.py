#!/usr/bin/python3
from unittest import TestCase, main
from sol2 import Solution

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Test(TestCase):

    sol = None

    def setUp(self):
        self.sol = Solution()

    def test0(self):
        headA = None
        headB = None
        self.assertEqual(self.sol.getIntersectionNode(headA, headB), None)

    def test1(self):
        headA = None
        headB = ListNode(1)
        self.assertEqual(self.sol.getIntersectionNode(headA, headB), None)

    def test2(self):
        headA = ListNode(1)
        headB = ListNode(1)
        self.assertEqual(self.sol.getIntersectionNode(headA, headB), headA)

    def test3(self):
        headA = ListNode(0)
        headA.next = ListNode(1)
        headB = ListNode(1)
        self.assertEqual(self.sol.getIntersectionNode(headA, headB), headA.next)

    def test4(self):
        headA = ListNode(2)
        headA.next = ListNode(3)
        headA.next.next = ListNode(4)
        headB = ListNode(1)
        headB.next = ListNode(4)
        self.assertEqual(self.sol.getIntersectionNode(headA, headB), headA.next.next)





if __name__ == "__main__":
    # logging.basicConfig( stream=sys.stderr )
    # logging.getLogger( "Test.testSomething" ).setLevel( logging.DEBUG )
    main()
