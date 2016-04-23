#!/usr/bin/python3
from unittest import TestCase, main
from sol1 import Solution


class Test(TestCase):
    sol = None

    def setUp(self):
        self.sol = Solution()

    # whole test
    def test0_0(self):
        n = []
        ans = [[]]
        self.run_test(n, ans)

    def test0_1(self):
        n = [1]
        ans = [[], [1]]
        self.run_test(n, ans)

    def test0_2(self):
        n = [1, 2, 2]
        ans = [[2], [1], [1, 2, 2], [2, 2], [1, 2], []]
        self.run_test(n, ans)

    def test0_3(self):
        n = [1, 2, 2, 4, 4]
        ans = [[], [1], [2], [4], [1, 2], [1, 4], [2, 2], [2, 4], [4, 4], [1, 2, 2], [1, 2, 4], [1, 4, 4], [2, 2, 4],
               [2, 4, 4], [1, 2, 2, 4], [1, 2, 4, 4], [2, 2, 4, 4], [1, 2, 2, 4, 4]]
        self.run_test(n, ans)

    # real cases

    def test1_1(self):
        n = [4, 1, 0]
        ans = [[], [0], [0, 1], [0, 1, 4], [0, 4], [1], [1, 4], [4]]
        self.run_test(n, ans)

    def run_test(self, n, ans):
        ret = self.sol.subsetsWithDup(n)
        self.assertEqual(sorted(ans), sorted(ret))


if __name__ == "__main__":
    # logging.basicConfig( stream=sys.stderr )
    # logging.getLogger( "Test.testSomething" ).setLevel( logging.DEBUG )
    main()
