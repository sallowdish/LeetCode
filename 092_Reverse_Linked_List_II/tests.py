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
        lst = []
        m = 1
        n = 1
        ans = None
        self.run_test(lst, m, n, ans)

    def test0_1(self):
        lst = [1, 2, 3]
        m = 1
        n = 1
        ans = lst
        self.run_test(lst, m, n, ans)

    def test0_2(self):
        lst = [1, 2, 3]
        m = 1
        n = 2
        ans = [2, 1, 3]
        self.run_test(lst, m, n, ans)

    def test0_3(self):
        lst = [1, 2, 3]
        m = 2
        n = 3
        ans = [1, 3, 2]
        self.run_test(lst, m, n, ans)

    def test0_4(self):
        lst = [1, 2, 3]
        m = 1
        n = 3
        ans = [3, 2, 1]
        self.run_test(lst, m, n, ans)

    def run_test(self, lst, m, n, ans):
        ret = self.sol.reverseBetween(build_linked_list_from_pylist(lst), m, n)
        self.assertEqual(ans, ret.to_list() if ret else ret)


if __name__ == "__main__":
    # logging.basicConfig( stream=sys.stderr )
    # logging.getLogger( "Test.testSomething" ).setLevel( logging.DEBUG )
    main()
