#!/usr/bin/python3
from unittest import TestCase, main
from sol1 import Solution

class Test(TestCase):

    sol = None

    def setUp(self):
        self.sol = Solution()

    def test0(self):
        self.assertEqual(self.sol.generate(0), [])

    def test1(self):
        self.assertEqual(self.sol.generate(1), [[1]])

    def test2(self):
        self.assertEqual(self.sol.generate(2), [[1],[1,1]])

    def test3(self):
        self.assertEqual(self.sol.generate(3), [[1],[1,1],[1,2,1]])

    def test4(self):
        self.assertEqual(self.sol.generate(10), [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1],[1,5,10,10,5,1],[1,6,15,20,15,6,1],[1,7,21,35,35,21,7,1],[1,8,28,56,70,56,28,8,1],[1,9,36,84,126,126,84,36,9,1]])





if __name__ == "__main__":
    # logging.basicConfig( stream=sys.stderr )
    # logging.getLogger( "Test.testSomething" ).setLevel( logging.DEBUG )
    main()
