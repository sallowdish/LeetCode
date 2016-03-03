#!/usr/bin/python3
from unittest import TestCase
from collections import Counter
from sol3 import Solution
import logging, unittest


class Test(TestCase):
    sol = None

    def setUp(self):
        self.sol = Solution()

    def test0(self):
        n = 1
        k = 1
        ans = "1"
        self.assertEqual(ans, self.sol.getPermutation(n, k))

    def test1(self):
        n = 2
        k = 1
        ans = "12"
        self.assertEqual(ans, self.sol.getPermutation(n, k))

    def test2(self):
        n = 2
        k = 2
        ans = "21"
        self.assertEqual(ans, self.sol.getPermutation(n, k))

    def test3(self):
        n = 3
        k = 2
        ans = "132"
        self.assertEqual(ans, self.sol.getPermutation(n, k))

    def test4(self):
        n = 3
        k = 6
        ans = "321"
        self.assertEqual(ans, self.sol.getPermutation(n, k))

    def test5(self):
        n = 8
        k = 11483
        ans = "32864715"
        self.assertEqual(ans, self.sol.getPermutation(n, k))

    def test6(self):
        n = 9
        k = 94626
        ans = "348567921"
        self.assertEqual(ans, self.sol.getPermutation(n, k))
        #
        # def test7(self):
        #     n = [1, 3, 5, 6]
        #
        #     ans = 0
        #     self.assertEqual(ans, self.sol.getPermutation(n, k))
        #
        # def test8(self):
        #     n = [1, 3]
        #
        #     ans = 0
        #     self.assertEqual(ans, self.sol.getPermutation(n, k))


if __name__ == "__main__":
    # logging.basicConfig( stream=sys.stderr )
    # logging.getLogger( "Test.testSomething" ).setLevel( logging.DEBUG )
    unittest.main()
