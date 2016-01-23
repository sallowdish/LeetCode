#!/usr/bin/python3
from unittest import TestCase, main
from sol1 import Solution

class Test(TestCase):

    sol = None

    def setUp(self):
        self.sol = Solution()

    def test0(self):
        self.assertEqual(self.sol.isPalindrome(""), 1)

    def test1(self):
        self.assertEqual(self.sol.isPalindrome("abc"), 0)

    def test2(self):
        self.assertEqual(self.sol.isPalindrome("a a"), 1)

    def test3(self):
        self.assertEqual(self.sol.isPalindrome("ab          a"), 1)

    def test4(self):
        self.assertEqual(self.sol.isPalindrome("ab   1  ba"), 1)





if __name__ == "__main__":
    # logging.basicConfig( stream=sys.stderr )
    # logging.getLogger( "Test.testSomething" ).setLevel( logging.DEBUG )
    main()
