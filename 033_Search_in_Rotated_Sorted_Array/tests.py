#!/usr/bin/python3
from unittest import TestCase, main
from sol1 import Solution
from collections import Counter


class Test(TestCase):
    sol = None

    def setUp(self):
        self.sol = Solution()

    # test binary_search
    def test0_0(self):
        nums = [1, 2, 3]
        target = -1
        ans = -1
        self.assertEqual(ans, self.sol.binary_search(nums, target))

    def test0_1(self):
        nums = [1, 2, 3]
        target = 2
        ans = 1
        self.assertEqual(ans, self.sol.binary_search(nums, target))

    def test0_2(self):
        nums = [1, 2, 3]
        target = 4
        ans = -1
        self.assertEqual(ans, self.sol.binary_search(nums, target))

    # whole test
    def test2_0(self):
        nums = [1, 2, 3]
        target = 2
        ans = 1
        self.assertEqual(ans, self.sol.search(nums, target))

    def test2_1(self):
        nums = [4, 5, 6, 7, 0, 1, 2]
        target = 2
        ans = 6
        self.assertEqual(ans, self.sol.search(nums, target))

    def test2_2(self):
        nums = [4, 5, 6, 7, 0, 1, 2]
        target = 5
        ans = 1
        self.assertEqual(ans, self.sol.search(nums, target))

    def test2_3(self):
        nums = [4, 5, 6, 7, 0, 1, 2]
        target = -1
        ans = -1
        self.assertEqual(ans, self.sol.search(nums, target))

    def test2_4(self):
        nums = [4, 5, 6, 7, 0, 1, 2]
        target = 10
        ans = -1
        self.assertEqual(ans, self.sol.search(nums, target))

    # LeetCode test case
    def test3_0(self):
        nums = [5, 1, 3]
        target = 0
        ans = -1
        self.assertEqual(ans, self.sol.search(nums, target))


if __name__ == "__main__":
    # logging.basicConfig( stream=sys.stderr )
    # logging.getLogger( "Test.testSomething" ).setLevel( logging.DEBUG )
    main()
