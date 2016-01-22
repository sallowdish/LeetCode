from unittest import TestCase
from sol1 import Solution

class Test(TestCase):
    sol = None

    def setUp(self):
        self.sol = Solution()

    def test0(self):
        strs = []
        self.assertEqual(self.sol.longestCommonPrefix(strs),"")

    def test1(self):
        strs = ["",""]
        self.assertEqual(self.sol.longestCommonPrefix(strs), "")

    def test2(self):
        strs = ["a","b"]
        self.assertEqual(self.sol.longestCommonPrefix(strs), "")

    def test3(self):
        strs = ["a","ab"]
        self.assertEqual(self.sol.longestCommonPrefix(strs), "a")

    def test4(self):
        strs = ["ac","ab", "abc"]
        self.assertEqual(self.sol.longestCommonPrefix(strs), "a")

    def test5(self):
        strs = ["a"]
        self.assertEqual(self.sol.longestCommonPrefix(strs), "a")

    def test6(self):
        strs = ["a", "a", "b"]
        self.assertEqual(self.sol.longestCommonPrefix(strs), "")

    def test6(self):
        strs = ["abc","abcc","abc","abca","abca"]
        self.assertEqual(self.sol.longestCommonPrefix(strs), "abc")

