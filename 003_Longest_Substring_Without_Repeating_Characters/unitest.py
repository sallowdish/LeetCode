from tests import TestCase
from sol2 import Solution

class Test(TestCase):
    sol = None

    def setUp(self):
        self.sol = Solution()

    def test1(self):
        with open("testcase/1.in") as f:
            s = f.readline()
            self.assertEqual(self.sol.lengthOfLongestSubstring(s), 0)

    def test2(self):
        with open("testcase/2.in") as f:
            s = f.readline()
            self.assertEqual(self.sol.lengthOfLongestSubstring(s), 1)

    def test3(self):
        with open("testcase/3.in") as f:
            s = f.readline()
            self.assertEqual(self.sol.lengthOfLongestSubstring(s), 1)

    def test4(self):
        with open("testcase/4.in") as f:
            s = f.readline()
            self.assertEqual(self.sol.lengthOfLongestSubstring(s), 2)

    def test5(self):
        with open("testcase/5.in") as f:
            s = f.readline()
            self.assertEqual(self.sol.lengthOfLongestSubstring(s), 5)

