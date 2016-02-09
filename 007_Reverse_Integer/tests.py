from unittest import TestCase
from sol1 import Solution

class Test(TestCase):
    sol = None

    def setUp(self):
        self.sol = Solution()

    def test0(self):
        self.assertEqual(self.sol.reverse(0),0)

    def test1(self):
        self.assertEqual(self.sol.reverse(123), 321)

    def test2(self):
        self.assertEqual(self.sol.reverse(-123), -321)

    def test3(self):
        self.assertEqual(self.sol.reverse(10), 1)

