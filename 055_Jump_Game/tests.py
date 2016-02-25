#!/usr/bin/python3
from unittest import TestCase
from sol2 import Solution
import logging, unittest


class Test(TestCase):
    sol = None

    def setUp(self):
        self.sol = Solution()

    def test1(self):
        array = [1]
        ans = True
        self.assertEqual(ans, self.sol.canJump(array))

    def test2(self):
        array = [1, 1]
        ans = True
        self.assertEqual(ans, self.sol.canJump(array))

    def test3(self):
        array = [1, 2, 3]
        ans = True
        self.assertEqual(ans, self.sol.canJump(array))

    def test4(self):
        array = [2,3,1,1,4]
        ans = True
        self.assertEqual(ans, self.sol.canJump(array))

    def test5(self):
        array = [3,2,1,0,4]
        ans = False
        self.assertEqual(ans, self.sol.canJump(array))

    def test6(self):
        array = [1] * 100000
        ans = True
        self.assertEqual(ans, self.sol.canJump(array))


if __name__ == "__main__":
    # logging.basicConfig( stream=sys.stderr )
    # logging.getLogger( "Test.testSomething" ).setLevel( logging.DEBUG )
    unittest.main()
