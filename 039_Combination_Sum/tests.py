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
        n = [2, 3, 6, 7]
        m = 7
        ans = [[2, 2, 3], [7]]
        self.assertEqual(ans, self.sol.combinationSum(n, m))

    def test1(self):
        n = [2, 3, 6, 7]
        m = 2
        ans = [[2]]
        self.assertEqual(ans, self.sol.combinationSum(n, m))

    def test2(self):
        n = [2, 3, 6, 7]
        m = 6
        ans = [[2, 2, 2], [3, 3], [6]]
        self.assertEqual(ans, self.sol.combinationSum(n, m))

    # def test3(self):
    #     n = [1, 2, 3, 4, 5]
    #     m = 3
    #     ans = 2
    #     self.assertEqual(ans, self.sol.combinationSum(n, m))
    #
    # def test4(self):
    #     n = [1, 2, 3]
    #     m = 3
    #     ans = 2
    #     self.assertEqual(ans, self.sol.combinationSum(n, m))
    #
    # def test5(self):
    #     n = [1, 3, 5, 6]
    #     m = 5
    #     ans = 2
    #     self.assertEqual(ans, self.sol.combinationSum(n, m))
    #
    # def test6(self):
    #     n = [1, 3, 5, 6]
    #     m = 2
    #     ans = 1
    #     self.assertEqual(ans, self.sol.combinationSum(n, m))
    #
    # def test7(self):
    #     n = [1, 3, 5, 6]
    #     m = 0
    #     ans = 0
    #     self.assertEqual(ans, self.sol.combinationSum(n, m))
    #
    # def test8(self):
    #     n = [1, 3]
    #     m = 1
    #     ans = 0
    #     self.assertEqual(ans, self.sol.combinationSum(n, m))


if __name__ == "__main__":
    # logging.basicConfig( stream=sys.stderr )
    # logging.getLogger( "Test.testSomething" ).setLevel( logging.DEBUG )
    unittest.main()
