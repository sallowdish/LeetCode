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
        self.assertEqual(self.sol.hasPathSum(r, 1), False)

    def test1(self):
        r = TreeNode(1)
        r.left = TreeNode(2)
        r.right = TreeNode(3)
        r.right.right = TreeNode(188)
        self.assertEqual(self.sol.hasPathSum(r, 192), True)

    def test2(self):
        r = None
        self.assertEqual(self.sol.hasPathSum(r, 0), False)

    def test3(self):
        r = TreeNode(1)
        r.right = TreeNode(3)
        r.right.right = TreeNode(7)
        self.assertEqual(self.sol.hasPathSum(r, 11), 1)

    def test4(self):
        r = TreeNode(1)
        r.left = TreeNode(2)
        self.assertEqual(self.sol.hasPathSum(r, 1), 0)





if __name__ == "__main__":
    # logging.basicConfig( stream=sys.stderr )
    # logging.getLogger( "Test.testSomething" ).setLevel( logging.DEBUG )
    main()
