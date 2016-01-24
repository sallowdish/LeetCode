#!/usr/bin/python3
from unittest import TestCase, main
from sol1 import Solution

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
        headA = "1"
        headB = "1.0"
        self.assertEqual(self.sol.compareVersion(headA, headB), 0)

    def test1(self):
        headA = "1"
        headB = "2"
        self.assertEqual(self.sol.compareVersion(headA, headB), -1)

    def test2(self):
        headA = "1.1"
        headB = "1.2"
        self.assertEqual(self.sol.compareVersion(headA, headB), -1)

    def test3(self):
        headA = "1.1.3"
        headB = "1.2.1"
        self.assertEqual(self.sol.compareVersion(headA, headB), -1)

    def test4(self):
        headA = "1.1"
        headB = "2.1"
        self.assertEqual(self.sol.compareVersion(headA, headB), -1)

    def test5(self):
        headA = "1.5.7"
        headB = "1.6"
        self.assertEqual(self.sol.compareVersion(headA, headB), -1)

    def test6(self):
        headA = "1"
        headB = "1.1"
        self.assertEqual(self.sol.compareVersion(headA, headB), -1)





if __name__ == "__main__":
    # logging.basicConfig( stream=sys.stderr )
    # logging.getLogger( "Test.testSomething" ).setLevel( logging.DEBUG )
    main()
