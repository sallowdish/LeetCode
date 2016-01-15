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
        l1 = []
        l2 = []
        ans = []
        self.assertEqual(self.sol.mergeTwoLists(ListNode.listToListNode(l1), ListNode.listToListNode(l2)),None)

    def test1(self):
        l1 = []
        l2 = [1]
        ans = [1]
        self.assertEqual(self.sol.mergeTwoLists(ListNode.listToListNode(l1), ListNode.listToListNode(l2)).toList(), ans)

    def test2(self):
        l1 = [1,2,3]
        l2 = [4,5,6]
        ans = [1,2,3,4,5,6]
        self.assertEqual(self.sol.mergeTwoLists(ListNode.listToListNode(l1), ListNode.listToListNode(l2)).toList(), ans)

    def test3(self):
        l1 = [1,5,10]
        l2 = [4,5,6]
        ans = [1,4,5,5,6,10]
        self.assertEqual(self.sol.mergeTwoLists(ListNode.listToListNode(l1), ListNode.listToListNode(l2)).toList(), ans)

    def test2(self):
        l1 = [1,2,3, 10 ,15]
        l2 = [4,5,6]
        ans = [1,2,3,4,5,6,10,15]
        self.assertEqual(self.sol.mergeTwoLists(ListNode.listToListNode(l1), ListNode.listToListNode(l2)).toList(), ans)
    #
    # def test5(self):
    #     ints = [-12,-1,4,-14,0,10,7,-7,-6,9,6,-2,7,13,9,-1,4,12,9,4,14,0,-4,0,0,10,2,-7,7,-4,-11,10,2,8,4,-12,-4,-12,-4,-3,12,9,11,4,-1,-3,10,-12,-6,-4,-1,-14,3,2,-7,-11,-3,10,-11,-10,13,-15,7,0,0,-4,-5,11,0,-2,-14,-11,-8,12,1,-1,-14,-12,-6,-5,0,9,-4,-12,-4,4,14,9,-9,10,14,-11,10,6,-3,-4,10,-1,14,-13,13,7,-9,12,4,-1,-4,5,3,6,8,10,0,11,13,11,-7,5,-3,-1,0,-4,-4,-4,10,0]
    #     ans = [[-15,1,14],[-15,2,13],[-15,3,12],[-15,4,11],[-15,5,10],[-15,6,9],[-15,7,8],[-14,0,14],[-14,1,13],[-14,2,12],[-14,3,11],[-14,4,10],[-14,5,9],[-14,6,8],[-14,7,7],[-13,-1,14],[-13,0,13],[-13,1,12],[-13,2,11],[-13,3,10],[-13,4,9],[-13,5,8],[-13,6,7],[-12,-2,14],[-12,-1,13],[-12,0,12],[-12,1,11],[-12,2,10],[-12,3,9],[-12,4,8],[-12,5,7],[-12,6,6],[-11,-3,14],[-11,-2,13],[-11,-1,12],[-11,0,11],[-11,1,10],[-11,2,9],[-11,3,8],[-11,4,7],[-11,5,6],[-10,-4,14],[-10,-3,13],[-10,-2,12],[-10,-1,11],[-10,0,10],[-10,1,9],[-10,2,8],[-10,3,7],[-10,4,6],[-10,5,5],[-9,-5,14],[-9,-4,13],[-9,-3,12],[-9,-2,11],[-9,-1,10],[-9,0,9],[-9,1,8],[-9,2,7],[-9,3,6],[-9,4,5],[-8,-6,14],[-8,-5,13],[-8,-4,12],[-8,-3,11],[-8,-2,10],[-8,-1,9],[-8,0,8],[-8,1,7],[-8,2,6],[-8,3,5],[-8,4,4],[-7,-7,14],[-7,-6,13],[-7,-5,12],[-7,-4,11],[-7,-3,10],[-7,-2,9],[-7,-1,8],[-7,0,7],[-7,1,6],[-7,2,5],[-7,3,4],[-6,-6,12],[-6,-5,11],[-6,-4,10],[-6,-3,9],[-6,-2,8],[-6,-1,7],[-6,0,6],[-6,1,5],[-6,2,4],[-6,3,3],[-5,-5,10],[-5,-4,9],[-5,-3,8],[-5,-2,7],[-5,-1,6],[-5,0,5],[-5,1,4],[-5,2,3],[-4,-4,8],[-4,-3,7],[-4,-2,6],[-4,-1,5],[-4,0,4],[-4,1,3],[-4,2,2],[-3,-3,6],[-3,-2,5],[-3,-1,4],[-3,0,3],[-3,1,2],[-2,-2,4],[-2,-1,3],[-2,0,2],[-1,-1,2],[-1,0,1],[0,0,0]]
    #     self.assertEqual(self.sol.ListNode(ints)), ans)
    #
    # def test6(self):
    #     ints = [2,5,5,8,-7,-9,5,-1,-4,2,8,4,-6,-2,-2,9,-2,13,1,0,9,9,4,-13,13,3,-14,11,-5,-13,3,4,7,-15,-11,7,13,1,13,-14,11,-1,5,-10,12,11,14,-13,1,-8,3,-4,-14,14,-10,-15,-6,-9,3,-4,-7,-8,-15,8,-8,12,-8,13,-2,-9,14,-6,5,-3,-9,-6,-7,-10,-3,9,-2,7,-10,-9,-2,-5,13,7,-6,2,-12,-6,1,10,9,0,7,-13,-2,-9,-7,-2,-8,5,10,-1,6,-12,4,10,12,9,2,10,8,-15,12,6,-1,-9,-7,2]
    #
    #     ans = [[-15,1,14],[-15,2,13],[-15,3,12],[-15,4,11],[-15,5,10],[-15,6,9],[-15,7,8],[-14,0,14],[-14,1,13],[-14,2,12],[-14,3,11],[-14,4,10],[-14,5,9],[-14,6,8],[-14,7,7],[-13,-1,14],[-13,0,13],[-13,1,12],[-13,2,11],[-13,3,10],[-13,4,9],[-13,5,8],[-13,6,7],[-12,-2,14],[-12,-1,13],[-12,0,12],[-12,1,11],[-12,2,10],[-12,3,9],[-12,4,8],[-12,5,7],[-12,6,6],[-11,-3,14],[-11,-2,13],[-11,-1,12],[-11,0,11],[-11,1,10],[-11,2,9],[-11,3,8],[-11,4,7],[-11,5,6],[-10,-4,14],[-10,-3,13],[-10,-2,12],[-10,-1,11],[-10,0,10],[-10,1,9],[-10,2,8],[-10,3,7],[-10,4,6],[-10,5,5],[-9,-5,14],[-9,-4,13],[-9,-3,12],[-9,-2,11],[-9,-1,10],[-9,0,9],[-9,1,8],[-9,2,7],[-9,3,6],[-9,4,5],[-8,-6,14],[-8,-5,13],[-8,-4,12],[-8,-3,11],[-8,-2,10],[-8,-1,9],[-8,0,8],[-8,1,7],[-8,2,6],[-8,3,5],[-8,4,4],[-7,-7,14],[-7,-6,13],[-7,-5,12],[-7,-4,11],[-7,-3,10],[-7,-2,9],[-7,-1,8],[-7,0,7],[-7,1,6],[-7,2,5],[-7,3,4],[-6,-6,12],[-6,-5,11],[-6,-4,10],[-6,-3,9],[-6,-2,8],[-6,-1,7],[-6,0,6],[-6,1,5],[-6,2,4],[-6,3,3],[-5,-5,10],[-5,-4,9],[-5,-3,8],[-5,-2,7],[-5,-1,6],[-5,0,5],[-5,1,4],[-5,2,3],[-4,-4,8],[-4,-3,7],[-4,-2,6],[-4,-1,5],[-4,0,4],[-4,1,3],[-4,2,2],[-3,-3,6],[-3,-2,5],[-3,-1,4],[-3,0,3],[-3,1,2],[-2,-2,4],[-2,-1,3],[-2,0,2],[-2,1,1],[-1,-1,2],[-1,0,1]]
    #
    #     self.assertEqual(self.sol.ListNode(ints)), ans)
    #
    # def test7(self):
    #     ints = [0,0,0]
    #
    #     ans = [[0,0,0]]
    #
    #     self.assertEqual(self.sol.ListNode(ints)), ans)


if __name__ == "__main__":
    # logging.basicConfig( stream=sys.stderr )
    # logging.getLogger( "Test.testSomething" ).setLevel( logging.DEBUG )
    unittest.main()
