#!/usr/bin/python3
from unittest import TestCase, main
from sol1 import Solution

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Test(TestCase):

    sol = None

    def setUp(self):
        self.sol = Solution()

    def test0(self):
        r = TreeNode(1)
        self.assertEqual(self.sol.isSymmetric(r), 1)

    # # overflow
    # def test1(self):
    #     l1 = [1,5,9]
    #     l2 = []
    #     self.assertEqual(self.sol.merge(l1, len(l1), l2, len(l2)) ,[1,5,9])





if __name__ == "__main__":
    # logging.basicConfig( stream=sys.stderr )
    # logging.getLogger( "Test.testSomething" ).setLevel( logging.DEBUG )
    main()
