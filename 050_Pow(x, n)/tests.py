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
        n = 0.00001
        m = 2147483647
        ans = 0
        self.assertAlmostEqual(ans, self.sol.myPow(n, m))

    def test1(self):
        n = 34.00515
        m = -3
        ans = 0.00003
        self.assertAlmostEqual(ans, self.sol.myPow(n, m), places=5)

    def test2(self):
        n = 3.89707
        m = 2
        ans = 15.18715
        self.assertAlmostEqual(ans, self.sol.myPow(n, m), places=5)

    def test3(self):
        n = 8.95371
        m = -1
        ans = 0.11169
        self.assertAlmostEqual(ans, self.sol.myPow(n, m), places=5)

    def test4(self):
        n = 4.70975
        m = -6
        ans = 0.00009
        self.assertAlmostEqual(ans, self.sol.myPow(n, m), places=5)
        #
        # def test5(self):
        #     n = [1, 3, 5, 6]
        #
        #     ans = 2
        #     self.assertAlmostEqual(ans, self.sol.myPow(n, m))
        #
        # def test6(self):
        #     n = [1, 3, 5, 6]
        #
        #     ans = 1
        #     self.assertAlmostEqual(ans, self.sol.myPow(n, m))
        #
        # def test7(self):
        #     n = [1, 3, 5, 6]
        #
        #     ans = 0
        #     self.assertAlmostEqual(ans, self.sol.myPow(n, m))
        #
        # def test8(self):
        #     n = [1, 3]
        #
        #     ans = 0
        #     self.assertAlmostEqual(ans, self.sol.myPow(n, m))


if __name__ == "__main__":
    # logging.basicConfig( stream=sys.stderr )
    # logging.getLogger( "Test.testSomething" ).setLevel( logging.DEBUG )
    unittest.main()
