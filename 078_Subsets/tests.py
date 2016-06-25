#!/usr/bin/python3
from unittest import TestCase, main
from sol1 import Solution


class Test(TestCase):
    sol = None

    def setUp(self):
        self.sol = Solution()

    def test0(self):
        n = []
        ans = [[]]
        self.assertEqual(ans, self.sol.subsets(n))

    def test1(self):
        n = [1]
        ans = [[], [1]]
        self.assertEqual(sorted(ans), sorted(self.sol.subsets(n)))

    def test2(self):
        n = [1, 2]
        ans = [[], [1], [2], [1, 2]]
        self.assertEqual(sorted(ans), sorted(self.sol.subsets(n)))

    def test3(self):
        n = [1, 2, 3]
        ans = [[3], [1], [2], [1, 2, 3], [1, 3], [2, 3], [1, 2], []]
        self.assertEqual(sorted(ans), sorted(self.sol.subsets(n)))

    def test4(self):
        n = [1, 3, 2]
        ans = [[3], [1], [2], [1, 2, 3], [1, 3], [2, 3], [1, 2], []]
        self.assertEqual(sorted(ans), sorted(self.sol.subsets(n)))

    def test4(self):
        n = [1, 2, 1]
        ans = [[], [1], [2], [1, 1], [1, 2], [1, 1, 2]]
        self.assertEqual(sorted(ans), sorted(self.sol.subsets(n)))


if __name__ == "__main__":
    # logging.basicConfig( stream=sys.stderr )
    # logging.getLogger( "Test.testSomething" ).setLevel( logging.DEBUG )
    main()
