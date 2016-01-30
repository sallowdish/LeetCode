#!/usr/bin/python3
from unittest import TestCase, main
from sol1 import Solution

class Test(TestCase):

    sol = None

    def setUp(self):
        self.sol = Solution()

    def test0(self):
        ans = 0
        n = 2
        self.assertEqual(self.sol.trailingZeroes(n), ans)

    def test1(self):
        ans = 1
        n = 5
        self.assertEqual(self.sol.trailingZeroes(n), ans)

    def test2_1(self):
        ans = 2
        n = 10
        self.assertEqual(self.sol.trailingZeroes(n), ans)

    def test2_2(self):
        ans = 3
        n = 15
        self.assertEqual(self.sol.trailingZeroes(n), ans)

    def test3(self):
        ans = 3
        n = 19
        self.assertEqual(self.sol.trailingZeroes(n), ans)

    def test4(self):
        ans = 4
        n = 20
        self.assertEqual(self.sol.trailingZeroes(n), ans)

    def test5(self):
        ans = 6
        n = 25
        self.assertEqual(self.sol.trailingZeroes(n), ans)

    def test6(self):
        ans = 8
        n = 35
        self.assertEqual(self.sol.trailingZeroes(n), ans)





if __name__ == "__main__":
    # logging.basicConfig( stream=sys.stderr )
    # logging.getLogger( "Test.testSomething" ).setLevel( logging.DEBUG )
    main()
