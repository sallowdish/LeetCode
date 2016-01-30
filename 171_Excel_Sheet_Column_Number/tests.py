#!/usr/bin/python3
from unittest import TestCase, main
from sol1 import Solution

class Test(TestCase):

    sol = None

    def setUp(self):
        self.sol = Solution()

    def test0(self):
        ans = 1
        n ="A"
        self.assertEqual(self.sol.titleToNumber(n), ans)

    def test1(self):
        ans = 2
        n ="B"
        self.assertEqual(self.sol.titleToNumber(n), ans)

    def test2_1(self):
        ans = 25
        n ="Y"
        self.assertEqual(self.sol.titleToNumber(n), ans)

    def test2_2(self):
        ans = 26
        n ="Z"
        self.assertEqual(self.sol.titleToNumber(n), ans)

    def test3(self):
        ans = 27
        n ="AA"
        self.assertEqual(self.sol.titleToNumber(n), ans)

    def test4(self):
        ans = 28
        n ="AB"
        self.assertEqual(self.sol.titleToNumber(n), ans)

    def test5(self):
        ans = 702
        n ="ZZ"
        self.assertEqual(self.sol.titleToNumber(n), ans)

    def test6(self):
        ans = 677
        n ="ZA"
        self.assertEqual(self.sol.titleToNumber(n), ans)





if __name__ == "__main__":
    # logging.basicConfig( stream=sys.stderr )
    # logging.getLogger( "Test.testSomething" ).setLevel( logging.DEBUG )
    main()
