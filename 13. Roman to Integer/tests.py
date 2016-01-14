from unittest import TestCase
from sol1 import Solution

class Test(TestCase):
    sol = None

    def setUp(self):
        self.sol = Solution()

    def test0(self):
        self.assertEqual(self.sol.romanToInt("MMDIV"),2504)

    def test1(self):
        self.assertEqual(self.sol.romanToInt(""), 0)

    def test2(self):
        self.assertEqual(self.sol.romanToInt("VI"), 6)

    def test3(self):
        self.assertEqual(self.sol.romanToInt("IV"), 4)

    def test4(self):
        self.assertEqual(self.sol.romanToInt("DCCCXC"), 890)

    def test5(self):
        self.assertEqual(self.sol.romanToInt("XCIX"), 99)

