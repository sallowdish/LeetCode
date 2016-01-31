#!/usr/bin/python3
from unittest import TestCase, main
from sol1 import Solution


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Test(TestCase):
    sol = None

    def setUp(self):
        self.sol = Solution()

    def test0(self):
        n = []
        ans = []
        val = 0
        self.assertEqual(True, self.sol.removeElements(n, val))

    def test1(self):
        n = ListNode(1)
        n.next=ListNode(2)
        n.next.next = ListNode(2)
        n.next.next.next = ListNode(2)
        k = 0
        val = 2
        self.assertEqual(n, self.sol.removeElements(n, val))
        self.assertEqual(1, n.next)

    # def test2_1(self):
    #     n = 4
    #     k = 1
    #     self.assertEqual(False, self.sol.removeElements(n, val))
    #
    # def test2_2(self):
    #     n = 14
    #     ans = False
    #     self.assertEqual(ans, self.sol.removeElements(n, val))
        #
        # def test3(self):
        #     n = [2,1,1,2]
        #     k = 4
        #     self.assertEqual(self.sol.removeElements(n, val), 4)
        #
        # def test4(self):
        #     n = [155,44,52,58,250,225,109,118,211,73,137,96,137,89,174,66,134,26,25,205,239,85,146,73,55,6,122,196,128,50,61,230,94,208,46,243,105,81,157,89,205,78,249,203,238,239,217,212,241,242,157,79,133,66,36,165]
        #     k = 4
        #     self.assertEqual(self.sol.removeElements(n, val), 4517)

        # def test5(self):
        #     n = [1,2,3,4]
        #     k = -1
        #     self.assertEqual(self.sol.removeElements(n, val), [4,1,2,3])

        # def test6(self):
        #     n = 8
        #     k = 35
        #     self.assertEqual(self.sol.removeElements(n, val), ans)


if __name__ == "__main__":
    # logging.basicConfig( stream=sys.stderr )
    # logging.getLogger( "Test.testSomething" ).setLevel( logging.DEBUG )
    main()
