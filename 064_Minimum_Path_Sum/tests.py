#!/usr/bin/python3
from unittest import TestCase
from collections import Counter
from sol1 import Solution
import logging, unittest


class Test(TestCase):
    sol = None

    def setUp(self):
        self.sol = Solution()

    def test0(self):
        n = [[0]]
        ans = 0
        self.assertEqual(ans, self.sol.minPathSum(n))

    def test1(self):
        n = [[1, 2]]
        ans = 3
        self.assertEqual(ans, self.sol.minPathSum(n))

    def test2(self):
        n = [[1,1],[2,2]]
        ans = 4
        self.assertEqual(ans, self.sol.minPathSum(n))

    def test3(self):
        n = [[1,2,3],[4,5,6],[7,8,9]]
        ans = 21
        self.assertEqual(ans, self.sol.minPathSum(n))

    # def test4(self):
    #     n = 3
    #     ans = [[1, 2, 3], [8, 9, 4], [7, 6, 5]]
    #     self.assertEqual(ans, self.sol.minPathSum(n))
    #
    #     # def test5(self):
    #     #     n = [[3], [2]]
    #     #     ans = [3, 2]
    #     #     self.assertEqual(ans, self.sol.minPathSum(n))


if __name__ == "__main__":
    # logging.basicConfig( stream=sys.stderr )
    # logging.getLogger( "Test.testSomething" ).setLevel( logging.DEBUG )
    unittest.main()
