#!/usr/bin/python3
from unittest import TestCase, main
from sol1 import Solution
from utils.ListNode import *


class Test(TestCase):
    sol = None

    def setUp(self):
        self.sol = Solution()

    # whole test
    def test0_0(self):
        nums = [1, 2, 3]
        head = build_linked_list_from_pylist(nums)
        target = 1
        ret = self.sol.partition(head, target)
        self.assertEqual(nums, ret.to_list())

    def test0_1(self):
        nums = [1, 2, 3]
        head = build_linked_list_from_pylist(nums)
        target = 2
        ret = self.sol.partition(head, target)
        self.assertEqual(nums, ret.to_list())

    def test0_2(self):
        nums = [1, 4, 3, 2, 5, 2]
        head = build_linked_list_from_pylist(nums)
        target = 2
        ret = self.sol.partition(head, target)
        self.assertEqual(nums, ret.to_list())

    def test0_3(self):
        nums = [1, 4, 3, 2, 5, 2]
        head = build_linked_list_from_pylist(nums)
        target = 3
        ret = self.sol.partition(head, target)
        self.assertEqual([1, 2, 2, 4, 3, 5], ret.to_list())

    # real cases


    def test1_0(self):
        nums = [2, 1]
        head = build_linked_list_from_pylist(nums)
        target = 2
        ret = self.sol.partition(head, target)
        self.assertEqual([1, 2], ret.to_list())

    def test1_1(self):
        nums = [2, 3, 1]
        head = build_linked_list_from_pylist(nums)
        target = 2
        ret = self.sol.partition(head, target)
        self.assertEqual([1, 2, 3], ret.to_list())

    def test1_2(self):
        nums = [3, 1, 2]
        head = build_linked_list_from_pylist(nums)
        target = 3
        ret = self.sol.partition(head, target)
        self.assertEqual([1, 2, 3], ret.to_list())


if __name__ == "__main__":
    # logging.basicConfig( stream=sys.stderr )
    # logging.getLogger( "Test.testSomething" ).setLevel( logging.DEBUG )
    main()
