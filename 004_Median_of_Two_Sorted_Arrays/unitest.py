from tests import TestCase
from sol1 import Solution

class Test(TestCase):
    sol = None

    def setUp(self):
        self.sol = Solution()

    def test1(self):
        with open("testcase/1.in") as f:
            s = []
            t = [1]
            self.assertEqual(self.sol.findMedianSortedArrays(s,t), 1)

    def test2(self):
        s = [1]
        t = [1]
        self.assertEqual(self.sol.findMedianSortedArrays(s,t), 1)

    def test3(self):
        s = [1, 2, 3]
        t = [1]
        self.assertEqual(self.sol.findMedianSortedArrays(s,t), 1.5)

    def test4(self):
        s = [1, 2, 3]
        t = [-3, 5, 10, 11]
        self.assertEqual(self.sol.findMedianSortedArrays(s,t), 3)

    def test5(self):
        s = []
        t = [2,3]
        self.assertEqual(self.sol.findMedianSortedArrays(s,t), 2.5)

