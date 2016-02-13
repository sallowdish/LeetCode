#!/usr/bin/python3
from unittest import TestCase
from sol1 import Solution
import logging, unittest


class Test(TestCase):
    sol = None

    def setUp(self):
        self.sol = Solution()

    def test0(self):
        n = 1
        m = 0
        ans = None
        self.assertEqual(ans, self.sol.divide(n, m))

    def test1(self):
        n = 0
        m = 1
        ans = 0
        self.assertEqual(ans, self.sol.divide(n, m))

    def test2(self):
        n = 1
        m = 1
        ans = 1
        self.assertEqual(ans, self.sol.divide(n, m))

    def test3(self):
        n = 1
        m = -1
        ans = -1
        self.assertEqual(ans, self.sol.divide(n, m))

    def test4(self):
        n = 5
        m = 2
        ans = 2
        self.assertEqual(ans, self.sol.divide(n, m))

    def test5(self):
        n = -5
        m = 2
        ans = -3
        self.assertEqual(ans, self.sol.divide(n, m))

    def test6(self):
        n = -456
        m = 87
        ans = -5
        self.assertEqual(ans, self.sol.divide(n, m))
if __name__ == "__main__":
    # logging.basicConfig( stream=sys.stderr )
    # logging.getLogger( "Test.testSomething" ).setLevel( logging.DEBUG )
    unittest.main()
