#!/usr/bin/python3
from unittest import TestCase, main
from sol1 import Solution

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
        n = ListNode.listToListNode([])
        self.assertEqual(self.sol.deleteDuplicates(n), None)

    # overflow
    def test1(self):
        n = ListNode.listToListNode([1])
        self.assertEqual(self.sol.deleteDuplicates(n).toList(),[1])

    # long overflow
    def test2(self):
        n = ListNode.listToListNode([1,2,3])
        self.assertEqual(self.sol.deleteDuplicates(n).toList(), [1,2,3])

    # dissolved overflow
    def test3(self):
        n = ListNode.listToListNode([1,1,1])
        self.assertEqual(self.sol.deleteDuplicates(n).toList(), [1])

    def test4(self):
        n = ListNode.listToListNode([1,2,3,1])
        self.assertEqual(self.sol.deleteDuplicates(n).toList() ,[1,2,3])

    def test5(self):
        n = ListNode.listToListNode([1,2,3,3,2,1])
        self.assertEqual(self.sol.deleteDuplicates(n).toList() ,[1,2,3])





if __name__ == "__main__":
    # logging.basicConfig( stream=sys.stderr )
    # logging.getLogger( "Test.testSomething" ).setLevel( logging.DEBUG )
    main()
