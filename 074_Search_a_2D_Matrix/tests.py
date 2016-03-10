#!/usr/bin/python3
from unittest import TestCase, main
from sol1 import Solution


class Test(TestCase):
    sol = None

    def setUp(self):
        self.sol = Solution()

    def test0(self):
        n = [[0, 1], [2, 3]]
        m = 1
        ans = True
        self.assertEqual(self.sol.searchMatrix(n, m), ans)

    def test1(self):
        n = [[0, 1], [2, 3]]
        m = 2
        ans = True
        self.assertEqual(self.sol.searchMatrix(n, m), ans)

    def test2(self):
        n = [[0, 1], [3, 4]]
        m = 2
        ans = False
        self.assertEqual(self.sol.searchMatrix(n, m), ans)

    def test3(self):
        n = [[0, 1], [2, 3]]
        m = 4
        ans = False
        self.assertEqual(self.sol.searchMatrix(n, m), ans)

    def test4(self):
        n = [
            [1, 3, 5, 7],
            [10, 11, 16, 20],
            [23, 30, 34, 50]
        ]
        m = 3
        ans = True
        self.assertEqual(self.sol.searchMatrix(n, m), ans)

    def test5(self):
        n = [[1]]
        m = 1
        ans = True
        self.assertEqual(self.sol.searchMatrix(n, m), ans)


if __name__ == "__main__":
    # logging.basicConfig( stream=sys.stderr )
    # logging.getLogger( "Test.testSomething" ).setLevel( logging.DEBUG )
    main()
