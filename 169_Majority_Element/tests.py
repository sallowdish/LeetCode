#!/usr/bin/python3
from unittest import TestCase, main
from sol1 import Solution

class Test(TestCase):

    sol = None

    def setUp(self):
        self.sol = Solution()

    def test0(self):
        n = 1
        ans = "A"
        self.assertEqual(self.sol.convertToTitle(n), ans)

    def test1(self):
        n = 2
        ans = "B"
        self.assertEqual(self.sol.convertToTitle(n), ans)

    def test2_1(self):
        n = 25
        ans = "Y"
        self.assertEqual(self.sol.convertToTitle(n), ans)

    def test2_2(self):
        n = 26
        ans = "Z"
        self.assertEqual(self.sol.convertToTitle(n), ans)

    def test3(self):
        n = 27
        ans = "AA"
        self.assertEqual(self.sol.convertToTitle(n), ans)

    def test4(self):
        n = 28
        ans = "AB"
        self.assertEqual(self.sol.convertToTitle(n), ans)

    def test5(self):
        n = 676
        ans = "ZZ"
        self.assertEqual(self.sol.convertToTitle(n), ans)

    def test6(self):
        n = 677
        ans = "ZA"
        self.assertEqual(self.sol.convertToTitle(n), ans)





if __name__ == "__main__":
    # logging.basicConfig( stream=sys.stderr )
    # logging.getLogger( "Test.testSomething" ).setLevel( logging.DEBUG )
    main()
