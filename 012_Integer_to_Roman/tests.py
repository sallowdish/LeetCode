from unittest import TestCase
from sol1 import Solution


class Test(TestCase):
    sol = None

    def setUp(self):
        self.sol = Solution()

    def test0(self):
        self.assertEqual(self.sol.myAtoi(""), 0)

    def test1(self):
        self.assertEqual(self.sol.myAtoi("0"), 0)

    def test2(self):
        self.assertEqual(self.sol.myAtoi("-123"), -123)

    def test3(self):
        self.assertEqual(self.sol.myAtoi("000890"), 890)
