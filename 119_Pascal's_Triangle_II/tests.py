#!/usr/bin/python3
from unittest import TestCase, main
from sol1 import Solution

class Test(TestCase):

    sol = None

    def setUp(self):
        self.sol = Solution()

    def test0(self):
        self.assertEqual(self.sol.getRow(0), [])

    def test1(self):
        self.assertEqual(self.sol.getRow(1), [1])

    def test2(self):
        self.assertEqual(self.sol.getRow(2), [1,1])

    def test3(self):
        self.assertEqual(self.sol.getRow(3), [1,2,1])

    def test4(self):
        self.assertEqual(self.sol.getRow(10), [1,9,36,84,126,126,84,36,9,1])





if __name__ == "__main__":
    # logging.basicConfig( stream=sys.stderr )
    # logging.getLogger( "Test.testSomething" ).setLevel( logging.DEBUG )
    main()
