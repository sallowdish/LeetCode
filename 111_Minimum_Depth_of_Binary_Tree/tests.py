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
        r = TreeNode(0)
        self.assertEqual(self.sol.minDepth(r), 1)

    def test1(self):
        r = TreeNode(1)
        r.left = TreeNode(2)
        r.right = TreeNode(3)
        r.right.right = TreeNode(188)
        self.assertEqual(self.sol.minDepth(r), 2)

    def test2(self):
        r = None
        self.assertEqual(self.sol.minDepth(r), 0)

    def test3(self):
        r = TreeNode(1)
        r.right = TreeNode(3)
        r.right.right = TreeNode(7)
        self.assertEqual(self.sol.minDepth(r), 3)

    def test4(self):
        r = TreeNode(1)
        r.left = TreeNode(2)
        self.assertEqual(self.sol.minDepth(r), 2)





if __name__ == "__main__":
    # logging.basicConfig( stream=sys.stderr )
    # logging.getLogger( "Test.testSomething" ).setLevel( logging.DEBUG )
    main()
