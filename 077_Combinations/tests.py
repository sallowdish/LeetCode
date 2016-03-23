#!/usr/bin/python3
from unittest import TestCase, main
from sol1 import Solution


class Test(TestCase):
    sol = None

    def setUp(self):
        self.sol = Solution()

    def test0(self):
        n = 0
        k = 0
        ans = [[]]
        self.assertEqual(ans, self.sol.combine(n, k))

    def test1(self):
        n = 1
        k = 1
        ans = [[1]]
        self.assertEqual(ans, self.sol.combine(n, k))

    def test2(self):
        n = 1
        k = 2
        with self.assertRaises(ValueError):
            self.sol.combine(n, k)

    def test3(self):
        n = 4
        k = 2
        ans = [[2, 4], [3, 4], [2, 3], [1, 2], [1, 3], [1, 4], ]
        self.assertEqual(sorted(ans), sorted(self.sol.combine(n, k)))


if __name__ == "__main__":
    # logging.basicConfig( stream=sys.stderr )
    # logging.getLogger( "Test.testSomething" ).setLevel( logging.DEBUG )
    main()
