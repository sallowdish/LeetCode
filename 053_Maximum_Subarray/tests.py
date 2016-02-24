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
        n = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
        ans = 6
        self.assertEqual(ans, self.sol.maxSubArray(n))

    def test1(self):
        n = [1, 2, 3]
        ans = 6
        self.assertEqual(ans, self.sol.maxSubArray(n))

    def test2(self):
        n = [-1, -2, -3]
        ans = -1
        self.assertEqual(ans, self.sol.maxSubArray(n))

    def test3(self):
        n = [-1]
        ans = -1
        self.assertEqual(ans, self.sol.maxSubArray(n))

    def test4(self):
        n = [-2, 1]
        ans = 1
        self.assertEqual(ans, self.sol.maxSubArray(n))
        #
        # def test5(self):
        #     n = [1, 3, 5, 6]
        #
        #     ans = 2
        #     self.assertEqual(ans, self.sol.maxSubArray(n))
        #
        # def test6(self):
        #     n = [1, 3, 5, 6]
        #
        #     ans = 1
        #     self.assertEqual(ans, self.sol.maxSubArray(n))
        #
        # def test7(self):
        #     n = [1, 3, 5, 6]
        #
        #     ans = 0
        #     self.assertEqual(ans, self.sol.maxSubArray(n))
        #
        # def test8(self):
        #     n = [1, 3]
        #
        #     ans = 0
        #     self.assertEqual(ans, self.sol.maxSubArray(n))


if __name__ == "__main__":
    # logging.basicConfig( stream=sys.stderr )
    # logging.getLogger( "Test.testSomething" ).setLevel( logging.DEBUG )
    unittest.main()
