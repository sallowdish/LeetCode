#!/usr/bin/python3
from unittest import TestCase, main
from sol2 import Solution


class Test(TestCase):
    sol = None

    def setUp(self):
        self.sol = Solution()

    def test0(self):
        n = []
        ans = []
        self.assertEqual(self.sol.sortColors(n), ans)

    def test1(self):
        n = [0, 1, 2]
        ans = [0, 1, 2]
        self.assertEqual(self.sol.sortColors(n), ans)

    def test2(self):
        n = [2, 1, 0]
        ans = [0, 1, 2]
        self.assertEqual(self.sol.sortColors(n), ans)

    def test3(self):
        n = [1, 1, 0, 1, 2, 1]
        ans = [0, 1, 1, 1, 1, 2]
        self.assertEqual(self.sol.sortColors(n), ans)

    def test4(self):
        n = [1, 1, 2, 1, 2, 1]
        ans = [1, 1, 1, 1, 2, 2]
        self.assertEqual(self.sol.sortColors(n), ans)


if __name__ == "__main__":
    # logging.basicConfig( stream=sys.stderr )
    # logging.getLogger( "Test.testSomething" ).setLevel( logging.DEBUG )
    main()
