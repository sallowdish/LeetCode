#!/usr/bin/python3
from unittest import TestCase
from sol1 import Solution
import logging, unittest

# # Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

    def listToListNode(arr):
        ptr = None
        for i in arr[::-1]:
            newNode = ListNode(i)
            newNode.next = ptr
            ptr = newNode
        return ptr

    def toList(self):
        l = [self.val]
        node = self.next
        while node:
            l.append(node.val)
            node = node.next
        return l

class Test(TestCase):
    sol = None

    def setUp(self):
        self.sol = Solution()

    def test0(self):
        l1 = ""
        l2 = ""
        ans = 0
        self.assertEqual(self.sol.strStr(l1, l2) ,ans)

    def test1(self):
        l1 = "abc"
        l2 = "abc"
        ans = 0
        self.assertEqual(self.sol.strStr(l1, l2) ,ans)

    def test2(self):
        l1 = "abcd"
        l2 = "1234"
        ans = -1
        self.assertEqual(self.sol.strStr(l1, l2) ,ans)

    def test3(self):
        l1 = "abCd"
        l2 = "bC"
        ans = 1
        self.assertEqual(self.sol.strStr(l1, l2) ,ans)

    def test4(self):
        l1 = "mississippi"
        l2 = "pi"
        ans = 9
        self.assertEqual(self.sol.strStr(l1, l2) ,ans)




if __name__ == "__main__":
    # logging.basicConfig( stream=sys.stderr )
    # logging.getLogger( "Test.testSomething" ).setLevel( logging.DEBUG )
    unittest.main()
